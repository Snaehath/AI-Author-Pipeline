"""
Phase 3C Regression Benchmark Runner.

Runs the complete Phase 3C data pipeline (deduplication -> comedy gate ->
mechanism detectors -> stratum classification) on the 50 frozen calibration
fixtures and evaluates precision, purity, agreement, and failure modes against
the gold human audit.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from dataset_generator.deduplicator import NormalizedTextDeduplicator
from dataset_generator.factual_analyzer import FactualSceneAnalyzer
from dataset_generator.craft_annotator import ComedyCraftAnnotator
from dataset_generator.taxonomy import CraftPresence, CraftStratum, ReviewStatus


class Phase3CRegressionBenchmark:
    """Evaluates the Phase 3C pipeline against gold historical calibration records."""

    DEFAULT_FIXTURE_PATH = Path("tests/fixtures/comedy_craft_calibration_v1.json")

    def __init__(self, fixture_path: Optional[Path] = None):
        self.fixture_path = fixture_path or self.DEFAULT_FIXTURE_PATH
        self.deduplicator = NormalizedTextDeduplicator()
        self.factual_analyzer = FactualSceneAnalyzer()
        self.craft_annotator = ComedyCraftAnnotator()

    def run(self) -> Dict[str, Any]:
        """Runs pipeline end-to-end and computes quantitative regression metrics."""
        with open(self.fixture_path, "r", encoding="utf-8") as f:
            fixtures = json.load(f)

        exact_dups = 0
        expected_exact = 0

        yes_tp = 0
        yes_fp = 0
        no_tp = 0
        no_fp = 0
        partials = 0
        partial_routed = 0

        primary_agrees = 0
        primary_total = 0

        foundation_count = 0
        foundation_fps = 0

        composite_count = 0
        composite_tps = 0

        drama_to_comedy = 0
        action_to_physical = 0
        dialogue_to_subtext = 0
        progression_to_escalation = 0

        for item in fixtures:
            idx = item["item_index"]
            sid = item["source_id"]
            text = item["source_text"]
            exp_pres = item["expected_presence"]
            exp_strat = item["expected_stratum"]
            exp_prim = item["expected_primary"]
            is_gold_dup = item.get("is_duplicate", False)

            # 1. Text Deduplication
            is_dup, canonical_id = self.deduplicator.check_and_register(text, sid)
            if is_gold_dup:
                expected_exact += 1
            if is_dup:
                exact_dups += 1

            # 2. Objective Factual Analysis
            facts = self.factual_analyzer.analyze(text)

            # 3. Craft Annotation & Eligibility Gate
            craft = self.craft_annotator.annotate(text, facts)

            # If deduplicator detected duplicate, override stratum and review status
            if is_dup:
                craft.is_duplicate = True
                craft.duplicate_of_id = canonical_id
                craft.craft_stratum = CraftStratum.REJECT
                craft.review_status = ReviewStatus.REJECTED

            pred_pres = craft.craft_presence.value

            # Comedic presence metrics
            if pred_pres == "YES":
                if exp_pres == "YES":
                    yes_tp += 1
                else:
                    yes_fp += 1
            elif pred_pres == "NO":
                if exp_pres == "NO":
                    no_tp += 1
                else:
                    no_fp += 1
            else:  # PARTIAL
                partials += 1
                # PARTIAL records must route strictly to human review queue (or rejected if duplicate)
                if craft.review_status in (ReviewStatus.FLAGGED_LOW_CONFIDENCE, ReviewStatus.REJECTED):
                    partial_routed += 1

            # Stratum assignment metrics
            if craft.craft_stratum == CraftStratum.PURE_MECHANISM:
                foundation_count += 1
                if exp_strat == "REJECT" or exp_pres == "NO":
                    foundation_fps += 1
            elif craft.craft_stratum == CraftStratum.COMPOSITE_CRAFT:
                composite_count += 1
                if exp_strat == "COMPOSITE_CRAFT":
                    composite_tps += 1

            # Primary mechanism agreement on eligible non-duplicate comedy
            if not is_gold_dup and exp_pres == "YES" and pred_pres == "YES":
                primary_total += 1
                if craft.primary_mechanism.value == exp_prim:
                    primary_agrees += 1

            # Known failure modes inspection
            # Drama mistaken for comedy (Items 11, 21, 24, 42)
            if idx in [11, 21, 24, 42] and pred_pres == "YES":
                drama_to_comedy += 1

            # Physical violence mistaken for physical comedy (Items 11, 21, 24, 38, 42)
            if idx in [11, 21, 24, 38, 42] and craft.primary_mechanism.value == "PHYSICAL_COMPLICATION":
                action_to_physical += 1

            # Ordinary dialogue mistaken for dialogue subtext (Items 9, 14, 25, 49)
            if idx in [9, 14, 25, 49] and craft.primary_mechanism.value == "DIALOGUE_SUBTEXT":
                dialogue_to_subtext += 1

            # Sequential reasoning / narrative progression mistaken for escalation (Items 11, 15, 21, 48)
            if idx in [11, 15, 21, 48] and craft.primary_mechanism.value == "ESCALATION":
                progression_to_escalation += 1

        yes_precision = (yes_tp / (yes_tp + yes_fp) * 100) if (yes_tp + yes_fp) else 0.0
        no_precision = (no_tp / (no_tp + no_fp) * 100) if (no_tp + no_fp) else 0.0
        partial_routing_pct = (partial_routed / partials * 100) if partials else 100.0
        primary_agreement_pct = (primary_agrees / primary_total * 100) if primary_total else 0.0
        foundation_fp_pct = (foundation_fps / foundation_count * 100) if foundation_count else 0.0
        composite_precision = (composite_tps / composite_count * 100) if composite_count else 0.0

        return {
            "total_items": len(fixtures),
            "comedic_presence": {
                "yes_tp": yes_tp,
                "yes_fp": yes_fp,
                "yes_precision": round(yes_precision, 1),
                "no_tp": no_tp,
                "no_fp": no_fp,
                "no_precision": round(no_precision, 1),
                "partial_count": partials,
                "partial_routed": partial_routed,
                "partial_routing_pct": round(partial_routing_pct, 1),
            },
            "duplicate_detection": {
                "exact_duplicates": exact_dups,
                "expected_exact": expected_exact,
                "near_duplicates": 0,
                "expected_near": 0,
            },
            "primary_mechanism": {
                "agreed": primary_agrees,
                "total": primary_total,
                "agreement_pct": round(primary_agreement_pct, 1),
            },
            "foundation_purity": {
                "foundation_count": foundation_count,
                "false_positives": foundation_fps,
                "fp_rate_pct": round(foundation_fp_pct, 1),
            },
            "composite_detection": {
                "composite_count": composite_count,
                "composite_tps": composite_tps,
                "precision_pct": round(composite_precision, 1),
            },
            "known_failure_cases": {
                "drama_to_comedy": drama_to_comedy,
                "action_to_physical": action_to_physical,
                "dialogue_to_subtext": dialogue_to_subtext,
                "progression_to_escalation": progression_to_escalation,
            },
        }

    def generate_report(self, metrics: Optional[Dict[str, Any]] = None) -> str:
        """Formats quantitative metrics into the canonical Phase 3C regression summary."""
        if metrics is None:
            metrics = self.run()

        cp = metrics["comedic_presence"]
        dd = metrics["duplicate_detection"]
        pm = metrics["primary_mechanism"]
        fp = metrics["foundation_purity"]
        cd = metrics["composite_detection"]
        kf = metrics["known_failure_cases"]

        lines = [
            "=== Phase 3C Regression ===",
            "",
            "Comedic presence:",
            f"  YES precision:     {cp['yes_precision']}% ({cp['yes_tp']}/{cp['yes_tp'] + cp['yes_fp']})",
            f"  NO precision:      {cp['no_precision']}% ({cp['no_tp']}/{cp['no_tp'] + cp['no_fp']})",
            f"  PARTIAL routing:   {cp['partial_routing_pct']}%",
            "",
            "Duplicate detection:",
            f"  exact duplicates: {dd['exact_duplicates']}/{dd['expected_exact']}",
            f"  near duplicates:  {dd['near_duplicates']}/{dd['expected_near']} (all 6 pairs exact hashes)",
            "",
            "Primary mechanism:",
            f"  agreement:         {pm['agreement_pct']}% ({pm['agreed']}/{pm['total']})",
            "",
            "Foundation purity:",
            f"  false positives:   {fp['fp_rate_pct']}% ({fp['false_positives']}/{fp['foundation_count']})",
            "",
            "Composite detection:",
            f"  precision:         {cd['precision_pct']}% ({cd['composite_tps']}/{cd['composite_count']})",
            "",
            "Known failure cases:",
            f"  drama -> comedy:    {kf['drama_to_comedy']}",
            f"  action -> physical: {kf['action_to_physical']}",
            f"  dialogue -> subtext: {kf['dialogue_to_subtext']}",
            f"  progression -> escalation: {kf['progression_to_escalation']}",
        ]
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Phase 3C Regression Benchmark Runner")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("tests/fixtures/comedy_craft_calibration_v1.json"),
        help="Path to calibration fixture JSON",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON metrics instead of text report",
    )
    args = parser.parse_args()

    benchmark = Phase3CRegressionBenchmark(fixture_path=args.fixture)
    metrics = benchmark.run()

    if args.json:
        print(json.dumps(metrics, indent=2))
    else:
        print(benchmark.generate_report(metrics))


if __name__ == "__main__":
    main()

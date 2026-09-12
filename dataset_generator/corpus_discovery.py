"""
Phase 3D Corpus Discovery Engine.

Executes the Phase 3C pipeline across the entire narrative corpus (~10,619 records)
to discover the true empirical distribution of comedic craft, deduplication rates,
gate selectivity, and mechanism representation without premature optimization.
"""

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from dataset_generator.deduplicator import NormalizedTextDeduplicator
from dataset_generator.factual_analyzer import FactualSceneAnalyzer
from dataset_generator.craft_annotator import ComedyCraftAnnotator
from dataset_generator.taxonomy import (
    ComicMechanism,
    CraftPresence,
    CraftStratum,
    ReviewStatus,
)


class CorpusDiscoveryAnalyzer:
    """Discovers structural craft distributions across large-scale narrative corpora."""

    MIN_TEXT_CHARS = 120
    MIN_WORD_COUNT = 25

    def __init__(self, input_path: Path):
        self.input_path = input_path
        self.deduplicator = NormalizedTextDeduplicator()
        self.factual_analyzer = FactualSceneAnalyzer()
        self.craft_annotator = ComedyCraftAnnotator()

    def run(self, max_passages: Optional[int] = None, log_interval: int = 1000) -> Dict[str, Any]:
        """Runs discovery pipeline across corpus and returns comprehensive discovery metrics."""
        t0 = time.time()

        total_lines = 0
        too_short = 0
        valid_passages = 0
        exact_duplicates = 0
        unique_passages = 0

        gate_counts = Counter()
        strata_counts = Counter()
        mechanism_counts_all = Counter()
        mechanism_counts_foundation = Counter()
        mechanism_counts_composite = Counter()
        source_book_counts = Counter()
        confidence_scores_foundation: List[float] = []
        confidence_scores_composite: List[float] = []

        with open(self.input_path, "r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f):
                if max_passages is not None and line_idx >= max_passages:
                    break

                total_lines += 1
                line = line.strip()
                if not line:
                    continue

                raw_item = json.loads(line)
                source_text = raw_item.get("output", "").strip()
                if not source_text or len(source_text) < self.MIN_TEXT_CHARS:
                    combined = f"{raw_item.get('input', '')}\n{source_text}".strip()
                    if len(combined) >= self.MIN_TEXT_CHARS:
                        source_text = combined
                    else:
                        too_short += 1
                        continue

                words = source_text.split()
                if len(words) < self.MIN_WORD_COUNT:
                    too_short += 1
                    continue

                valid_passages += 1
                source_book = raw_item.get("source_book", "Unknown British Comic Work")
                source_book_counts[source_book] += 1
                chapter_index = raw_item.get("chapter_index", 1)
                source_id = f"{source_book.lower().replace(' ', '_')}_ch{chapter_index}_{line_idx:05d}"

                # 1. Deduplication Check
                is_dup, canonical_id = self.deduplicator.check_and_register(source_text, source_id)
                if is_dup:
                    exact_duplicates += 1
                    continue

                unique_passages += 1

                # 2. Level 1: Factual Analysis
                facts = self.factual_analyzer.analyze(source_text)

                # 3. Level 2: Craft Annotation & Eligibility Gate
                craft = self.craft_annotator.annotate(source_text, facts)

                gate_status = craft.craft_presence.value
                gate_counts[gate_status] += 1

                # Stratum classification
                stratum = craft.craft_stratum.value
                strata_counts[stratum] += 1

                # Track mechanism representation
                if craft.craft_presence == CraftPresence.YES:
                    mech_name = craft.primary_mechanism.value
                    mechanism_counts_all[mech_name] += 1

                    if craft.craft_stratum == CraftStratum.PURE_MECHANISM:
                        mechanism_counts_foundation[mech_name] += 1
                        confidence_scores_foundation.append(craft.detector_confidence)
                    elif craft.craft_stratum == CraftStratum.COMPOSITE_CRAFT:
                        mechanism_counts_composite[mech_name] += 1
                        confidence_scores_composite.append(craft.detector_confidence)

                if (line_idx + 1) % log_interval == 0:
                    elapsed = time.time() - t0
                    print(
                        f"[{elapsed:6.1f}s] Processed {line_idx + 1} lines... "
                        f"Unique: {unique_passages}, YES: {gate_counts['YES']}, "
                        f"PARTIAL: {gate_counts['PARTIAL']}, NO: {gate_counts['NO']}",
                        file=sys.stderr,
                    )

        elapsed_total = time.time() - t0

        # Percentages
        u_base = max(1, unique_passages)
        yes_pct = (gate_counts["YES"] / u_base) * 100
        partial_pct = (gate_counts["PARTIAL"] / u_base) * 100
        no_pct = (gate_counts["NO"] / u_base) * 100

        all_mechs = [m.value for m in ComicMechanism]
        complete_mech_dist = {m: mechanism_counts_all.get(m, 0) for m in all_mechs}

        avg_foundation_conf = (
            sum(confidence_scores_foundation) / len(confidence_scores_foundation)
            if confidence_scores_foundation
            else 0.0
        )
        avg_composite_conf = (
            sum(confidence_scores_composite) / len(confidence_scores_composite)
            if confidence_scores_composite
            else 0.0
        )

        return {
            "total_lines": total_lines,
            "valid_passages": valid_passages,
            "too_short_passages": too_short,
            "deduplication": {
                "unique_passages": unique_passages,
                "duplicates_detected": exact_duplicates,
                "duplicate_rate_pct": round(
                    (exact_duplicates / max(1, valid_passages)) * 100, 1
                ),
            },
            "comedy_gate": {
                "yes_count": gate_counts["YES"],
                "yes_pct": round(yes_pct, 1),
                "partial_count": gate_counts["PARTIAL"],
                "partial_pct": round(partial_pct, 1),
                "no_count": gate_counts["NO"],
                "no_pct": round(no_pct, 1),
            },
            "eligibility_breakdown": {
                "foundation_candidates": strata_counts[CraftStratum.PURE_MECHANISM.value],
                "composite_candidates": strata_counts[CraftStratum.COMPOSITE_CRAFT.value],
                "human_review_candidates": gate_counts["PARTIAL"],
                "rejected_count": strata_counts[CraftStratum.REJECT.value] + exact_duplicates,
            },
            "mechanisms": complete_mech_dist,
            "mechanisms_foundation": {
                m: mechanism_counts_foundation.get(m, 0) for m in all_mechs
            },
            "mechanisms_composite": {
                m: mechanism_counts_composite.get(m, 0) for m in all_mechs
            },
            "confidence_metrics": {
                "mean_foundation_confidence": round(avg_foundation_conf, 3),
                "mean_composite_confidence": round(avg_composite_conf, 3),
            },
            "source_book_counts": dict(source_book_counts),
            "execution_time_seconds": round(elapsed_total, 2),
        }

    def format_report(self, metrics: Dict[str, Any]) -> str:
        """Generates the canonical Phase 3D Corpus Discovery summary report."""
        cg = metrics["comedy_gate"]
        dd = metrics["deduplication"]
        el = metrics["eligibility_breakdown"]
        mechs = metrics["mechanisms"]

        lines = [
            "=== Phase 3D Corpus Discovery ===",
            "",
            "Input:",
            f"  {metrics['total_lines']:,} passages (valid: {metrics['valid_passages']:,}, skipped short: {metrics['too_short_passages']:,})",
            "",
            "Deduplication:",
            f"  unique:        {dd['unique_passages']:,}",
            f"  duplicates:    {dd['duplicates_detected']:,} ({dd['duplicate_rate_pct']}%)",
            "",
            "Comedy gate:",
            f"  YES:           {cg['yes_count']:,} ({cg['yes_pct']}%)",
            f"  PARTIAL:       {cg['partial_count']:,} ({cg['partial_pct']}%)",
            f"  NO:            {cg['no_count']:,} ({cg['no_pct']}%)",
            "",
            "Eligible:",
            f"  Foundation candidates: {el['foundation_candidates']:,}",
            f"  Composite candidates:  {el['composite_candidates']:,}",
            f"  Human review:          {el['human_review_candidates']:,}",
            "",
            "Mechanisms:",
        ]

        # Ordered by taxonomy definition
        for m in ComicMechanism:
            count = mechs.get(m.value, 0)
            lines.append(f"  {m.value:23s}: {count:,}")

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Phase 3D Corpus Discovery Runner")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("datasets/train.jsonl"),
        help="Path to source JSONL dataset",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("reports"),
        help="Directory to save discovery reports",
    )
    parser.add_argument(
        "--max-passages",
        type=int,
        default=None,
        help="Maximum passages to process (for testing/partial runs)",
    )
    args = parser.parse_args()

    analyzer = CorpusDiscoveryAnalyzer(input_path=args.input)
    print(f"Starting Phase 3D Corpus Discovery across {args.input}...", file=sys.stderr)
    metrics = analyzer.run(max_passages=args.max_passages)

    report = analyzer.format_report(metrics)
    print("\n" + report)

    # Save reports
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "phase_3d_corpus_discovery.json"
    md_path = args.output_dir / "phase_3d_corpus_discovery.md"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Phase 3D Corpus Discovery Report\n\n```text\n{report}\n```\n\n")
        f.write(f"**Execution time:** {metrics['execution_time_seconds']} seconds\n\n")
        f.write("## Stratum Confidence Metrics\n\n")
        f.write(f"- Mean Foundation Candidate Confidence: `{metrics['confidence_metrics']['mean_foundation_confidence']}`\n")
        f.write(f"- Mean Composite Candidate Confidence: `{metrics['confidence_metrics']['mean_composite_confidence']}`\n\n")
        f.write("## Representation by Source Work\n\n")
        f.write("| Source Work | Raw Passage Count |\n| :--- | :---: |\n")
        for book, cnt in sorted(metrics["source_book_counts"].items(), key=lambda x: x[1], reverse=True):
            f.write(f"| {book} | {cnt:,} |\n")

    print(f"\nSaved discovery artifacts to:\n- {json_path}\n- {md_path}", file=sys.stderr)


if __name__ == "__main__":
    main()

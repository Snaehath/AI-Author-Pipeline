"""
Phase 3D.1 Stratified Audit Sampler.

Selects ~160-220 diverse passages across Foundation (15/15), Composite (50-75),
PARTIAL review queue (75-100), and NO negative controls (20-30) with explicit
source-work diversity caps to prevent single-work concentration.
"""

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from dataset_generator.deduplicator import NormalizedTextDeduplicator
from dataset_generator.factual_analyzer import FactualSceneAnalyzer
from dataset_generator.craft_annotator import ComedyCraftAnnotator
from dataset_generator.taxonomy import (
    ComicMechanism,
    CraftPresence,
    CraftStratum,
    MechanismHorizon,
    ReviewStatus,
    get_mechanism_horizon,
)


class AuditSampler:
    """Samples stratified, source-diverse passages for targeted human ground-truth calibration."""

    MIN_TEXT_CHARS = 120
    MIN_WORD_COUNT = 25

    def __init__(self, input_path: Path, seed: int = 42):
        self.input_path = input_path
        self.seed = seed
        self.deduplicator = NormalizedTextDeduplicator()
        self.factual_analyzer = FactualSceneAnalyzer()
        self.craft_annotator = ComedyCraftAnnotator()
        random.seed(self.seed)

    def extract_candidates(
        self, max_lines: Optional[int] = None
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Runs the pipeline across the corpus and partitions valid unique passages into candidate pools."""
        pools: Dict[str, List[Dict[str, Any]]] = {
            "FOUNDATION": [],
            "COMPOSITE": [],
            "PARTIAL": [],
            "NO_CONTROL": [],
        }

        with open(self.input_path, "r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f):
                if max_lines is not None and line_idx >= max_lines:
                    break
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
                        continue

                words = source_text.split()
                if len(words) < self.MIN_WORD_COUNT:
                    continue

                source_book = raw_item.get("source_book", "Unknown British Comic Work")
                chapter_index = raw_item.get("chapter_index", 1)
                source_id = f"{source_book.lower().replace(' ', '_')}_ch{chapter_index}_{line_idx:05d}"

                # Deduplication check
                is_dup, canonical_id = self.deduplicator.check_and_register(source_text, source_id)
                if is_dup:
                    continue

                facts = self.factual_analyzer.analyze(source_text)
                craft = self.craft_annotator.annotate(source_text, facts)

                item_meta = {
                    "line_idx": line_idx,
                    "source_id": source_id,
                    "source_book": source_book,
                    "chapter_index": chapter_index,
                    "source_text": source_text,
                    "facts": facts.to_dict(),
                    "craft": craft.to_dict(),
                }

                if craft.craft_presence == CraftPresence.YES:
                    if craft.craft_stratum == CraftStratum.PURE_MECHANISM:
                        pools["FOUNDATION"].append(item_meta)
                    elif craft.craft_stratum == CraftStratum.COMPOSITE_CRAFT:
                        pools["COMPOSITE"].append(item_meta)
                elif craft.craft_presence == CraftPresence.PARTIAL:
                    pools["PARTIAL"].append(item_meta)
                elif craft.craft_presence == CraftPresence.NO:
                    pools["NO_CONTROL"].append(item_meta)

        return pools

    def _sample_with_diversity(
        self, items: List[Dict[str, Any]], target_count: int, max_per_book: int
    ) -> List[Dict[str, Any]]:
        """Samples items respecting a maximum contribution cap per source book."""
        if len(items) <= target_count:
            return items

        # Group by book
        by_book = defaultdict(list)
        for it in items:
            by_book[it["source_book"]].append(it)

        for b in by_book:
            random.shuffle(by_book[b])

        sampled: List[Dict[str, Any]] = []
        book_counts = Counter()

        # Round-robin allocation to ensure diverse books are selected first
        books = sorted(by_book.keys())
        added_in_round = True
        while len(sampled) < target_count and added_in_round:
            added_in_round = False
            for b in books:
                if len(sampled) >= target_count:
                    break
                if by_book[b] and book_counts[b] < max_per_book:
                    it = by_book[b].pop(0)
                    sampled.append(it)
                    book_counts[b] += 1
                    added_in_round = True

        # If cap was too strict and we still need items, fill from remaining
        if len(sampled) < target_count:
            remaining = [it for b in by_book for it in by_book[b]]
            random.shuffle(remaining)
            needed = target_count - len(sampled)
            sampled.extend(remaining[:needed])

        return sampled

    def build_audit_dataset(
        self,
        composite_sample_size: int = 60,
        partial_sample_size: int = 80,
        no_control_sample_size: int = 25,
        max_per_book_cap: int = 15,
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """Builds the targeted ~180 audit dataset across all 4 pools with diversity constraints."""
        pools = self.extract_candidates()

        foundation_items = pools["FOUNDATION"]  # All 15
        composite_sampled = self._sample_with_diversity(
            pools["COMPOSITE"], composite_sample_size, max_per_book=max_per_book_cap
        )
        partial_sampled = self._sample_with_diversity(
            pools["PARTIAL"], partial_sample_size, max_per_book=max_per_book_cap
        )
        no_sampled = self._sample_with_diversity(
            pools["NO_CONTROL"], no_control_sample_size, max_per_book=max_per_book_cap
        )

        all_sampled_batches = [
            ("FOUNDATION", foundation_items),
            ("COMPOSITE", composite_sampled),
            ("PARTIAL", partial_sampled),
            ("NO_CONTROL", no_sampled),
        ]

        audit_records: List[Dict[str, Any]] = []
        global_idx = 1
        book_distribution = Counter()

        for pool_name, batch in all_sampled_batches:
            for it in batch:
                craft_data = it["craft"]
                primary_m = craft_data.get("primary_mechanism", "MISUNDERSTANDING")
                try:
                    c_enum = ComicMechanism(primary_m)
                    horizon = get_mechanism_horizon(c_enum).value
                except ValueError:
                    horizon = MechanismHorizon.LOCAL.value

                book_name = it["source_book"]
                book_distribution[book_name] += 1

                audit_rec = {
                    "audit_id": f"audit_{global_idx:03d}",
                    "audit_index": global_idx,
                    "sample_pool": pool_name,
                    "source_id": it["source_id"],
                    "source_book": book_name,
                    "chapter_index": it["chapter_index"],
                    "source_text": it["source_text"],
                    "detector_prediction": {
                        "presence": craft_data.get("craft_presence"),
                        "stratum": craft_data.get("craft_stratum"),
                        "primary_mechanism": primary_m,
                        "secondary_mechanisms": craft_data.get("secondary_mechanisms", []),
                        "confidence": craft_data.get("detector_confidence", 0.0),
                        "mechanism_horizon": horizon,
                        "tone": craft_data.get("tone"),
                        "setup": craft_data.get("setup_summary"),
                        "escalation": craft_data.get("escalation_summary"),
                        "reversal": craft_data.get("reversal_summary"),
                        "payoff": craft_data.get("payoff_summary"),
                    },
                    "human_audit": {
                        "craft_presence": "UNREVIEWED",
                        "craft_stratum": "UNREVIEWED",
                        "primary_mechanism": None,
                        "secondary_mechanisms": [],
                        "mechanism_horizon": "LOCAL",
                        "setup_accurate": None,
                        "escalation_accurate": None,
                        "reversal_accurate": None,
                        "payoff_accurate": None,
                        "literary_quality": None,
                        "training_value": None,
                        "keep_verdict": "UNREVIEWED",
                        "detector_correct": None,
                        "notes": "",
                    },
                }
                audit_records.append(audit_rec)
                global_idx += 1

        stats = {
            "total_sampled": len(audit_records),
            "pool_counts": {
                "FOUNDATION": len(foundation_items),
                "COMPOSITE": len(composite_sampled),
                "PARTIAL": len(partial_sampled),
                "NO_CONTROL": len(no_sampled),
            },
            "source_book_distribution": dict(book_distribution),
            "distinct_works_count": len(book_distribution),
        }
        return audit_records, stats

    def export_audit_batch(
        self,
        output_json: Path,
        output_md: Path,
        composite_sample_size: int = 60,
        partial_sample_size: int = 80,
        no_control_sample_size: int = 25,
        max_per_book_cap: int = 15,
    ) -> Dict[str, Any]:
        """Generates and exports both JSON and Markdown audit sheets."""
        records, stats = self.build_audit_dataset(
            composite_sample_size=composite_sample_size,
            partial_sample_size=partial_sample_size,
            no_control_sample_size=no_control_sample_size,
            max_per_book_cap=max_per_book_cap,
        )

        output_json.parent.mkdir(parents=True, exist_ok=True)
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

        # Markdown review document
        with open(output_md, "w", encoding="utf-8") as f:
            f.write("# Phase 3D.1 Comedy Craft Human Calibration Batch (180 Passages)\n\n")
            f.write("## Sampling Strategy & Pool Representation\n\n")
            f.write(f"- **Total Passages Audited:** {stats['total_sampled']}\n")
            f.write(f"- **Foundation Candidates (`PURE_MECHANISM`):** {stats['pool_counts']['FOUNDATION']} (100% of discovered Foundation candidates)\n")
            f.write(f"- **Composite Candidates (`COMPOSITE_CRAFT`):** {stats['pool_counts']['COMPOSITE']}\n")
            f.write(f"- **PARTIAL Review Queue:** {stats['pool_counts']['PARTIAL']} (Testing high-value borderline rescue)\n")
            f.write(f"- **NO Negative Controls:** {stats['pool_counts']['NO_CONTROL']} (Testing gate false-negative rate / recall)\n")
            f.write(f"- **Distinct Source Works Represented:** {stats['distinct_works_count']}\n\n")

            f.write("### Source Work Representation\n\n")
            f.write("| Source Work | Sampled Count |\n| :--- | :---: |\n")
            for book, cnt in sorted(stats["source_book_distribution"].items(), key=lambda x: x[1], reverse=True):
                f.write(f"| {book} | {cnt} |\n")

            f.write("\n---\n\n## Audit Instructions\n\n")
            f.write(
                "For each passage, independently assess:\n"
                "1. **`craft_presence`**: `YES`, `NO`, or `PARTIAL`\n"
                "2. **`craft_stratum`**: `PURE_MECHANISM`, `COMPOSITE_CRAFT`, or `REJECT`\n"
                "3. **`primary_mechanism`**: What is the dominant mechanism? (Independent of detector hypothesis)\n"
                "4. **`mechanism_horizon`**: `LOCAL` (manifests within scene) vs `LONG_HORIZON` (requires context)\n"
                "5. **`detector_correct`**: `true` if detector primary matches actual craft, `false` otherwise\n"
                "6. **`training_value`**: 1 (worthless/unfunny) to 10 (flawless comedic exemplar)\n"
                "7. **`keep_verdict`**: `KEEP` (enters Gold SFT/DPO), `REJECT`, or `REVISE`\n\n"
                "---\n\n"
            )

            # Summaries for each pool
            for rec in records:
                idx = rec["audit_index"]
                pool = rec["sample_pool"]
                book = rec["source_book"]
                sid = rec["source_id"]
                pred = rec["detector_prediction"]
                txt = rec["source_text"]

                f.write(f"### Passage {idx:03d} [{pool}] — *{book}* (`{sid}`)\n\n")
                f.write(f"> {txt}\n\n")
                f.write(f"- **Detector Prediction:** `{pred['presence']}` | Stratum: `{pred['stratum']}` | Primary: `{pred['primary_mechanism']}` (conf: `{pred['confidence']}`)\n")
                f.write(f"- **Temporal Horizon:** `{pred['mechanism_horizon']}` | Secondary: `{pred['secondary_mechanisms']}`\n\n")
                f.write("```json\n")
                f.write(json.dumps(rec["human_audit"], indent=2))
                f.write("\n```\n\n---\n\n")

        return stats


def main():
    parser = argparse.ArgumentParser(description="Phase 3D.1 Stratified Audit Sampler")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("datasets/train.jsonl"),
        help="Path to source JSONL dataset",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("reports/comedy_craft_audit_batch_180.json"),
        help="Path to export audit JSON sheet",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("reports/comedy_craft_audit_batch_180.md"),
        help="Path to export human audit markdown document",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for deterministic sampling",
    )
    args = parser.parse_args()

    sampler = AuditSampler(input_path=args.input, seed=args.seed)
    print(f"Sampling Phase 3D.1 audit dataset from {args.input}...", file=sys.stderr)
    stats = sampler.export_audit_batch(
        output_json=args.output_json,
        output_md=args.output_md,
    )

    print("\n=== Phase 3D.1 Audit Batch Created ===")
    print(f"Total Sampled: {stats['total_sampled']}")
    for pool, cnt in stats["pool_counts"].items():
        print(f"  {pool:12s}: {cnt}")
    print(f"Distinct works represented: {stats['distinct_works_count']}")
    print(f"\nExported to:\n- {args.output_json}\n- {args.output_md}")


if __name__ == "__main__":
    main()

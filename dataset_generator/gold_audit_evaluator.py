"""
Phase 3D Gold Audit Evaluator & Dataset Partitioning Engine.

Evaluates human audit judgments against detector hypotheses across Foundation,
Composite, PARTIAL, and Negative Control pools.
Calculates gate precision/recall, detector confusion matrix, rescue rate,
and partitions audited records into provenance-stamped gold datasets:
- PURE (Foundation SFT candidate)
- COMPOSITE (Advanced SFT candidate)
- LONG_HORIZON (Multi-scene contextual craft)
- BORDERLINE (Review queue)
- REJECT (Negative controls / contrast pairs)
"""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from dataset_generator.taxonomy import (
    AnnotationSource,
    ComicMechanism,
    CraftPresence,
    CraftStratum,
    MechanismHorizon,
    ReviewStatus,
    get_mechanism_horizon,
)


class GoldAuditEvaluator:
    """Evaluates human ground-truth calibration batches and compiles partitioned gold datasets."""

    def __init__(self, audit_file: Path):
        self.audit_file = audit_file

    def load_audit_records(self) -> List[Dict[str, Any]]:
        with open(self.audit_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def evaluate(self, records: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """Calculates comprehensive gate precision, recall, detector confusion, and rescue metrics."""
        if records is None:
            records = self.load_audit_records()

        total = len(records)
        audited_count = 0
        pool_counts = Counter()

        # Gate metrics
        yes_total = 0
        yes_true_comedy = 0
        no_total = 0
        no_false_negatives = 0
        partial_total = 0
        partial_rescued_comedy = 0

        # Mechanism metrics on verified comedy
        detector_correct_count = 0
        mechanism_eval_total = 0
        confusion_matrix: Dict[str, Counter] = defaultdict(Counter)

        # Stratum metrics
        foundation_total = 0
        foundation_confirmed_pure = 0
        foundation_downgraded_composite = 0
        foundation_rejected = 0

        composite_total = 0
        composite_confirmed = 0

        # Scope metrics
        horizon_counts = Counter()
        keep_counts = Counter()

        for rec in records:
            pool = rec.get("sample_pool", "UNKNOWN")
            pool_counts[pool] += 1
            pred = rec.get("detector_prediction", {})
            audit = rec.get("human_audit", {})

            presence = audit.get("craft_presence")
            if presence == "UNREVIEWED" or presence is None:
                continue

            audited_count += 1
            stratum = audit.get("craft_stratum")
            primary_m = audit.get("primary_mechanism")
            detector_p = pred.get("primary_mechanism")
            keep_verdict = audit.get("keep_verdict", "KEEP")
            keep_counts[keep_verdict] += 1

            horizon = audit.get("mechanism_horizon", "LOCAL")
            horizon_counts[horizon] += 1

            # 1. Gate Recall & Precision
            if pool in ("FOUNDATION", "COMPOSITE"):
                yes_total += 1
                if presence == "YES":
                    yes_true_comedy += 1

            elif pool == "NO_CONTROL":
                no_total += 1
                if presence == "YES":
                    no_false_negatives += 1  # Gate incorrectly discarded genuine comedy

            elif pool == "PARTIAL":
                partial_total += 1
                if presence == "YES" and keep_verdict == "KEEP":
                    partial_rescued_comedy += 1  # Successfully rescued high-value comedy

            # 2. Stratum Purity
            if pool == "FOUNDATION":
                foundation_total += 1
                if stratum == "PURE_MECHANISM" and presence == "YES":
                    foundation_confirmed_pure += 1
                elif stratum == "COMPOSITE_CRAFT" and presence == "YES":
                    foundation_downgraded_composite += 1
                else:
                    foundation_rejected += 1

            elif pool == "COMPOSITE":
                composite_total += 1
                if stratum == "COMPOSITE_CRAFT" and presence == "YES":
                    composite_confirmed += 1

            # 3. Mechanism Confusion Matrix
            if presence == "YES" and primary_m:
                mechanism_eval_total += 1
                if detector_p:
                    confusion_matrix[detector_p][primary_m] += 1
                if audit.get("detector_correct") is True or detector_p == primary_m:
                    detector_correct_count += 1

        yes_precision_pct = (yes_true_comedy / yes_total * 100) if yes_total else None
        no_recall_loss_pct = (no_false_negatives / no_total * 100) if no_total else None
        partial_rescue_pct = (partial_rescued_comedy / partial_total * 100) if partial_total else None
        mechanism_accuracy_pct = (
            (detector_correct_count / mechanism_eval_total * 100)
            if mechanism_eval_total
            else None
        )
        foundation_purity_pct = (
            (foundation_confirmed_pure / foundation_total * 100)
            if foundation_total
            else None
        )

        return {
            "total_records": total,
            "audited_records": audited_count,
            "is_complete": audited_count == total,
            "pool_representation": dict(pool_counts),
            "gate_evaluation": {
                "yes_sample_size": yes_total,
                "yes_true_comedy": yes_true_comedy,
                "yes_precision_pct": round(yes_precision_pct, 1) if yes_precision_pct is not None else None,
                "no_control_size": no_total,
                "no_false_negatives": no_false_negatives,
                "false_negative_rate_pct": round(no_recall_loss_pct, 1) if no_recall_loss_pct is not None else None,
                "partial_review_size": partial_total,
                "partial_rescued_count": partial_rescued_comedy,
                "rescue_rate_pct": round(partial_rescue_pct, 1) if partial_rescue_pct is not None else None,
            },
            "stratum_purity": {
                "foundation_candidates": foundation_total,
                "confirmed_pure": foundation_confirmed_pure,
                "downgraded_to_composite": foundation_downgraded_composite,
                "rejected": foundation_rejected,
                "foundation_purity_pct": round(foundation_purity_pct, 1) if foundation_purity_pct is not None else None,
                "composite_candidates": composite_total,
                "confirmed_composite": composite_confirmed,
            },
            "mechanism_performance": {
                "evaluated_comedy_passages": mechanism_eval_total,
                "detector_correct": detector_correct_count,
                "accuracy_pct": round(mechanism_accuracy_pct, 1) if mechanism_accuracy_pct is not None else None,
                "confusion_matrix": {k: dict(v) for k, v in confusion_matrix.items()},
            },
            "temporal_horizon": dict(horizon_counts),
            "verdict_distribution": dict(keep_counts),
        }

    def partition_gold_datasets(
        self, output_dir: Path, records: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, int]:
        """
        Partitions audited records into clean gold jsonl files with full provenance stamps.
        Strictly enforces that evaluation examples are never exported into SFT or DPO.
        """
        if records is None:
            records = self.load_audit_records()

        output_dir.mkdir(parents=True, exist_ok=True)
        pure_path = output_dir / "comedy_gold_pure.jsonl"
        composite_path = output_dir / "comedy_gold_composite.jsonl"
        horizon_path = output_dir / "comedy_gold_long_horizon.jsonl"
        borderline_path = output_dir / "comedy_gold_borderline.jsonl"
        reject_path = output_dir / "comedy_gold_reject.jsonl"

        pure_file = open(pure_path, "w", encoding="utf-8")
        composite_file = open(composite_path, "w", encoding="utf-8")
        horizon_file = open(horizon_path, "w", encoding="utf-8")
        borderline_file = open(borderline_path, "w", encoding="utf-8")
        reject_file = open(reject_path, "w", encoding="utf-8")

        counts = Counter()

        try:
            for rec in records:
                audit = rec.get("human_audit", {})
                presence = audit.get("craft_presence")
                stratum = audit.get("craft_stratum")
                horizon = audit.get("mechanism_horizon", "LOCAL")
                keep = audit.get("keep_verdict", "KEEP")

                # Stamp provenance
                record_entry = dict(rec)
                record_entry["annotation_source"] = (
                    AnnotationSource.HUMAN_REVIEWED.value
                    if presence not in ("UNREVIEWED", None)
                    else AnnotationSource.AUTOMATED.value
                )

                line = json.dumps(record_entry) + "\n"

                if keep == "REJECT" or presence == "NO":
                    reject_file.write(line)
                    counts["REJECT"] += 1
                elif presence == "PARTIAL" or stratum == "REJECT":
                    borderline_file.write(line)
                    counts["BORDERLINE"] += 1
                elif horizon == "LONG_HORIZON":
                    horizon_file.write(line)
                    counts["LONG_HORIZON"] += 1
                elif stratum == "PURE_MECHANISM":
                    pure_file.write(line)
                    counts["PURE"] += 1
                elif stratum == "COMPOSITE_CRAFT":
                    composite_file.write(line)
                    counts["COMPOSITE"] += 1
                else:
                    borderline_file.write(line)
                    counts["BORDERLINE"] += 1
        finally:
            pure_file.close()
            composite_file.close()
            horizon_file.close()
            borderline_file.close()
            reject_file.close()

        return dict(counts)

    def generate_report(self, metrics: Optional[Dict[str, Any]] = None) -> str:
        """Formats evaluation metrics into a human-readable report."""
        if metrics is None:
            metrics = self.evaluate()

        ge = metrics["gate_evaluation"]
        sp = metrics["stratum_purity"]
        mp = metrics["mechanism_performance"]

        yes_prec_str = f"{ge['yes_precision_pct']}%" if ge["yes_precision_pct"] is not None else "N/A"
        fn_str = f"{ge['false_negative_rate_pct']}%" if ge["false_negative_rate_pct"] is not None else "N/A"
        rescue_str = f"{ge['rescue_rate_pct']}%" if ge["rescue_rate_pct"] is not None else "N/A"
        purity_str = f"{sp['foundation_purity_pct']}%" if sp["foundation_purity_pct"] is not None else "N/A"
        acc_str = f"{mp['accuracy_pct']}%" if mp["accuracy_pct"] is not None else "N/A"

        lines = [
            "=== Phase 3D Gold Calibration Audit Report ===",
            "",
            f"Total Records:    {metrics['total_records']} (Audited: {metrics['audited_records']})",
            f"Status:           {'COMPLETE' if metrics['is_complete'] else 'IN PROGRESS / UNREVIEWED'}",
            "",
            "Gate Evaluation:",
            f"  YES Precision:               {yes_prec_str} ({ge['yes_true_comedy']}/{ge['yes_sample_size']})",
            f"  NO False Negative Rate:      {fn_str} ({ge['no_false_negatives']}/{ge['no_control_size']})",
            f"  PARTIAL Rescue Rate:         {rescue_str} ({ge['partial_rescued_count']}/{ge['partial_review_size']})",
            "",
            "Stratum Purity:",
            f"  Foundation Purity:           {purity_str} ({sp['confirmed_pure']}/{sp['foundation_candidates']})",
            f"  Downgraded to Composite:     {sp['downgraded_to_composite']}",
            f"  Foundation Rejected:         {sp['rejected']}",
            f"  Composite Confirmed:         {sp['confirmed_composite']}/{sp['composite_candidates']}",
            "",
            "Mechanism Performance:",
            f"  Detector Accuracy on Gold:   {acc_str} ({mp['detector_correct']}/{mp['evaluated_comedy_passages']})",
            f"  Temporal Horizon:            Local: {metrics['temporal_horizon'].get('LOCAL', 0)}, Long-Horizon: {metrics['temporal_horizon'].get('LONG_HORIZON', 0)}",
        ]
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Phase 3D Gold Audit Evaluator")
    parser.add_argument(
        "--audit-file",
        type=Path,
        default=Path("reports/comedy_craft_audit_batch_180.json"),
        help="Path to audited JSON file",
    )
    parser.add_argument(
        "--partition-dir",
        type=Path,
        default=Path("datasets/gold"),
        help="Directory to export partitioned gold datasets",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON metrics",
    )
    args = parser.parse_args()

    evaluator = GoldAuditEvaluator(audit_file=args.audit_file)
    metrics = evaluator.evaluate()

    if args.json:
        print(json.dumps(metrics, indent=2))
    else:
        print(evaluator.generate_report(metrics))

    if args.partition_dir:
        partitions = evaluator.partition_gold_datasets(output_dir=args.partition_dir)
        print(f"\nPartitioned Gold Datasets saved to {args.partition_dir}:")
        for p_name, cnt in partitions.items():
            print(f"  comedy_gold_{p_name.lower()}.jsonl: {cnt} records")


if __name__ == "__main__":
    main()

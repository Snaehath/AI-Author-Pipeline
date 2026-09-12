"""
CLI Runner for Comedy Craft Dataset Generation.

Builds stratified samples, full train/val/test splits, and validation audit reports.
"""

import argparse
import json
import sys
from pathlib import Path

# Add project root and ML parent to path
AI_AUTHOR_DIR = Path(__file__).resolve().parent.parent
ML_DIR = AI_AUTHOR_DIR.parent
for p in [str(AI_AUTHOR_DIR), str(ML_DIR)]:
    if p not in sys.path:
        sys.path.insert(0, p)

from dataset_generator.comedy_craft_builder import ComedyCraftPipeline


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build Comedy Craft Dataset and Stratified Inspection Samples."
    )
    parser.add_argument(
        "--input-file",
        type=str,
        default=str(AI_AUTHOR_DIR / "datasets" / "train.jsonl"),
        help="Path to source JSONL file.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=50,
        help="Number of stratified examples to export for inspection.",
    )
    parser.add_argument(
        "--output-sample",
        type=str,
        default=str(AI_AUTHOR_DIR / "datasets" / "comedy_craft_sample_50.json"),
        help="Path to save the human-inspectable sample JSON.",
    )
    parser.add_argument(
        "--report-path",
        type=str,
        default=str(AI_AUTHOR_DIR / "reports" / "comedy_craft_build_report.json"),
        help="Path to save the JSON build and audit report.",
    )
    parser.add_argument(
        "--full-build",
        action="store_true",
        help="Whether to compile the full train/val/test dataset splits.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Deterministic random seed.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    input_path = Path(args.input_file)
    output_sample_path = Path(args.output_sample)
    report_path = Path(args.report_path)

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    print(f"=== Starting Comedy Craft Dataset Builder ===")
    print(f"Source: {input_path}")
    print(f"Seed: {args.seed}")

    pipeline = ComedyCraftPipeline(random_seed=args.seed)

    # If extracting a sample, we scan enough candidates to achieve a rich stratified sample
    max_scan = args.sample_size * 20 if not args.full_build else None
    records, stats = pipeline.build_from_jsonl(
        input_path, max_records=args.sample_size, stratified=True
    )

    print(f"\nExtracted {len(records)} stratified comedy craft records.")
    print(f"Source scanned: {stats['source_examples_scanned']}")
    print(f"Mechanism distribution:")
    for mech, pct in stats["mechanism_distribution_pct"].items():
        print(f"  - {mech:24s}: {stats['mechanism_distribution'][mech]:3d} ({pct})")

    # Ensure output directories exist
    output_sample_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # Save sample JSON
    serialized = [r.to_dict() for r in records]
    with open(output_sample_path, "w", encoding="utf-8") as f:
        json.dump(serialized, f, indent=2, ensure_ascii=False)
    print(f"\n[OK] Saved stratified sample ({len(records)} records) to: {output_sample_path}")

    # Save build report
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"[OK] Saved build report to: {report_path}")

    if args.full_build:
        print("\nPartitioning into Three Architectural Strata...")
        foundation, advanced, eval_benchmark, rejected = pipeline.partition_strata(records)
        
        foundation_path = output_sample_path.parent / "comedy_craft_foundation_sft.jsonl"
        advanced_path = output_sample_path.parent / "comedy_craft_advanced_sft.jsonl"
        eval_path = output_sample_path.parent / "comedy_craft_eval_benchmark.jsonl"

        for p, subset in [
            (foundation_path, foundation),
            (advanced_path, advanced),
            (eval_path, eval_benchmark),
        ]:
            with open(p, "w", encoding="utf-8") as f:
                for item in subset:
                    f.write(json.dumps(item.to_dict(), ensure_ascii=False) + "\n")
        print(
            f"[OK] Three-tier dataset written: "
            f"foundation={len(foundation)}, advanced={len(advanced)}, "
            f"eval_benchmark={len(eval_benchmark)}, rejected={len(rejected)}"
        )

        print("\nBuilding traditional train/val/test splits (80/10/10)...")
        train, val, test = pipeline.split_dataset(foundation + advanced)
        train_path = output_sample_path.parent / "comedy_craft_train.jsonl"
        val_path = output_sample_path.parent / "comedy_craft_val.jsonl"
        test_path = output_sample_path.parent / "comedy_craft_test.jsonl"

        for p, subset in [(train_path, train), (val_path, val), (test_path, test)]:
            with open(p, "w", encoding="utf-8") as f:
                for item in subset:
                    f.write(json.dumps(item.to_dict(), ensure_ascii=False) + "\n")
        print(f"[OK] Full splits written: train={len(train)}, val={len(val)}, test={len(test)}")

    print("\n=== Comedy Craft Dataset Build Completed Successfully ===")



if __name__ == "__main__":
    main()

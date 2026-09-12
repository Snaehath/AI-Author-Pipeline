"""
dataset_generator/sft_pipeline.py

Phase 3E orchestrator: scorer -> eval splitter -> partitioner.

Single entry point for the complete SFT dataset preparation pipeline.
Derives all counts from the audit JSON (never hard-codes them) and
validates the KEEP count before producing any output.

Usage:
    python -m dataset_generator.sft_pipeline
    python -m dataset_generator.sft_pipeline --audit-file reports/comedy_craft_audit_batch_180.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from dataset_generator.sft_eval_splitter import build_eval_set, write_eval_set
from dataset_generator.sft_partitioner import partition, write_balance_report, write_outputs
from dataset_generator.sft_scorer import score_all_records, write_scored_records
from dataset_generator.sft_train_builder import build_and_save_dataset


def run_pipeline(
    audit_path: Path,
    out_dir: Path,
    report_manifest_path: Path | None = Path("reports/comedy_sft_train_manifest.json"),
) -> dict[str, Any]:
    print("=" * 60)
    print("Phase 3F: SFT Dataset Preparation & Manifest Pipeline")
    print("=" * 60)

    # ------------------------------------------------------------------ #
    # Step 1: Score all records                                           #
    # ------------------------------------------------------------------ #
    print("\n[Step 1] Scoring audit records...")
    scored, tier_counts = score_all_records(audit_path)

    scored_path = out_dir / "scored_records.jsonl"
    write_scored_records(scored, scored_path)

    print("\nTier breakdown (KEEP records only):")
    for tier, count in sorted(tier_counts.items()):
        print(f"  {tier:8s}: {count}")

    total_keep = sum(
        1 for r in scored if r["human_audit"].get("keep_verdict") == "KEEP"
    )
    print(f"\n  Total KEEP (derived from audit): {total_keep}")

    # ------------------------------------------------------------------ #
    # Step 2: Build frozen evaluation set                                 #
    # ------------------------------------------------------------------ #
    print("\n[Step 2] Building stratified frozen evaluation set...")
    eval_records, eval_ids = build_eval_set(scored)
    write_eval_set(eval_records, eval_ids, out_dir)

    # ------------------------------------------------------------------ #
    # Step 3: Partition into curricula and tier files                     #
    # ------------------------------------------------------------------ #
    print("\n[Step 3] Partitioning into curricula and tier files...")
    outputs = partition(scored, eval_ids)

    print("\nOutput files:")
    write_outputs(outputs, out_dir)
    write_balance_report(outputs, eval_records, out_dir / "sft_balance_report.json")

    # ------------------------------------------------------------------ #
    # Step 4: Build canonical training stream and manifest               #
    # ------------------------------------------------------------------ #
    print("\n[Step 4] Building training stream and manifest (Phase 3F)...")
    manifest = build_and_save_dataset(
        scored_records=scored,
        eval_records=eval_records,
        eval_ids=eval_ids,
        curriculum_outputs=outputs,
        sft_dir=out_dir,
        source_audit_path=audit_path,
        report_manifest_path=report_manifest_path,
    )

    # ------------------------------------------------------------------ #
    # Summary                                                             #
    # ------------------------------------------------------------------ #
    print("\n" + "=" * 60)
    print("Pipeline complete.")
    print(f"  Audit KEEP:       {total_keep}")
    print(f"  Eval set:         {len(eval_records)}")
    print(f"  Training stream:  {manifest['training']['count']}")
    print(f"  Train SHA-256:    {manifest['hashes']['train_sha256']}")
    print(f"  Eval SHA-256:     {manifest['hashes']['eval_sha256']}")
    print(f"  Gold tier:        {len(outputs['gold'])}")
    print(f"  Strong tier:      {len(outputs['strong'])}")
    print(f"  Curriculum 1:     {len(outputs['curriculum_1'])}")
    print(f"  Curriculum 2:     {len(outputs['curriculum_2'])}")
    print(f"  Curriculum 3:     {len(outputs['curriculum_3'])}")
    print(f"  Curriculum 4:     {len(outputs['curriculum_4'])}")
    print(f"  Curriculum 5:     {len(outputs['curriculum_5'])}")
    print(f"  Pref candidates:  {len(outputs['preference_candidates'])}")
    print(f"  Conservation:     {manifest['reconciliation']['conservation']}")
    print(f"  Verification:     {manifest['verification']['passed']}")
    print(f"  Output dir:       {out_dir}")
    print("=" * 60)

    # Sanity: audit_050 (Right Ho ch10 tent farce) must be in gold + curriculum_4 + training
    audit_050_in_gold = any(r.get("audit_id") == "audit_050" for r in outputs["gold"])
    audit_050_in_c4 = any(
        r.get("audit_id") == "audit_050" for r in outputs["curriculum_4"]
    )
    audit_050_in_train = manifest["protected_examples"]["audit_050"]["in_train"]
    audit_050_in_eval = manifest["protected_examples"]["audit_050"]["in_eval"]

    if not audit_050_in_gold:
        print("WARNING: audit_050 not found in Gold tier!")
    if not audit_050_in_c4:
        print("WARNING: audit_050 not found in Curriculum 4!")
    if not audit_050_in_train:
        print("WARNING: audit_050 not found in training stream!")
    if audit_050_in_eval:
        print("WARNING: audit_050 leaked into eval set!")
    if audit_050_in_gold and audit_050_in_c4 and audit_050_in_train and not audit_050_in_eval:
        print("audit_050 correctly present in Gold, Curriculum 4, and Training stream. OK")

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 3F: Full SFT dataset preparation and manifest pipeline."
    )
    parser.add_argument(
        "--audit-file",
        type=Path,
        default=Path("reports/comedy_craft_audit_batch_180.json"),
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("datasets/sft"),
    )
    parser.add_argument(
        "--report-manifest",
        type=Path,
        default=Path("reports/comedy_sft_train_manifest.json"),
    )
    args = parser.parse_args()
    run_pipeline(args.audit_file, args.out_dir, args.report_manifest)


if __name__ == "__main__":
    main()


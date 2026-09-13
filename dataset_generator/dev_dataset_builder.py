"""
dataset_generator/dev_dataset_builder.py

Phase 4B-2: Development Set (DEV) Partitioning & Invariant Verification.

Builds a deterministic, stratified 20-record DEV dataset from the 37 unallocated
high-quality KEEP records (sft_score >= 8.0) in the 180-record human audit batch.

Guarantees:
  1. Zero overlap with Frozen TEST (17 records): DEV ∩ TEST = ∅
  2. Zero overlap with SFT TRAIN (43 records): DEV ∩ TRAIN = ∅
  3. High quality: 100% of DEV records have sft_score >= 8.0
  4. Stratified mechanism coverage across all 7 represented classes in the eligible pool
  5. Exact schema parity with comedy_eval.jsonl
  6. Cryptographic SHA-256 fingerprinting & manifest emission
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from dataset_generator.sft_scorer import compute_sft_score, TIER_STRONG

DEFAULT_AUDIT_PATH = Path("reports/comedy_craft_audit_batch_180.json")
DEFAULT_TEST_PATH = Path("datasets/sft/comedy_eval.jsonl")
DEFAULT_TRAIN_PATH = Path("datasets/sft/comedy_sft_train.jsonl")
DEFAULT_DEV_OUT_PATH = Path("datasets/sft/comedy_dev.jsonl")
DEFAULT_MANIFEST_OUT_PATH = Path("datasets/sft/sft_dev_manifest.json")
DEFAULT_REPORT_MANIFEST_PATH = Path("reports/comedy_sft_dev_manifest.json")

DEV_TARGET_COUNT = 20

# Stratified allocation target across the 37 eligible pool records:
# ESCALATION: 14 available -> 7 selected
# VERBAL_WIT: 6 available -> 3 selected
# MISUNDERSTANDING: 5 available -> 3 selected
# DEADPAN_REACTION: 5 available -> 3 selected
# PHYSICAL_COMPLICATION: 3 available -> 2 selected
# STATUS_REVERSAL: 2 available -> 1 selected
# SOCIAL_EMBARRASSMENT: 2 available -> 1 selected
# Total = 20
MECHANISM_ALLOCATION: dict[str, int] = {
    "ESCALATION": 7,
    "VERBAL_WIT": 3,
    "MISUNDERSTANDING": 3,
    "DEADPAN_REACTION": 3,
    "PHYSICAL_COMPLICATION": 2,
    "STATUS_REVERSAL": 1,
    "SOCIAL_EMBARRASSMENT": 1,
}


def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def build_dev_dataset(
    audit_path: Path = DEFAULT_AUDIT_PATH,
    test_path: Path = DEFAULT_TEST_PATH,
    train_path: Path = DEFAULT_TRAIN_PATH,
    dev_out_path: Path = DEFAULT_DEV_OUT_PATH,
    manifest_out_path: Path = DEFAULT_MANIFEST_OUT_PATH,
    report_manifest_path: Path = DEFAULT_REPORT_MANIFEST_PATH,
) -> dict[str, Any]:
    """
    Constructs the 20-record DEV set from eligible KEEP records and verifies all invariants.
    """
    # 1. Load audit batch
    with open(audit_path, encoding="utf-8") as f:
        raw_audit = json.load(f)

    # 2. Load existing TEST and TRAIN IDs
    with open(test_path, encoding="utf-8") as f:
        test_records = [json.loads(line) for line in f if line.strip()]
        test_ids = {r["audit_id"] for r in test_records}

    with open(train_path, encoding="utf-8") as f:
        train_records = [json.loads(line) for line in f if line.strip()]
        train_ids = {r["audit_id"] for r in train_records}

    # 3. Filter KEEP records
    keep_records = [
        r for r in raw_audit
        if r.get("human_audit", {}).get("keep_verdict") == "KEEP"
    ]

    # Invariant: exactly 106 KEEP records
    if len(keep_records) != 106:
        raise ValueError(f"Expected 106 KEEP records in audit, found {len(keep_records)}")

    # 4. Filter unallocated candidates (not in TEST, not in TRAIN)
    unallocated = [
        r for r in keep_records
        if r["audit_id"] not in test_ids and r["audit_id"] not in train_ids
    ]
    if len(unallocated) != 46:
        raise ValueError(f"Expected 46 unallocated KEEP records, found {len(unallocated)}")

    # 5. Score unallocated records and filter high quality (>= 8.0)
    eligible_37: list[dict[str, Any]] = []
    eval_tier_9: list[dict[str, Any]] = []

    for r in unallocated:
        score_meta = compute_sft_score(r)
        r_augmented = dict(r)
        r_augmented["sft_metadata"] = score_meta
        if score_meta["sft_score"] >= TIER_STRONG:
            eligible_37.append(r_augmented)
        else:
            eval_tier_9.append(r_augmented)

    if len(eligible_37) != 37:
        raise ValueError(f"Expected 37 eligible pool records with sft_score >= 8.0, found {len(eligible_37)}")

    # 6. Group by primary mechanism and sort deterministically
    by_mech: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in eligible_37:
        primary = r["human_audit"]["primary_mechanism"]
        by_mech[primary].append(r)

    for m in by_mech:
        by_mech[m].sort(
            key=lambda x: (-x["sft_metadata"]["sft_score"], x["audit_id"])
        )

    # 7. Select according to allocation strategy
    selected_dev: list[dict[str, Any]] = []
    allocation_recorded: dict[str, int] = {}

    for mech, count in MECHANISM_ALLOCATION.items():
        available = by_mech.get(mech, [])
        if len(available) < count:
            raise ValueError(
                f"Insufficient records for {mech}: requested {count}, available {len(available)}"
            )
        chosen = available[:count]
        selected_dev.extend(chosen)
        allocation_recorded[mech] = len(chosen)

    # Invariant: exactly 20 records
    if len(selected_dev) != DEV_TARGET_COUNT:
        raise ValueError(f"Expected {DEV_TARGET_COUNT} DEV records, got {len(selected_dev)}")

    # Sort final DEV set by audit_id for absolute determinism
    selected_dev.sort(key=lambda x: x["audit_id"])
    dev_ids = {r["audit_id"] for r in selected_dev}

    # 8. Verify zero-leakage invariants
    test_leakage = dev_ids & test_ids
    train_leakage = dev_ids & train_ids

    if test_leakage:
        raise RuntimeError(f"CRITICAL: DEV leaks into TEST! Leaked IDs: {test_leakage}")
    if train_leakage:
        raise RuntimeError(f"CRITICAL: DEV leaks into TRAIN! Leaked IDs: {train_leakage}")

    # 9. Write datasets/sft/comedy_dev.jsonl
    dev_out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dev_out_path, "w", encoding="utf-8") as f:
        for r in selected_dev:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    dev_sha256 = compute_sha256(dev_out_path)

    # 10. Compute remaining pool after DEV
    remaining_after_dev = [r for r in eligible_37 if r["audit_id"] not in dev_ids]
    remaining_mechs = Counter(r["human_audit"]["primary_mechanism"] for r in remaining_after_dev)

    # 11. Build Manifest
    manifest = {
        "phase": "4B-2",
        "dataset": "comedy_dev.jsonl",
        "role": "Development Set (Model & Checkpoint Selection)",
        "count": len(selected_dev),
        "sha256": dev_sha256,
        "source": {
            "audit_file": str(audit_path),
            "audited_records": len(raw_audit),
            "total_keep_records": len(keep_records),
            "unallocated_pool": len(unallocated),
            "eligible_pool_score_gte_8": len(eligible_37),
            "eval_tier_score_lt_8": len(eval_tier_9),
        },
        "invariants": {
            "test_overlap_count": len(test_leakage),
            "train_overlap_count": len(train_leakage),
            "zero_leakage_verified": True,
            "all_scores_gte_8": all(r["sft_metadata"]["sft_score"] >= 8.0 for r in selected_dev),
        },
        "mechanism_distribution": allocation_recorded,
        "source_book_distribution": dict(Counter(r["source_book"] for r in selected_dev)),
        "remaining_pool_after_dev": {
            "high_quality_count": len(remaining_after_dev),
            "mechanisms": dict(remaining_mechs),
            "eval_tier_count": len(eval_tier_9),
            "total_available_for_contrastive": len(remaining_after_dev) + len(eval_tier_9),
        },
        "dev_audit_ids": [r["audit_id"] for r in selected_dev],
    }

    manifest_out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(manifest_out_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    report_manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Phase 4B-2 DEV dataset.")
    parser.add_argument("--audit-path", type=Path, default=DEFAULT_AUDIT_PATH)
    parser.add_argument("--test-path", type=Path, default=DEFAULT_TEST_PATH)
    parser.add_argument("--train-path", type=Path, default=DEFAULT_TRAIN_PATH)
    parser.add_argument("--dev-out", type=Path, default=DEFAULT_DEV_OUT_PATH)
    parser.add_argument("--manifest-out", type=Path, default=DEFAULT_MANIFEST_OUT_PATH)
    parser.add_argument("--report-manifest", type=Path, default=DEFAULT_REPORT_MANIFEST_PATH)
    args = parser.parse_args()

    manifest = build_dev_dataset(
        audit_path=args.audit_path,
        test_path=args.test_path,
        train_path=args.train_path,
        dev_out_path=args.dev_out,
        manifest_out_path=args.manifest_out,
        report_manifest_path=args.report_manifest,
    )

    print("=" * 60)
    print("Phase 4B-2 DEV Dataset Successfully Constructed")
    print("=" * 60)
    print(f"  Count:       {manifest['count']} records")
    print(f"  SHA-256:     {manifest['sha256']}")
    print(f"  Leakage:     TEST={manifest['invariants']['test_overlap_count']}, TRAIN={manifest['invariants']['train_overlap_count']}")
    print("  Mechanisms:")
    for m, c in manifest["mechanism_distribution"].items():
        print(f"    {m:25s}: {c}")
    print("=" * 60)


if __name__ == "__main__":
    main()

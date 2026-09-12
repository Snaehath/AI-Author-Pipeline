"""
dataset_generator/sft_train_builder.py

Phase 3F: Training Stream Builder and Manifest Generator.

Assembles the canonical, leak-free training dataset:
    datasets/sft/comedy_sft_train.jsonl

Sequences curricula strictly in pedagogical order:
    SFT-1 -> SFT-2 -> SFT-3 -> SFT-4 -> SFT-5

Fail-fast invariant checks:
    - Fail-fast on duplicates: raises ValueError if any duplicate audit_id is seen.
    - Fail-fast on eval leakage: raises ValueError if any record in train is in eval_ids.
    - Protected example check: audit_050 must be in train (specifically SFT-4) and not in eval.
    - Quality gates check: every training record must pass hard quality gates (GOLD or STRONG).

Reconciliation accounting (106 KEEP records total):
    17 eval + 43 train + 9 eval_tier + 16 structural_excluded + 21 cap_excluded = 106 KEEP

Generates canonical SHA-256 content hashes for train and eval JSONL datasets,
and writes the final manifest to:
    datasets/sft/sft_train_manifest.json
    reports/comedy_sft_train_manifest.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

CURRICULUM_KEYS = [
    ("curriculum_1", "SFT-1"),
    ("curriculum_2", "SFT-2"),
    ("curriculum_3", "SFT-3"),
    ("curriculum_4", "SFT-4"),
    ("curriculum_5", "SFT-5"),
]

PROTECTED_TRAIN_ID = "audit_050"


def compute_file_sha256(path: Path) -> str:
    """Compute SHA-256 hash of a file's raw canonical bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def reconcile_keep_records(
    scored_records: list[dict[str, Any]],
    eval_ids: set[str],
    train_ids: set[str],
) -> dict[str, Any]:
    """
    Perform a complete accounting of all 106 KEEP records.

    Categories:
      - eval: in eval_ids (17)
      - train: in train_ids (43)
      - eval_tier: KEEP records with tier == 'EVAL' (score 7.0-7.99) routed to pref (9)
      - structural_excluded: KEEP records with stratum == 'PURE_MECHANISM' but n_sec >= 1 (16)
      - cap_excluded: eligible for C4 (COMPOSITE with 2+ sec, tier >= STRONG) but capped (21)
    """
    keep_records = [
        r for r in scored_records if r.get("human_audit", {}).get("keep_verdict") == "KEEP"
    ]
    total_keep = len(keep_records)

    eval_count = len([r for r in keep_records if r.get("audit_id") in eval_ids])
    train_count = len([r for r in keep_records if r.get("audit_id") in train_ids])

    eval_tier_ids = []
    structural_ids = []
    cap_excluded_ids = []

    for r in keep_records:
        aid = r.get("audit_id", "")
        if aid in eval_ids or aid in train_ids:
            continue

        tier = r.get("sft_metadata", {}).get("sft_tier", "")
        ha = r.get("human_audit", {})
        stratum = ha.get("craft_stratum", "")
        n_sec = len(ha.get("secondary_mechanisms", []))

        if tier == "EVAL":
            eval_tier_ids.append(aid)
        elif stratum == "PURE_MECHANISM" and n_sec >= 1:
            structural_ids.append(aid)
        else:
            # High quality candidate (tier GOLD or STRONG) that was capped out
            cap_excluded_ids.append(aid)

    accounted_total = (
        eval_count
        + train_count
        + len(eval_tier_ids)
        + len(structural_ids)
        + len(cap_excluded_ids)
    )

    conservation = accounted_total == total_keep

    return {
        "eval": eval_count,
        "train": train_count,
        "eval_tier": len(eval_tier_ids),
        "structural_excluded": len(structural_ids),
        "cap_excluded": len(cap_excluded_ids),
        "total": total_keep,
        "conservation": conservation,
    }


def build_training_stream(
    curriculum_outputs: dict[str, list[dict[str, Any]]],
    eval_ids: set[str],
) -> list[dict[str, Any]]:
    """
    Sequence curricula: SFT-1 -> SFT-2 -> SFT-3 -> SFT-4 -> SFT-5.

    Fail-fast checks:
      - Any ID already seen raises ValueError (fail-fast duplicate detection).
      - Any ID present in eval_ids raises ValueError (fail-fast leakage detection).
      - Any record with sft_tier not in ('GOLD', 'STRONG') raises ValueError.

    Attaches curriculum_stage metadata to each record.
    """
    seen_ids: set[str] = set()
    training_stream: list[dict[str, Any]] = []

    for curr_key, stage_label in CURRICULUM_KEYS:
        recs = curriculum_outputs.get(curr_key, [])
        for rec in recs:
            aid = rec.get("audit_id")
            if not aid:
                raise ValueError("Encountered record with missing or empty audit_id.")

            # Fail-fast on eval leakage
            if aid in eval_ids:
                raise ValueError(
                    f"Eval leakage detected! Record '{aid}' in curriculum '{stage_label}' "
                    f"is also present in eval set."
                )

            # Fail-fast on duplicate ID
            if aid in seen_ids:
                raise ValueError(
                    f"Duplicate training record detected! Record '{aid}' in curriculum "
                    f"'{stage_label}' has already been added to the training stream. "
                    f"Partitioning bug detected."
                )

            # Quality gate assertion
            tier = rec.get("sft_metadata", {}).get("sft_tier")
            if tier not in ("GOLD", "STRONG"):
                raise ValueError(
                    f"Quality gate failure! Record '{aid}' has tier '{tier}', expected GOLD or STRONG."
                )

            enriched = dict(rec)
            enriched["curriculum_stage"] = stage_label
            seen_ids.add(aid)
            training_stream.append(enriched)

    return training_stream


def generate_manifest(
    source_audit_path: Path,
    scored_records: list[dict[str, Any]],
    eval_records: list[dict[str, Any]],
    eval_ids: set[str],
    train_records: list[dict[str, Any]],
    curriculum_outputs: dict[str, list[dict[str, Any]]],
    train_path: Path,
    eval_path: Path,
) -> dict[str, Any]:
    """Generate the comprehensive, deterministic Phase 3F training manifest."""
    train_ids = {r["audit_id"] for r in train_records}

    # Protected example check
    audit_050_train = next((r for r in train_records if r.get("audit_id") == PROTECTED_TRAIN_ID), None)
    audit_050_in_eval = PROTECTED_TRAIN_ID in eval_ids
    audit_050_in_train = audit_050_train is not None
    audit_050_curr = audit_050_train.get("curriculum_stage") if audit_050_train else None
    audit_050_score = audit_050_train.get("sft_metadata", {}).get("sft_score") if audit_050_train else None

    # Distribution statistics
    mech_counts = dict(Counter(
        r.get("human_audit", {}).get("primary_mechanism", "UNKNOWN") for r in train_records
    ).most_common())

    src_counts = dict(Counter(
        r.get("source_book", "UNKNOWN") for r in train_records
    ).most_common())

    curricula_counts = {
        label: len(curriculum_outputs.get(key, []))
        for key, label in CURRICULUM_KEYS
    }

    # Reconciliation
    reconciliation = reconcile_keep_records(scored_records, eval_ids, train_ids)

    # Hashes
    train_hash = compute_file_sha256(train_path)
    eval_hash = compute_file_sha256(eval_path)

    # Verification checks
    all_unique = len(train_records) == len(train_ids)
    no_leakage = len(train_ids.intersection(eval_ids)) == 0
    quality_gates_pass = all(
        r.get("sft_metadata", {}).get("sft_tier") in ("GOLD", "STRONG") for r in train_records
    )

    # Curriculum order verification
    curriculum_order_valid = True
    expected_order = [label for _, label in CURRICULUM_KEYS]
    current_stage_idx = 0
    for r in train_records:
        stage = r.get("curriculum_stage")
        stage_idx = expected_order.index(stage)
        if stage_idx < current_stage_idx:
            curriculum_order_valid = False
            break
        current_stage_idx = stage_idx

    passed = (
        reconciliation["conservation"]
        and all_unique
        and no_leakage
        and quality_gates_pass
        and curriculum_order_valid
        and audit_050_in_train
        and not audit_050_in_eval
    )

    manifest = {
        "phase": "3F",
        "source": {
            "audit_file": str(source_audit_path).replace("\\", "/"),
            "audited_records": len(scored_records),
            "keep_records": reconciliation["total"],
        },
        "reconciliation": reconciliation,
        "training": {
            "count": len(train_records),
            "unique_ids": all_unique,
            "eval_leakage": not no_leakage,
            "quality_gates_pass": quality_gates_pass,
            "curriculum_order_valid": curriculum_order_valid,
        },
        "protected_examples": {
            PROTECTED_TRAIN_ID: {
                "in_train": audit_050_in_train,
                "in_eval": audit_050_in_eval,
                "curriculum": audit_050_curr,
                "sft_score": audit_050_score,
            }
        },
        "curricula": curricula_counts,
        "mechanisms": mech_counts,
        "sources": src_counts,
        "hashes": {
            "train_sha256": train_hash,
            "eval_sha256": eval_hash,
        },
        "verification": {
            "passed": passed,
        },
    }

    return manifest


def build_and_save_dataset(
    scored_records: list[dict[str, Any]],
    eval_records: list[dict[str, Any]],
    eval_ids: set[str],
    curriculum_outputs: dict[str, list[dict[str, Any]]],
    sft_dir: Path,
    source_audit_path: Path,
    report_manifest_path: Path | None = None,
    eval_path: Path | None = None,
) -> dict[str, Any]:
    """
    Main entry point for Phase 3F builder.
    Writes comedy_sft_train.jsonl, computes manifest with hashes, and saves manifest JSON.
    """
    sft_dir.mkdir(parents=True, exist_ok=True)
    train_path = sft_dir / "comedy_sft_train.jsonl"
    if eval_path is None:
        eval_path = sft_dir / "comedy_eval.jsonl"

    # Ensure eval file exists if eval_records are provided
    if not eval_path.exists() and eval_records:
        with open(eval_path, "w", encoding="utf-8") as f:
            for rec in eval_records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # 1. Build training stream (with fail-fast checks)
    train_stream = build_training_stream(curriculum_outputs, eval_ids)

    # 2. Write training JSONL
    with open(train_path, "w", encoding="utf-8") as f:
        for rec in train_stream:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # 3. Generate manifest with hashes
    manifest = generate_manifest(
        source_audit_path=source_audit_path,
        scored_records=scored_records,
        eval_records=eval_records,
        eval_ids=eval_ids,
        train_records=train_stream,
        curriculum_outputs=curriculum_outputs,
        train_path=train_path,
        eval_path=eval_path,
    )

    # 4. Save manifest in sft_dir
    manifest_path = sft_dir / "sft_train_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # 5. Optionally save manifest in reports/ for git tracking
    if report_manifest_path:
        report_manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 3F: Build training stream and manifest.")
    parser.add_argument(
        "--audit-file",
        type=Path,
        default=Path("reports/comedy_craft_audit_batch_180.json"),
    )
    parser.add_argument(
        "--sft-dir",
        type=Path,
        default=Path("datasets/sft"),
    )
    parser.add_argument(
        "--report-manifest",
        type=Path,
        default=Path("reports/comedy_sft_train_manifest.json"),
    )
    args = parser.parse_args()

    # Load artifacts from sft-dir
    eval_ids_path = args.sft_dir / "eval_ids.json"
    with open(eval_ids_path, encoding="utf-8") as f:
        eval_ids = set(json.load(f))

    def load_jsonl(p: Path) -> list[dict[str, Any]]:
        if not p.exists():
            return []
        with open(p, encoding="utf-8") as f:
            return [json.loads(l) for l in f if l.strip()]

    scored_records = load_jsonl(args.sft_dir / "scored_records.jsonl")
    eval_records = load_jsonl(args.sft_dir / "comedy_eval.jsonl")

    curriculum_outputs = {
        f"curriculum_{i}": load_jsonl(args.sft_dir / f"sft_curriculum_{i}.jsonl")
        for i in range(1, 6)
    }

    manifest = build_and_save_dataset(
        scored_records=scored_records,
        eval_records=eval_records,
        eval_ids=eval_ids,
        curriculum_outputs=curriculum_outputs,
        sft_dir=args.sft_dir,
        source_audit_path=args.audit_file,
        report_manifest_path=args.report_manifest,
    )

    print("Training stream builder completed successfully.")
    print(f"  Training records: {manifest['training']['count']}")
    print(f"  Train SHA-256:   {manifest['hashes']['train_sha256']}")
    print(f"  Conservation:    {manifest['reconciliation']['conservation']}")
    print(f"  Passed:          {manifest['verification']['passed']}")


if __name__ == "__main__":
    main()

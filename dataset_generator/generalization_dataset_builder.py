"""
dataset_generator/generalization_dataset_builder.py

Phase 4C-1: Deterministic Generalization Benchmark Construction & Sealing.

Builds a fresh, deterministic, stratified 25-record benchmark from the unconsumed
audit records in reports/comedy_craft_audit_batch_180.json.

Guarantees & Invariants:
  1. Zero leakage across all prior splits:
       GEN_TEST ∩ TRAIN_48 = ∅
       GEN_TEST ∩ TRAIN_43 = ∅
       GEN_TEST ∩ DEV_20 = ∅
       GEN_TEST ∩ TEST_17 = ∅
  2. Unseen, mixed craft quality:
       craft_presence ∈ {"YES", "PARTIAL"}, capturing realistic out-of-sample difficulty.
  3. Predeclared stratification rule:
       Maximum feasible stratification across available mechanisms in the eligible pool.
  4. Fully deterministic selection with seed=42 and provenance logging.
  5. Sealed with SHA-256 fingerprint BEFORE any scaffold design or execution.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

DEFAULT_AUDIT_PATH = Path("reports/comedy_craft_audit_batch_180.json")
DEFAULT_CONTRASTIVE_TRAIN_PATH = Path("datasets/sft/comedy_contrastive_train.jsonl")
DEFAULT_SFT_TRAIN_PATH = Path("datasets/sft/comedy_sft_train.jsonl")
DEFAULT_DEV_PATH = Path("datasets/sft/comedy_dev.jsonl")
DEFAULT_TEST_PATH = Path("datasets/sft/comedy_eval.jsonl")

DEFAULT_OUT_PATH = Path("datasets/sft/comedy_generalization_test.jsonl")
DEFAULT_MANIFEST_PATH = Path("reports/comedy_generalization_manifest.json")

TARGET_BENCHMARK_SIZE = 25
SELECTION_SEED = 42


def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def load_ids_from_jsonl(path: Path) -> set[str]:
    """Load audit_id set from a JSONL file if it exists."""
    if not path.exists():
        return set()
    ids = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if line_str:
                rec = json.loads(line_str)
                ids.add(rec["audit_id"])
    return ids


def build_generalization_dataset(
    audit_path: Path = DEFAULT_AUDIT_PATH,
    contrastive_train_path: Path = DEFAULT_CONTRASTIVE_TRAIN_PATH,
    sft_train_path: Path = DEFAULT_SFT_TRAIN_PATH,
    dev_path: Path = DEFAULT_DEV_PATH,
    test_path: Path = DEFAULT_TEST_PATH,
    out_path: Path = DEFAULT_OUT_PATH,
    manifest_path: Path = DEFAULT_MANIFEST_PATH,
    target_count: int = TARGET_BENCHMARK_SIZE,
    seed: int = SELECTION_SEED,
) -> dict[str, Any]:
    """
    Construct, validate, and seal the fresh 25-record generalization benchmark.
    """
    if not audit_path.exists():
        raise FileNotFoundError(f"Audit batch file not found at: {audit_path}")

    with open(audit_path, encoding="utf-8") as f:
        raw_audits = json.load(f)
    audits: list[dict[str, Any]] = raw_audits if isinstance(raw_audits, list) else raw_audits.get("audits", [])

    # Collect excluded IDs
    contrastive_train_ids = load_ids_from_jsonl(contrastive_train_path)
    sft_train_ids = load_ids_from_jsonl(sft_train_path)
    dev_ids = load_ids_from_jsonl(dev_path)
    test_ids = load_ids_from_jsonl(test_path)

    all_excluded = contrastive_train_ids | sft_train_ids | dev_ids | test_ids

    # Filter eligible pool
    eligible_pool: list[dict[str, Any]] = []
    for audit in audits:
        aid = audit["audit_id"]
        ha = audit.get("human_audit", {})
        presence = ha.get("craft_presence")
        if aid not in all_excluded and presence in ("YES", "PARTIAL"):
            eligible_pool.append(audit)

    if len(eligible_pool) < target_count:
        raise ValueError(
            f"Insufficient eligible candidates in pool: found {len(eligible_pool)}, required {target_count}"
        )

    # Group eligible candidates by primary mechanism
    by_mech: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rec in sorted(eligible_pool, key=lambda x: (x.get("audit_index", 0), x["audit_id"])):
        mech = rec["human_audit"]["primary_mechanism"]
        by_mech[mech].append(rec)

    # Deterministic shuffling within each class
    rng = random.Random(seed)
    sorted_mechs = sorted(by_mech.keys())
    for m in sorted_mechs:
        rng.shuffle(by_mech[m])

    # Predeclared round-robin stratification rule
    selected: list[dict[str, Any]] = []
    while len(selected) < target_count:
        added_in_round = False
        for m in sorted_mechs:
            if by_mech[m] and len(selected) < target_count:
                selected.append(by_mech[m].pop(0))
                added_in_round = True
        if not added_in_round:
            break

    if len(selected) != target_count:
        raise RuntimeError(f"Failed to select target count: got {len(selected)}, expected {target_count}")

    # Sort final selection deterministically by audit_index
    selected.sort(key=lambda x: x.get("audit_index", 0))

    # Verify zero-leakage invariants
    selected_ids = {r["audit_id"] for r in selected}
    leak_contrastive = selected_ids & contrastive_train_ids
    leak_sft = selected_ids & sft_train_ids
    leak_dev = selected_ids & dev_ids
    leak_test = selected_ids & test_ids

    if leak_contrastive:
        raise RuntimeError(f"Leakage detected with contrastive train! IDs: {leak_contrastive}")
    if leak_sft:
        raise RuntimeError(f"Leakage detected with SFT train! IDs: {leak_sft}")
    if leak_dev:
        raise RuntimeError(f"Leakage detected with DEV! IDs: {leak_dev}")
    if leak_test:
        raise RuntimeError(f"Leakage detected with original TEST! IDs: {leak_test}")

    # Write output JSONL
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        for rec in selected:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    benchmark_sha256 = compute_sha256(out_path)

    distribution = dict(Counter(r["human_audit"]["primary_mechanism"] for r in selected).most_common())
    presence_dist = dict(Counter(r["human_audit"]["craft_presence"] for r in selected).most_common())

    manifest = {
        "benchmark_name": "comedy_generalization_test",
        "phase": "4C-1",
        "objective": "Fresh Generalization Benchmark for Inference-Time Contrastive Scaffolding",
        "n_records": len(selected),
        "target_count": target_count,
        "selection_seed": seed,
        "selection_rule": "Deterministic round-robin stratification across all available mechanisms in eligible unseen pool (craft_presence in {'YES', 'PARTIAL'})",
        "created_before_scaffold_design": True,
        "output_file": str(out_path).replace("\\", "/"),
        "sha256": benchmark_sha256,
        "source_corpus": str(audit_path).replace("\\", "/"),
        "mechanism_distribution": distribution,
        "craft_presence_distribution": presence_dist,
        "leakage_verification": {
            "contrastive_train_48_overlap": len(leak_contrastive),
            "sft_train_43_overlap": len(leak_sft),
            "dev_20_overlap": len(leak_dev),
            "original_test_17_overlap": len(leak_test),
            "status": "ZERO_LEAKAGE_VERIFIED",
        },
        "selected_audit_ids": [r["audit_id"] for r in selected],
    }

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("=" * 60)
    print("Phase 4C-1 Generalization Benchmark Sealed")
    print("=" * 60)
    print(f"  Benchmark File: {out_path} ({len(selected)} records)")
    print(f"  SHA-256:        {benchmark_sha256}")
    print(f"  Manifest:       {manifest_path}")
    print(f"  Mechanisms:     {len(distribution)} distinct classes represented")
    for m, c in distribution.items():
        print(f"    - {m:25}: {c}")
    print(f"  Craft Presence: {presence_dist}")
    print(f"  Leakage Status: ALL ZERO ({len(selected_ids)} unique unseen IDs)")
    print("=" * 60)

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Phase 4C-1 Generalization Benchmark.")
    parser.add_argument("--audit-path", type=Path, default=DEFAULT_AUDIT_PATH)
    parser.add_argument("--out-path", type=Path, default=DEFAULT_OUT_PATH)
    parser.add_argument("--manifest-path", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--count", type=int, default=TARGET_BENCHMARK_SIZE)
    parser.add_argument("--seed", type=int, default=SELECTION_SEED)
    args = parser.parse_args()

    build_generalization_dataset(
        audit_path=args.audit_path,
        out_path=args.out_path,
        manifest_path=args.manifest_path,
        target_count=args.count,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()

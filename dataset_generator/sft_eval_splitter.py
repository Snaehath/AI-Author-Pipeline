"""
dataset_generator/sft_eval_splitter.py

Phase 3E — Step 2: Stratified frozen evaluation set construction.

Strategy: For each primary mechanism, select:
    - 1 high-quality example  (highest sft_score, ≥ GOLD or STRONG tier)
    - 1 representative example (second-highest or lower quality within mechanism)

Where possible, aim for PURE_MECHANISM and COMPOSITE_CRAFT diversity within
each mechanism slot.

Target: 18–20 eval examples covering all mechanisms present in the KEEP set.
The eval IDs are written to a sidecar JSON so downstream steps can exclude them.

Output:
    datasets/sft/comedy_eval.jsonl
    datasets/sft/eval_ids.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

# Desired per-mechanism selections: (n_high, n_representative)
_PER_MECHANISM_SLOTS = (1, 1)

# Absolute upper bound on eval set size
_EVAL_SIZE_CAP = 22


def _is_keep(rec: dict[str, Any]) -> bool:
    return rec["human_audit"].get("keep_verdict") == "KEEP"


def _sft_score(rec: dict[str, Any]) -> float:
    return rec.get("sft_metadata", {}).get("sft_score", 0.0)


def _primary_mechanism(rec: dict[str, Any]) -> str:
    return rec["human_audit"].get("primary_mechanism", "UNKNOWN")


def _stratum(rec: dict[str, Any]) -> str:
    return rec["human_audit"].get("craft_stratum", "")


def build_eval_set(
    scored: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], set[str]]:
    """
    Construct the stratified frozen evaluation set.

    Returns:
        eval_records: list of selected evaluation records
        eval_ids: set of audit_id strings
    """
    # Flagship training examples that must NEVER be pulled into the eval set.
    # audit_050 is the canonical multi-mechanism SFT-4 example (Right Ho ch10).
    _PROTECTED_TRAINING_IDS: frozenset[str] = frozenset({"audit_050"})

    # Only KEEP records are eligible; protected IDs are excluded from eval
    keep = [r for r in scored if _is_keep(r) and r.get("audit_id") not in _PROTECTED_TRAINING_IDS]

    # Group by primary mechanism, sorted best-first within each group
    by_mechanism: dict[str, list[dict[str, Any]]] = {}
    for rec in keep:
        mech = _primary_mechanism(rec)
        by_mechanism.setdefault(mech, []).append(rec)

    for mech in by_mechanism:
        by_mechanism[mech].sort(
            key=lambda r: (_sft_score(r), r["audit_index"]),
            reverse=True,
        )

    eval_records: list[dict[str, Any]] = []
    eval_ids: set[str] = set()

    for mech, candidates in sorted(by_mechanism.items()):
        if len(eval_records) >= _EVAL_SIZE_CAP:
            break

        n_high, n_rep = _PER_MECHANISM_SLOTS
        selected_for_mech: list[dict[str, Any]] = []
        used_strata: set[str] = set()

        # High-quality slot: prefer stratum diversity
        for rec in candidates:
            if len(selected_for_mech) >= n_high:
                break
            s = _stratum(rec)
            if s not in used_strata or len(used_strata) == 0:
                selected_for_mech.append(rec)
                used_strata.add(s)

        # Representative slot: prefer a different stratum and lower score
        # than the high-quality pick
        high_score = _sft_score(selected_for_mech[0]) if selected_for_mech else 10.0
        for rec in reversed(candidates):  # lower scores first
            if len(selected_for_mech) >= n_high + n_rep:
                break
            if rec["audit_id"] in {r["audit_id"] for r in selected_for_mech}:
                continue
            if _sft_score(rec) <= high_score:
                selected_for_mech.append(rec)

        for rec in selected_for_mech:
            if rec["audit_id"] not in eval_ids and len(eval_records) < _EVAL_SIZE_CAP:
                eval_records.append(rec)
                eval_ids.add(rec["audit_id"])

    return eval_records, eval_ids


def write_eval_set(
    eval_records: list[dict[str, Any]],
    eval_ids: set[str],
    out_dir: Path,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    eval_path = out_dir / "comedy_eval.jsonl"
    ids_path = out_dir / "eval_ids.json"

    with open(eval_path, "w", encoding="utf-8") as f:
        for rec in eval_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    with open(ids_path, "w", encoding="utf-8") as f:
        json.dump(sorted(eval_ids), f, indent=2)

    print(f"Eval set: {len(eval_records)} records -> {eval_path}")
    print(f"Eval IDs: {len(eval_ids)} -> {ids_path}")

    # Print per-mechanism breakdown
    mech_counts: dict[str, int] = {}
    for rec in eval_records:
        m = _primary_mechanism(rec)
        mech_counts[m] = mech_counts.get(m, 0) + 1
    print("  Eval mechanism breakdown:")
    for m, c in sorted(mech_counts.items()):
        print(f"    {m}: {c}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 3E Step 2: Build stratified frozen evaluation set."
    )
    parser.add_argument(
        "--scored-file",
        type=Path,
        default=Path("datasets/sft/scored_records.jsonl"),
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("datasets/sft"),
    )
    args = parser.parse_args()

    scored: list[dict[str, Any]] = []
    with open(args.scored_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                scored.append(json.loads(line))

    eval_records, eval_ids = build_eval_set(scored)
    write_eval_set(eval_records, eval_ids, args.out_dir)


if __name__ == "__main__":
    main()

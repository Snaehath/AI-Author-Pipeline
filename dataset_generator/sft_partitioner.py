"""
dataset_generator/sft_partitioner.py

Phase 3E — Step 3: Deterministic curriculum partitioner.

Takes the scored_records.jsonl and eval_ids.json, excludes eval records,
then assigns each remaining KEEP record to:
  - Tier files (quality view): comedy_sft_gold.jsonl, comedy_sft_strong.jsonl
  - Curriculum files (training order view): sft_curriculum_1.jsonl … sft_curriculum_5.jsonl
  - Preference candidates: comedy_preference_candidates.jsonl

Curriculum definitions:
  SFT-1: PURE_MECHANISM, 0 secondary mechanisms, score ≥ STRONG
  SFT-2: COMPOSITE_CRAFT, 0 secondary mechanisms, score ≥ STRONG
  SFT-3: COMPOSITE_CRAFT, exactly 1 secondary mechanism, score ≥ STRONG
  SFT-4: COMPOSITE_CRAFT, 2+ secondary mechanisms, score ≥ STRONG
  SFT-5: mechanism_horizon = LONG_HORIZON, score ≥ EVAL

Sorting (deterministic):
  1. sft_score DESC
  2. mechanism_rarity DESC  (mechanisms with fewer examples come first)
  3. source_rarity DESC     (books with fewer KEEP examples come first)
  4. audit_id ASC

Balance caps per curriculum:
  mechanism_cap = 5
  source_cap    = 4

Tier and curriculum files are OVERLAPPING VIEWS (same record can appear in both
comedy_sft_gold.jsonl and sft_curriculum_4.jsonl). The canonical training stream
should be built from curriculum files only, not by concatenating tier files.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

MECHANISM_CAP = 5
SOURCE_CAP = 4

# Score thresholds (must match sft_scorer.py)
TIER_GOLD = 9.0
TIER_STRONG = 8.0
TIER_EVAL = 7.0


def _sft_score(rec: dict[str, Any]) -> float:
    return rec.get("sft_metadata", {}).get("sft_score", 0.0)


def _tier(rec: dict[str, Any]) -> str:
    return rec.get("sft_metadata", {}).get("sft_tier", "EXCLUDE")


def _primary_mechanism(rec: dict[str, Any]) -> str:
    return rec["human_audit"].get("primary_mechanism", "UNKNOWN")


def _source_book(rec: dict[str, Any]) -> str:
    return rec.get("source_book", "UNKNOWN")


def _stratum(rec: dict[str, Any]) -> str:
    return rec["human_audit"].get("craft_stratum", "")


def _n_secondary(rec: dict[str, Any]) -> int:
    return len(rec["human_audit"].get("secondary_mechanisms", []))


def _horizon(rec: dict[str, Any]) -> str:
    return rec["human_audit"].get("mechanism_horizon", "LOCAL")


def _is_keep(rec: dict[str, Any]) -> bool:
    return rec["human_audit"].get("keep_verdict") == "KEEP"


def _curriculum_label(rec: dict[str, Any]) -> str | None:
    """
    Return which curriculum (1–5) a record belongs to, or None if it
    does not qualify for any SFT curriculum.
    """
    score = _sft_score(rec)
    horizon = _horizon(rec)
    stratum = _stratum(rec)
    n_sec = _n_secondary(rec)

    # SFT-5: Long-horizon, any tier ≥ EVAL
    if horizon == "LONG_HORIZON" and score >= TIER_EVAL:
        return "5"

    # SFT-1: Pure, single-mechanism
    if stratum == "PURE_MECHANISM" and n_sec == 0 and score >= TIER_STRONG:
        return "1"

    # SFT-2: Composite, 0 secondary
    if stratum == "COMPOSITE_CRAFT" and n_sec == 0 and score >= TIER_STRONG:
        return "2"

    # SFT-3: Composite, exactly 1 secondary
    if stratum == "COMPOSITE_CRAFT" and n_sec == 1 and score >= TIER_STRONG:
        return "3"

    # SFT-4: Composite, 2+ secondary
    if stratum == "COMPOSITE_CRAFT" and n_sec >= 2 and score >= TIER_STRONG:
        return "4"

    return None


def _sort_key(
    rec: dict[str, Any],
    mechanism_rarity: dict[str, int],
    source_rarity: dict[str, int],
) -> tuple:
    """
    Deterministic sort: score DESC, mechanism_rarity DESC, source_rarity DESC, audit_id ASC.
    Rarity = lower count -> higher sort priority (rarer mechanisms come first).
    We negate counts so that lower count -> higher (less negative) sort value.
    """
    return (
        -_sft_score(rec),
        mechanism_rarity.get(_primary_mechanism(rec), 0),
        source_rarity.get(_source_book(rec), 0),
        rec.get("audit_id", ""),
    )


def partition(
    scored: list[dict[str, Any]],
    eval_ids: set[str],
) -> dict[str, list[dict[str, Any]]]:
    """
    Partition scored KEEP records (excluding eval IDs) into curricula,
    tier files, and preference candidates.

    Returns a dict of output_name -> list[record].
    """
    keep_non_eval = [
        r
        for r in scored
        if _is_keep(r) and r.get("audit_id") not in eval_ids
    ]

    # Compute rarity weights (lower count = rarer = higher priority)
    mech_counts = Counter(_primary_mechanism(r) for r in keep_non_eval)
    src_counts = Counter(_source_book(r) for r in keep_non_eval)
    # Convert to rarity rank: rarest mechanism gets highest value
    max_mech = max(mech_counts.values(), default=1)
    max_src = max(src_counts.values(), default=1)
    mechanism_rarity = {m: max_mech - c for m, c in mech_counts.items()}
    source_rarity = {s: max_src - c for s, c in src_counts.items()}

    # Sort deterministically
    sorted_records = sorted(
        keep_non_eval,
        key=lambda r: _sort_key(r, mechanism_rarity, source_rarity),
    )

    outputs: dict[str, list[dict[str, Any]]] = {
        "gold": [],
        "strong": [],
        "curriculum_1": [],
        "curriculum_2": [],
        "curriculum_3": [],
        "curriculum_4": [],
        "curriculum_5": [],
        "preference_candidates": [],
    }

    # Track caps per curriculum
    curr_mech_counts: dict[str, Counter] = {
        f"curriculum_{i}": Counter() for i in range(1, 6)
    }
    curr_src_counts: dict[str, Counter] = {
        f"curriculum_{i}": Counter() for i in range(1, 6)
    }

    for rec in sorted_records:
        score = _sft_score(rec)
        tier = _tier(rec)

        # Tier files (quality view, no cap)
        if tier == "GOLD":
            outputs["gold"].append(rec)
        elif tier == "STRONG":
            outputs["strong"].append(rec)
        elif tier == "EVAL":
            # Eval tier (score 7–<8): goes to preference candidates
            outputs["preference_candidates"].append(rec)
            continue  # does not enter curricula
        else:
            # EXCLUDE
            continue

        # Curriculum assignment
        curr_key = _curriculum_label(rec)
        if curr_key is None:
            continue

        curriculum_name = f"curriculum_{curr_key}"
        mech = _primary_mechanism(rec)
        src = _source_book(rec)

        mech_ok = curr_mech_counts[curriculum_name][mech] < MECHANISM_CAP
        src_ok = curr_src_counts[curriculum_name][src] < SOURCE_CAP

        if mech_ok and src_ok:
            outputs[curriculum_name].append(rec)
            curr_mech_counts[curriculum_name][mech] += 1
            curr_src_counts[curriculum_name][src] += 1

    # Add PARTIAL records to preference candidates (from all records)
    partial_records = [
        r for r in scored if r["human_audit"].get("craft_presence") == "PARTIAL"
    ]
    outputs["preference_candidates"].extend(partial_records)

    return outputs


def write_balance_report(
    outputs: dict[str, list[dict[str, Any]]],
    eval_records: list[dict[str, Any]],
    out_path: Path,
) -> None:
    """Write sft_balance_report.json with per-tier/mechanism/source statistics."""

    def stats_for(records: list[dict[str, Any]]) -> dict:
        mechanisms = Counter(_primary_mechanism(r) for r in records)
        sources = Counter(_source_book(r) for r in records)
        strata = Counter(_stratum(r) for r in records)
        scores = [_sft_score(r) for r in records]
        return {
            "count": len(records),
            "mechanisms": dict(mechanisms.most_common()),
            "sources": dict(sources.most_common()),
            "strata": dict(strata),
            "score_min": round(min(scores), 3) if scores else None,
            "score_max": round(max(scores), 3) if scores else None,
            "score_mean": round(sum(scores) / len(scores), 3) if scores else None,
        }

    report = {
        "tier_files": {
            name: stats_for(recs)
            for name, recs in outputs.items()
            if name in ("gold", "strong")
        },
        "eval_set": stats_for(eval_records),
        "curricula": {
            name: stats_for(recs)
            for name, recs in outputs.items()
            if name.startswith("curriculum_")
        },
        "preference_candidates": stats_for(outputs["preference_candidates"]),
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Balance report -> {out_path}")


def write_outputs(
    outputs: dict[str, list[dict[str, Any]]],
    out_dir: Path,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    name_map = {
        "gold": "comedy_sft_gold.jsonl",
        "strong": "comedy_sft_strong.jsonl",
        "curriculum_1": "sft_curriculum_1.jsonl",
        "curriculum_2": "sft_curriculum_2.jsonl",
        "curriculum_3": "sft_curriculum_3.jsonl",
        "curriculum_4": "sft_curriculum_4.jsonl",
        "curriculum_5": "sft_curriculum_5.jsonl",
        "preference_candidates": "comedy_preference_candidates.jsonl",
    }
    for key, filename in name_map.items():
        records = outputs.get(key, [])
        path = out_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"  {filename}: {len(records)} records")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 3E Step 3: Deterministic curriculum partitioner."
    )
    parser.add_argument(
        "--scored-file",
        type=Path,
        default=Path("datasets/sft/scored_records.jsonl"),
    )
    parser.add_argument(
        "--eval-ids-file",
        type=Path,
        default=Path("datasets/sft/eval_ids.json"),
    )
    parser.add_argument(
        "--eval-file",
        type=Path,
        default=Path("datasets/sft/comedy_eval.jsonl"),
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

    with open(args.eval_ids_file, encoding="utf-8") as f:
        eval_ids: set[str] = set(json.load(f))

    eval_records: list[dict[str, Any]] = []
    with open(args.eval_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                eval_records.append(json.loads(line))

    outputs = partition(scored, eval_ids)

    print("\nPartition results:")
    write_outputs(outputs, args.out_dir)
    write_balance_report(outputs, eval_records, args.out_dir / "sft_balance_report.json")


if __name__ == "__main__":
    main()

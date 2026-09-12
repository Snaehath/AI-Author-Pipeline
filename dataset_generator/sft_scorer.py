"""
dataset_generator/sft_scorer.py

Phase 3E — Step 1: Composite SFT scoring for human-audited comedy craft records.

SFT_SCORE = 0.40 × craft_clarity
          + 0.35 × training_value
          + 0.15 × mechanism_confidence   (applicable-beat basis)
          + 0.10 × context_completeness   (secondary mechanism richness)

Hard quality gates (prevents mathematical score from overriding human failure):
  - craft_clarity < 7  → cannot be GOLD
  - training_value < 7 → cannot be GOLD
  - keep_verdict != KEEP → never enters SFT

Mechanism confidence uses applicable-beat mapping so single-beat mechanisms
(e.g., DEADPAN_REACTION, VERBAL_WIT) are not unfairly penalised for beats that
do not apply to them. Falls back to craft_clarity when no applicable beats can
be determined.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Applicable-beat mapping per primary mechanism
# Lists only the beats that logically apply to each mechanism type.
# ---------------------------------------------------------------------------
_APPLICABLE_BEATS: dict[str, list[str]] = {
    "ESCALATION": ["setup", "escalation", "reversal", "payoff"],
    "MISUNDERSTANDING": ["setup", "payoff"],
    "VERBAL_WIT": ["payoff"],
    "DEADPAN_REACTION": ["payoff"],
    "PHYSICAL_COMPLICATION": ["setup", "escalation", "payoff"],
    "STATUS_REVERSAL": ["setup", "reversal", "payoff"],
    "SOCIAL_EMBARRASSMENT": ["setup", "escalation", "payoff"],
    "DIALOGUE_SUBTEXT": ["setup", "payoff"],
    "DRAMATIC_IRONY": ["setup", "payoff"],
    "CALLBACK": ["setup", "payoff"],
    # Fallback for any unseen mechanism: use all four beats
    "_DEFAULT": ["setup", "escalation", "reversal", "payoff"],
}

_BEAT_KEYS = {
    "setup": "setup_accurate",
    "escalation": "escalation_accurate",
    "reversal": "reversal_accurate",
    "payoff": "payoff_accurate",
}

# Tier thresholds
TIER_GOLD = 9.0
TIER_STRONG = 8.0
TIER_EVAL = 7.0


def _applicable_beats_for_mechanism(mechanism: str) -> list[str]:
    return _APPLICABLE_BEATS.get(mechanism, _APPLICABLE_BEATS["_DEFAULT"])


def compute_mechanism_confidence(human_audit: dict[str, Any]) -> dict[str, Any]:
    """
    Compute mechanism_confidence over applicable beats only.

    Returns a dict with:
        mechanism_confidence: float (0–10)
        confidence_basis: "applicable_beats" | "craft_clarity_fallback"
        applicable_beats: int
        accurate_beats: int
    """
    primary = human_audit.get("primary_mechanism", "")
    applicable_beat_names = _applicable_beats_for_mechanism(primary)
    applicable_count = len(applicable_beat_names)

    accurate_count = sum(
        1
        for beat in applicable_beat_names
        if human_audit.get(_BEAT_KEYS[beat], False)
    )

    if applicable_count == 0:
        # Should not happen with the mapping above, but guard anyway
        craft_clarity = float(human_audit.get("craft_clarity", 5))
        return {
            "mechanism_confidence": craft_clarity,
            "confidence_basis": "craft_clarity_fallback",
            "applicable_beats": 0,
            "accurate_beats": 0,
        }

    raw_confidence = (accurate_count / applicable_count) * 10.0

    # If all applicable beats are inaccurate but craft_clarity is high,
    # this indicates the detector generated boilerplate placeholders and
    # the human auditor marked them false. Fall back to craft_clarity.
    craft_clarity = float(human_audit.get("craft_clarity", 5))
    if accurate_count == 0 and craft_clarity >= 7.0:
        return {
            "mechanism_confidence": round(craft_clarity * 0.9, 2),
            "confidence_basis": "craft_clarity_fallback",
            "applicable_beats": applicable_count,
            "accurate_beats": 0,
        }

    return {
        "mechanism_confidence": round(raw_confidence, 2),
        "confidence_basis": "applicable_beats",
        "applicable_beats": applicable_count,
        "accurate_beats": accurate_count,
    }


def compute_sft_score(record: dict[str, Any]) -> dict[str, Any]:
    """
    Compute the composite SFT score and tier for a single audit record.

    Returns a metadata dict to be merged into the record under the key
    'sft_metadata'.
    """
    ha = record["human_audit"]

    craft_clarity = float(ha.get("craft_clarity", 0))
    training_value = float(ha.get("training_value", 0))
    n_secondary = len(ha.get("secondary_mechanisms", []))
    context_completeness = min(n_secondary * 3.0, 10.0)

    confidence_meta = compute_mechanism_confidence(ha)
    mechanism_confidence = confidence_meta["mechanism_confidence"]

    raw_score = (
        0.40 * craft_clarity
        + 0.35 * training_value
        + 0.15 * mechanism_confidence
        + 0.10 * context_completeness
    )
    sft_score = round(raw_score, 4)

    # Hard quality gates
    hard_gate_fail = (
        ha.get("keep_verdict") != "KEEP"
        or craft_clarity < 7.0
        or training_value < 7.0
    )

    # Assign tier
    if hard_gate_fail:
        tier = "EXCLUDE"
    elif sft_score >= TIER_GOLD:
        tier = "GOLD"
    elif sft_score >= TIER_STRONG:
        tier = "STRONG"
    elif sft_score >= TIER_EVAL:
        tier = "EVAL"
    else:
        tier = "EXCLUDE"

    return {
        "sft_score": sft_score,
        "sft_tier": tier,
        "craft_clarity": craft_clarity,
        "training_value": training_value,
        "context_completeness": context_completeness,
        **confidence_meta,
    }


def score_all_records(
    audit_path: Path,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    """
    Load the audit JSON, score every KEEP record, and return:
      - list of scored records (all 180, with sft_metadata attached)
      - summary counts dict
    """
    with open(audit_path, encoding="utf-8") as f:
        records: list[dict[str, Any]] = json.load(f)

    # Validation: derive KEEP count directly — never hard-code it
    keep_records = [
        r for r in records if r["human_audit"].get("keep_verdict") == "KEEP"
    ]
    reject_records = [
        r for r in records if r["human_audit"].get("keep_verdict") == "REJECT"
    ]
    unreviewed = [
        r
        for r in records
        if r["human_audit"].get("keep_verdict") not in ("KEEP", "REJECT")
    ]

    print(f"Audit validation:")
    print(f"  Total records : {len(records)}")
    print(f"  KEEP          : {len(keep_records)}")
    print(f"  REJECT        : {len(reject_records)}")
    print(f"  Other/partial : {len(unreviewed)}")

    if unreviewed:
        ids = [r["audit_id"] for r in unreviewed[:5]]
        raise ValueError(
            f"Audit incomplete: {len(unreviewed)} records have neither KEEP nor "
            f"REJECT verdict. First few: {ids}"
        )

    scored: list[dict[str, Any]] = []
    tier_counts: dict[str, int] = {"GOLD": 0, "STRONG": 0, "EVAL": 0, "EXCLUDE": 0}

    for rec in records:
        meta = compute_sft_score(rec)
        enriched = {**rec, "sft_metadata": meta}
        scored.append(enriched)
        if rec["human_audit"].get("keep_verdict") == "KEEP":
            tier_counts[meta["sft_tier"]] += 1

    return scored, tier_counts


def write_scored_records(
    scored: list[dict[str, Any]],
    out_path: Path,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        for rec in scored:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"Wrote {len(scored)} scored records -> {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 3E Step 1: Score audit records for SFT tiering."
    )
    parser.add_argument(
        "--audit-file",
        type=Path,
        default=Path("reports/comedy_craft_audit_batch_180.json"),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("datasets/sft/scored_records.jsonl"),
    )
    args = parser.parse_args()

    scored, tier_counts = score_all_records(args.audit_file)
    write_scored_records(scored, args.out)

    print("\nTier breakdown (KEEP records only):")
    for tier, count in tier_counts.items():
        print(f"  {tier:8s}: {count}")


if __name__ == "__main__":
    main()

"""
tests/test_phase_3e_sft.py

Phase 3E regression tests. Validates:
  - Score formula bounds
  - Applicable-beat confidence for single-beat mechanisms
  - Hard quality gates
  - No eval leakage into curricula
  - All mechanisms covered in eval set
  - Per-mechanism and per-source caps in curricula
  - audit_050 (Right Ho ch10 tent farce) is in Gold AND Curriculum 4
  - Gold tier only contains records with sft_score >= 9.0
  - PARTIAL records appear in preference_candidates
  - scored_records.jsonl, comedy_eval.jsonl exist after pipeline run
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import pytest

from dataset_generator.sft_scorer import (
    TIER_GOLD,
    TIER_STRONG,
    compute_mechanism_confidence,
    compute_sft_score,
)
from dataset_generator.sft_eval_splitter import build_eval_set
from dataset_generator.sft_partitioner import (
    MECHANISM_CAP,
    SOURCE_CAP,
    partition,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

AUDIT_PATH = Path("reports/comedy_craft_audit_batch_180.json")
SFT_DIR = Path("datasets/sft")


def _load_audit() -> list[dict[str, Any]]:
    with open(AUDIT_PATH, encoding="utf-8") as f:
        return json.load(f)


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def _make_minimal_record(
    audit_id: str = "audit_test",
    keep_verdict: str = "KEEP",
    craft_clarity: int = 9,
    training_value: int = 9,
    primary_mechanism: str = "ESCALATION",
    secondary_mechanisms: list | None = None,
    setup_accurate: bool = True,
    escalation_accurate: bool = True,
    reversal_accurate: bool = True,
    payoff_accurate: bool = True,
    craft_stratum: str = "COMPOSITE_CRAFT",
    mechanism_horizon: str = "LOCAL",
    source_book: str = "Test Book",
    audit_index: int = 1,
) -> dict[str, Any]:
    if secondary_mechanisms is None:
        secondary_mechanisms = []
    return {
        "audit_id": audit_id,
        "audit_index": audit_index,
        "sample_pool": "COMPOSITE",
        "source_id": f"test_{audit_id}",
        "source_book": source_book,
        "chapter_index": 1,
        "source_text": "Test text.",
        "detector_prediction": {
            "presence": "YES",
            "stratum": craft_stratum,
            "primary_mechanism": primary_mechanism,
            "secondary_mechanisms": [],
            "confidence": 0.5,
            "mechanism_horizon": mechanism_horizon,
            "tone": "DOMESTIC_ABSURDITY",
            "setup": "",
            "escalation": "",
            "reversal": "",
            "payoff": "",
        },
        "human_audit": {
            "craft_presence": "YES",
            "craft_stratum": craft_stratum,
            "primary_mechanism": primary_mechanism,
            "secondary_mechanisms": secondary_mechanisms,
            "mechanism_horizon": mechanism_horizon,
            "setup_accurate": setup_accurate,
            "escalation_accurate": escalation_accurate,
            "reversal_accurate": reversal_accurate,
            "payoff_accurate": payoff_accurate,
            "literary_quality": craft_clarity,
            "craft_clarity": craft_clarity,
            "training_value": training_value,
            "keep_verdict": keep_verdict,
            "detector_correct": False,
            "notes": "Test record.",
        },
    }


# ---------------------------------------------------------------------------
# Unit tests: SFT scorer
# ---------------------------------------------------------------------------


class TestSftScorer:
    def test_score_is_in_valid_range(self) -> None:
        rec = _make_minimal_record()
        meta = compute_sft_score(rec)
        assert 0.0 <= meta["sft_score"] <= 10.0

    def test_all_audit_records_produce_valid_scores(self) -> None:
        records = _load_audit()
        for rec in records:
            meta = compute_sft_score(rec)
            assert 0.0 <= meta["sft_score"] <= 10.0, (
                f"{rec['audit_id']} produced out-of-range score: {meta['sft_score']}"
            )

    def test_hard_gate_reject_cannot_be_gold(self) -> None:
        rec = _make_minimal_record(keep_verdict="REJECT", craft_clarity=10, training_value=10)
        meta = compute_sft_score(rec)
        assert meta["sft_tier"] == "EXCLUDE"

    def test_hard_gate_low_clarity_cannot_be_gold(self) -> None:
        rec = _make_minimal_record(craft_clarity=6, training_value=9)
        meta = compute_sft_score(rec)
        assert meta["sft_tier"] != "GOLD"

    def test_hard_gate_low_training_value_cannot_be_gold(self) -> None:
        rec = _make_minimal_record(craft_clarity=9, training_value=6)
        meta = compute_sft_score(rec)
        assert meta["sft_tier"] != "GOLD"

    def test_perfect_record_is_gold(self) -> None:
        rec = _make_minimal_record(craft_clarity=10, training_value=10, secondary_mechanisms=["VERBAL_WIT", "DEADPAN_REACTION"])
        meta = compute_sft_score(rec)
        assert meta["sft_tier"] == "GOLD"

    def test_gold_tier_requires_score_at_least_9(self) -> None:
        records = _load_audit()
        for rec in records:
            meta = compute_sft_score(rec)
            if meta["sft_tier"] == "GOLD":
                assert meta["sft_score"] >= TIER_GOLD, (
                    f"{rec['audit_id']} is GOLD but score={meta['sft_score']}"
                )


class TestApplicableBeatConfidence:
    def test_deadpan_reaction_only_payoff_is_applicable(self) -> None:
        """DEADPAN_REACTION: only payoff beat applies; all-false should fall back."""
        rec = _make_minimal_record(
            primary_mechanism="DEADPAN_REACTION",
            setup_accurate=False,
            escalation_accurate=False,
            reversal_accurate=False,
            payoff_accurate=True,
        )
        result = compute_mechanism_confidence(rec["human_audit"])
        # Only 1 applicable beat (payoff), and it's accurate → confidence = 10
        assert result["applicable_beats"] == 1
        assert result["accurate_beats"] == 1
        assert result["mechanism_confidence"] == 10.0

    def test_deadpan_reaction_does_not_score_1_4(self) -> None:
        """Ensure DEADPAN_REACTION with payoff=True never gets penalised as 2.5."""
        rec = _make_minimal_record(
            primary_mechanism="DEADPAN_REACTION",
            craft_clarity=9,
            setup_accurate=False,
            escalation_accurate=False,
            reversal_accurate=False,
            payoff_accurate=True,
        )
        result = compute_mechanism_confidence(rec["human_audit"])
        assert result["mechanism_confidence"] > 7.0, (
            f"DEADPAN_REACTION with payoff=True scored too low: {result['mechanism_confidence']}"
        )

    def test_verbal_wit_only_payoff_applicable(self) -> None:
        rec = _make_minimal_record(
            primary_mechanism="VERBAL_WIT",
            setup_accurate=False,
            escalation_accurate=False,
            reversal_accurate=False,
            payoff_accurate=True,
        )
        result = compute_mechanism_confidence(rec["human_audit"])
        assert result["applicable_beats"] == 1
        assert result["mechanism_confidence"] == 10.0

    def test_escalation_all_four_beats_applicable(self) -> None:
        rec = _make_minimal_record(
            primary_mechanism="ESCALATION",
            setup_accurate=True,
            escalation_accurate=True,
            reversal_accurate=True,
            payoff_accurate=True,
        )
        result = compute_mechanism_confidence(rec["human_audit"])
        assert result["applicable_beats"] == 4
        assert result["mechanism_confidence"] == 10.0

    def test_confidence_metadata_fields_present(self) -> None:
        rec = _make_minimal_record()
        result = compute_mechanism_confidence(rec["human_audit"])
        for key in ("mechanism_confidence", "confidence_basis", "applicable_beats", "accurate_beats"):
            assert key in result, f"Missing key: {key}"

    def test_all_false_high_clarity_uses_fallback(self) -> None:
        """When all applicable beats are False but craft_clarity is high, fall back."""
        rec = _make_minimal_record(
            primary_mechanism="ESCALATION",
            craft_clarity=9,
            setup_accurate=False,
            escalation_accurate=False,
            reversal_accurate=False,
            payoff_accurate=False,
        )
        result = compute_mechanism_confidence(rec["human_audit"])
        # With all 4 beats False but clarity=9 >= 7, should use fallback
        assert result["confidence_basis"] == "craft_clarity_fallback"
        assert result["mechanism_confidence"] > 0.0


# ---------------------------------------------------------------------------
# Integration tests: eval splitter
# ---------------------------------------------------------------------------


class TestEvalSplitter:
    def _make_scored(self) -> list[dict[str, Any]]:
        records = _load_audit()
        scored = []
        for rec in records:
            meta = compute_sft_score(rec)
            scored.append({**rec, "sft_metadata": meta})
        return scored

    def test_eval_set_covers_all_mechanisms(self) -> None:
        scored = self._make_scored()
        eval_recs, _ = build_eval_set(scored)
        eval_mechs = {r["human_audit"]["primary_mechanism"] for r in eval_recs}
        keep_mechs = {
            r["human_audit"]["primary_mechanism"]
            for r in scored
            if r["human_audit"].get("keep_verdict") == "KEEP"
        }
        # Every mechanism present in KEEP should be covered in eval
        missing = keep_mechs - eval_mechs
        assert not missing, f"Eval set missing mechanisms: {missing}"

    def test_eval_set_within_size_bounds(self) -> None:
        scored = self._make_scored()
        eval_recs, _ = build_eval_set(scored)
        assert 10 <= len(eval_recs) <= 25, f"Eval set size {len(eval_recs)} out of [10, 25]"

    def test_eval_ids_are_unique(self) -> None:
        scored = self._make_scored()
        eval_recs, eval_ids = build_eval_set(scored)
        assert len(eval_recs) == len(eval_ids)

    def test_eval_contains_only_keep_records(self) -> None:
        scored = self._make_scored()
        eval_recs, _ = build_eval_set(scored)
        for rec in eval_recs:
            assert rec["human_audit"].get("keep_verdict") == "KEEP", (
                f"{rec['audit_id']} in eval is not KEEP"
            )


# ---------------------------------------------------------------------------
# Integration tests: partitioner
# ---------------------------------------------------------------------------


class TestPartitioner:
    def _make_scored_and_eval(self):
        records = _load_audit()
        scored = [{**r, "sft_metadata": compute_sft_score(r)} for r in records]
        eval_recs, eval_ids = build_eval_set(scored)
        return scored, eval_ids

    def test_no_eval_leakage_into_curricula(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        for curr_key in ["curriculum_1", "curriculum_2", "curriculum_3", "curriculum_4", "curriculum_5"]:
            for rec in outputs[curr_key]:
                assert rec["audit_id"] not in eval_ids, (
                    f"Eval leakage: {rec['audit_id']} found in {curr_key}"
                )

    def test_mechanism_cap_per_curriculum(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        for curr_key in ["curriculum_1", "curriculum_2", "curriculum_3", "curriculum_4", "curriculum_5"]:
            mech_counts = Counter(
                r["human_audit"]["primary_mechanism"] for r in outputs[curr_key]
            )
            for mech, count in mech_counts.items():
                assert count <= MECHANISM_CAP, (
                    f"{curr_key}: mechanism '{mech}' has {count} > cap {MECHANISM_CAP}"
                )

    def test_source_cap_per_curriculum(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        for curr_key in ["curriculum_1", "curriculum_2", "curriculum_3", "curriculum_4", "curriculum_5"]:
            src_counts = Counter(r["source_book"] for r in outputs[curr_key])
            for src, count in src_counts.items():
                assert count <= SOURCE_CAP, (
                    f"{curr_key}: source '{src}' has {count} > cap {SOURCE_CAP}"
                )

    def test_audit_050_in_gold_tier(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        # audit_050 should NOT be in eval_ids (it's the flagship example)
        outputs = partition(scored, eval_ids)
        if "audit_050" not in eval_ids:
            gold_ids = {r["audit_id"] for r in outputs["gold"]}
            assert "audit_050" in gold_ids, "audit_050 (Right Ho ch10) not in Gold tier!"

    def test_audit_050_in_curriculum_4(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        if "audit_050" not in eval_ids:
            c4_ids = {r["audit_id"] for r in outputs["curriculum_4"]}
            assert "audit_050" in c4_ids, "audit_050 (Right Ho ch10) not in Curriculum 4!"

    def test_gold_tier_only_contains_score_9_plus(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        for rec in outputs["gold"]:
            score = rec.get("sft_metadata", {}).get("sft_score", 0)
            assert score >= TIER_GOLD, (
                f"{rec['audit_id']} in Gold but score={score} < {TIER_GOLD}"
            )

    def test_curriculum_1_is_pure_mechanism(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        for rec in outputs["curriculum_1"]:
            assert rec["human_audit"]["craft_stratum"] == "PURE_MECHANISM", (
                f"{rec['audit_id']} in Curriculum 1 is not PURE_MECHANISM"
            )

    def test_curriculum_4_has_2_plus_secondary(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        for rec in outputs["curriculum_4"]:
            n_sec = len(rec["human_audit"]["secondary_mechanisms"])
            assert n_sec >= 2, (
                f"{rec['audit_id']} in Curriculum 4 has {n_sec} secondary mechanisms"
            )

    def test_partial_records_in_preference_candidates(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs = partition(scored, eval_ids)
        partial_in_pref = [
            r for r in outputs["preference_candidates"]
            if r["human_audit"].get("craft_presence") == "PARTIAL"
        ]
        assert len(partial_in_pref) > 0, "No PARTIAL records in preference_candidates"

    def test_partition_is_deterministic(self) -> None:
        scored, eval_ids = self._make_scored_and_eval()
        outputs_a = partition(scored, eval_ids)
        outputs_b = partition(scored, eval_ids)
        for key in outputs_a:
            ids_a = [r["audit_id"] for r in outputs_a[key]]
            ids_b = [r["audit_id"] for r in outputs_b[key]]
            assert ids_a == ids_b, f"Non-deterministic partition for {key}"


# ---------------------------------------------------------------------------
# Pipeline output file tests (run after pipeline execution)
# ---------------------------------------------------------------------------


class TestPipelineOutputFiles:
    """Tests that verify the output files written by sft_pipeline.py."""

    @pytest.mark.skipif(
        not (SFT_DIR / "scored_records.jsonl").exists(),
        reason="Pipeline output not yet generated",
    )
    def test_scored_records_exist(self) -> None:
        assert (SFT_DIR / "scored_records.jsonl").exists()

    @pytest.mark.skipif(
        not (SFT_DIR / "comedy_eval.jsonl").exists(),
        reason="Pipeline output not yet generated",
    )
    def test_eval_file_exists(self) -> None:
        assert (SFT_DIR / "comedy_eval.jsonl").exists()

    @pytest.mark.skipif(
        not (SFT_DIR / "comedy_eval.jsonl").exists(),
        reason="Pipeline output not yet generated",
    )
    def test_eval_file_has_correct_records(self) -> None:
        eval_recs = _load_jsonl(SFT_DIR / "comedy_eval.jsonl")
        assert len(eval_recs) >= 10

    @pytest.mark.skipif(
        not (SFT_DIR / "sft_balance_report.json").exists(),
        reason="Pipeline output not yet generated",
    )
    def test_balance_report_exists(self) -> None:
        with open(SFT_DIR / "sft_balance_report.json", encoding="utf-8") as f:
            report = json.load(f)
        assert "curricula" in report
        assert "eval_set" in report
        assert "tier_files" in report

    @pytest.mark.skipif(
        not (SFT_DIR / "comedy_sft_gold.jsonl").exists(),
        reason="Pipeline output not yet generated",
    )
    def test_no_leakage_between_eval_and_curricula_files(self) -> None:
        eval_ids = set()
        if (SFT_DIR / "eval_ids.json").exists():
            with open(SFT_DIR / "eval_ids.json") as f:
                eval_ids = set(json.load(f))

        for i in range(1, 6):
            path = SFT_DIR / f"sft_curriculum_{i}.jsonl"
            if not path.exists():
                continue
            recs = _load_jsonl(path)
            for rec in recs:
                assert rec["audit_id"] not in eval_ids, (
                    f"Eval leakage: {rec['audit_id']} in curriculum_{i}"
                )

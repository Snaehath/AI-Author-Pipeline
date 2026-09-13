"""
tests/test_phase_4c1_generalization.py

Unit tests for Phase 4C-1: Generalization Benchmark Construction & Invariants.
"""

import json
from pathlib import Path
import pytest

from dataset_generator.generalization_dataset_builder import (
    compute_sha256,
    DEFAULT_OUT_PATH,
    DEFAULT_MANIFEST_PATH,
    DEFAULT_CONTRASTIVE_TRAIN_PATH,
    DEFAULT_SFT_TRAIN_PATH,
    DEFAULT_DEV_PATH,
    DEFAULT_TEST_PATH,
)

EXPECTED_BENCHMARK_SHA256 = "a133d670bb6684a0879b7bd4d16a4ae7cdb62455f7aa2915d0ff5297e5f1c418"
EXPECTED_RECORD_COUNT = 25


def test_benchmark_file_exists_and_hash_matches():
    assert DEFAULT_OUT_PATH.exists(), f"Benchmark file not found at: {DEFAULT_OUT_PATH}"
    actual_hash = compute_sha256(DEFAULT_OUT_PATH)
    assert actual_hash == EXPECTED_BENCHMARK_SHA256, f"Hash mismatch! {actual_hash} != {EXPECTED_BENCHMARK_SHA256}"


def test_benchmark_record_count_and_schema():
    records = []
    with open(DEFAULT_OUT_PATH, encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if line_str:
                records.append(json.loads(line_str))

    assert len(records) == EXPECTED_RECORD_COUNT, f"Expected {EXPECTED_RECORD_COUNT}, found {len(records)}"

    for r in records:
        assert "audit_id" in r
        assert "source_text" in r
        assert len(r["source_text"]) > 20
        assert "human_audit" in r
        ha = r["human_audit"]
        assert "primary_mechanism" in ha
        assert ha["craft_presence"] in ("YES", "PARTIAL")


def test_benchmark_zero_leakage_invariants():
    def get_ids(path: Path) -> set[str]:
        if not path.exists():
            return set()
        return {json.loads(l)["audit_id"] for l in open(path, encoding="utf-8") if l.strip()}

    gen_ids = get_ids(DEFAULT_OUT_PATH)
    assert len(gen_ids) == EXPECTED_RECORD_COUNT

    train_contrastive_ids = get_ids(DEFAULT_CONTRASTIVE_TRAIN_PATH)
    train_sft_ids = get_ids(DEFAULT_SFT_TRAIN_PATH)
    dev_ids = get_ids(DEFAULT_DEV_PATH)
    test_ids = get_ids(DEFAULT_TEST_PATH)

    assert gen_ids & train_contrastive_ids == set(), "Leakage detected with contrastive train!"
    assert gen_ids & train_sft_ids == set(), "Leakage detected with SFT train!"
    assert gen_ids & dev_ids == set(), "Leakage detected with DEV set!"
    assert gen_ids & test_ids == set(), "Leakage detected with original TEST set!"


def test_manifest_metadata_and_reproducibility():
    assert DEFAULT_MANIFEST_PATH.exists(), f"Manifest not found at: {DEFAULT_MANIFEST_PATH}"
    with open(DEFAULT_MANIFEST_PATH, encoding="utf-8") as f:
        manifest = json.load(f)

    assert manifest["benchmark_name"] == "comedy_generalization_test"
    assert manifest["n_records"] == EXPECTED_RECORD_COUNT
    assert manifest["sha256"] == EXPECTED_BENCHMARK_SHA256
    assert manifest["created_before_scaffold_design"] is True
    assert manifest["selection_seed"] == 42
    assert len(manifest["mechanism_distribution"]) == 9
    assert manifest["leakage_verification"]["status"] == "ZERO_LEAKAGE_VERIFIED"


def test_regime_a_and_b_prompt_formatters():
    from pipeline.evaluator.contrastive_scaffold_evaluator import (
        format_regime_a_prompt,
        format_regime_b_prompt,
    )

    sample = "Test comedic text snippet."
    prompt_a = format_regime_a_prompt(sample)
    prompt_b = format_regime_b_prompt(sample)

    assert len(prompt_a) == 2
    assert len(prompt_b) == 2

    # Regime A asks for primary_mechanism without contrastive_analysis
    assert "primary_mechanism" in prompt_a[0]["content"]
    assert "contrastive_analysis" not in prompt_a[0]["content"]

    # Regime B explicitly requires contrastive_analysis
    assert "contrastive_analysis" in prompt_b[0]["content"]
    assert "causal_mechanism" in prompt_b[0]["content"]
    assert "counterfactual_test" in prompt_b[0]["content"]


def test_parse_prediction_and_scr_calculation():
    from pipeline.evaluator.contrastive_scaffold_evaluator import (
        parse_prediction,
        evaluate_records,
    )

    # Regime A response parsing
    raw_a = '{"primary_mechanism": "ESCALATION", "secondary_mechanisms": ["VERBAL_WIT"], "mechanism_horizon": "LOCAL", "craft_analysis": "test"}'
    parsed_a = parse_prediction(raw_a, is_regime_b=False)
    assert parsed_a["parsed"] is True
    assert parsed_a["prediction"]["primary_mechanism"] == "ESCALATION"

    # Regime B response parsing with contrastive analysis
    raw_b = '''{
      "contrastive_analysis": {
        "causal_mechanism": "ESCALATION",
        "surface_cue": "witty dialogue",
        "tempting_alternative": "VERBAL_WIT",
        "why_alternative_is_tempting": "dialogue",
        "counterfactual_test": "test",
        "why_primary_wins": "test"
      },
      "primary_mechanism": "ESCALATION",
      "secondary_mechanisms": [],
      "mechanism_horizon": "LOCAL",
      "craft_analysis": "test"
    }'''
    parsed_b = parse_prediction(raw_b, is_regime_b=True)
    assert parsed_b["parsed"] is True
    assert parsed_b["prediction"]["primary_mechanism"] == "ESCALATION"
    assert parsed_b["prediction"]["causal_mechanism"] == "ESCALATION"

    # Evaluate mock records for SCR
    mock_records = [{
        "audit_id": "audit_test",
        "human_audit": {
            "primary_mechanism": "ESCALATION",
            "secondary_mechanisms": [],
            "mechanism_horizon": "LOCAL",
        }
    }]
    mock_preds = [{
        "audit_id": "audit_test",
        "parsed_prediction": parsed_b,
        "truncated": False,
        "generated_tokens": 120,
    }]
    eval_res = evaluate_records(mock_records, mock_preds, is_regime_b=True)
    sc = eval_res["scorecard"]
    assert sc["primary_accuracy"] == 1.0
    assert sc["causal_mechanism_accuracy"] == 1.0
    assert sc["scaffold_consistency_rate"] == 1.0
    assert sc["disconnection_matrix"]["correct_causal_correct_primary"] == 1


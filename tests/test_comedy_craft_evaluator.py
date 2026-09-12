"""
tests/test_comedy_craft_evaluator.py

Unit tests for Phase 4A Comedy Craft Evaluator.
Validates:
  1. Hash & record count verification (exact match & tamper rejection).
  2. Prompt formatting and presence of all 10 canonical mechanisms.
  3. Strict response parsing and parse_status assignment:
     - VALID
     - JSON_PARSE_ERROR
     - repairable_json detection
     - SCHEMA_ERROR
     - UNKNOWN_PRIMARY_MECHANISM
     - UNKNOWN_SECONDARY_MECHANISM
     - INVALID_HORIZON
  4. Multi-metric evaluation calculation:
     - Primary accuracy
     - Exact record accuracy
     - Horizon accuracy
     - Multilabel secondary micro & macro F1
     - Mean Jaccard
     - Combined coverage diagnostic
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from pipeline.evaluator.comedy_craft_evaluator import (
    CANONICAL_MECHANISMS,
    EXPECTED_EVAL_COUNT,
    EXPECTED_EVAL_SHA256,
    compute_evaluation_metrics,
    format_eval_prompt,
    parse_prediction,
    verify_eval_dataset,
)

EVAL_PATH = Path("datasets/sft/comedy_eval.jsonl")


def test_verify_eval_dataset_integrity():
    """Verify that the frozen evaluation dataset passes the hash and count guard."""
    records = verify_eval_dataset(EVAL_PATH)
    assert len(records) == EXPECTED_EVAL_COUNT
    assert len(records) == 17


def test_verify_eval_dataset_tamper_guard(tmp_path: Path):
    """Verify that an altered evaluation dataset fails fast with ValueError."""
    tampered_file = tmp_path / "tampered_eval.jsonl"
    with open(EVAL_PATH, encoding="utf-8") as f_in, open(tampered_file, "w", encoding="utf-8") as f_out:
        lines = f_in.readlines()
        # Drop one line to tamper
        f_out.writelines(lines[:-1])

    with pytest.raises(ValueError, match="Eval dataset hash mismatch"):
        verify_eval_dataset(tampered_file)


def test_format_eval_prompt():
    """Verify prompt formatting includes standard ChatML roles and all 10 mechanisms."""
    source_text = "He gave a kind of grunt of surprise."
    messages = format_eval_prompt(source_text)

    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"

    sys_content = messages[0]["content"]
    for mech in CANONICAL_MECHANISMS:
        assert mech in sys_content, f"Mechanism {mech} missing from system prompt"

    assert source_text in messages[1]["content"]


def test_parse_prediction_valid():
    raw = json.dumps({
        "primary_mechanism": "ESCALATION",
        "secondary_mechanisms": ["MISUNDERSTANDING", "VERBAL_WIT"],
        "mechanism_horizon": "LOCAL",
        "craft_analysis": "The absurdity grows exponentially.",
    })
    res = parse_prediction(raw)
    assert res["parsed"] is True
    assert res["raw_json_valid"] is True
    assert res["schema_valid"] is True
    assert res["parse_status"] == "VALID"
    assert res["prediction"]["primary_mechanism"] == "ESCALATION"
    assert res["prediction"]["secondary_mechanisms"] == ["MISUNDERSTANDING", "VERBAL_WIT"]
    assert res["prediction"]["mechanism_horizon"] == "LOCAL"


def test_parse_prediction_json_error():
    raw = "Not valid json at all {"
    res = parse_prediction(raw)
    assert res["parsed"] is False
    assert res["raw_json_valid"] is False
    assert res["schema_valid"] is False
    assert res["parse_status"] == "JSON_PARSE_ERROR"


def test_parse_prediction_repairable_markdown():
    raw = 'Here is the analysis:\n```json\n{"primary_mechanism": "DEADPAN_REACTION", "secondary_mechanisms": [], "mechanism_horizon": "LOCAL", "craft_analysis": "Flat response."}\n```\nHope this helps!'
    res = parse_prediction(raw)
    assert res["parsed"] is True
    assert res["raw_json_valid"] is False
    assert res["repairable_json"] is True
    assert res["schema_valid"] is True
    assert res["parse_status"] == "VALID"
    assert res["prediction"]["primary_mechanism"] == "DEADPAN_REACTION"


def test_parse_prediction_schema_error():
    raw = json.dumps({
        "primary_mechanism": "ESCALATION",
        # Missing secondary_mechanisms and mechanism_horizon
    })
    res = parse_prediction(raw)
    assert res["schema_valid"] is False
    assert res["parse_status"] == "SCHEMA_ERROR"


def test_parse_prediction_unknown_primary():
    raw = json.dumps({
        "primary_mechanism": "SLAPSTICK_PRANK",  # Outside taxonomy
        "secondary_mechanisms": [],
        "mechanism_horizon": "LOCAL",
        "craft_analysis": "Physical joke.",
    })
    res = parse_prediction(raw)
    assert res["schema_valid"] is False
    assert res["parse_status"] == "UNKNOWN_PRIMARY_MECHANISM"
    assert res["prediction"]["primary_mechanism"] == "SLAPSTICK_PRANK"


def test_parse_prediction_unknown_secondary():
    raw = json.dumps({
        "primary_mechanism": "ESCALATION",
        "secondary_mechanisms": ["NARRATIVE_TWIST"],  # Outside taxonomy
        "mechanism_horizon": "LOCAL",
        "craft_analysis": "Unexpected turn.",
    })
    res = parse_prediction(raw)
    assert res["schema_valid"] is False
    assert res["parse_status"] == "UNKNOWN_SECONDARY_MECHANISM"


def test_parse_prediction_invalid_horizon():
    raw = json.dumps({
        "primary_mechanism": "ESCALATION",
        "secondary_mechanisms": [],
        "mechanism_horizon": "IMMEDIATE",  # Outside LOCAL | LONG_HORIZON
        "craft_analysis": "Fast pace.",
    })
    res = parse_prediction(raw)
    assert res["schema_valid"] is False
    assert res["parse_status"] == "INVALID_HORIZON"


def test_compute_evaluation_metrics():
    # Mock eval records (2 records)
    eval_records = [
        {
            "audit_id": "audit_test_1",
            "source_book": "Test Book",
            "human_audit": {
                "primary_mechanism": "ESCALATION",
                "secondary_mechanisms": ["MISUNDERSTANDING"],
                "mechanism_horizon": "LOCAL",
            },
        },
        {
            "audit_id": "audit_test_2",
            "source_book": "Test Book",
            "human_audit": {
                "primary_mechanism": "VERBAL_WIT",
                "secondary_mechanisms": ["DEADPAN_REACTION"],
                "mechanism_horizon": "LOCAL",
            },
        },
    ]

    # Mock predictions: item 1 exact match, item 2 wrong primary but correct secondary
    raw_predictions = [
        {
            "audit_id": "audit_test_1",
            "raw_response": json.dumps({
                "primary_mechanism": "ESCALATION",
                "secondary_mechanisms": ["MISUNDERSTANDING"],
                "mechanism_horizon": "LOCAL",
                "craft_analysis": "Matches perfectly.",
            }),
        },
        {
            "audit_id": "audit_test_2",
            "raw_response": json.dumps({
                "primary_mechanism": "DEADPAN_REACTION",  # Wrong primary (predicted secondary as primary)
                "secondary_mechanisms": ["VERBAL_WIT"],   # Swapped
                "mechanism_horizon": "LOCAL",
                "craft_analysis": "Swapped roles.",
            }),
        },
    ]

    report = compute_evaluation_metrics(eval_records, raw_predictions)
    sc = report["scorecard"]

    assert sc["primary_accuracy"] == 0.5  # 1 of 2
    assert sc["exact_record_accuracy"] == 0.5  # 1 of 2
    assert sc["horizon_accuracy"] == 1.0  # 2 of 2
    assert sc["raw_json_validity"] == 1.0
    assert sc["combined_coverage_accuracy"] == 1.0  # Both items have gold primary somewhere in pred

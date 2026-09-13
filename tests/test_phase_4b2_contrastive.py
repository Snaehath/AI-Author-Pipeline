"""
tests/test_phase_4b2_contrastive.py

Unit and regression tests for Phase 4B-2 contrastive training dataset,
schema validation, zero-leakage invariants, and cryptographic determinism.
"""

import json
from pathlib import Path

import pytest

from dataset_generator.build_contrastive_dataset import (
    DEFAULT_DEV_PATH,
    DEFAULT_MANIFEST_PATH,
    DEFAULT_OUT_PATH,
    DEFAULT_REPORT_MANIFEST_PATH,
    DEFAULT_TEST_PATH,
    compute_sha256,
)

EXPECTED_TRAIN_COUNT = 48
EXPECTED_TRAIN_SHA256 = "65f6ec332b10c375b60d8bd57427c770eac5fd91406b40de01777eb7b5353da3"


def test_contrastive_file_exists_and_count():
    assert DEFAULT_OUT_PATH.exists(), "comedy_contrastive_train.jsonl must exist"
    with open(DEFAULT_OUT_PATH, encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    assert len(records) == EXPECTED_TRAIN_COUNT


def test_contrastive_unique_ids():
    with open(DEFAULT_OUT_PATH, encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    ids = [r["audit_id"] for r in records]
    assert len(ids) == len(set(ids)), "All training audit IDs must be unique"


def test_zero_leakage_with_test():
    with open(DEFAULT_OUT_PATH, encoding="utf-8") as f:
        train_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    with open(DEFAULT_TEST_PATH, encoding="utf-8") as f:
        test_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    overlap = train_ids & test_ids
    assert len(overlap) == 0, f"Contrastive train leaks into TEST: {overlap}"


def test_zero_leakage_with_dev():
    with open(DEFAULT_OUT_PATH, encoding="utf-8") as f:
        train_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    with open(DEFAULT_DEV_PATH, encoding="utf-8") as f:
        dev_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    overlap = train_ids & dev_ids
    assert len(overlap) == 0, f"Contrastive train leaks into DEV: {overlap}"


def test_contrastive_schema_completeness():
    required_contrastive_keys = [
        "primary_mechanism",
        "causal_mechanism",
        "surface_cue",
        "tempting_alternative",
        "why_alternative_is_tempting",
        "counterfactual_test",
        "why_primary_wins",
    ]
    with open(DEFAULT_OUT_PATH, encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]

    for r in records:
        assert "contrastive_analysis" in r, f"Record {r['audit_id']} missing contrastive_analysis"
        ca = r["contrastive_analysis"]
        for k in required_contrastive_keys:
            assert k in ca, f"Record {r['audit_id']} missing {k} in contrastive_analysis"
            assert isinstance(ca[k], str) and len(ca[k].strip()) > 0, f"Record {r['audit_id']} field {k} is empty"

        # Tempting alternative must differ from primary mechanism
        assert ca["primary_mechanism"] != ca["tempting_alternative"], (
            f"Record {r['audit_id']} has identical primary and tempting alternative"
        )


def test_contrastive_hash_determinism():
    current_sha256 = compute_sha256(DEFAULT_OUT_PATH)
    assert current_sha256 == EXPECTED_TRAIN_SHA256, (
        f"Hash mismatch: expected {EXPECTED_TRAIN_SHA256}, got {current_sha256}"
    )


def test_manifest_integrity():
    assert DEFAULT_MANIFEST_PATH.exists()
    assert DEFAULT_REPORT_MANIFEST_PATH.exists()

    with open(DEFAULT_MANIFEST_PATH, encoding="utf-8") as f:
        manifest = json.load(f)

    assert manifest["count"] == EXPECTED_TRAIN_COUNT
    assert manifest["sha256"] == EXPECTED_TRAIN_SHA256
    assert manifest["invariants"]["zero_leakage_verified"] is True
    assert manifest["invariants"]["test_overlap_count"] == 0
    assert manifest["invariants"]["dev_overlap_count"] == 0
    assert manifest["tier_breakdown"]["tier1_count"] == 32
    assert manifest["tier_breakdown"]["tier2_count"] == 2

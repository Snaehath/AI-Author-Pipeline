"""
tests/test_phase_4b2_dev.py

Unit and regression tests for Phase 4B-2 DEV set partitioning, invariants, and determinism.
"""

import json
from pathlib import Path

import pytest

from dataset_generator.dev_dataset_builder import (
    DEFAULT_DEV_OUT_PATH,
    DEFAULT_MANIFEST_OUT_PATH,
    DEFAULT_REPORT_MANIFEST_PATH,
    DEFAULT_TEST_PATH,
    DEFAULT_TRAIN_PATH,
    build_dev_dataset,
    compute_sha256,
)

EXPECTED_DEV_COUNT = 20
EXPECTED_DEV_SHA256 = "18838c6ddd9bcd89d80df6e223b41bfd68cb25a1ae18976f4dd6ecd2c476829e"


def test_dev_file_exists_and_count():
    assert DEFAULT_DEV_OUT_PATH.exists(), "comedy_dev.jsonl must exist"
    with open(DEFAULT_DEV_OUT_PATH, encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    assert len(records) == EXPECTED_DEV_COUNT


def test_dev_unique_ids():
    with open(DEFAULT_DEV_OUT_PATH, encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    ids = [r["audit_id"] for r in records]
    assert len(ids) == len(set(ids)), "DEV records must have unique audit IDs"


def test_no_test_leakage():
    with open(DEFAULT_DEV_OUT_PATH, encoding="utf-8") as f:
        dev_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    with open(DEFAULT_TEST_PATH, encoding="utf-8") as f:
        test_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    overlap = dev_ids & test_ids
    assert len(overlap) == 0, f"DEV leaks into TEST: {overlap}"


def test_no_train_leakage():
    with open(DEFAULT_DEV_OUT_PATH, encoding="utf-8") as f:
        dev_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    with open(DEFAULT_TRAIN_PATH, encoding="utf-8") as f:
        train_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}
    overlap = dev_ids & train_ids
    assert len(overlap) == 0, f"DEV leaks into TRAIN: {overlap}"


def test_dev_quality_gate_all_scores_gte_8():
    with open(DEFAULT_DEV_OUT_PATH, encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    for r in records:
        score = r.get("sft_metadata", {}).get("sft_score", 0.0)
        assert score >= 8.0, f"Record {r['audit_id']} has score {score} < 8.0"


def test_dev_hash_determinism():
    current_sha256 = compute_sha256(DEFAULT_DEV_OUT_PATH)
    assert current_sha256 == EXPECTED_DEV_SHA256, f"DEV hash mismatch: expected {EXPECTED_DEV_SHA256}, got {current_sha256}"


def test_manifest_integrity():
    assert DEFAULT_MANIFEST_OUT_PATH.exists()
    assert DEFAULT_REPORT_MANIFEST_PATH.exists()

    with open(DEFAULT_MANIFEST_OUT_PATH, encoding="utf-8") as f:
        manifest = json.load(f)

    assert manifest["count"] == EXPECTED_DEV_COUNT
    assert manifest["sha256"] == EXPECTED_DEV_SHA256
    assert manifest["invariants"]["zero_leakage_verified"] is True
    assert manifest["invariants"]["test_overlap_count"] == 0
    assert manifest["invariants"]["train_overlap_count"] == 0
    assert manifest["source"]["total_keep_records"] == 106

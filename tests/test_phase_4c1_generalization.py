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

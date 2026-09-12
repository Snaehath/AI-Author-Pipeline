"""
tests/test_phase_3f_manifest.py

Phase 3F Regression & Invariant Tests.
Validates:
  1. Train file existence, exact record count (43), and ID uniqueness.
  2. Fail-fast duplicate detection in training builder.
  3. Zero eval leakage and fail-fast leakage detection in training builder.
  4. Protected example (audit_050) presence in train (SFT-4) and absence from eval.
  5. Strict curriculum ordering across the entire training sequence:
     SFT-1 -> SFT-2 -> SFT-3 -> SFT-4 -> SFT-5.
  6. Exact mathematical reconciliation conservation:
     17 eval + 43 train + 9 eval_tier + 16 structural_excluded + 21 cap_excluded = 106.
  7. Determinism: repeated builds produce byte-for-byte identical datasets and hashes.
  8. Manifest structure, schema compliance, content SHA-256 verification, and passed flag.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from dataset_generator.sft_train_builder import (
    CURRICULUM_KEYS,
    PROTECTED_TRAIN_ID,
    build_and_save_dataset,
    build_training_stream,
    compute_file_sha256,
    reconcile_keep_records,
)

AUDIT_PATH = Path("reports/comedy_craft_audit_batch_180.json")
SFT_DIR = Path("datasets/sft")
TRAIN_PATH = SFT_DIR / "comedy_sft_train.jsonl"
EVAL_PATH = SFT_DIR / "comedy_eval.jsonl"
EVAL_IDS_PATH = SFT_DIR / "eval_ids.json"
MANIFEST_PATH = SFT_DIR / "sft_train_manifest.json"
REPORT_MANIFEST_PATH = Path("reports/comedy_sft_train_manifest.json")


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    assert path.exists(), f"File {path} does not exist."
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


@pytest.fixture(scope="module")
def train_records() -> list[dict[str, Any]]:
    return _load_jsonl(TRAIN_PATH)


@pytest.fixture(scope="module")
def eval_records() -> list[dict[str, Any]]:
    return _load_jsonl(EVAL_PATH)


@pytest.fixture(scope="module")
def eval_ids() -> set[str]:
    with open(EVAL_IDS_PATH, encoding="utf-8") as f:
        return set(json.load(f))


@pytest.fixture(scope="module")
def manifest() -> dict[str, Any]:
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Test 1: File existence, count, uniqueness
# ---------------------------------------------------------------------------

def test_train_file_exists_and_count(train_records: list[dict[str, Any]]):
    assert len(train_records) == 43, f"Expected 43 training records, found {len(train_records)}"
    ids = [r["audit_id"] for r in train_records]
    assert len(ids) == len(set(ids)), "Duplicate audit_id found in comedy_sft_train.jsonl"


# ---------------------------------------------------------------------------
# Test 2: Fail-fast duplicate check
# ---------------------------------------------------------------------------

def test_builder_fail_fast_on_duplicates(eval_ids: set[str]):
    dummy_rec = {
        "audit_id": "audit_test_dup",
        "sft_metadata": {"sft_tier": "GOLD", "sft_score": 9.5},
        "human_audit": {"craft_stratum": "PURE_MECHANISM", "secondary_mechanisms": []},
    }
    curriculum_outputs = {
        "curriculum_1": [dummy_rec],
        "curriculum_2": [],
        "curriculum_3": [dummy_rec],  # Duplicate in curriculum 3
        "curriculum_4": [],
        "curriculum_5": [],
    }

    with pytest.raises(ValueError, match="Duplicate training record detected"):
        build_training_stream(curriculum_outputs, eval_ids)


# ---------------------------------------------------------------------------
# Test 3: Zero eval leakage & fail-fast leakage detection
# ---------------------------------------------------------------------------

def test_no_eval_leakage(train_records: list[dict[str, Any]], eval_ids: set[str]):
    train_ids = {r["audit_id"] for r in train_records}
    leakage = train_ids.intersection(eval_ids)
    assert len(leakage) == 0, f"Eval leakage detected: {leakage}"


def test_builder_fail_fast_on_eval_leakage(eval_ids: set[str]):
    leak_id = next(iter(eval_ids))
    dummy_rec = {
        "audit_id": leak_id,
        "sft_metadata": {"sft_tier": "GOLD", "sft_score": 9.5},
        "human_audit": {"craft_stratum": "PURE_MECHANISM", "secondary_mechanisms": []},
    }
    curriculum_outputs = {
        "curriculum_1": [dummy_rec],
        "curriculum_2": [],
        "curriculum_3": [],
        "curriculum_4": [],
        "curriculum_5": [],
    }

    with pytest.raises(ValueError, match="Eval leakage detected"):
        build_training_stream(curriculum_outputs, eval_ids)


# ---------------------------------------------------------------------------
# Test 4: Protected example (audit_050) check
# ---------------------------------------------------------------------------

def test_protected_example_in_training_and_not_eval(
    train_records: list[dict[str, Any]],
    eval_ids: set[str],
):
    assert PROTECTED_TRAIN_ID not in eval_ids, f"{PROTECTED_TRAIN_ID} leaked into eval set"

    match = next((r for r in train_records if r.get("audit_id") == PROTECTED_TRAIN_ID), None)
    assert match is not None, f"{PROTECTED_TRAIN_ID} not found in training records"
    assert match.get("curriculum_stage") == "SFT-4"
    assert match.get("sft_metadata", {}).get("sft_score") == 10.0


# ---------------------------------------------------------------------------
# Test 5: Strict curriculum ordering verification
# ---------------------------------------------------------------------------

def test_strict_curriculum_ordering(train_records: list[dict[str, Any]]):
    expected_order = [label for _, label in CURRICULUM_KEYS]
    current_idx = 0

    stage_counts = {label: 0 for label in expected_order}

    for rec in train_records:
        stage = rec.get("curriculum_stage")
        assert stage in expected_order, f"Unknown curriculum stage: {stage}"
        idx = expected_order.index(stage)
        assert idx >= current_idx, (
            f"Curriculum ordering violated: record {rec.get('audit_id')} with stage "
            f"{stage} (index {idx}) appeared after stage index {current_idx}."
        )
        current_idx = idx
        stage_counts[stage] += 1

    assert stage_counts["SFT-1"] == 4
    assert stage_counts["SFT-2"] == 0
    assert stage_counts["SFT-3"] == 7
    assert stage_counts["SFT-4"] == 32
    assert stage_counts["SFT-5"] == 0


# ---------------------------------------------------------------------------
# Test 6: Reconciliation conservation
# ---------------------------------------------------------------------------

def test_reconciliation_conservation(manifest: dict[str, Any]):
    recon = manifest["reconciliation"]
    assert recon["eval"] == 17
    assert recon["train"] == 43
    assert recon["eval_tier"] == 9
    assert recon["structural_excluded"] == 16
    assert recon["cap_excluded"] == 21
    assert recon["total"] == 106
    assert recon["conservation"] is True

    computed_sum = (
        recon["eval"]
        + recon["train"]
        + recon["eval_tier"]
        + recon["structural_excluded"]
        + recon["cap_excluded"]
    )
    assert computed_sum == 106


# ---------------------------------------------------------------------------
# Test 7: Determinism check (repeated build produces identical bytes and hashes)
# ---------------------------------------------------------------------------

def test_builder_determinism(tmp_path: Path, eval_ids: set[str]):
    # Load inputs from datasets/sft
    scored_records = _load_jsonl(SFT_DIR / "scored_records.jsonl")
    eval_records = _load_jsonl(EVAL_PATH)
    curriculum_outputs = {
        f"curriculum_{i}": _load_jsonl(SFT_DIR / f"sft_curriculum_{i}.jsonl")
        for i in range(1, 6)
    }

    dir1 = tmp_path / "run1"
    dir2 = tmp_path / "run2"

    manifest1 = build_and_save_dataset(
        scored_records=scored_records,
        eval_records=eval_records,
        eval_ids=eval_ids,
        curriculum_outputs=curriculum_outputs,
        sft_dir=dir1,
        source_audit_path=AUDIT_PATH,
    )

    manifest2 = build_and_save_dataset(
        scored_records=scored_records,
        eval_records=eval_records,
        eval_ids=eval_ids,
        curriculum_outputs=curriculum_outputs,
        sft_dir=dir2,
        source_audit_path=AUDIT_PATH,
    )

    # Byte-level check on generated JSONL files
    content1 = (dir1 / "comedy_sft_train.jsonl").read_bytes()
    content2 = (dir2 / "comedy_sft_train.jsonl").read_bytes()
    assert content1 == content2, "Repeated build produced divergent JSONL bytes!"

    # Manifest check
    assert manifest1["hashes"]["train_sha256"] == manifest2["hashes"]["train_sha256"]
    assert manifest1 == manifest2, "Repeated build produced divergent manifests!"


# ---------------------------------------------------------------------------
# Test 8: Manifest schema and SHA-256 hash verification
# ---------------------------------------------------------------------------

def test_manifest_schema_and_hash_integrity(manifest: dict[str, Any]):
    assert manifest["phase"] == "3F"
    assert manifest["source"]["audited_records"] == 180
    assert manifest["source"]["keep_records"] == 106

    # Verify SHA-256 match with actual on-disk files
    actual_train_hash = compute_file_sha256(TRAIN_PATH)
    actual_eval_hash = compute_file_sha256(EVAL_PATH)

    assert manifest["hashes"]["train_sha256"] == actual_train_hash
    assert manifest["hashes"]["eval_sha256"] == actual_eval_hash

    # Verification section
    assert manifest["verification"]["passed"] is True
    assert manifest["training"]["eval_leakage"] is False
    assert manifest["training"]["unique_ids"] is True
    assert manifest["training"]["quality_gates_pass"] is True
    assert manifest["training"]["curriculum_order_valid"] is True

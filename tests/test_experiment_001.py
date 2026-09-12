"""
Acceptance Test Suite for Experiment 001: Baseline vs Stateful vs Compiler BoN.

Verifies:
1. Benchmark dataset validity (20 scenes across 4 stress categories).
2. Experiment harness initialization and mock execution.
3. Baseline failure tracking under unconstrained generation.
4. Stateful transactional state commits.
5. Compiler-Guided BoN selection audit logging.
6. Reporter metric calculations: Valid Scene Rate (VSR) and Cost-Adjusted Validity (CAV).
"""

import json
import tempfile
from pathlib import Path
import pytest

from experiments.runner import ExperimentHarness
from experiments.reporter import ExperimentReporter


@pytest.fixture
def exp_paths():
    base_dir = Path(__file__).resolve().parent.parent / "experiments" / "experiment_001"
    config_path = base_dir / "config.json"
    dataset_path = base_dir / "dataset.json"
    return config_path, dataset_path


def test_dataset_integrity(exp_paths):
    """Verifies that dataset.json contains 20 valid benchmark scenes across all 4 categories."""
    config_path, dataset_path = exp_paths
    assert dataset_path.exists()

    with open(dataset_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    assert len(dataset) == 20
    categories = {s["category"] for s in dataset}
    assert categories == {"spatial", "possession", "epistemic", "complex_action"}

    for scene in dataset:
        assert "scene_id" in scene
        assert "contract" in scene
        contract = scene["contract"]
        assert "pov_character" in contract
        assert "primary_location" in contract
        assert "allowed_participants" in contract


def test_harness_mock_execution(exp_paths):
    """Verifies that ExperimentHarness runs all three arms deterministically in mock mode."""
    config_path, dataset_path = exp_paths

    with open(dataset_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    test_scene = dataset[0]  # scene_001: Adjoining transit to library
    harness = ExperimentHarness(config_path=config_path, mock_mode=True)

    world_a, truth_a, epi_a = harness.build_initial_environment()
    rec_a = harness.run_baseline_scene(test_scene, world_a, truth_a, epi_a)
    assert rec_a["system_id"] == "baseline"
    assert "token_economics" in rec_a

    world_b, truth_b, epi_b = harness.build_initial_environment()
    rec_b, new_world_b = harness.run_stateful_scene(test_scene, world_b, truth_b, epi_b)
    assert rec_b["system_id"] == "stateful"
    assert rec_b["is_valid"] is True
    assert new_world_b.characters["lord_reginald"].location == "library"

    world_c, truth_c, epi_c = harness.build_initial_environment()
    with tempfile.TemporaryDirectory() as tmp_dir:
        audit_dir = Path(tmp_dir) / "audit_test"
        rec_c, new_world_c = harness.run_bon_scene(test_scene, world_c, truth_c, epi_c, output_audit_dir=audit_dir)
        assert rec_c["system_id"] == "bon"
        assert rec_c["is_valid"] is True
        assert (audit_dir / "selection_audit.json").exists()


def test_baseline_detects_stuffed_secret_leak(exp_paths):
    """Verifies that Baseline arm naturally flags secret leak when prompted with stuffed secrets."""
    config_path, dataset_path = exp_paths
    with open(dataset_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    # scene_011: forbidden revelation of fact_teapot_mislaid
    secret_scene = next(s for s in dataset if s["scene_id"] == "scene_011")
    harness = ExperimentHarness(config_path=config_path, mock_mode=True)

    world, truth, epi = harness.build_initial_environment()
    rec_a = harness.run_baseline_scene(secret_scene, world, truth, epi)

    # In mock mode with naive prompt stuffing, baseline blurted the secret
    assert rec_a["is_valid"] is False
    assert any((v.get("violation_type") == "EPISTEMIC_LEAK" or v.get("type") == "EPISTEMIC_LEAK") for v in rec_a["violations"])


def test_reporter_vsr_and_cav_calculation():
    """Verifies that ExperimentReporter correctly computes VSR and CAV mathematical metrics."""
    records = [
        {
            "is_valid": True,
            "violations": [],
            "token_economics": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150, "generation_time_ms": 300},
            "quality_score": 0.85,
        },
        {
            "is_valid": False,
            "violations": [{"type": "EPISTEMIC_LEAK", "severity": "FATAL"}],
            "token_economics": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150, "generation_time_ms": 300},
            "quality_score": 0.50,
        },
    ]

    summary = ExperimentReporter.analyze_system_results("test_sys", "Test System", records)
    assert summary["total_scenes"] == 2
    assert summary["valid_scenes"] == 1
    assert summary["vsr_percent"] == 50.0  # 1/2 = 50%
    # CAV = (valid_scenes / total_tokens) * 1000 = (1 / 300) * 1000 = 3.3333
    assert abs(summary["cav_score"] - 3.3333) < 0.01
    assert summary["violations"]["fatal"] == 1

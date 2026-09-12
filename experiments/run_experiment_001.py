"""
Master CLI Entrypoint for Experiment 001.

Executes controlled ablation:
Baseline (1.5B) vs Stateful (1.5B) vs Compiler-Guided BoN (1.5B)
over benchmark dataset scenes.

Usage:
  python -m experiments.run_experiment_001 --mock --scenes 5
  python -m experiments.run_experiment_001 --scenes 20
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure project root is in sys.path
AI_AUTHOR_DIR = Path(__file__).resolve().parent.parent
ML_DIR = AI_AUTHOR_DIR.parent
for p in (AI_AUTHOR_DIR, ML_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from experiments.runner import ExperimentHarness
from experiments.reporter import ExperimentReporter
from story_engine.state.checkpoints import StoryCheckpointManager
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Experiments.Run001")


def main():
    parser = argparse.ArgumentParser(description="Run Experiment 001: Compiler vs Small Model")
    parser.add_argument("--scenes", type=int, default=20, help="Number of benchmark scenes to evaluate (1-20, default: 20)")
    parser.add_argument("--mock", action="store_true", help="Run with deterministic mock generator for rapid verification")
    parser.add_argument("--output_dir", type=str, default="experiments/experiment_001", help="Target experiment directory")

    args = parser.parse_args()

    exp_dir = Path(args.output_dir).resolve()
    config_file = exp_dir / "config.json"
    dataset_file = exp_dir / "dataset.json"

    if not config_file.exists() or not dataset_file.exists():
        logger.error(f"Missing config or dataset in '{exp_dir}'. Please ensure config.json and dataset.json exist.")
        sys.exit(1)

    with open(dataset_file, "r", encoding="utf-8") as f:
        full_dataset = json.load(f)

    eval_scenes = full_dataset[:args.scenes]
    logger.info("================================================================================")
    logger.info(f"STARTING EXPERIMENT 001: '{exp_dir.name}'")
    logger.info(f"Evaluating {len(eval_scenes)} Scenes across 3 Systems (Mock Mode: {args.mock})")
    logger.info("================================================================================")

    harness = ExperimentHarness(config_path=config_file, mock_mode=args.mock)

    # Output subdirectories
    baseline_dir = exp_dir / "baseline"
    stateful_dir = exp_dir / "stateful"
    bon_dir = exp_dir / "bon"
    for d in (baseline_dir, stateful_dir, bon_dir):
        d.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------
    # ARM A: Baseline (Unconstrained Generation + Post-hoc Audit)
    # ---------------------------------------------------------
    logger.info(">>> Running ARM A: Baseline (1.5B Unconstrained) <<<")
    baseline_records = []
    base_world, base_truth, base_epistemic = harness.build_initial_environment()

    for idx, sc in enumerate(eval_scenes, 1):
        logger.info(f"[Baseline {idx}/{len(eval_scenes)}] Evaluating '{sc['scene_id']}: {sc['title']}'...")
        rec = harness.run_baseline_scene(sc, base_world, base_truth, base_epistemic)
        baseline_records.append(rec)
        with open(baseline_dir / f"{sc['scene_id']}.json", "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2)

    # ---------------------------------------------------------
    # ARM B: Stateful (Context Budgeter + State Transitions)
    # ---------------------------------------------------------
    logger.info(">>> Running ARM B: Stateful (1.5B + Scene Compiler, 1 Cand) <<<")
    stateful_records = []
    st_world, st_truth, st_epistemic = harness.build_initial_environment()
    st_ckpt_mgr = StoryCheckpointManager(base_dir=stateful_dir / "checkpoints")

    for idx, sc in enumerate(eval_scenes, 1):
        logger.info(f"[Stateful {idx}/{len(eval_scenes)}] Evaluating '{sc['scene_id']}: {sc['title']}'...")
        rec, st_world = harness.run_stateful_scene(sc, st_world, st_truth, st_epistemic, checkpoint_manager=st_ckpt_mgr)
        stateful_records.append(rec)
        with open(stateful_dir / f"{sc['scene_id']}.json", "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2)

    # ---------------------------------------------------------
    # ARM C: Compiler-Guided BoN (Best-of-3 + 3-Stage Gating)
    # ---------------------------------------------------------
    logger.info(">>> Running ARM C: Compiler-Guided BoN (1.5B + Best-of-3) <<<")
    bon_records = []
    bon_world, bon_truth, bon_epistemic = harness.build_initial_environment()
    bon_ckpt_mgr = StoryCheckpointManager(base_dir=bon_dir / "checkpoints")

    for idx, sc in enumerate(eval_scenes, 1):
        logger.info(f"[BoN {idx}/{len(eval_scenes)}] Evaluating '{sc['scene_id']}: {sc['title']}'...")
        scene_audit_dir = bon_dir / "checkpoints" / sc["scene_id"]
        rec, bon_world = harness.run_bon_scene(
            sc, bon_world, bon_truth, bon_epistemic,
            output_audit_dir=scene_audit_dir,
            checkpoint_manager=bon_ckpt_mgr,
        )
        bon_records.append(rec)
        with open(bon_dir / f"{sc['scene_id']}.json", "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2)

    # ---------------------------------------------------------
    # Analyze & Generate Reports
    # ---------------------------------------------------------
    logger.info("================================================================================")
    logger.info("Compiling Comparative Results & Token Economics...")

    summary_a = ExperimentReporter.analyze_system_results("baseline", "Baseline (1.5B)", baseline_records)
    summary_b = ExperimentReporter.analyze_system_results("stateful", "Stateful (1.5B)", stateful_records)
    summary_c = ExperimentReporter.analyze_system_results("bon", "Compiler-Guided BoN (1.5B)", bon_records)

    all_summaries = [summary_a, summary_b, summary_c]

    results_data = {
        "experiment_id": "experiment_001",
        "total_evaluated_scenes": len(eval_scenes),
        "mock_mode": args.mock,
        "systems": {
            "baseline": summary_a,
            "stateful": summary_b,
            "bon": summary_c,
        },
    }

    results_file = exp_dir / "results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(results_data, f, indent=2)
    logger.info(f"Saved structured results to: '{results_file}'")

    report_file = exp_dir / "report.md"
    report_md = ExperimentReporter.generate_full_report(
        experiment_id="experiment_001",
        title="Does a Compiler Make a Small Model Better?",
        config=harness.config,
        system_summaries=all_summaries,
        output_file=report_file,
    )
    logger.info(f"Generated research report: '{report_file}'")

    print("\n" + "=" * 80)
    print("EXPERIMENT 001 RESULTS SUMMARY")
    print("=" * 80)
    print(f"{'System':<28} | {'VSR (%)':<8} | {'Viols/Sc':<8} | {'Fatal':<6} | {'CAV':<8} | {'Avg Toks':<8}")
    print("-" * 80)
    for s in all_summaries:
        print(
            f"{s['system_name']:<28} | "
            f"{s['vsr_percent']:<8.1f} | "
            f"{s['violations']['per_scene']:<8.2f} | "
            f"{s['violations']['fatal']:<6} | "
            f"{s['cav_score']:<8.4f} | "
            f"{s['token_economics']['avg_tokens_per_scene']:<8.1f}"
        )
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()

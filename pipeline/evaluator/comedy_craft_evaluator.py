"""
pipeline/evaluator/comedy_craft_evaluator.py

Phase 4A: Comedy Craft Evaluation Framework.
Evaluates model comedy-craft understanding on the 17 frozen eval examples.

Design Invariants:
  1. Hash & Count Guard:
     Enforces len(eval_records) == 17 and SHA-256 == EXPECTED_EVAL_SHA256.
     Aborts immediately if dataset diverges.
  2. Separation of Generation and Evaluation:
     Generation outputs raw_predictions.jsonl.
     Evaluation parses raw_predictions.jsonl and scores metrics.
     Evaluation can be run independently on pre-generated predictions.
  3. Deterministic Greedy Inference:
     do_sample=False, temperature=None, max_new_tokens=256, model.eval(), torch.inference_mode().
  4. Explicit parse_status (no silent masking):
     VALID, JSON_PARSE_ERROR, SCHEMA_ERROR, UNKNOWN_PRIMARY_MECHANISM,
     UNKNOWN_SECONDARY_MECHANISM, INVALID_HORIZON.
  5. Multi-metric Scorecard:
     Primary accuracy, Secondary micro/macro F1, Mean Jaccard, Horizon accuracy,
     Taxonomy violation rate, Raw JSON validity, Repairable JSON validity,
     Exact record accuracy (primary + horizon + secondary exact match).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))
if str(WORKSPACE_ROOT.parent) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT.parent))

try:
    import pyarrow
except (OSError, ModuleNotFoundError, ImportError):
    sys.modules["pyarrow"] = None

EXPECTED_EVAL_SHA256 = "685ad4369fd731b952801e83ed23f0e3bb7c320876052710abd01c8bd3cb3470"
EXPECTED_EVAL_COUNT = 17

EXPECTED_DEV_SHA256 = "18838c6ddd9bcd89d80df6e223b41bfd68cb25a1ae18976f4dd6ecd2c476829e"
EXPECTED_DEV_COUNT = 20

CANONICAL_MECHANISMS = [
    "ESCALATION",
    "MISUNDERSTANDING",
    "VERBAL_WIT",
    "DEADPAN_REACTION",
    "PHYSICAL_COMPLICATION",
    "STATUS_REVERSAL",
    "SOCIAL_EMBARRASSMENT",
    "DIALOGUE_SUBTEXT",
    "DRAMATIC_IRONY",
    "CALLBACK",
]

CANONICAL_HORIZONS = ["LOCAL", "LONG_HORIZON"]


def compute_file_sha256(path: Path) -> str:
    """Compute SHA-256 hash of a file's raw canonical bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def verify_eval_dataset(eval_path: Path) -> list[dict[str, Any]]:
    """Assert count and SHA-256 hash match the designated evaluation set."""
    if not eval_path.exists():
        raise FileNotFoundError(f"Evaluation file not found at: {eval_path}")

    actual_hash = compute_file_sha256(eval_path)
    if eval_path.name == "comedy_dev.jsonl":
        expected_hash = EXPECTED_DEV_SHA256
        expected_count = EXPECTED_DEV_COUNT
    else:
        expected_hash = EXPECTED_EVAL_SHA256
        expected_count = EXPECTED_EVAL_COUNT

    if actual_hash != expected_hash:
        raise ValueError(
            f"Eval dataset hash mismatch!\n"
            f"  Expected: {expected_hash}\n"
            f"  Actual:   {actual_hash}\n"
            f"Evaluation aborted to protect evaluation integrity."
        )

    records: list[dict[str, Any]] = []
    with open(eval_path, encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if line_str:
                records.append(json.loads(line_str))

    if expected_count and len(records) != expected_count:
        raise ValueError(
            f"Eval record count mismatch for {eval_path.name}! Expected {expected_count}, found {len(records)}."
        )

    return records


def format_eval_prompt(source_text: str) -> list[dict[str, str]]:
    """Format prompt for Qwen ChatML template."""
    mechanisms_list = "\n".join(f"- {m}" for m in CANONICAL_MECHANISMS)
    system_prompt = (
        "You are an expert literary scholar and comedy craft analyst specializing in "
        "classic British and early 20th-century comedy (e.g., P.G. Wodehouse, Jerome K. Jerome).\n"
        "Analyze the comedy craft of the provided text. You must select the primary mechanism "
        f"from the standard 10 comedy mechanisms:\n{mechanisms_list}\n\n"
        "Respond ONLY with a valid JSON object matching this schema:\n"
        "{\n"
        '  "primary_mechanism": "<one of the 10 mechanisms>",\n'
        '  "secondary_mechanisms": ["<zero or more mechanisms>"],\n'
        '  "mechanism_horizon": "LOCAL" | "LONG_HORIZON",\n'
        '  "craft_analysis": "<1-3 sentence explanation of the comedic engine>"\n'
        "}"
    )

    user_prompt = f'Passage:\n"""{source_text}"""'

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def parse_prediction(raw_text: str) -> dict[str, Any]:
    """
    Parse model output strictly without silent repair.

    Returns dict containing:
      - parsed: bool
      - raw_json_valid: bool
      - repairable_json: bool
      - schema_valid: bool
      - parse_status: str
      - prediction: dict (normalized fields)
    """
    cleaned = raw_text.strip()

    # Step 1: Raw JSON parse attempt
    parsed_json = None
    raw_json_valid = False

    try:
        parsed_json = json.loads(cleaned)
        raw_json_valid = True
    except Exception:
        pass

    # Step 2: Diagnostic repair attempt (e.g. markdown code blocks)
    repairable = False
    if not raw_json_valid:
        # Extract from ```json ... ``` or first { ... }
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", cleaned, re.DOTALL)
        if not match:
            match = re.search(r"(\{.*\})", cleaned, re.DOTALL)
        if match:
            try:
                parsed_json = json.loads(match.group(1))
                repairable = True
            except Exception:
                pass

    if parsed_json is None:
        return {
            "parsed": False,
            "raw_json_valid": False,
            "repairable_json": False,
            "schema_valid": False,
            "parse_status": "JSON_PARSE_ERROR",
            "prediction": {
                "primary_mechanism": "UNKNOWN",
                "secondary_mechanisms": [],
                "mechanism_horizon": "UNKNOWN",
                "craft_analysis": "",
            },
        }

    # Step 3: Schema validation
    if not isinstance(parsed_json, dict):
        return {
            "parsed": True,
            "raw_json_valid": raw_json_valid,
            "repairable_json": repairable,
            "schema_valid": False,
            "parse_status": "SCHEMA_ERROR",
            "prediction": {
                "primary_mechanism": "UNKNOWN",
                "secondary_mechanisms": [],
                "mechanism_horizon": "UNKNOWN",
                "craft_analysis": "",
            },
        }

    primary = parsed_json.get("primary_mechanism")
    secondary = parsed_json.get("secondary_mechanisms")
    horizon = parsed_json.get("mechanism_horizon")
    analysis = parsed_json.get("craft_analysis", "")

    if not isinstance(primary, str) or not isinstance(secondary, list) or not isinstance(horizon, str):
        return {
            "parsed": True,
            "raw_json_valid": raw_json_valid,
            "repairable_json": repairable,
            "schema_valid": False,
            "parse_status": "SCHEMA_ERROR",
            "prediction": {
                "primary_mechanism": str(primary) if primary else "UNKNOWN",
                "secondary_mechanisms": secondary if isinstance(secondary, list) else [],
                "mechanism_horizon": str(horizon) if horizon else "UNKNOWN",
                "craft_analysis": str(analysis),
            },
        }

    # Normalize casing/whitespace
    primary_norm = primary.strip().upper()
    secondary_norm = [str(s).strip().upper() for s in secondary]
    horizon_norm = horizon.strip().upper()

    # Step 4: Enum / Taxonomy validation
    if primary_norm not in CANONICAL_MECHANISMS:
        return {
            "parsed": True,
            "raw_json_valid": raw_json_valid,
            "repairable_json": repairable,
            "schema_valid": False,
            "parse_status": "UNKNOWN_PRIMARY_MECHANISM",
            "prediction": {
                "primary_mechanism": primary_norm,
                "secondary_mechanisms": secondary_norm,
                "mechanism_horizon": horizon_norm,
                "craft_analysis": str(analysis),
            },
        }

    unknown_sec = [s for s in secondary_norm if s not in CANONICAL_MECHANISMS]
    if unknown_sec:
        return {
            "parsed": True,
            "raw_json_valid": raw_json_valid,
            "repairable_json": repairable,
            "schema_valid": False,
            "parse_status": "UNKNOWN_SECONDARY_MECHANISM",
            "prediction": {
                "primary_mechanism": primary_norm,
                "secondary_mechanisms": secondary_norm,
                "mechanism_horizon": horizon_norm,
                "craft_analysis": str(analysis),
            },
        }

    if horizon_norm not in CANONICAL_HORIZONS:
        return {
            "parsed": True,
            "raw_json_valid": raw_json_valid,
            "repairable_json": repairable,
            "schema_valid": False,
            "parse_status": "INVALID_HORIZON",
            "prediction": {
                "primary_mechanism": primary_norm,
                "secondary_mechanisms": secondary_norm,
                "mechanism_horizon": horizon_norm,
                "craft_analysis": str(analysis),
            },
        }

    # Everything strictly valid
    return {
        "parsed": True,
        "raw_json_valid": raw_json_valid,
        "repairable_json": repairable,
        "schema_valid": True,
        "parse_status": "VALID",
        "prediction": {
            "primary_mechanism": primary_norm,
            "secondary_mechanisms": secondary_norm,
            "mechanism_horizon": horizon_norm,
            "craft_analysis": str(analysis),
        },
    }


def compute_evaluation_metrics(
    eval_records: list[dict[str, Any]],
    raw_predictions: list[dict[str, Any]],
    eval_sha256: str | None = None,
    dataset_name: str | None = None,
) -> dict[str, Any]:
    """
    Score model predictions against frozen human ground truth.
    Computes all micro/macro metrics, exact record accuracy, confusion matrix, and scorecard.
    """
    eval_map = {r["audit_id"]: r for r in eval_records}
    total = len(eval_records)
    assert total > 0, "No evaluation records provided."

    parsed_count = 0
    raw_json_valid_count = 0
    repairable_json_count = 0
    schema_valid_count = 0
    valid_status_count = 0
    parse_status_counts: Counter[str] = Counter()

    primary_correct = 0
    horizon_correct = 0
    exact_record_correct = 0

    combined_coverage_matches = 0

    # For secondary multilabel metrics
    total_tp = 0
    total_fp = 0
    total_fn = 0
    jaccard_scores: list[float] = []

    per_mechanism_tp: Counter[str] = Counter()
    per_mechanism_fp: Counter[str] = Counter()
    per_mechanism_fn: Counter[str] = Counter()

    confusion_pairs: list[dict[str, str]] = []
    per_example_results: list[dict[str, Any]] = []

    for pred_item in raw_predictions:
        aid = pred_item.get("audit_id", "")
        gold_rec = eval_map.get(aid)
        if not gold_rec:
            continue

        raw_response = pred_item.get("raw_response", "")
        parsed_res = parse_prediction(raw_response)

        status = parsed_res["parse_status"]
        parse_status_counts[status] += 1

        if parsed_res["parsed"]:
            parsed_count += 1
        if parsed_res["raw_json_valid"]:
            raw_json_valid_count += 1
        if parsed_res["repairable_json"] or parsed_res["raw_json_valid"]:
            repairable_json_count += 1
        if parsed_res["schema_valid"]:
            schema_valid_count += 1
        if status == "VALID":
            valid_status_count += 1

        pred = parsed_res["prediction"]
        ha = gold_rec.get("human_audit", {})

        gold_primary = ha.get("primary_mechanism", "UNKNOWN")
        gold_secondary = set(ha.get("secondary_mechanisms", []))
        gold_horizon = ha.get("mechanism_horizon", "LOCAL")

        pred_primary = pred["primary_mechanism"]
        pred_secondary = set(pred["secondary_mechanisms"])
        pred_horizon = pred["mechanism_horizon"]

        # 1. Primary mechanism accuracy
        is_primary_correct = (pred_primary == gold_primary)
        if is_primary_correct:
            primary_correct += 1

        confusion_pairs.append({
            "audit_id": aid,
            "gold": gold_primary,
            "predicted": pred_primary,
            "correct": is_primary_correct,
        })

        # 2. Horizon accuracy
        is_horizon_correct = (pred_horizon == gold_horizon)
        if is_horizon_correct:
            horizon_correct += 1

        # 3. Secondary multilabel matching
        sec_tp = len(pred_secondary.intersection(gold_secondary))
        sec_fp = len(pred_secondary.difference(gold_secondary))
        sec_fn = len(gold_secondary.difference(pred_secondary))

        total_tp += sec_tp
        total_fp += sec_fp
        total_fn += sec_fn

        # Per mechanism TP/FP/FN for macro F1
        for m in gold_secondary:
            if m in pred_secondary:
                per_mechanism_tp[m] += 1
            else:
                per_mechanism_fn[m] += 1
        for m in pred_secondary:
            if m not in gold_secondary:
                per_mechanism_fp[m] += 1

        union_sec = gold_secondary.union(pred_secondary)
        if not union_sec:
            # Both empty: perfect match
            jaccard = 1.0
        else:
            jaccard = sec_tp / len(union_sec)
        jaccard_scores.append(jaccard)

        # 4. Combined coverage diagnostic (did model identify gold primary anywhere?)
        gold_all = {gold_primary}.union(gold_secondary)
        pred_all = {pred_primary}.union(pred_secondary)
        if gold_primary in pred_all:
            combined_coverage_matches += 1

        # 5. Exact craft record accuracy: primary + horizon + secondary sets exactly match
        is_exact = is_primary_correct and is_horizon_correct and (pred_secondary == gold_secondary)
        if is_exact:
            exact_record_correct += 1

        per_example_results.append({
            "audit_id": aid,
            "source_book": gold_rec.get("source_book", "UNKNOWN"),
            "gold": {
                "primary": gold_primary,
                "secondary": sorted(list(gold_secondary)),
                "horizon": gold_horizon,
            },
            "predicted": {
                "primary": pred_primary,
                "secondary": sorted(list(pred_secondary)),
                "horizon": pred_horizon,
                "craft_analysis": pred.get("craft_analysis", ""),
            },
            "checks": {
                "parse_status": status,
                "raw_json_valid": parsed_res["raw_json_valid"],
                "schema_valid": parsed_res["schema_valid"],
                "primary_correct": is_primary_correct,
                "horizon_correct": is_horizon_correct,
                "secondary_jaccard": round(jaccard, 3),
                "exact_record_match": is_exact,
            },
            "raw_response": raw_response,
        })

    # Micro F1
    micro_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
    micro_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
    micro_f1 = (
        (2 * micro_precision * micro_recall) / (micro_precision + micro_recall)
        if (micro_precision + micro_recall) > 0
        else 0.0
    )

    # Macro F1 across active mechanisms in secondary annotations
    macro_f1_list: list[float] = []
    for m in CANONICAL_MECHANISMS:
        tp = per_mechanism_tp[m]
        fp = per_mechanism_fp[m]
        fn = per_mechanism_fn[m]
        if (tp + fp + fn) > 0:
            prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1 = (2 * prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0
            macro_f1_list.append(f1)

    macro_f1 = sum(macro_f1_list) / len(macro_f1_list) if macro_f1_list else 0.0
    mean_jaccard = sum(jaccard_scores) / len(jaccard_scores) if jaccard_scores else 0.0

    primary_accuracy = primary_correct / total
    horizon_accuracy = horizon_correct / total
    exact_accuracy = exact_record_correct / total
    combined_coverage_acc = combined_coverage_matches / total

    taxonomy_violations = sum(
        parse_status_counts[s]
        for s in ("UNKNOWN_PRIMARY_MECHANISM", "UNKNOWN_SECONDARY_MECHANISM", "INVALID_HORIZON")
    )
    taxonomy_violation_rate = taxonomy_violations / total

    return {
        "evaluation": {
            "n": total,
            "dataset_name": dataset_name or "comedy_eval.jsonl",
            "human_gold": True,
            "eval_sha256": eval_sha256 or EXPECTED_EVAL_SHA256,
        },
        "scorecard": {
            "primary_accuracy": round(primary_accuracy, 4),
            "primary_correct": primary_correct,
            "exact_record_accuracy": round(exact_accuracy, 4),
            "exact_record_correct": exact_record_correct,
            "horizon_accuracy": round(horizon_accuracy, 4),
            "secondary_micro_precision": round(micro_precision, 4),
            "secondary_micro_recall": round(micro_recall, 4),
            "secondary_micro_f1": round(micro_f1, 4),
            "secondary_macro_f1": round(macro_f1, 4),
            "mean_jaccard": round(mean_jaccard, 4),
            "combined_coverage_accuracy": round(combined_coverage_acc, 4),
            "raw_json_validity": round(raw_json_valid_count / total, 4),
            "repairable_json_validity": round(repairable_json_count / total, 4),
            "schema_validity": round(schema_valid_count / total, 4),
            "taxonomy_violation_rate": round(taxonomy_violation_rate, 4),
        },
        "failure_breakdown": {
            "json_failures": total - raw_json_valid_count,
            "schema_failures": total - schema_valid_count,
            "wrong_primary": total - primary_correct,
            "wrong_horizon": total - horizon_correct,
            "exact_failures": total - exact_record_correct,
            "parse_statuses": dict(parse_status_counts),
        },
        "confusion_matrix": confusion_pairs,
        "per_example": per_example_results,
    }


def generate_markdown_report(report_data: dict[str, Any], model_name: str) -> str:
    """Format markdown scorecard and diagnostic report."""
    sc = report_data["scorecard"]
    fb = report_data["failure_breakdown"]
    eval_meta = report_data["evaluation"]

    md = []
    md.append(f"# Comedy Craft Baseline Evaluation Report: {model_name}\n")
    md.append(f"- **Model**: `{model_name}`")
    md.append(f"- **Dataset**: `{eval_meta.get('dataset_name', 'comedy_eval.jsonl')}` (Human Gold Truth, n = {eval_meta['n']})")
    md.append(f"- **Eval SHA-256**: `{eval_meta['eval_sha256']}`\n")

    md.append("## 1. Core Scorecard\n")
    md.append("| Metric | Result | Target / Ideal |")
    md.append("|---|:---:|:---:|")
    md.append(f"| **Primary Mechanism Accuracy** | **{sc['primary_accuracy'] * 100:.1f}%** ({sc['primary_correct']}/{eval_meta['n']}) | > 60.0% |")
    md.append(f"| **Exact Record Accuracy** | **{sc['exact_record_accuracy'] * 100:.1f}%** ({sc['exact_record_correct']}/{eval_meta['n']}) | > 35.0% |")
    md.append(f"| **Horizon Accuracy** | **{sc['horizon_accuracy'] * 100:.1f}%** | > 80.0% |")
    md.append(f"| **Secondary Micro F1** | **{sc['secondary_micro_f1'] * 100:.1f}%** | > 50.0% |")
    md.append(f"| **Secondary Macro F1** | **{sc['secondary_macro_f1'] * 100:.1f}%** | > 40.0% |")
    md.append(f"| **Mean Jaccard Similarity** | **{sc['mean_jaccard'] * 100:.1f}%** | > 50.0% |")
    md.append(f"| **Combined Coverage (Primary anywhere)** | **{sc['combined_coverage_accuracy'] * 100:.1f}%** | > 70.0% |")
    md.append(f"| **Raw JSON Validity** | **{sc['raw_json_validity'] * 100:.1f}%** | 100.0% |")
    md.append(f"| **Repairable JSON Validity** | **{sc['repairable_json_validity'] * 100:.1f}%** | 100.0% |")
    md.append(f"| **Schema Validity** | **{sc['schema_validity'] * 100:.1f}%** | 100.0% |")
    md.append(f"| **Taxonomy Violations** | **{sc['taxonomy_violation_rate'] * 100:.1f}%** | 0.0% |\n")

    md.append("## 2. Failure Breakdown\n")
    md.append(f"- **JSON Syntax Failures**: {fb['json_failures']}")
    md.append(f"- **Schema/Taxonomy Failures**: {fb['schema_failures']}")
    md.append(f"- **Incorrect Primary Mechanism**: {fb['wrong_primary']}")
    md.append(f"- **Incorrect Mechanism Horizon**: {fb['wrong_horizon']}")
    md.append(f"- **Exact Craft Record Failures**: {fb['exact_failures']}")
    md.append("- **Parse Status Breakdown**:")
    for status, count in fb["parse_statuses"].items():
        md.append(f"  - `{status}`: {count}")
    md.append("")

    md.append("## 3. Per-Example Diagnostic Log\n")
    md.append("| Audit ID | Gold Primary | Predicted Primary | Gold Horizon | Pred Horizon | JSON | Status | Exact |")
    md.append("|---|---|---|---|---|:---:|:---:|:---:|")
    for ex in report_data["per_example"]:
        aid = ex["audit_id"]
        g_prim = ex["gold"]["primary"]
        p_prim = ex["predicted"]["primary"]
        g_hor = ex["gold"]["horizon"]
        p_hor = ex["predicted"]["horizon"]
        json_ok = "✓" if ex["checks"]["raw_json_valid"] else "✗"
        status = ex["checks"]["parse_status"]
        exact_ok = "✅" if ex["checks"]["exact_record_match"] else "❌"
        prim_match = "✓" if ex["checks"]["primary_correct"] else "✗"

        md.append(f"| `{aid}` | {g_prim} | {p_prim} ({prim_match}) | {g_hor} | {p_hor} | {json_ok} | `{status}` | {exact_ok} |")
    md.append("")

    return "\n".join(md)


def run_model_inference(
    model_path: Path,
    eval_records: list[dict[str, Any]],
    raw_out_path: Path,
    max_new_tokens: int = 256,
    adapter_path: Path | None = None,
) -> list[dict[str, Any]]:
    """
    Run greedy decoding inference using local Hugging Face model and tokenizer.
    Enforces do_sample=False, torch.inference_mode(), model.eval().
    Saves raw predictions to raw_out_path line-by-line.
    """
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"Loading tokenizer from: {model_path}...")
    tokenizer = AutoTokenizer.from_pretrained(str(model_path), trust_remote_code=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading model on device: {device}...")

    dtype = torch.bfloat16 if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else torch.float16
    if device == "cpu":
        dtype = torch.float32

    model = AutoModelForCausalLM.from_pretrained(
        str(model_path),
        torch_dtype=dtype,
        device_map="auto" if device == "cuda" else None,
        trust_remote_code=True,
    )

    if adapter_path is not None:
        from peft import PeftModel
        print(f"Attaching LoRA adapter from: {adapter_path}...")
        model = PeftModel.from_pretrained(model, str(adapter_path))

    model.eval()

    raw_out_path.parent.mkdir(parents=True, exist_ok=True)
    raw_predictions: list[dict[str, Any]] = []

    print(f"Running inference across {len(eval_records)} frozen evaluation examples (greedy decoding)...")

    with open(raw_out_path, "w", encoding="utf-8") as f_out:
        with torch.inference_mode():
            for idx, rec in enumerate(eval_records, 1):
                aid = rec["audit_id"]
                src_text = rec["source_text"]

                messages = format_eval_prompt(src_text)
                prompt_text = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True,
                )

                inputs = tokenizer([prompt_text], return_tensors="pt").to(model.device)

                output_ids = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                    pad_token_id=tokenizer.eos_token_id,
                )

                # Decode only generated tokens
                generated_tokens = output_ids[0][inputs.input_ids.shape[1] :]
                raw_response = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

                item = {
                    "audit_id": aid,
                    "model": str(model_path).replace("\\", "/"),
                    "generation_config": {
                        "do_sample": False,
                        "temperature": None,
                        "max_new_tokens": max_new_tokens,
                    },
                    "prompt_messages": messages,
                    "raw_response": raw_response,
                }
                raw_predictions.append(item)
                f_out.write(json.dumps(item, ensure_ascii=False) + "\n")
                f_out.flush()

                print(f"  [{idx}/{len(eval_records)}] Evaluated {aid}")

    print(f"Raw predictions saved to: {raw_out_path}")
    return raw_predictions


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 4A: Comedy Craft Evaluator & Baseline Runner.")
    parser.add_argument(
        "--model-path",
        type=Path,
        default=Path("models/Qwen2.5-1.5B-Instruct"),
        help="Path to model directory or Hugging Face ID.",
    )
    parser.add_argument(
        "--adapter-path",
        type=Path,
        default=None,
        help="Optional path to PEFT LoRA adapter directory to evaluate.",
    )
    parser.add_argument(
        "--eval-file",
        type=Path,
        default=Path("datasets/sft/comedy_eval.jsonl"),
        help="Path to frozen 17-example evaluation JSONL.",
    )
    parser.add_argument(
        "--raw-out",
        type=Path,
        default=Path("experiments/baseline/raw_predictions_qwen1.5b_base.jsonl"),
        help="Where to write raw predictions JSONL.",
    )
    parser.add_argument(
        "--report-json",
        type=Path,
        default=Path("reports/baseline_eval_qwen1.5b_base.json"),
        help="Where to write full JSON report.",
    )
    parser.add_argument(
        "--report-md",
        type=Path,
        default=Path("reports/baseline_eval_qwen1.5b_base.md"),
        help="Where to write markdown scorecard.",
    )
    parser.add_argument(
        "--eval-only",
        action="store_true",
        help="Skip model inference and evaluate existing raw predictions.",
    )
    args = parser.parse_args()

    # 1. Verify evaluation set integrity
    eval_records = verify_eval_dataset(args.eval_file)
    actual_hash = compute_file_sha256(args.eval_file)
    print(f"Evaluation dataset verified: {args.eval_file.name} ({len(eval_records)} records, SHA-256 = {actual_hash})")

    # 2. Obtain raw predictions (via generation or existing file)
    if args.eval_only:
        print(f"Eval-only mode: loading raw predictions from {args.raw_out}...")
        if not args.raw_out.exists():
            raise FileNotFoundError(f"Raw predictions file not found: {args.raw_out}")
        raw_predictions = []
        with open(args.raw_out, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    raw_predictions.append(json.loads(line))
    else:
        raw_predictions = run_model_inference(
            model_path=args.model_path,
            eval_records=eval_records,
            raw_out_path=args.raw_out,
            adapter_path=args.adapter_path,
        )

    # 3. Score predictions
    report_data = compute_evaluation_metrics(
        eval_records=eval_records,
        raw_predictions=raw_predictions,
        eval_sha256=actual_hash,
        dataset_name=args.eval_file.name,
    )
    report_data["model"] = {
        "path": str(args.model_path).replace("\\", "/"),
        "generation": {
            "do_sample": False,
            "temperature": None,
            "max_new_tokens": 256,
        },
    }

    # 4. Save reports
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    with open(args.report_json, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)

    md_report = generate_markdown_report(report_data, model_name=args.model_path.name)
    with open(args.report_md, "w", encoding="utf-8") as f:
        f.write(md_report)

    # 5. Print summary
    sc = report_data["scorecard"]
    print("\n" + "=" * 60)
    print(f"Baseline Evaluation Complete: {args.model_path.name}")
    total_n = len(eval_records)
    print(f"  Primary Mechanism Accuracy:  {sc['primary_accuracy'] * 100:.1f}% ({sc['primary_correct']}/{total_n})")
    print(f"  Exact Record Accuracy:       {sc['exact_record_accuracy'] * 100:.1f}% ({sc['exact_record_correct']}/{total_n})")
    print(f"  Horizon Accuracy:            {sc['horizon_accuracy'] * 100:.1f}%")
    print(f"  Secondary Micro F1:          {sc['secondary_micro_f1'] * 100:.1f}%")
    print(f"  Secondary Macro F1:          {sc['secondary_macro_f1'] * 100:.1f}%")
    print(f"  Mean Jaccard:                {sc['mean_jaccard'] * 100:.1f}%")
    print(f"  Combined Coverage:           {sc['combined_coverage_accuracy'] * 100:.1f}%")
    print(f"  Raw JSON Validity:           {sc['raw_json_validity'] * 100:.1f}%")
    print(f"  Repairable JSON Validity:    {sc['repairable_json_validity'] * 100:.1f}%")
    print(f"  Schema Validity:             {sc['schema_validity'] * 100:.1f}%")
    print(f"  Taxonomy Violations:         {sc['taxonomy_violation_rate'] * 100:.1f}%")
    print(f"  JSON Report:                 {args.report_json}")
    print(f"  Markdown Report:             {args.report_md}")
    print("=" * 60)


if __name__ == "__main__":
    main()

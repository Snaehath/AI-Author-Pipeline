"""
pipeline/trainer/run_sft_experiment_001.py

Phase 4B: SFT Experiment 1 Runner.
Fine-tunes Qwen2.5-1.5B-Instruct on the 43 human-curated comedy craft training records.

Experimental Controls:
  - Base Model: models/Qwen2.5-1.5B-Instruct
  - Training Data: datasets/sft/comedy_sft_train.jsonl (43 records, curriculum ordered)
  - Method: 4-bit QLoRA (NF4) with prepare_model_for_kbit_training
  - Hyperparameters:
      lr = 1e-4
      epochs = 3
      r = 16, alpha = 32, dropout = 0.05
      effective batch size = 4 (batch size 1, gradient accumulation 4)
      seed = 42
  - Checkpoints:
      models/comedy_sft_adapter/checkpoint-epoch-1
      models/comedy_sft_adapter/checkpoint-epoch-2
      models/comedy_sft_adapter/checkpoint-epoch-3
  - Memorization diagnostic on 5 training records.
  - Experiment fingerprint saved with canonical dataset hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import sys
from pathlib import Path
from typing import Any

# Safeguard against WinError 6714 on Windows when pyarrow is probed
sys.modules.setdefault("pyarrow", None)

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    get_cosine_schedule_with_warmup,
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training,
)

from dataset_generator.sft_dataset_formatter import (
    load_and_format_train_records,
    tokenize_sft_example,
)
from pipeline.evaluator.comedy_craft_evaluator import (
    compute_file_sha256,
    format_eval_prompt,
    parse_prediction,
)

EXPECTED_TRAIN_SHA256 = "63e6a602f4f54d2809b43f1c638edeef3df861750b39390c373b58361fe5a0d6"
EXPECTED_EVAL_SHA256 = "685ad4369fd731b952801e83ed23f0e3bb7c320876052710abd01c8bd3cb3470"


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def collate_fn(batch: list[dict[str, list[int]]], pad_token_id: int) -> dict[str, torch.Tensor]:
    max_len = max(len(item["input_ids"]) for item in batch)

    input_ids = []
    attention_mask = []
    labels = []

    for item in batch:
        pad_len = max_len - len(item["input_ids"])
        input_ids.append(item["input_ids"] + [pad_token_id] * pad_len)
        attention_mask.append(item["attention_mask"] + [0] * pad_len)
        labels.append(item["labels"] + [-100] * pad_len)

    return {
        "input_ids": torch.tensor(input_ids, dtype=torch.long),
        "attention_mask": torch.tensor(attention_mask, dtype=torch.long),
        "labels": torch.tensor(labels, dtype=torch.long),
    }


def run_memorization_diagnostic(
    model: Any,
    tokenizer: Any,
    train_records: list[dict[str, Any]],
    sample_ids: list[str],
) -> dict[str, Any]:
    """Diagnostic check on a sample of training records to detect memorization vs learning."""
    model.eval()
    results = []
    correct_count = 0

    record_map = {r["audit_id"]: r for r in train_records}

    with torch.inference_mode():
        for aid in sample_ids:
            rec = record_map.get(aid)
            if not rec:
                continue

            src_text = rec["source_text"]
            src_tokens = tokenizer.encode(src_text, add_special_tokens=False)
            if len(src_tokens) > 650:
                src_text = tokenizer.decode(src_tokens[:650], skip_special_tokens=True)

            messages = format_eval_prompt(src_text)
            prompt_text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            inputs = tokenizer([prompt_text], return_tensors="pt").to(model.device)

            output_ids = model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )
            gen_tokens = output_ids[0][inputs.input_ids.shape[1] :]
            raw_text = tokenizer.decode(gen_tokens, skip_special_tokens=True).strip()

            parsed = parse_prediction(raw_text)
            gold_primary = rec.get("human_audit", {}).get("primary_mechanism")
            pred_primary = parsed["prediction"]["primary_mechanism"]
            is_correct = (pred_primary == gold_primary)

            if is_correct:
                correct_count += 1

            results.append({
                "audit_id": aid,
                "gold_primary": gold_primary,
                "pred_primary": pred_primary,
                "correct": is_correct,
                "parse_status": parsed["parse_status"],
            })

    accuracy = correct_count / len(results) if results else 0.0
    return {
        "sample_size": len(results),
        "correct": correct_count,
        "accuracy": round(accuracy, 4),
        "details": results,
    }


def train_sft_experiment(
    base_model_path: Path,
    train_path: Path,
    output_dir: Path,
    report_fingerprint_path: Path,
    lr: float = 1e-4,
    epochs: int = 3,
    lora_r: int = 16,
    lora_alpha: int = 32,
    lora_dropout: float = 0.05,
    gradient_accumulation_steps: int = 4,
    seed: int = 42,
) -> dict[str, Any]:
    print("=" * 60)
    print("Phase 4B: SFT Experiment 1 Training Runner")
    print("=" * 60)

    set_seed(seed)

    # 1. Dataset Integrity Verification
    if not train_path.exists():
        raise FileNotFoundError(f"Training dataset not found: {train_path}")

    actual_train_hash = compute_file_sha256(train_path)
    if actual_train_hash != EXPECTED_TRAIN_SHA256:
        raise ValueError(
            f"Training dataset hash mismatch!\n"
            f"  Expected: {EXPECTED_TRAIN_SHA256}\n"
            f"  Actual:   {actual_train_hash}\n"
            f"Training aborted to protect experimental control."
        )

    train_records = load_and_format_train_records(train_path)
    assert len(train_records) == 43, f"Expected 43 training records, found {len(train_records)}"
    print(f"Training dataset verified: 43 records, SHA-256 = {actual_train_hash}")

    # 2. Tokenizer
    print(f"Loading tokenizer from: {base_model_path}...")
    tokenizer = AutoTokenizer.from_pretrained(str(base_model_path), trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 3. Model Loading with 4-bit Quantization
    print("Configuring 4-bit BitsAndBytes quantization (NF4, double quant)...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    print(f"Loading base model weights from: {base_model_path}...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    base_model = AutoModelForCausalLM.from_pretrained(
        str(base_model_path),
        quantization_config=bnb_config if device == "cuda" else None,
        torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,
        device_map="auto" if device == "cuda" else None,
        trust_remote_code=True,
    )

    if device == "cuda":
        base_model = prepare_model_for_kbit_training(base_model, use_gradient_checkpointing=True)
        base_model.gradient_checkpointing_enable()

    # 4. LoRA Adapter Setup
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
    peft_config = LoraConfig(
        r=lora_r,
        lora_alpha=lora_alpha,
        target_modules=target_modules,
        lora_dropout=lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(base_model, peft_config)
    if device == "cuda":
        model.enable_input_require_grads()

    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    trainable_pct = 100 * trainable_params / total_params

    print("\n--- Model Parameter Sanity Check ---")
    print(f"  Trainable parameters: {trainable_params:,}")
    print(f"  Total parameters:     {total_params:,}")
    print(f"  Trainable %:          {trainable_pct:.4f}%")
    assert trainable_pct < 5.0, f"Trainable parameter percentage {trainable_pct:.2f}% unexpectedly high for LoRA!"

    # 5. Tokenize Dataset
    print("\nTokenizing training examples with prompt token masking...")
    tokenized_dataset = [
        tokenize_sft_example(rec, tokenizer, max_seq_length=768)
        for rec in train_records
    ]

    # 6. Optimizer & Scheduler
    optimizer = torch.optim.AdamW(
        [p for p in model.parameters() if p.requires_grad],
        lr=lr,
        weight_decay=0.01,
    )

    total_steps = math.ceil(len(tokenized_dataset) / gradient_accumulation_steps) * epochs
    warmup_steps = max(1, int(0.05 * total_steps))

    scheduler = get_cosine_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
        num_training_steps=total_steps,
    )

    print(f"Total training steps: {total_steps} (warmup steps: {warmup_steps})")

    # 7. Training Loop (with per-epoch checkpointing)
    output_dir.mkdir(parents=True, exist_ok=True)
    epoch_losses = []

    model.train()
    step_count = 0

    for epoch in range(1, epochs + 1):
        epoch_loss = 0.0
        accumulated_loss = 0.0
        optimizer.zero_grad()

        print(f"\n--- Epoch {epoch}/{epochs} ---")
        for i, example in enumerate(tokenized_dataset):
            batch = collate_fn([example], pad_token_id=tokenizer.pad_token_id)
            input_ids = batch["input_ids"].to(model.device)
            attention_mask = batch["attention_mask"].to(model.device)
            labels = batch["labels"].to(model.device)

            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels,
            )
            raw_loss = outputs.loss
            assert not torch.isnan(raw_loss), (
                f"Encountered NaN loss at epoch {epoch}, record {i} ({train_records[i].get('audit_id')})!"
            )

            loss = raw_loss / gradient_accumulation_steps
            loss.backward()

            accumulated_loss += loss.item()
            epoch_loss += raw_loss.item()

            if (i + 1) % gradient_accumulation_steps == 0 or (i + 1) == len(tokenized_dataset):
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
                step_count += 1
                accumulated_loss = 0.0

            if device == "cuda":
                torch.cuda.empty_cache()

        avg_epoch_loss = epoch_loss / len(tokenized_dataset)
        epoch_losses.append(avg_epoch_loss)
        print(f"Epoch {epoch} finished. Average Loss: {avg_epoch_loss:.4f}")

        # Save per-epoch checkpoint
        checkpoint_dir = output_dir / f"checkpoint-epoch-{epoch}"
        checkpoint_dir.mkdir(parents=True, exist_ok=True)
        model.save_pretrained(str(checkpoint_dir))
        tokenizer.save_pretrained(str(checkpoint_dir))
        print(f"Saved checkpoint -> {checkpoint_dir}")

    # Save final adapter
    model.save_pretrained(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))
    print(f"\nSaved final SFT adapter -> {output_dir}")

    # 8. Training Memorization Diagnostic Check
    diagnostic_ids = ["audit_005", "audit_013", "audit_050", "audit_100", "audit_044"]
    print(f"\nRunning training memorization diagnostic on 5 sample records: {diagnostic_ids}...")
    mem_diag = run_memorization_diagnostic(model, tokenizer, train_records, diagnostic_ids)
    print(f"Training diagnostic accuracy: {mem_diag['accuracy'] * 100:.1f}% ({mem_diag['correct']}/{mem_diag['sample_size']})")
    for d in mem_diag["details"]:
        print(f"  {d['audit_id']}: gold={d['gold_primary']}, pred={d['pred_primary']} (correct={d['correct']})")

    # 9. Record Fingerprint
    fingerprint = {
        "experiment": "001",
        "phase": "4B",
        "base_model": str(base_model_path).replace("\\", "/"),
        "train_sha256": EXPECTED_TRAIN_SHA256,
        "eval_sha256": EXPECTED_EVAL_SHA256,
        "train_count": len(train_records),
        "eval_count": 17,
        "hyperparameters": {
            "learning_rate": lr,
            "epochs": epochs,
            "effective_batch_size": gradient_accumulation_steps,
            "lora_rank": lora_r,
            "lora_alpha": lora_alpha,
            "lora_dropout": lora_dropout,
            "seed": seed,
            "optimizer": "AdamW",
            "scheduler": "cosine",
            "warmup_steps": warmup_steps,
        },
        "model_parameters": {
            "trainable_parameters": trainable_params,
            "total_parameters": total_params,
            "trainable_percent": round(trainable_pct, 4),
        },
        "training_curve": {
            f"epoch_{i+1}_loss": round(l, 4) for i, l in enumerate(epoch_losses)
        },
        "memorization_diagnostic": mem_diag,
    }

    report_fingerprint_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_fingerprint_path, "w", encoding="utf-8") as f:
        json.dump(fingerprint, f, indent=2, ensure_ascii=False)

    with open(output_dir / "experiment_fingerprint.json", "w", encoding="utf-8") as f:
        json.dump(fingerprint, f, indent=2, ensure_ascii=False)

    print(f"Experiment fingerprint saved -> {report_fingerprint_path}")
    return fingerprint


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 4B: Run SFT Experiment 1.")
    parser.add_argument(
        "--base-model",
        type=Path,
        default=Path("models/Qwen2.5-1.5B-Instruct"),
    )
    parser.add_argument(
        "--train-file",
        type=Path,
        default=Path("datasets/sft/comedy_sft_train.jsonl"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("models/comedy_sft_adapter"),
    )
    parser.add_argument(
        "--fingerprint-out",
        type=Path,
        default=Path("reports/sft_experiment_001_fingerprint.json"),
    )
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument("--grad-accum", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    train_sft_experiment(
        base_model_path=args.base_model,
        train_path=args.train_file,
        output_dir=args.output_dir,
        report_fingerprint_path=args.fingerprint_out,
        lr=args.lr,
        epochs=args.epochs,
        lora_r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        gradient_accumulation_steps=args.grad_accum,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()

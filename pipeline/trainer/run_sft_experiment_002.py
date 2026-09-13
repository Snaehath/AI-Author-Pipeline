"""
pipeline/trainer/run_sft_experiment_002.py

Phase 4B-2: SFT Experiment 2 Runner (Contrastive & Counterfactual Supervision).
Fine-tunes Qwen2.5-1.5B-Instruct on the 48 human-grounded contrastive training records.

Experimental Controls (Strictly matched to 4B-1 for controlled comparison):
  - Base Model: models/Qwen2.5-1.5B-Instruct
  - Training Data: datasets/sft/comedy_contrastive_train.jsonl (48 records, prioritized confusion hubs)
  - Method: 4-bit QLoRA (NF4) with prepare_model_for_kbit_training
  - Hyperparameters:
      lr = 1e-4
      epochs = 3
      r = 16, alpha = 32, dropout = 0.05
      effective batch size = 4 (batch size 1, gradient accumulation 4)
      max_seq_length = 768
      seed = 42
  - Checkpoints:
      models/comedy_contrastive_adapter/checkpoint-epoch-1
      models/comedy_contrastive_adapter/checkpoint-epoch-2
      models/comedy_contrastive_adapter/checkpoint-epoch-3
  - Invariants:
      Zero leakage with DEV (20 records) and TEST (17 records).
      Checkpoint selection is performed strictly on DEV (comedy_dev.jsonl).
      TEST set is LOCKED and sealed until final evaluation.
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

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))
if str(WORKSPACE_ROOT.parent) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT.parent))

# Safeguard against WinError 6714 on Windows when pyarrow is probed
try:
    import pyarrow
except (OSError, ModuleNotFoundError, ImportError):
    sys.modules["pyarrow"] = None

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
    tokenize_sft_example,
)
from pipeline.evaluator.comedy_craft_evaluator import (
    compute_file_sha256,
    format_eval_prompt,
    parse_prediction,
)

EXPECTED_TRAIN_SHA256 = "65f6ec332b10c375b60d8bd57427c770eac5fd91406b40de01777eb7b5353da3"
EXPECTED_DEV_SHA256 = "18838c6ddd9bcd89d80df6e223b41bfd68cb25a1ae18976f4dd6ecd2c476829e"
EXPECTED_TEST_SHA256 = "685ad4369fd731b952801e83ed23f0e3bb7c320876052710abd01c8bd3cb3470"

DEFAULT_MODEL_PATH = Path("models/Qwen2.5-1.5B-Instruct")
DEFAULT_TRAIN_PATH = Path("datasets/sft/comedy_contrastive_train.jsonl")
DEFAULT_DEV_PATH = Path("datasets/sft/comedy_dev.jsonl")
DEFAULT_TEST_PATH = Path("datasets/sft/comedy_eval.jsonl")
DEFAULT_ADAPTER_DIR = Path("models/comedy_contrastive_adapter")
DEFAULT_FINGERPRINT_PATH = Path("reports/sft_experiment_002_fingerprint.json")


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def verify_phase_4b2_invariants(
    train_path: Path,
    dev_path: Path,
    test_path: Path,
) -> tuple[list[dict[str, Any]], str]:
    """Verify hashes and zero-leakage invariants before training."""
    if not train_path.exists():
        raise FileNotFoundError(f"Training data not found at: {train_path}")
    if not dev_path.exists():
        raise FileNotFoundError(f"DEV data not found at: {dev_path}")
    if not test_path.exists():
        raise FileNotFoundError(f"TEST data not found at: {test_path}")

    actual_train_sha256 = compute_file_sha256(train_path)
    if actual_train_sha256 != EXPECTED_TRAIN_SHA256:
        raise ValueError(
            f"Train hash mismatch!\nExpected: {EXPECTED_TRAIN_SHA256}\nActual:   {actual_train_sha256}"
        )

    actual_dev_sha256 = compute_file_sha256(dev_path)
    if actual_dev_sha256 != EXPECTED_DEV_SHA256:
        raise ValueError(
            f"DEV hash mismatch!\nExpected: {EXPECTED_DEV_SHA256}\nActual:   {actual_dev_sha256}"
        )

    actual_test_sha256 = compute_file_sha256(test_path)
    if actual_test_sha256 != EXPECTED_TEST_SHA256:
        raise ValueError(
            f"TEST hash mismatch!\nExpected: {EXPECTED_TEST_SHA256}\nActual:   {actual_test_sha256}"
        )

    train_records = []
    with open(train_path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                train_records.append(json.loads(line))

    with open(dev_path, encoding="utf-8") as f:
        dev_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}

    with open(test_path, encoding="utf-8") as f:
        test_ids = {json.loads(line)["audit_id"] for line in f if line.strip()}

    train_ids = {r["audit_id"] for r in train_records}

    leak_dev = train_ids & dev_ids
    leak_test = train_ids & test_ids

    if leak_dev:
        raise RuntimeError(f"CRITICAL: Train leaks into DEV! Overlap: {leak_dev}")
    if leak_test:
        raise RuntimeError(f"CRITICAL: Train leaks into TEST! Overlap: {leak_test}")

    print("=" * 60)
    print("Phase 4B-2 Pre-Training Invariants Verified")
    print("=" * 60)
    print(f"  Training Records: 48 (SHA-256: {actual_train_sha256[:16]}...)")
    print(f"  DEV Records:      20 (SHA-256: {actual_dev_sha256[:16]}...)")
    print(f"  TEST Records:     17 (SHA-256: {actual_test_sha256[:16]}...) [LOCKED]")
    print("  Overlap:          TRAIN intersect DEV = 0, TRAIN intersect TEST = 0")
    print("=" * 60)

    return train_records, actual_train_sha256


def train_contrastive_sft(
    model_path: Path = DEFAULT_MODEL_PATH,
    train_path: Path = DEFAULT_TRAIN_PATH,
    dev_path: Path = DEFAULT_DEV_PATH,
    test_path: Path = DEFAULT_TEST_PATH,
    adapter_dir: Path = DEFAULT_ADAPTER_DIR,
    fingerprint_path: Path = DEFAULT_FINGERPRINT_PATH,
    learning_rate: float = 1e-4,
    epochs: int = 3,
    lora_r: int = 16,
    lora_alpha: int = 32,
    lora_dropout: float = 0.05,
    grad_accum_steps: int = 4,
    max_seq_length: int = 768,
    seed: int = 42,
) -> dict[str, Any]:
    """Execute Phase 4B-2 QLoRA fine-tuning and save multi-epoch checkpoints."""
    set_seed(seed)

    # 1. Verify invariants
    train_records, train_sha256 = verify_phase_4b2_invariants(
        train_path=train_path,
        dev_path=dev_path,
        test_path=test_path,
    )

    # 2. Setup Tokenizer
    print(f"Loading tokenizer from: {model_path}...")
    tokenizer = AutoTokenizer.from_pretrained(str(model_path), trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 3. Load Base Model in 4-bit NF4
    print(f"Loading base model in 4-bit QLoRA from: {model_path}...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        str(model_path),
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )

    base_model = prepare_model_for_kbit_training(base_model, use_gradient_checkpointing=True)
    base_model.gradient_checkpointing_enable()

    # 4. Attach LoRA Adapter
    lora_config = LoraConfig(
        r=lora_r,
        lora_alpha=lora_alpha,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(base_model, lora_config)
    model.enable_input_require_grads()
    model.print_trainable_parameters()

    # 5. Tokenize training dataset
    print(f"Tokenizing {len(train_records)} contrastive training records (max_seq_length={max_seq_length})...")
    tokenized_dataset = []
    for r in train_records:
        tok_data = tokenize_sft_example(r, tokenizer, max_seq_length=max_seq_length)
        tokenized_dataset.append(tok_data)

    # 6. Setup Optimizer & Cosine Schedule
    total_steps = math.ceil((len(tokenized_dataset) * epochs) / grad_accum_steps)
    warmup_steps = max(1, int(total_steps * 0.05))

    optimizer = torch.optim.AdamW(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=learning_rate,
        weight_decay=0.01,
    )
    scheduler = get_cosine_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
        num_training_steps=total_steps,
    )

    print(f"Training plan: {epochs} epochs, {total_steps} optimizer steps, {warmup_steps} warmup steps.")

    # 7. Training Loop with Multi-Checkpoint Saving
    adapter_dir.mkdir(parents=True, exist_ok=True)
    step_count = 0
    epoch_losses: list[dict[str, Any]] = []

    model.train()

    for epoch in range(1, epochs + 1):
        print(f"\n--- Starting Epoch {epoch}/{epochs} ---")
        epoch_loss_total = 0.0
        optimizer.zero_grad()

        # Deterministic shuffle per epoch based on seed
        epoch_indices = list(range(len(tokenized_dataset)))
        random.Random(seed + epoch).shuffle(epoch_indices)

        for i, idx in enumerate(epoch_indices):
            ex = tokenized_dataset[idx]
            input_ids = torch.tensor([ex["input_ids"]], device=model.device)
            attention_mask = torch.tensor([ex["attention_mask"]], device=model.device)
            labels = torch.tensor([ex["labels"]], device=model.device)

            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels,
            )
            raw_loss = outputs.loss

            if torch.isnan(raw_loss) or torch.isinf(raw_loss):
                raise RuntimeError(
                    f"NaN or Inf loss encountered at epoch {epoch}, example index {idx} ({train_records[idx]['audit_id']})!"
                )

            loss = raw_loss / grad_accum_steps
            loss.backward()

            epoch_loss_total += raw_loss.item()

            if (i + 1) % grad_accum_steps == 0 or (i + 1) == len(epoch_indices):
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
                step_count += 1

            del outputs, raw_loss, loss, input_ids, attention_mask, labels
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        avg_loss = epoch_loss_total / len(epoch_indices)
        print(f"Epoch {epoch} Complete. Average Loss: {avg_loss:.4f}")

        epoch_checkpoint_dir = adapter_dir / f"checkpoint-epoch-1" if epoch == 1 else (
            adapter_dir / f"checkpoint-epoch-2" if epoch == 2 else adapter_dir / f"checkpoint-epoch-3"
        )
        print(f"Saving Checkpoint: {epoch_checkpoint_dir}...")
        model.save_pretrained(str(epoch_checkpoint_dir))
        tokenizer.save_pretrained(str(epoch_checkpoint_dir))

        epoch_losses.append({
            "epoch": epoch,
            "average_loss": round(avg_loss, 4),
            "checkpoint": str(epoch_checkpoint_dir),
        })

    # Save final adapter
    print(f"\nSaving Final Model Adapter to: {adapter_dir}...")
    model.save_pretrained(str(adapter_dir))
    tokenizer.save_pretrained(str(adapter_dir))

    # 8. Build Experiment Fingerprint
    fingerprint = {
        "experiment_id": "sft_experiment_002",
        "phase": "4B-2",
        "objective": "Contrastive & Counterfactual Supervision for Comedy Mechanism Discrimination",
        "base_model": str(model_path).replace("\\", "/"),
        "training_data": {
            "path": str(train_path).replace("\\", "/"),
            "records": len(train_records),
            "sha256": train_sha256,
        },
        "dev_data": {
            "path": str(dev_path).replace("\\", "/"),
            "records": 20,
            "sha256": EXPECTED_DEV_SHA256,
        },
        "test_data": {
            "path": str(test_path).replace("\\", "/"),
            "records": 17,
            "sha256": EXPECTED_TEST_SHA256,
            "status": "SEALED",
        },
        "hyperparameters": {
            "epochs": epochs,
            "learning_rate": learning_rate,
            "lora_r": lora_r,
            "lora_alpha": lora_alpha,
            "lora_dropout": lora_dropout,
            "effective_batch_size": grad_accum_steps,
            "max_seq_length": max_seq_length,
            "seed": seed,
        },
        "epoch_losses": epoch_losses,
        "adapter_dir": str(adapter_dir).replace("\\", "/"),
        "checkpoints": [ep["checkpoint"].replace("\\", "/") for ep in epoch_losses],
    }

    fingerprint_path.parent.mkdir(parents=True, exist_ok=True)
    with open(fingerprint_path, "w", encoding="utf-8") as f:
        json.dump(fingerprint, f, indent=2, ensure_ascii=False)

    print(f"Experiment Fingerprint saved to: {fingerprint_path}")
    return fingerprint


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 4B-2 SFT Experiment 2 Runner.")
    parser.add_argument("--model-path", type=Path, default=DEFAULT_MODEL_PATH)
    parser.add_argument("--train-path", type=Path, default=DEFAULT_TRAIN_PATH)
    parser.add_argument("--dev-path", type=Path, default=DEFAULT_DEV_PATH)
    parser.add_argument("--test-path", type=Path, default=DEFAULT_TEST_PATH)
    parser.add_argument("--adapter-dir", type=Path, default=DEFAULT_ADAPTER_DIR)
    parser.add_argument("--fingerprint", type=Path, default=DEFAULT_FINGERPRINT_PATH)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--max-seq-length", type=int, default=768)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    train_contrastive_sft(
        model_path=args.model_path,
        train_path=args.train_path,
        dev_path=args.dev_path,
        test_path=args.test_path,
        adapter_dir=args.adapter_dir,
        fingerprint_path=args.fingerprint,
        learning_rate=args.lr,
        epochs=args.epochs,
        lora_r=args.lora_r,
        lora_alpha=args.lora_alpha,
        grad_accum_steps=args.batch_size,
        max_seq_length=args.max_seq_length,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()

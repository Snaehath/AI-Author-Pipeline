"""
Training Pipeline Orchestrator Module.

Loads train/val SFT datasets, builds 4-bit QLoRA model, runs local training,
and saves fine-tuned LoRA adapters to models/story_lora_adapter/.
"""

import sys
try:
    import pyarrow
except OSError:
    sys.modules["pyarrow"] = None

import json
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, Optional

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from .dataset_loader import load_and_tokenize_sft_dataset
from .qlora_builder import build_qlora_model_and_tokenizer, TrainingDependencyError
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Trainer.Pipeline")


@dataclass
class TrainingResult:
    """Dataclass holding training output metrics and file locations."""
    adapter_output_dir: Path
    base_model_used: str
    total_train_examples: int
    total_val_examples: int
    training_timestamp: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts TrainingResult to dictionary."""
        data = asdict(self)
        data["adapter_output_dir"] = str(self.adapter_output_dir)
        return data


class TrainingPipeline:
    """Orchestrates local QLoRA fine-tuning for Qwen 2.5 1.5B Instruct."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initializes TrainingPipeline.

        Args:
            config_path: Path to train_config.json.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "train_config.json")
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Loads training configuration JSON if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded training config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read train config file ({e}). Using defaults.")
        return {}

    def run_training(self) -> TrainingResult:
        """Executes full QLoRA fine-tuning pipeline.

        Returns:
            TrainingResult object containing output paths and metrics.
        """
        logger.info(f"==================================================")
        logger.info(f"Starting AI Author Studio Local Training Pipeline...")

        # Step 1: Resolve Model Path
        raw_base_path = self.config.get("base_model_path", "models/Qwen2.5-1.5B-Instruct")
        local_base_path = self.root_dir / raw_base_path
        if local_base_path.exists():
            target_model = str(local_base_path)
            logger.info(f"Using local base model at: '{target_model}'")
        else:
            target_model = self.config.get("fallback_model_id", "Qwen/Qwen2.5-1.5B-Instruct")
            logger.info(f"Local model path not found. Falling back to Hugging Face Hub ID: '{target_model}'")

        # Step 2: Resolve Datasets
        train_rel = self.config.get("train_dataset_path", "datasets/train.jsonl")
        val_rel = self.config.get("val_dataset_path", "datasets/val.jsonl")

        train_path = self.root_dir / train_rel
        val_path = self.root_dir / val_rel

        if not train_path.exists():
            raise FileNotFoundError(f"Train dataset missing at '{train_path}'. Please run Module 8 first.")

        # Step 3: Build Model & Tokenizer
        lora_settings = self.config.get("lora", {})
        use_4bit = self.config.get("use_4bit", False)
        try:
            model, tokenizer = build_qlora_model_and_tokenizer(target_model, lora_settings, use_4bit=use_4bit)
        except TrainingDependencyError as e:
            logger.error(str(e))
            raise

        # Step 4: Tokenize Datasets
        t_cfg = self.config.get("training", {})
        max_seq_len = t_cfg.get("max_seq_length", 512)

        train_ds = load_and_tokenize_sft_dataset(train_path, tokenizer, max_seq_len)
        val_ds = load_and_tokenize_sft_dataset(val_path, tokenizer, max_seq_len) if val_path.exists() else None

        # Step 5: Configure Training Arguments
        out_rel = self.config.get("output_dir", "models/story_lora_adapter")
        adapter_output_path = self.root_dir / out_rel
        adapter_output_path.mkdir(parents=True, exist_ok=True)

        try:
            try:
                from trl import SFTConfig, SFTTrainer

                sft_args = SFTConfig(
                    output_dir=str(adapter_output_path),
                    per_device_train_batch_size=t_cfg.get("per_device_train_batch_size", 1),
                    per_device_eval_batch_size=t_cfg.get("per_device_eval_batch_size", 1),
                    gradient_accumulation_steps=t_cfg.get("gradient_accumulation_steps", 8),
                    learning_rate=t_cfg.get("learning_rate", 2e-4),
                    num_train_epochs=t_cfg.get("num_train_epochs", 3),
                    warmup_ratio=t_cfg.get("warmup_ratio", 0.05),
                    fp16=t_cfg.get("fp16", True),
                    bf16=t_cfg.get("bf16", False),
                    gradient_checkpointing=t_cfg.get("gradient_checkpointing", True),
                    optim=t_cfg.get("optim", "paged_adamw_8bit"),
                    logging_steps=t_cfg.get("logging_steps", 1),
                    save_strategy=t_cfg.get("save_strategy", "epoch"),
                    eval_strategy=t_cfg.get("eval_strategy", t_cfg.get("evaluation_strategy", "epoch")) if val_ds else "no",
                    max_length=max_seq_len,
                    dataset_text_field="text",
                    report_to="none",
                )

                trainer = SFTTrainer(
                    model=model,
                    train_dataset=train_ds,
                    eval_dataset=val_ds,
                    args=sft_args,
                )
            except Exception as trl_err:
                logger.info(f"SFTConfig initialization note ({trl_err}). Using standard Hugging Face Trainer.")
                from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling

                training_args = TrainingArguments(
                    output_dir=str(adapter_output_path),
                    per_device_train_batch_size=t_cfg.get("per_device_train_batch_size", 1),
                    per_device_eval_batch_size=t_cfg.get("per_device_eval_batch_size", 1),
                    gradient_accumulation_steps=t_cfg.get("gradient_accumulation_steps", 8),
                    learning_rate=t_cfg.get("learning_rate", 2e-4),
                    num_train_epochs=t_cfg.get("num_train_epochs", 3),
                    warmup_ratio=t_cfg.get("warmup_ratio", 0.05),
                    fp16=t_cfg.get("fp16", True),
                    bf16=t_cfg.get("bf16", False),
                    gradient_checkpointing=t_cfg.get("gradient_checkpointing", True),
                    optim=t_cfg.get("optim", "paged_adamw_8bit"),
                    logging_steps=1,
                    save_strategy=t_cfg.get("save_strategy", "epoch"),
                    eval_strategy=t_cfg.get("eval_strategy", "epoch") if val_ds else "no",
                    report_to="none",
                )

                def tokenize_fn(examples):
                    return tokenizer(examples["text"], truncation=True, max_length=max_seq_len)

                train_tokenized = train_ds.map(tokenize_fn, batched=True, remove_columns=["text"])
                val_tokenized = val_ds.map(tokenize_fn, batched=True, remove_columns=["text"]) if val_ds else None

                trainer = Trainer(
                    model=model,
                    train_dataset=train_tokenized,
                    eval_dataset=val_tokenized,
                    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
                    args=training_args,
                )

            logger.info("Executing QLoRA fine-tuning...")
            trainer.train()

            # Save LoRA Adapter
            logger.info(f"Saving fine-tuned LoRA adapter weights to: '{adapter_output_path}'")
            trainer.model.save_pretrained(str(adapter_output_path))
            tokenizer.save_pretrained(str(adapter_output_path))

        except Exception as e:
            logger.error(f"Training failed: {e}")
            raise

        timestamp = datetime.now(timezone.utc).isoformat()
        metrics = {
            "base_model": target_model,
            "adapter_output_dir": str(adapter_output_path),
            "timestamp": timestamp,
            "status": "completed",
        }
        with open(adapter_output_path / "training_metrics.json", "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2)

        logger.info("Local QLoRA fine-tuning complete!")
        logger.info(f"==================================================")

        return TrainingResult(
            adapter_output_dir=adapter_output_path,
            base_model_used=target_model,
            total_train_examples=len(train_ds),
            total_val_examples=len(val_ds) if val_ds else 0,
            training_timestamp=timestamp,
        )


if __name__ == "__main__":
    pipeline = TrainingPipeline()
    res = pipeline.run_training()
    print(json.dumps(res.to_dict(), indent=2))

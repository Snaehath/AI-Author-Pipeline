"""
Training Module for AI Author Studio.

Implements QLoRA 4-bit fine-tuning of Qwen 2.5 1.5B Instruct optimized for low-VRAM hardware.
"""

from .dataset_loader import load_and_tokenize_sft_dataset
from .qlora_builder import build_qlora_model_and_tokenizer
from .train_pipeline import TrainingPipeline

__all__ = [
    "load_and_tokenize_sft_dataset",
    "build_qlora_model_and_tokenizer",
    "TrainingPipeline",
]

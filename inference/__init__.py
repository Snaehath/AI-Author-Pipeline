"""
Inference Engine Module for AI Author Studio.

Loads base model with fine-tuned LoRA adapter and provides 10 core storytelling generation functions.
"""

from .model_loader import load_inference_model_and_tokenizer
from .generator import StoryGenerator

__all__ = [
    "load_inference_model_and_tokenizer",
    "StoryGenerator",
]

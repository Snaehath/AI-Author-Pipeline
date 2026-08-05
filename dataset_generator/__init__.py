"""
Dataset Generator Module for AI Author Studio.

Synthesizes extracted book knowledge into Supervised Fine-Tuning (SFT) datasets
covering 8 core writing capabilities.
"""

from .prompt_templates import PromptTemplates
from .sft_synthesizer import SFTSynthesizer, SFTExample
from .dataset_pipeline import DatasetPipeline

__all__ = [
    "PromptTemplates",
    "SFTSynthesizer",
    "SFTExample",
    "DatasetPipeline",
]

"""
Evaluation Suite Module for AI Author Studio.

Computes BLEU, ROUGE, Perplexity, and Author Style Consistency metrics
comparing generated novel manuscripts against reference human prose.
"""

from .bleu_rouge_evaluator import calculate_bleu_rouge
from .style_consistency import calculate_style_consistency
from .eval_pipeline import EvaluationPipeline

__all__ = [
    "calculate_bleu_rouge",
    "calculate_style_consistency",
    "EvaluationPipeline",
]

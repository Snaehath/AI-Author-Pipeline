"""
Author Style Consistency Module.

Evaluates narrative style metrics: Type-Token Ratio (TTR) vocabulary richness,
sentence length distributions, dialogue-to-narration ratio, and POV consistency.
"""

import re
from typing import Dict, Any, List


def calculate_ttr(tokens: List[str]) -> float:
    """Calculates Type-Token Ratio (Vocabulary Richness)."""
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def get_sentences(text: str) -> List[str]:
    """Splits text into clean non-empty sentences."""
    raw_sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in raw_sentences if s.strip()]


def calculate_style_consistency(hypothesis_text: str, reference_text: str) -> Dict[str, Any]:
    """Computes author style consistency metrics comparing hypothesis against reference.

    Args:
        hypothesis_text: Generated story manuscript.
        reference_text: Target human author manuscript.

    Returns:
        Dictionary containing style consistency breakdown and overall similarity score.
    """
    hyp_words = [w.strip().lower() for w in hypothesis_text.replace("\n", " ").split() if w.strip()]
    raw_ref_words = [w.strip().lower() for w in reference_text.replace("\n", " ").split() if w.strip()]
    
    # Standardize reference comparison window to matching sample size (max 4,000 words)
    sample_size = max(1000, len(hyp_words))
    ref_words = raw_ref_words[:sample_size] if len(raw_ref_words) > sample_size else raw_ref_words

    hyp_ttr = calculate_ttr(hyp_words)
    ref_ttr = calculate_ttr(ref_words)

    # Sentence Length Distributions
    hyp_sents = get_sentences(hypothesis_text)
    ref_sents = get_sentences(" ".join(reference_text.split()[:sample_size * 2]))

    hyp_avg_sent = sum(len(s.split()) for s in hyp_sents) / max(1, len(hyp_sents))
    ref_avg_sent = sum(len(s.split()) for s in ref_sents) / max(1, len(ref_sents))

    # Dialogue Ratios
    hyp_dialogue_chars = sum(len(m) for m in re.findall(r'"([^"]*)"', hypothesis_text))
    ref_dialogue_sample = reference_text[:len(hypothesis_text) * 2]
    ref_dialogue_chars = sum(len(m) for m in re.findall(r'"([^"]*)"', ref_dialogue_sample))

    hyp_dialogue_ratio = hyp_dialogue_chars / max(1, len(hypothesis_text))
    ref_dialogue_ratio = ref_dialogue_chars / max(1, len(ref_dialogue_sample))

    # Metric Similarities (0.0 to 1.0)
    ttr_sim = 1.0 - min(1.0, abs(hyp_ttr - ref_ttr) / max(1e-6, ref_ttr))
    sent_len_sim = 1.0 - min(1.0, abs(hyp_avg_sent - ref_avg_sent) / max(1e-6, ref_avg_sent))
    dialogue_sim = 1.0 - min(1.0, abs(hyp_dialogue_ratio - ref_dialogue_ratio) / max(1e-6, max(0.1, ref_dialogue_ratio)))

    overall_consistency = round((ttr_sim * 0.35) + (sent_len_sim * 0.35) + (dialogue_sim * 0.30), 4)

    return {
        "generated_ttr": round(hyp_ttr, 4),
        "reference_ttr": round(ref_ttr, 4),
        "ttr_similarity": round(ttr_sim, 4),
        "generated_avg_sentence_length": round(hyp_avg_sent, 2),
        "reference_avg_sentence_length": round(ref_avg_sent, 2),
        "sentence_length_similarity": round(sent_len_sim, 4),
        "generated_dialogue_ratio": round(hyp_dialogue_ratio, 4),
        "reference_dialogue_ratio": round(ref_dialogue_ratio, 4),
        "dialogue_ratio_similarity": round(dialogue_sim, 4),
        "overall_style_consistency": overall_consistency,
    }

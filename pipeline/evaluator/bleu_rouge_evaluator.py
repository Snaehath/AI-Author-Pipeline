"""
BLEU & ROUGE Evaluator Module.

Calculates N-gram precision (BLEU-1 to BLEU-4) and recall/precision/F1 metrics
(ROUGE-1, ROUGE-2, ROUGE-L) comparing generated text against reference text.
"""

import math
from collections import Counter
from typing import Dict, Any, List


def get_ngrams(tokens: List[str], n: int) -> List[tuple]:
    """Extracts n-grams from a list of word tokens."""
    return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]


def calculate_bleu(hyp_tokens: List[str], ref_tokens: List[str], max_n: int = 4) -> Dict[str, float]:
    """Calculates modified n-gram precision BLEU scores (BLEU-1 to BLEU-4)."""
    if not hyp_tokens or not ref_tokens:
        return {"bleu_1": 0.0, "bleu_2": 0.0, "bleu_3": 0.0, "bleu_4": 0.0, "overall_bleu": 0.0}

    precisions = []
    for n in range(1, max_n + 1):
        hyp_ngrams = get_ngrams(hyp_tokens, n)
        ref_ngrams = get_ngrams(ref_tokens, n)

        if not hyp_ngrams:
            precisions.append(0.0)
            continue

        hyp_counts = Counter(hyp_ngrams)
        ref_counts = Counter(ref_ngrams)

        clipped_matches = sum(min(count, ref_counts[gram]) for gram, count in hyp_counts.items())
        precision = clipped_matches / len(hyp_ngrams)
        precisions.append(precision)

    # Brevity Penalty
    c = len(hyp_tokens)
    r = len(ref_tokens)
    bp = 1.0 if c > r else math.exp(1 - (r / max(1, c)))

    # Overall BLEU (Geometric Mean)
    if all(p > 0 for p in precisions):
        geo_mean = math.exp(sum(math.log(p) for p in precisions) / max_n)
    else:
        geo_mean = 0.0

    overall_bleu = round(bp * geo_mean, 4)

    return {
        "bleu_1": round(precisions[0], 4),
        "bleu_2": round(precisions[1], 4),
        "bleu_3": round(precisions[2], 4),
        "bleu_4": round(precisions[3], 4),
        "brevity_penalty": round(bp, 4),
        "overall_bleu": overall_bleu,
    }


def lcs_length(seq1: List[str], seq2: List[str]) -> int:
    """Calculates Longest Common Subsequence (LCS) length for ROUGE-L."""
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def calculate_rouge(hyp_tokens: List[str], ref_tokens: List[str]) -> Dict[str, Dict[str, float]]:
    """Calculates ROUGE-1, ROUGE-2, and ROUGE-L scores."""
    def calc_pr_f1(matches: int, hyp_len: int, ref_len: int) -> Dict[str, float]:
        precision = matches / max(1, hyp_len)
        recall = matches / max(1, ref_len)
        f1 = (2 * precision * recall) / max(1e-6, (precision + recall)) if (precision + recall) > 0 else 0.0
        return {"precision": round(precision, 4), "recall": round(recall, 4), "f1": round(f1, 4)}

    # ROUGE-1
    h1, r1 = Counter(hyp_tokens), Counter(ref_tokens)
    r1_matches = sum(min(count, r1[w]) for w, count in h1.items())
    rouge_1 = calc_pr_f1(r1_matches, len(hyp_tokens), len(ref_tokens))

    # ROUGE-2
    h2_ng = get_ngrams(hyp_tokens, 2)
    r2_ng = get_ngrams(ref_tokens, 2)
    h2, r2 = Counter(h2_ng), Counter(r2_ng)
    r2_matches = sum(min(count, r2[gram]) for gram, count in h2.items())
    rouge_2 = calc_pr_f1(r2_matches, len(h2_ng), len(r2_ng))

    # ROUGE-L
    lcs_val = lcs_length(hyp_tokens, ref_tokens)
    rouge_l = calc_pr_f1(lcs_val, len(hyp_tokens), len(ref_tokens))

    return {
        "rouge_1": rouge_1,
        "rouge_2": rouge_2,
        "rouge_l": rouge_l,
    }


def calculate_bleu_rouge(hypothesis_text: str, reference_text: str) -> Dict[str, Any]:
    """Calculates complete BLEU and ROUGE metric suite.

    Args:
        hypothesis_text: Generated story text.
        reference_text: Reference author text.

    Returns:
        Dictionary containing BLEU and ROUGE score distributions.
    """
    hyp_tokens = [w.strip().lower() for w in hypothesis_text.replace("\n", " ").split() if w.strip()]
    ref_tokens = [w.strip().lower() for w in reference_text.replace("\n", " ").split() if w.strip()]

    bleu_metrics = calculate_bleu(hyp_tokens, ref_tokens)
    rouge_metrics = calculate_rouge(hyp_tokens, ref_tokens)

    return {
        "bleu_scores": bleu_metrics,
        "rouge_scores": rouge_metrics,
    }

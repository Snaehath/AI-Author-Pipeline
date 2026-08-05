# Module 12: Evaluation Suite — Documentation

## Overview
**Module 12 (Evaluation Suite)** evaluates generated novel manuscripts against reference human author prose across 4 core quantitative and qualitative metrics:
1. 🎯 **BLEU Score** (BLEU-1 to BLEU-4 n-gram precision).
2. 📊 **ROUGE Score** (ROUGE-1, ROUGE-2, ROUGE-L precision, recall, and F1).
3. 🌀 **Fluency & Perplexity Metric**.
4. 🖋️ **Author Style Consistency Score** (Type-Token Ratio vocabulary richness, average sentence length, and dialogue-to-narration ratio).

Outputs are saved to `outputs/<book_slug>/evaluation_report.json` and `outputs/<book_slug>/evaluation_summary.md`.

---

## Architecture & Components

```
AI_Author/evaluator/
├── bleu_rouge_evaluator.py # Computes BLEU-1 to BLEU-4 and ROUGE-1/2/L metrics
├── style_consistency.py   # Computes Author Style Consistency & TTR vocabulary richness
└── eval_pipeline.py       # Main pipeline orchestrator
```

### 1. BLEU & ROUGE Evaluator (`bleu_rouge_evaluator.py`)
Calculates precision and recall overlap:
- **BLEU-1 to BLEU-4**: N-gram precision matches with brevity penalty calculation.
- **ROUGE-1, ROUGE-2, ROUGE-L**: Unigram, bigram, and Longest Common Subsequence (LCS) precision, recall, and F1 scores.

### 2. Style Consistency Evaluator (`style_consistency.py`)
Measures stylistic fidelity:
- **Type-Token Ratio (TTR)**: Unique words divided by total words.
- **Sentence Length Distribution**: Average sentence length matching.
- **Dialogue Ratio**: Proportion of dialogue text to total manuscript text.

---

## Output Schema (`evaluation_report.json`)

```json
{
  "book_title": "Generated Novel",
  "reference_book": "Sample Novel",
  "evaluation_timestamp": "2026-08-03T11:15:00.000Z",
  "bleu_scores": {
    "bleu_1": 0.52,
    "bleu_2": 0.38,
    "bleu_3": 0.28,
    "bleu_4": 0.22,
    "brevity_penalty": 1.0,
    "overall_bleu": 0.35
  },
  "rouge_scores": {
    "rouge_1": {"precision": 0.58, "recall": 0.52, "f1": 0.55},
    "rouge_2": {"precision": 0.32, "recall": 0.28, "f1": 0.30},
    "rouge_l": {"precision": 0.52, "recall": 0.48, "f1": 0.50}
  },
  "author_style_consistency": {
    "generated_ttr": 0.65,
    "reference_ttr": 0.68,
    "ttr_similarity": 0.95,
    "generated_avg_sentence_length": 14.2,
    "reference_avg_sentence_length": 15.1,
    "sentence_length_similarity": 0.94,
    "generated_dialogue_ratio": 0.25,
    "reference_dialogue_ratio": 0.28,
    "dialogue_ratio_similarity": 0.89,
    "overall_style_consistency": 0.93
  }
}
```

---

## How to Run & Test

### Running Automated Novel Builder (Generating Full Novel)
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python inference/novel_builder.py
```

### Running Evaluation Unit Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_evaluator.py
```

### Executing Evaluation Suite on Generated Book
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python evaluator/eval_pipeline.py outputs/generated_novel --reference_dir outputs/sample_novel
```

# Module 5: Dialogue Analyzer — Documentation

## Overview
**Module 5 (Dialogue Analyzer)** performs deep linguistic and narrative analysis on every spoken line of dialogue extracted from Module 2 (`outputs/<book_slug>/chapters/chapter_XX.json`).

Every extracted dialogue metric strictly adheres to our metric contract:
```json
{
  "value": "<Extracted Dialogue Attribute>",
  "confidence": 0.88,
  "evidence": "<Direct Dialogue / Speech Tag Quote>"
}
```

Outputs are written to `outputs/<book_slug>/dialogue_analysis.json`.

---

## Architecture & Components

```
AI_Author/analyzer/
├── dialogue_emotion_analyzer.py # Dialogue emotion & sub-conflict classifier
├── speech_style_analyzer.py    # Humor, speech style, vocabulary & length metric parser
└── dialogue_analyzer.py        # Main pipeline orchestrator
```

### 1. Dialogue Emotion Analyzer (`dialogue_emotion_analyzer.py`)
- **Emotion**: `Urgent / Cautious`, `Fearful`, `Hopeful / Reassuring`, `Angry / Hostile`, `Sarcastic / Witty`, `Calm / Conversational`.
- **Sub-Conflict**: `Warning / Friction`, `Direct Disagreement`, `Cooperative / Harmonious`, `Inquiry / Questioning`.

### 2. Speech Style Analyzer (`speech_style_analyzer.py`)
- **Humor**: `Witty / Sarcastic`, `Playful`, `None`.
- **Speech Style**: `Imperative / Advice`, `Short / Punchy`, `Formal / Ornate`, `Casual / Direct`.
- **Vocabulary Level**: `Everyday / Direct`, `High Fantasy / Formal`.
- **Dialogue Length**: `Brief (1-5 words)`, `Moderate (6-15 words)`, `Extended (16+ words)`.

### 3. Dialogue Analyzer Orchestrator (`dialogue_analyzer.py`)
- Reads all `chapter_XX.json` files for a book.
- Iterates over all dialogue items across scenes.
- Computes aggregated dialogue metrics (`average_words_per_dialogue`, `dialogue_conflict_distribution`).
- Writes `outputs/<book_slug>/dialogue_analysis.json`.

---

## Output Schema (`dialogue_analysis.json`)

```json
{
  "book_title": "Sample Novel",
  "total_dialogues_analyzed": 3,
  "dialogue_metrics_summary": {
    "average_words_per_dialogue": 7.3,
    "dialogue_conflict_distribution": {
      "Warning / Friction": 2,
      "Inquiry / Questioning": 1
    }
  },
  "dialogues": [
    {
      "chapter_index": 1,
      "scene_index": 1,
      "speaker": {
        "value": "Kane",
        "confidence": 0.9,
        "evidence": "\"We should make camp before nightfall\" Kane said"
      },
      "spoken_text": "We should make camp before nightfall",
      "speech_tag": "Kane said, leaning on his wooden staff",
      "emotion": {
        "value": "Urgent / Cautious",
        "confidence": 0.86,
        "evidence": "\"We should make camp before nightfall\""
      },
      "conflict": {
        "value": "Warning / Friction",
        "confidence": 0.86,
        "evidence": "\"We should make camp before nightfall\""
      },
      "humor": {
        "value": "None",
        "confidence": 0.9,
        "evidence": "\"We should make camp before nightfall\""
      },
      "speech_style": {
        "value": "Imperative / Advice",
        "confidence": 0.88,
        "evidence": "\"We should make camp before nightfall\""
      },
      "vocabulary": {
        "value": "Everyday / Direct",
        "confidence": 0.9,
        "evidence": "\"We should make camp before nightfall\""
      },
      "dialogue_length": {
        "value": "Brief (6 words)",
        "confidence": 1.0,
        "evidence": "6 words"
      }
    }
  ]
}
```

---

## How to Run & Test

### Running Unit & Integration Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_dialogue_analyzer.py
```

### Analyzing Dialogue for a Processed Book
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python analyzer/dialogue_analyzer.py outputs/sample_novel
```

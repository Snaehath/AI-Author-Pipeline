# Module 6: Emotion Analyzer — Documentation

## Overview
**Module 6 (Emotion Analyzer)** tracks emotional progression throughout a story, measuring emotional valence (-1.0 to +1.0), emotional intensity (0.0 to 1.0), transition triggers, and generating a structured **emotion timeline**.

Every extracted emotion metric strictly adheres to our metric contract:
```json
{
  "value": "<Extracted Emotion Metric>",
  "confidence": 0.88,
  "evidence": "<Direct Narrative Snippet>"
}
```

Outputs are written to `outputs/<book_slug>/emotion_analysis.json`.

---

## Architecture & Components

```
AI_Author/analyzer/
├── valence_intensity_calculator.py # Valence (-1.0 to +1.0) & Intensity (0.0 to 1.0) calculator
├── emotion_timeline_tracker.py    # Dominant emotion classifier & shift trigger detector
└── emotion_analyzer.py            # Main pipeline orchestrator
```

### 1. Valence & Intensity Calculator (`valence_intensity_calculator.py`)
- **Valence**: Measures polarity from `-1.0` (deep negative/fearful/somber) to `+1.0` (deep positive/joyful/triumphant).
- **Intensity**: Measures emotional arousal energy score from `0.0` (calm/passive) to `1.0` (high action/climax).

### 2. Emotion Timeline Tracker (`emotion_timeline_tracker.py`)
- **Dominant Emotion**: Classifies primary state (`Wonder / Awe & Triumph`, `Hopeful / Reassuring`, `Fear / Dread & Tension`, `Anticipation / Caution`, `Reflective / Calm`).
- **Shift Triggers**: Identifies narrative events causing emotional transitions (`Discovery of Pedestal`, `Threat of Wolves`, etc.).

### 3. Emotion Analyzer Orchestrator (`emotion_analyzer.py`)
- Reads all `chapter_XX.json` files for a book.
- Builds chapter-by-chapter emotion timeline checkpoints.
- Computes overall book-level average valence and intensity metrics.
- Writes `outputs/<book_slug>/emotion_analysis.json`.

---

## Output Schema (`emotion_analysis.json`)

```json
{
  "book_title": "Sample Novel",
  "total_timeline_points": 5,
  "overall_emotional_arc": {
    "value": "Emotional Arc Trajectory (Anticipation / Caution -> Wonder / Awe & Triumph)",
    "confidence": 0.9,
    "evidence": "Overall Book Average Valence: +0.35, Average Intensity: 0.68"
  },
  "average_book_valence": 0.35,
  "average_book_intensity": 0.68,
  "emotion_timeline": [
    {
      "chapter_index": 1,
      "chapter_title": "CHAPTER 1: The Whispering Wind",
      "dominant_emotion": {
        "value": "Anticipation / Caution",
        "confidence": 0.82,
        "evidence": "The Chronicles of Eldoria: The Lost Artifact"
      },
      "valence": -0.2,
      "intensity": 0.6,
      "emotional_shift_trigger": {
        "value": "Narrative Trigger: Aria adjusted her leather cloak as the cold mountain wind howled...",
        "confidence": 0.88,
        "evidence": "Aria adjusted her leather cloak as the cold mountain wind howled through the canyon."
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
python tests/test_emotion_analyzer.py
```

### Analyzing Emotion Timeline for a Processed Book
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python analyzer/emotion_analyzer.py outputs/sample_novel
```

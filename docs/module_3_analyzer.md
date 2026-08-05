# Module 3: Story Analyzer — Documentation

## Overview
**Module 3 (Story Analyzer)** extracts structural storytelling knowledge (not plain text summaries) from the parsed chapters generated in Module 2 (`outputs/<book_slug>/chapters/chapter_XX.json`).

Every extracted storytelling dimension strictly adheres to our metric contract:
```json
{
  "value": "<Extracted Narrative Feature>",
  "confidence": 0.85,
  "evidence": "<Direct Text Snippet / Context Proof>"
}
```

The output is written to `outputs/<book_slug>/story_analysis.json`.

---

## Architecture & Components

```
AI_Author/analyzer/
├── __init__.py                  # Package exports
├── pov_detector.py              # Narrative Point of View detector (First-Person, Third-Person)
├── tone_mood_analyzer.py        # Tone, Mood, and structural Pacing metrics
├── conflict_scene_analyzer.py   # Conflict taxonomy & Scene Purpose analyzer
├── foreshadow_twist_analyzer.py # Foreshadowing, Cliffhanger, and Theme detector
└── story_analyzer.py            # Main pipeline orchestrator
```

### 1. POV Detector (`pov_detector.py`)
- Analyzes pronoun distributions (`I/me/my/we` vs `he/she/they`).
- Classifies narrative perspective as `First-Person`, `Third-Person Limited`, or `Third-Person Omniscient`.

### 2. Tone, Mood & Pacing Analyzer (`tone_mood_analyzer.py`)
- **Tone**: `Suspenseful`, `Somber`, `Adventurous`, `Humorous`, `Dramatic`, `Neutral`.
- **Mood**: `Tense`, `Mysterious`, `Hopeful`, `Atmospheric`.
- **Pacing**: `Fast-Paced`, `Moderate`, `Slow / Descriptive` calculated from sentence length distributions and dialogue ratios.

### 3. Conflict & Scene Purpose Analyzer (`conflict_scene_analyzer.py`)
- **Conflict Taxonomy**: `Person vs Nature`, `Person vs Person`, `Internal Conflict`, `Person vs Society`.
- **Scene Purpose**: `Establish Setting & Goal`, `Escalate Tension & Plot`, `Climax & Resolution`.
- **Character Introductions**: Extracts first occurrences of proper noun character names with contextual evidence.

### 4. Foreshadowing, Twist & Theme Analyzer (`foreshadow_twist_analyzer.py`)
- Detects premonitions, ominous warnings, and chapter-ending cliffhangers.
- Extracts core story themes (`Discovery`, `Survival`, `Courage & Friendship`).

### 5. Story Analyzer Orchestrator (`story_analyzer.py`)
- Reads all `chapter_XX.json` files for a book.
- Combines chapter-level analysis and overall book-level aggregate knowledge.
- Generates `outputs/<book_slug>/story_analysis.json`.

---

## Output Schema (`story_analysis.json`)

```json
{
  "book_title": "Sample Novel",
  "total_chapters_analyzed": 5,
  "overall_narrative_pov": {
    "value": "Third-Person Limited",
    "confidence": 0.95,
    "evidence": "Aria adjusted her leather cloak as the cold mountain wind howled."
  },
  "overall_tone": {
    "value": "Suspenseful",
    "confidence": 0.88,
    "evidence": "The sun was dipping below the sharp peaks... the wolves in these parts don't care much for travelers."
  },
  "primary_themes": [
    {
      "value": "Discovery",
      "confidence": 0.85,
      "evidence": "In the center of the chamber, resting upon a pedestal of black obsidian, shone the Lost Artifact."
    }
  ],
  "chapter_analyses": [
    {
      "chapter_index": 1,
      "chapter_title": "CHAPTER 1: The Whispering Wind",
      "word_count": 85,
      "narrative_pov": {
        "value": "Third-Person Limited",
        "confidence": 0.92,
        "evidence": "Aria adjusted her leather cloak as the cold mountain wind howled."
      },
      "tone": {
        "value": "Suspenseful",
        "confidence": 0.85,
        "evidence": "The sun was dipping below the sharp peaks of the Frostclaw Mountains."
      },
      "mood": {
        "value": "Tense",
        "confidence": 0.88,
        "evidence": "The cold mountain wind howled through the canyon."
      },
      "pacing": {
        "value": "Moderate",
        "confidence": 0.82,
        "evidence": "Balanced narrative flow with average sentence length of 14.2 words."
      },
      "conflict": {
        "value": "Person vs Nature",
        "confidence": 0.85,
        "evidence": "cold mountain wind howled through the canyon"
      },
      "scene_purposes": [
        {
          "scene_index": 1,
          "purpose": "Establish Setting & Goal",
          "confidence": 0.9,
          "evidence": "Aria adjusted her leather cloak as the cold mountain wind howled through the canyon."
        }
      ],
      "character_introductions": [
        {
          "value": "Aria",
          "confidence": 0.88,
          "evidence": "Aria adjusted her leather cloak as the cold mountain wind howled through the canyon."
        },
        {
          "value": "Kane",
          "confidence": 0.88,
          "evidence": "\"We should make camp before nightfall,\" Kane said, leaning on his wooden staff."
        }
      ],
      "foreshadowing": {
        "value": "Implicit / Atmospheric Foreshadowing",
        "confidence": 0.65,
        "evidence": "The map marks the entrance right past the twin pillars."
      },
      "cliffhanger": {
        "value": "Standard Scene Resolution",
        "confidence": 0.75,
        "evidence": "The map marks the entrance right past the twin pillars."
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
python tests/test_analyzer.py
```

### Analyzing Story Knowledge for a Processed Book
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python analyzer/story_analyzer.py outputs/sample_novel
```

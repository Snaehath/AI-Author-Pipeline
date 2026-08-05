# Module 2: Chapter Parser — Documentation

## Overview
**Module 2 (Chapter Parser)** consumes the ingested book outputs from Module 1 (`metadata.json` and `cleaned.txt`) and parses each chapter into fine-grained structural components: **scenes**, **paragraphs**, **dialogue blocks**, and **narration blocks**.

Outputs are saved in `outputs/<book_slug>/chapters/chapter_XX.json` along with a top-level `parsing_summary.json`.

---

## Architecture & Components

```
AI_Author/parser/
├── __init__.py           # Package exports
├── dialogue_extractor.py # Spoken text & speech tag isolation
├── paragraph_parser.py  # Paragraph segmentation & classification (narration, dialogue, mixed)
├── scene_parser.py      # Scene transition detector (***, ---, ###)
└── chapter_parser.py    # Main pipeline orchestrator
```

### 1. Dialogue Extractor (`dialogue_extractor.py`)
- Finds spoken dialogue inside quotes.
- Extracts speech tags (e.g. `Kane said, leaning on his wooden staff`).
- Infers potential speaker hints based on adjacent proper nouns.

### 2. Paragraph Parser (`paragraph_parser.py`)
- Classifies each paragraph into:
  - `"narration"`: Pure narrative prose.
  - `"dialogue"`: Spoken dialogue inside quotes without surrounding narration.
  - `"mixed"`: Combination of narrative prose and spoken dialogue.

### 3. Scene Parser (`scene_parser.py`)
- Detects explicit scene transition dividers (`***`, `---`, `###`, `* * *`).
- Groups classified paragraphs into distinct scene units.

### 4. Chapter Parser Orchestrator (`chapter_parser.py`)
- Loads `metadata.json` from Module 1.
- Generates `outputs/<book_slug>/chapters/chapter_01.json`, `chapter_02.json`, etc.
- Computes `narration_ratio` and `dialogue_ratio` metrics per chapter.
- Generates `outputs/<book_slug>/parsing_summary.json`.

---

## Output Schema (`chapter_01.json`)

```json
{
  "book_title": "Sample Novel",
  "chapter_index": 1,
  "chapter_title": "CHAPTER 1: The Whispering Wind",
  "total_scenes": 1,
  "total_paragraphs": 3,
  "total_dialogues": 1,
  "word_count": 85,
  "narration_ratio": 0.929,
  "dialogue_ratio": 0.071,
  "scenes": [
    {
      "scene_index": 1,
      "word_count": 85,
      "paragraphs": [
        {
          "paragraph_index": 2,
          "text": "\"We should make camp before nightfall,\" Kane said.",
          "type": "mixed",
          "word_count": 8,
          "has_dialogue": true,
          "dialogues": [
            {
              "spoken_text": "We should make camp before nightfall",
              "speech_tag": "Kane said",
              "speaker_hint": "Kane",
              "quote_char_start": 0,
              "quote_char_end": 39,
              "word_count": 6
            }
          ]
        }
      ]
    }
  ]
}
```

---

## How to Run & Test

### Running Unit & Integration Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_parser.py
```

### Parsing a Processed Book Directory
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python parser/chapter_parser.py outputs/sample_novel
```

# Module 4: Character Analyzer — Documentation

## Overview
**Module 4 (Character Analyzer)** extracts structured character profiles, aliases, physical appearance traits, personality dimensions, goals, motivations, pairwise relationships, character arcs, growth, strengths, and weaknesses from the parsed chapters created in Module 2 (`outputs/<book_slug>/chapters/chapter_XX.json`).

Every extracted attribute strictly adheres to our metric contract:
```json
{
  "value": "<Extracted Attribute>",
  "confidence": 0.88,
  "evidence": "<Direct Narrative Snippet>"
}
```

Outputs are written to `outputs/<book_slug>/character_analysis.json`.

---

## Architecture & Components

```
AI_Author/analyzer/
├── character_extractor.py       # Discovers character names & alias groupings
├── trait_extractor.py           # Physical appearance, personality, strengths & weaknesses
├── goal_relationship_mapper.py  # Goals, motivations, and pairwise relationships
├── arc_tracker.py               # Character presence & growth trajectory across chapters
└── character_analyzer.py        # Main pipeline orchestrator
```

### 1. Character Extractor (`character_extractor.py`)
- Discovers major and minor character names across dialogue tags and narration text.
- Filters out non-character stop words and groups aliases.

### 2. Trait Extractor (`trait_extractor.py`)
- **Appearance**: Physical features, gear, clothing (`leather cloak`, `wooden staff`, `brass lantern`).
- **Personality**: Trait classification (`Determined`, `Cautious`, `Brave`, `Curious`).
- **Strengths & Weaknesses**: Asset and vulnerability extraction with narrative evidence.

### 3. Goal & Relationship Mapper (`goal_relationship_mapper.py`)
- **Goals**: Immediate and overarching objectives (`Find the Lost Artifact`, `Make camp before nightfall`).
- **Motivations**: Underlying drives (`Protection & Discovery`, `Kingdom Safety`).
- **Pairwise Relationships**: Inter-character connection dynamics (`Traveling Companions / Allies`).

### 4. Arc Tracker (`arc_tracker.py`)
- Tracks character presence across chapters.
- Classifies character arc trajectory (`Heroic Steadfast / Growth Arc`, `Supporting Character Arc`) and key growth moments.

### 5. Character Analyzer Orchestrator (`character_analyzer.py`)
- Reads all `chapter_XX.json` files for a book.
- Combines character discovery, traits, goals, relationships, and arcs.
- Generates `outputs/<book_slug>/character_analysis.json`.

---

## Output Schema (`character_analysis.json`)

```json
{
  "book_title": "Sample Novel",
  "total_characters_identified": 2,
  "relationships": [
    {
      "character_a": "Aria",
      "character_b": "Kane",
      "relationship_type": "Traveling Companions / Allies",
      "confidence": 0.9,
      "evidence": "Aria adjusted her leather cloak while Kane prepared the lantern."
    }
  ],
  "characters": [
    {
      "name": "Aria",
      "aliases": ["Aria"],
      "appearance": [
        {
          "value": "Wears/carries cloak, lantern",
          "confidence": 0.88,
          "evidence": "Aria adjusted her leather cloak while Kane prepared the lantern."
        }
      ],
      "personality": [
        {
          "value": "Determined & Focused",
          "confidence": 0.65,
          "evidence": "Aria actively participates in events."
        }
      ],
      "goals": [
        {
          "value": "Goal: Reach target in narrative",
          "confidence": 0.85,
          "evidence": "\"We must reach the twin pillars,\" Aria said."
        }
      ],
      "motivations": [
        {
          "value": "Personal Commitment & Safety",
          "confidence": 0.6,
          "evidence": "Aria responds to plot developments."
        }
      ],
      "character_arc": {
        "value": "Heroic Steadfast / Growth Arc",
        "confidence": 0.88,
        "evidence": "Aria actively progresses across Chapters [1, 2]."
      },
      "growth": {
        "value": "Demonstrates leadership and perseverance from Chapter 1 to Chapter 2",
        "confidence": 0.88,
        "evidence": "Aria actively progresses across Chapters [1, 2]."
      },
      "strengths": [
        {
          "value": "Perceptive & Resourceful",
          "confidence": 0.85,
          "evidence": "Aria adjusted her leather cloak while Kane prepared the lantern."
        }
      ],
      "weaknesses": [
        {
          "value": "Human Vulnerability",
          "confidence": 0.6,
          "evidence": "Aria faces environmental challenges."
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
python tests/test_character_analyzer.py
```

### Analyzing Character Knowledge for a Processed Book
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python analyzer/character_analyzer.py outputs/sample_novel
```

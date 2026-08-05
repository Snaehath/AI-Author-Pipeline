# Module 7: Plot Analyzer — Documentation

## Overview
**Module 7 (Plot Analyzer)** maps narrative structure milestones across classic 3-Act / 8-Point Story Structure: **Hook**, **Inciting Incident**, **First Plot Point**, **Midpoint**, **Reversal**, **Darkest Moment**, **Climax**, **Resolution**, and **Epilogue**.

Every extracted plot milestone strictly adheres to our metric contract:
```json
{
  "value": "<Extracted Plot Milestone>",
  "confidence": 0.88,
  "evidence": "<Direct Narrative Snippet>"
}
```

Outputs are written to `outputs/<book_slug>/plot_analysis.json`.

---

## Architecture & Components

```
AI_Author/analyzer/
├── plot_point_classifier.py # Classifies 8-point story structure milestones
└── plot_analyzer.py        # Main pipeline orchestrator
```

### 1. Plot Point Classifier (`plot_point_classifier.py`)
- Maps 8-point story milestones:
  - 🪝 **Hook**: Opening setup capturing reader attention.
  - ⚡ **Inciting Incident**: Status quo disruption and quest call.
  - 🚪 **First Plot Point**: Point of no return.
  - 🔄 **Midpoint**: Central discovery / revelation on pedestal.
  - 🔀 **Reversal**: Sudden shift in stakes and direction.
  - 🌑 **Darkest Moment**: Lowest emotional point / major threat.
  - ⚔️ **Climax**: Peak tension confrontation / goal achievement.
  - 🌅 **Resolution**: Restoration of new equilibrium.
  - 📖 **Epilogue**: Post-resolution teaser / next-stage hook.

### 2. Plot Analyzer Orchestrator (`plot_analyzer.py`)
- Reads all `chapter_XX.json` files for a book.
- Executes plot milestone mapping across story progression.
- Writes `outputs/<book_slug>/plot_analysis.json`.

---

## Output Schema (`plot_analysis.json`)

```json
{
  "book_title": "Sample Novel",
  "total_chapters": 5,
  "plot_structure_summary": "Classic 3-Act Heroic Arc (Hook -> Inciting Incident -> Midpoint -> Climax -> Resolution)",
  "plot_points": {
    "hook": {
      "value": "Hook: The Chronicles of Eldoria: The Lost Artifact...",
      "confidence": 0.9,
      "evidence": "The Chronicles of Eldoria: The Lost Artifact"
    },
    "inciting_incident": {
      "value": "Inciting Incident: Call to Action / Goal Setup",
      "confidence": 0.85,
      "evidence": "\"We should make camp before nightfall,\" Kane said, leaning on his wooden staff."
    },
    "first_plot_point": {
      "value": "First Plot Point: Point of No Return",
      "confidence": 0.88,
      "evidence": "The entrance to the ancient hall was framed by colossal stone arches."
    },
    "midpoint": {
      "value": "Midpoint: Major Discovery / Central Revelation",
      "confidence": 0.92,
      "evidence": "In the center of the chamber, resting upon a pedestal of black obsidian, shone the Lost Artifact."
    },
    "reversal": {
      "value": "Reversal: Shift in Stakes & Tension",
      "confidence": 0.8,
      "evidence": "\"It's breath-taking,\" Kane whispered, holding his torch high."
    },
    "darkest_moment": {
      "value": "Darkest Moment: Major Threat / All Hope is Lost",
      "confidence": 0.78,
      "evidence": "With the artifact secured, the kingdom was safe once more."
    },
    "climax": {
      "value": "Climax: Peak Confrontation & Goal Achievement",
      "confidence": 0.9,
      "evidence": "With the artifact secured, the kingdom was safe once more."
    },
    "resolution": {
      "value": "Resolution: Restoration of Equilibrium",
      "confidence": 0.92,
      "evidence": "With the artifact secured, the kingdom was safe once more."
    },
    "epilogue": {
      "value": "Epilogue: Post-Resolution Teaser",
      "confidence": 0.95,
      "evidence": "EPILOGUE: But deep in the shadows, a new shadow began to stir..."
    }
  }
}
```

---

## How to Run & Test

### Running Unit & Integration Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_plot_analyzer.py
```

### Mapping Plot Structure for a Processed Book
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python analyzer/plot_analyzer.py outputs/sample_novel
```

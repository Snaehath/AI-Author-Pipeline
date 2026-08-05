# Module 8: Dataset Generator — Documentation

## Overview
**Module 8 (Dataset Generator)** synthesizes the extracted storytelling knowledge from Modules 1-7 into a high-quality Supervised Fine-Tuning (SFT) instruction-response dataset (`train.jsonl` and `val.jsonl`).

The generated dataset teaches 8 core professional writing capabilities:
1. **Story Planning**
2. **Character Writing**
3. **Dialogue Generation**
4. **Scene Construction**
5. **Pacing Control**
6. **Prose Polish & Editing**
7. **Emotional Writing**
8. **Revision & Tension Escalation**

Outputs are written to `datasets/train.jsonl`, `datasets/val.jsonl`, and `datasets/dataset_summary.json`.

---

## Architecture & Components

```
AI_Author/dataset_generator/
├── prompt_templates.py   # System prompts & instruction prompt generators
├── sft_synthesizer.py    # Converts book knowledge into 8 task-type instruction pairs
└── dataset_pipeline.py   # Main pipeline orchestrator (writes train.jsonl & val.jsonl)
```

### 1. Prompt Templates (`prompt_templates.py`)
- Standardizes central author system prompt:
  > `"You are a professional AI novel author specializing in immersive fiction, rich character development, engaging dialogue, and balanced pacing."`
- Formats instruction queries and context input strings.

### 2. SFT Synthesizer (`sft_synthesizer.py`)
- Synthesizes SFT instruction-response pairs across all 8 writing categories.

### 3. Dataset Pipeline Orchestrator (`dataset_pipeline.py`)
- Loads extracted knowledge JSON files for one or multiple books.
- Executes SFT synthesis and deterministically shuffles examples.
- Splits dataset into 90% training (`datasets/train.jsonl`) and 10% validation (`datasets/val.jsonl`).
- Generates `datasets/dataset_summary.json`.

---

## Output Schema (`train.jsonl` / `val.jsonl`)

Each line in `train.jsonl` and `val.jsonl` is a valid JSON object formatted for SFT training:

```json
{
  "system": "You are a professional AI novel author specializing in immersive fiction, rich character development, engaging dialogue, and balanced pacing.",
  "instruction": "Write a dialogue exchange between the specified characters adhering to the target emotion and speech style: Speaker: Kane",
  "input": "Speaker: Kane | Target Emotion: Urgent / Cautious",
  "output": "\"We should make camp before nightfall,\" Kane said, leaning on his wooden staff.",
  "task_type": "dialogue_generation",
  "source_book": "Sample Novel",
  "chapter_index": 1
}
```

---

## How to Run & Test

### Running Unit & Integration Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_dataset_generator.py
```

### Synthesizing SFT Dataset for Processed Books
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python dataset_generator/dataset_pipeline.py outputs/sample_novel
```

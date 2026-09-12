# AI-Author-Pipeline

An end-to-end framework for fine-tuning LLMs on creative fiction and orchestrating multi-chapter story generation with pre-prose blueprints, story state databases, and preference-aligned editing crews.

---

## Overview

Generating long-form creative fiction with small language models (e.g., 1.5B parameters) often leads to semantic drift, character name confusion, and ungrounded scene transitions. 

This repository implements a modular pipeline that combines:
1. **Dataset Synthesis & Anonymization:** Ingests public domain comedy books (Wodehouse, Jerome, Grossmith) into 11,799 SFT instruction pairs and anonymizes character names (`Bertie` -> `[PROTAGONIST]`, `Jeeves` -> `[COMPANION]`) to mitigate direct memorization risks.
2. **4-Bit QLoRA & DPO Alignment:** Fine-tunes `Qwen2.5-1.5B-Instruct` on GPU with 4-bit NormalFloat (`NF4`) quantization and Direct Preference Optimization (DPO) to enforce comedic timing and dialogue brevity.
3. **Structured Orchestration:** Plans pre-prose chapter blueprints (Goal, Conflict, Emotional Arc, Reversal) before generating prose.
4. **Selective Memory (Fiction RAG):** Tracks character states, inventories, and trust scores scene-by-scene.
5. **Reward-Guided Selection:** Evaluates candidate scenes against a multi-signal reward model scoring story coherence, character voice, comedic timing, and reader curiosity.

---

## System Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                        RAW REFERENCE BOOKS (20 Books)                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  STAGE 1: NLP INGESTION & ANONYMIZER                                   │
│  • Scene/Chapter Splitter & Dialogue Turn Parser                       │
│  • Character Role Anonymizer (Bertie -> [PROTAGONIST])                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  STAGE 2: 4-BIT QLoRA & DPO ALIGNMENT                                  │
│  • Qwen2.5-1.5B-Instruct in 4-bit NormalFloat (NF4)                    │
│  • DPO Comedic Timing Alignment (1,000 preference pairs)               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  STAGE 3: INFERENCE ORCHESTRATION ENGINE                               │
│  • Pre-Prose Blueprint Planner + Story Bible DB + Fiction RAG Memory   │
│  • Multi-Agent Revision Crew + Best-of-N Composite Reward Selector     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  EXPORTER & EVALUATION SUITE                                           │
│  • Formatted .docx, .pdf, and .md manuscripts                          │
│  • Stylometric Cosine Similarity & Reader Experience Metrics           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Technical Pipeline Breakdown

### 1. Ingestion & Feature Extraction
Raw books are parsed into scenes (~700–900 words) and analyzed for speaker turn frequency, character role relationships, and 8-point narrative arcs. Character names are anonymized during SFT to prevent memorization of copyrighted names while learning general genre voice.

### 2. 2-Stage Training
- **Supervised Fine-Tuning (SFT):** Fine-tunes LoRA adapters ($r=32, \alpha=64$) over 11,799 anonymized instruction pairs.
- **Direct Preference Optimization (DPO):** Aligns the model on preference pairs (`chosen`: sharp deadpan punchlines vs `rejected`: long monologues).

### 3. Generation & Revision Workflow
1. **Pre-Prose Blueprint & Scene Contract:** Outlines scene goals, spatial locations, required props, and strict prohibitions (forbidden secrets, thread lockouts).
2. **Epistemic Context Budgeting:** Packs strictly isolated context (only facts legitimately known to the active POV character) within token budgets.
3. **Drafting & Multi-Agent Polish:** Expands the contract into prose and applies specialized revision passes (voice contrast, comedy timing).
4. **State Extraction & Continuity Compilation:** Extracts candidate symbolic events (`MOVE`, `PICK_UP`, `REVEAL_FACT`) and compiles them against the Narrative Type System (`INV_LOCATION`, `INV_POSSESSION`, `INV_EPISTEMIC`, `INV_VITALITY`, `INV_CONTRACT`).
5. **Best-of-N & Ledger Commit:** Candidates with invariant violations receive heavy reward penalties or fatal rejection. Valid state diffs are committed to the append-only `EventLedger`.
6. **Token Substitution & Export:** Replaces abstract tokens (`[COMPANION]` -> `Barnaby`) via `text_sanitizer.py` and exports `.docx` and `.pdf` files via `manuscript_exporter.py`.

---

## Quickstart

### Installation

```bash
git clone https://github.com/Snaehath/AI-Author-Pipeline.git
cd AI-Author-Pipeline
pip install -r requirements.txt
```

### Automated Workspace Setup

Download Project Gutenberg reference books and base model weights (`Qwen2.5-1.5B-Instruct`):

```powershell
python setup_project.py
```

### Run Alignment & Novel Generation

```powershell
# 1. Run DPO Preference Alignment Trainer
python trainer/dpo_trainer.py

# 2. Run Story Continuity Compiler & Invariant Verification Suite
python -m story_engine.test

# 3. Generate Novel (5 Chapters) with Stateful Engine
python inference/novel_builder_v2.py --chapters 5 --title "The Mischief at Blackwood Manor"

# 4. Export Word & PDF Manuscripts
python utils/manuscript_exporter.py outputs/generated_novel

# 5. Evaluate Stylometric Consistency
python evaluator/eval_pipeline.py outputs/generated_novel --reference_dir outputs/right_ho
```

---

## Evaluation Metrics

- **Dialogue Match Ratio:** **48.27%** (75.1% match against reference P. G. Wodehouse dialogue frequency).
- **Style Consistency Score:** **0.3177 – 0.565** (Weighted stylometric cosine similarity across sentence length, dialogue ratio, and vocabulary richness).
- **Standardized Scene Depth:** **650 – 800 words** per chapter.
- **Narrative Invariant Compliance:** 100% enforcement of spatial, possession, epistemic, vitality, and contract invariants via the Continuity Compiler.

---

## Repository Structure

```
├── story_engine/       # Stateful narrative engine (world state, epistemic model, event ledger, contracts)
│   ├── state/          # Characters, physical objects, spatial graph, relationships, timeline
│   ├── epistemic/      # World truth, character knowledge isolation, reader knowledge
│   ├── events/         # Atomic StoryEvents, StateDelta, immutable EventLedger
│   ├── contracts/      # SceneContract schemas & Narrative Invariants (Type System)
│   ├── context/        # Knapsack ContextBudgeter enforcing epistemic boundaries
│   └── test.py         # Story Continuity Compiler test runner
├── compiler/           # Continuity compiler, symbolic invariant checker, state extractor, repair engine
├── dataset_generator/  # SFT & DPO preference dataset synthesis
├── trainer/            # QLoRA fine-tuning & DPO alignment scripts
├── inference/          # Blueprint planner, Story Bible DB, Fiction RAG, Best-of-N selector
├── evaluator/          # Stylometric evaluation suite & composite reward model
├── utils/              # Token sanitizer & manuscript exporter (.docx, .pdf)
├── tests/              # Pytest test suite for state engine, invariants, contracts, and compiler
├── setup_project.py    # Automated book downloader & workspace setup
└── requirements.txt    # Python dependencies
```

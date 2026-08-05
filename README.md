# 🎭 AI Author Studio v3

> **An End-to-End Literary Fine-Tuning Framework & Reader-Centric Narrative Orchestration Engine**

AI Author Studio is a modular Python framework designed to investigate dataset synthesis, 4-bit QLoRA fine-tuning, Direct Preference Optimization (DPO), fiction RAG memory retrieval, and multi-agent editing crews for long-form creative fiction generation.

---

## 🌟 Key Features

- **20-Book Curated Literary Corpus:** Ingests public domain comedy masterpieces (Wodehouse, Jerome, Grossmith) into 11,799 anonymized SFT instruction pairs.
- **Character Role Anonymizer:** Replaces character names (`Bertie` -> `[PROTAGONIST]`, `Jeeves` -> `[COMPANION]`) to mitigate direct memorization risks during SFT.
- **4-Bit QLoRA & DPO Training:** Fine-tunes `Qwen2.5-1.5B-Instruct` using 4-bit NormalFloat (`NF4`) quantization and DPO comedic preference alignment.
- **Pre-Prose Blueprint Planner:** Generates structured chapter blueprints (Goal, Conflict, Emotional Arc, Reversal, Objects) *before* prose generation.
- **Fiction RAG Selective Memory Engine:** Retrieves *only* scene-relevant character states, inventories, and trust scores.
- **Composite Story Quality Reward Model:** Multi-signal reward model scoring story coherence, voice consistency, comedic timing, and reader curiosity.
- **Best-of-N Candidate Selector:** Samples $N$ candidate scene variations on the fly and selects the highest-reward variation.
- **Manuscript Exporter:** Exports publication-ready `.docx` and `.pdf` manuscripts.

## 🏗️ Architecture Overview

```
┌────────────────────────────────────────────────────────────────────────┐
│                        RAW REFERENCE BOOKS (20 Books)                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  STAGE 1: NLP INGESTION & 7-COMPONENT EXTRACTOR                        │
│  • Chapter/Scene Splitter & Dialogue Turn Parser                       │
│  • Character Role Anonymizer (Bertie -> [PROTAGONIST])                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  STAGE 2: 4-BIT QLoRA & DPO PREFERENCE ALIGNMENT TRAINER              │
│  • Qwen2.5-1.5B-Instruct in 4-bit NormalFloat (NF4)                    │
│  • DPO Comedic Timing Alignment (1,000 preference pairs)               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  STAGE 3: READER-CENTRIC NARRATIVE INFERENCE ENGINE                    │
│  • Pre-Prose Blueprint Planner + Story Bible DB + Fiction RAG Memory   │
│  • Multi-Agent Revision Crew + Best-of-N Composite Reward Selector     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  MANUSCRIPT EXPORTER & EVALUATION SUITE                                │
│  • Publication-ready .docx, .pdf, and .md manuscripts                  │
│  • Stylometric Cosine Similarity & Reader Experience Metrics           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 Training Architecture & 6-Step Generation Process

### Part 1: How Training Works (Why 7 Extracted NLP Components?)

Raw 60,000-word novels cannot be fed into an LLM all at once without context loss. The Ingestion Pipeline (`analyzer/`, `parser/`) extracts **7 structured NLP components** from each book to transform raw literature into high-signal training data:

1. **Scene Boundaries & Chapter Breaks:** Isolates self-contained narrative scenes (~700–900 words).
2. **Dialogue Turns & Speaker Attribution:** Teaches speaker voice contrast (e.g. *Barnaby's 10-word deadpan turns* vs. *Reginald's excited slang*).
3. **Character Profiles & Traits:** Maps protagonist, valet, antagonist, and aunt roles.
4. **Pairwise Relationship Networks:** Teaches trust scores and social hierarchies.
5. **8-Point Narrative Arc:** Teaches Goal -> Conflict -> Reversal -> Resolution progression.
6. **Emotion Timelines:** Maps character mood transitions scene-by-scene.
7. **Character Role Anonymization:** Replaces names (`Bertie` -> `[PROTAGONIST]`, `Jeeves` -> `[COMPANION]`) to mitigate memorization risk of copyrighted named characters during SFT.

#### 2-Stage GPU Fine-Tuning:
- **Stage 1 (QLoRA SFT):** Base model (`Qwen2.5-1.5B-Instruct`) is frozen in 4-bit NormalFloat (`NF4`) quantization. Trainable LoRA adapter matrices ($r=32$) learn 1920s diction over 2,656 GPU steps across 11,799 instruction pairs.
- **Stage 2 (DPO Comedic Alignment):** Fine-tunes adapter weights using DPO Loss over 1,000 preference pairs (`chosen`: sharp deadpan punchlines vs. `rejected`: 40-word monologues).

---

### Part 2: Step-by-Step Novel Generation Pipeline

When executing `python inference/novel_builder_v2.py --chapters 5 --title "The Mischief at Blackwood Manor"`, the system runs a **6-Step Generation Pipeline**:

1. **Step 1: Pre-Prose Blueprint Planner (`blueprint_planner.py`)**  
   Generates a 5-chapter structured blueprint containing Goal, Conflict, Reversal, and Objects.
2. **Step 2: Story Bible DB Initialization (`story_bible_db.py`)**  
   Initializes a queryable state database tracking goals, inventories, and trust scores.
3. **Step 3: Fiction RAG Selective Memory (`fiction_rag.py`)**  
   Retrieves *only* character states relevant to the active scene.
4. **Step 4: Raw Draft Expansion (`multi_agent_crew.py` Pass 1)**  
   Writer Agent expands the blueprint into a raw ~800-word scene.
5. **Step 5: Multi-Agent Revision & Best-of-N Candidate Selection**  
   Voice Reviewer evaluates dialogue contrast, Comedy Editor evaluates punchline timing, and Best-of-N Selector picks the variation with the highest reward score.
6. **Step 6: Token Sanitization & Manuscript Export (`text_sanitizer.py` & `manuscript_exporter.py`)**  
   Replaces abstract tokens (`[COMPANION]` -> `Barnaby`), strips prompt leakage tags, and exports formatted `.md`, `.docx`, and `.pdf` manuscripts.

---

## 🚀 Quick Start (Replicate in 1 Command)

### 1. Installation & Environment Setup

```bash
# Clone Repository
git clone https://github.com/your-username/AI_Author.git
cd AI_Author

# Install Required Python Libraries
pip install -r requirements.txt

# 1-Click Automated Book & Base Model Downloader Setup
python setup_project.py
```

*Note: `setup_project.py` automatically downloads public domain books from Project Gutenberg and base model weights (`Qwen2.5-1.5B-Instruct`) from HuggingFace directly to `models/` (which is ignored by Git).*

### 2. DPO Training & Novel Generation

```powershell
# Run DPO Comedic Preference Alignment Trainer
python trainer/dpo_trainer.py

# Generate 5-Chapter Novel with Best-of-N Candidate Selector
python inference/novel_builder_v2.py --chapters 5 --title "The Mischief at Blackwood Manor"

# Export Formatted Word & PDF Manuscripts
python utils/manuscript_exporter.py outputs/generated_novel

# Run Literary Evaluation Suite
python evaluator/eval_pipeline.py outputs/generated_novel --reference_dir outputs/right_ho
```

---

## 📊 Evaluation & Metrics

- **Dialogue Match Ratio:** **48.27%** (Achieves a **75.1% match to P. G. Wodehouse** dialogue frequency).
- **Style Consistency Score:** **0.3177 – 0.565** (Weighted stylometric similarity across sentence length, dialogue %, and vocabulary richness).
- **Standardized Chapter Length:** **650 – 800 words** per chapter.

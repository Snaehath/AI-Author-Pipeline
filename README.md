# AI-Author-Pipeline

An end-to-end framework for training small language models (1.5B) into **creative comedy specialists** and orchestrating multi-chapter story generation with deterministic state continuity compilers, pre-prose contracts, and compiler-guided Best-of-N search.

---

## Overview: The Three Pillars

Generating long-form creative fiction with small language models (e.g. 1.5B parameters) frequently suffers from two competing failure modes: **continuity collapse** (hallucinated locations, epistemic leaks, object teleportation) and **prose superficiality** (imitating period vocabulary rather than understanding comedic craft).

This repository solves both through three cleanly decoupled architectural pillars:

```text
                    ┌─────────────────────────┐
                    │  1.5B BASE LANGUAGE LM  │
                    └────────────┬────────────┘
                                 │
                     Learns comedic machinery
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 1. COMEDY CRAFT SPECIALIST (SFT + DPO)                          │
│    • Learns how to CREATE COMEDY (Mechanisms & Structural Beats)│
│    • 10 Comedic Mechanisms decoupled from surface slang         │
│    • Contrast-purity validated DPO for comedic restraint/subtext│
│    • GENERATE_FROM_STRUCTURE for transferable original comedy   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. STATE ENGINE & CONTINUITY COMPILER                           │
│    • Enforces that the model CANNOT BREAK THE STORY             │
│    • Pure state transition: State_n + Contract + CandidateDiff  │
│    • Spatial, possession, vitality, and epistemic invariants    │
│    • Atomic checkpoint manifests with rollback/replay           │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. COMPILER-GUIDED BEST-OF-N SEARCH                             │
│    • Finds the STRONGEST VALID ATTEMPT                          │
│    • 3-Stage Gating Hierarchy: World -> Contract -> Quality/E(c)│
│    • Contract-Relevance State Efficiency Metric E(c)            │
│    • Dominant-pattern targeted repair                           │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
                          CANONICAL STORY
```

1. **Training** makes the model better at **creating comedy**.
2. **The Compiler** makes the model better at **not breaking the story**.
3. **Best-of-N Search** makes the system better at **finding the strongest valid attempt**.

---

## Empirical Verification: Experiment 001

In a controlled ablation across 20 multi-constraint benchmark scenes testing movement, inventory transfer, and character interaction:

| Metric | System A (Baseline 1.5B) | System B (Stateful Compiler) | System C (Compiler BoN) | Delta (C vs A) |
| :--- | :---: | :---: | :---: | :---: |
| **Valid Scene Rate (VSR)** | **20.0%** (4/20) | **75.0%** (15/20) | **80.0%** (16/20) | **+60.0%** |
| **Cumulative Anomaly Violations (CAV)** | **10.15** | **6.69** | **2.02** | **-80.1%** |
| **Contract Fulfillment Rate** | 63.3% | 76.7% | **83.3%** | **+20.0%** |
| **Epistemic Leaks** | 1 detected | 0 | **0** | **100% eliminated** |

---

## Phase 3 — Comedy Craft Framework & Human Calibration

Rather than training the 1.5B model to mimic surface slang (*"By Jove!"*, *"old chap"*), Phase 3 extracts transferable **comedic principles** from classic British comic fiction / social farce (Wodehouse, Jerome, Grossmith).

### 1. Four-Tier Unified Record Schema
Every annotation is irrevocably bound to its original unabridged source passage:
$$\text{SOURCE} \longrightarrow \text{FACTS} \longrightarrow \text{CRAFT} \longrightarrow \text{OPERATIONS / DPO}$$

- **Source:** Source book, chapter index, unique source ID, and raw text.
- **Objective Facts:** Speaking characters, honorifics, vocatives, locations, physical objects, dialogue ratio, and turn counts.
- **Craft Annotation:** Primary and secondary mechanisms, 4-stage structural arc (Setup $\to$ Escalation $\to$ Reversal $\to$ Payoff), tone, and isolated surface slang features.
- **Craft Operations & DPO:**
  - `IDENTIFY_MECHANISM`: Identifies dominant comic mechanism and supporting dynamics.
  - `EXTRACT_STRUCTURE`: Deconstructs 4-beat comedic structure.
  - `REWRITE_RESTRAINT`: Rewrites scene with deadpan restraint, stripping over-explanation.
  - `CONTINUE_TENSION`: Continues scene while preserving unresolved comedic tension.
  - `GENERATE_FROM_STRUCTURE`: **Transferable comedy generator** — takes an abstract structure and produces a brand new original scene with new characters and setting.
  - **Controlled Contrast DPO Pairs:** Audited by `ContrastPurityValidator` (requiring $\ge 0.85$ purity and verified preference strength).

### 2. Comedic Mechanism Taxonomy
1. `MISUNDERSTANDING`: Two characters operate under incompatible premises.
2. `STATUS_REVERSAL`: Sudden shift in social superiority or competence (e.g. valet over master).
3. `ESCALATION`: Compounding complications from a simple initial issue.
4. `DEADPAN_REACTION`: Emotional under-reaction or stoic understatement during catastrophe.
5. `SOCIAL_EMBARRASSMENT`: Desperate attempts to maintain decorum or hide awkward truths.
6. `VERBAL_WIT`: Subtextual barbs, irony, register collision, and semantic incongruity.
7. `DRAMATIC_IRONY`: The reader possesses critical knowledge concealed from characters.
8. `DIALOGUE_SUBTEXT`: Saying polite trivialities while intensely negotiating conflict.
9. `CALLBACK`: Reintroducing an earlier throwaway detail with compounded payoff.
10. `PHYSICAL_COMPLICATION`: Farce elements, timing obstacles, and physical entanglements.

---

## Phase 3B Freeze & Development Roadmap

The architecture is currently frozen at **Phase 3B** to validate the data layer with human calibration before any model training:

```text
                         COMPLETE
                            │
                            ▼
┌──────────────────────────────────────────────┐
│ Phase 3A — Comedy Craft Dataset Generation   │
│ ✓ taxonomy & schemas                         │
│ ✓ factual & craft detectors                  │
│ ✓ structural extraction (4 beats)            │
│ ✓ contrast purity validator                  │
│ ✓ GENERATE_FROM_STRUCTURE operation          │
│ ✓ 50-example stratified sample               │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ Phase 3B — Human Calibration                 │
│ ✓ multidimensional rubric                    │
│ ✓ literary quality vs training value         │
│ ✓ mechanism confidence scoring               │
│ ✓ disagreement taxonomy                      │
│ ✓ secondary mechanisms                       │
│ ✓ calibration sheet & audit tooling          │
│                                              │
│             ← CURRENT STATE                  │
└──────────────────────┬───────────────────────┘
                       │
                 HUMAN AUDIT
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ Phase 3C — Calibration Analysis              │
│ detector fixes / taxonomy fixes / rejection  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ Phase 3D — Dataset Expansion                 │
│ ~1,000–2,000 high-quality craft records      │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ Phase 4 — Comedy Specialist Training         │
│ SFT → structure benchmark → DPO              │
└──────────────────────────────────────────────┘
```

> **Important Constraint:** Do **NOT** start SFT or DPO training yet. The 50 passages are a calibration experiment, not training data yet. The resulting audit data provides the empirical foundation for designing the Phase 4 mixture, weighting, SFT curriculum, LoRA hyperparameters, DPO pairs, and held-out benchmark.

---

## Human Calibration Gate (Recommended Gate Before Phase 4)

The 50 stratified inspection examples in `datasets/comedy_craft_sample_50.json` are audited using [`reports/comedy_craft_calibration_sheet.md`](reports/comedy_craft_calibration_sheet.md) or [`reports/comedy_craft_calibration_sheet.json`](reports/comedy_craft_calibration_sheet.json).

### 1. Ten Post-Annotation Calibration Metrics
Following human annotation of the 50 calibration examples, calculate:
1. **Primary mechanism agreement**
2. **Secondary mechanism agreement**
3. **Setup agreement**
4. **Escalation agreement**
5. **Reversal agreement**
6. **Payoff agreement**
7. **Mean literary quality**
8. **Mean training value**
9. **Mean mechanism confidence**
10. **Disagreement-category distribution**

### 2. Calibration Decision Tree
A data-driven decision tree guides post-audit actions:

```text
                 50 human audits
                       │
                       ▼
             Is mechanism agreement
                  sufficiently high?
                 /                  \
               YES                  NO
                │                    │
                │              inspect disagreements
                │                    │
                │          ┌─────────┴─────────┐
                │          ▼                   ▼
                │    detector problem     taxonomy problem
                │          │                   │
                │       fix detector       revise taxonomy
                │
                ▼
       Is training value high?
             /          \
           YES          NO
            │            │
            ▼            ▼
       retain example   reject/downweight
            │
            ▼
     Expand dataset (~1,000–2,000)
```

### 3. Multi-Field Human Audit Record Schema
The human audit does not collapse into a simplistic boolean `approved: true/false`. It captures structured multidimensional judgment:

```json
{
  "human_verdict": "AGREE",
  "human_primary_mechanism": "MISUNDERSTANDING",
  "human_secondary_mechanisms": [
    "ESCALATION",
    "DEADPAN_REACTION"
  ],
  "human_literary_quality": 9,
  "human_training_value": 10,
  "human_mechanism_confidence": 9,
  "disagreement_category": null
}
```

### 4. Weighted Training Example Policy
This schema enables **weighted training examples** rather than treating every passage identically:

- **Training value 9–10 + confidence 9–10:** Strongest SFT examples (high sample weight).
- **Training value 7–8:** Normal SFT examples (standard weight).
- **Training value 5–6:** Potentially downweighted in SFT curriculum.
- **Training value < 5:** Excluded from training set.
- **Mechanism confidence < 5:** Excluded from comedic mechanism supervision.

*(These thresholds represent initial calibration policy and will be calibrated by the 50-example audit).*

---

## Held-Out Evaluation Benchmark (`GENERATE_FROM_STRUCTURE`)

The `GENERATE_FROM_STRUCTURE` operation is designed as a **held-out evaluation set**, not merely another training task:

```text
TRAIN
─────────────────────────────
Source passage
      ↓
Facts
      ↓
Comic mechanism
      ↓
Structural beats
      ↓
SFT / DPO


TEST (Held-Out Benchmark)
─────────────────────────────
Abstract structure
      ↓
      1.5B
      ↓
NEW characters
NEW setting
NEW situation
      ↓
Original comedy
```

> **Critical Evaluation Invariant:** Never expose the test structures verbatim during SFT. Holding out evaluation structures ensures we verify whether the 1.5B model has acquired transferable comedic machinery rather than memorized structural templates.

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

### Run Tests

Run the full automated test suite (106 tests covering state engine, invariants, compiler, search, and comedy craft pipeline):

```powershell
python -m pytest tests/
```

### Build Stratified Comedy Craft Sample

```powershell
# Extract 50 stratified inspection examples across all 10 mechanisms
python -m dataset_generator.build_comedy_dataset --sample-size 50

# Generate human calibration review sheet and JSON audit template
python -m dataset_generator.annotation_calibration_report

# Calculate 10 agreement & quality metrics from completed human audit
python -m dataset_generator.annotation_calibration_report --audit-file reports/comedy_craft_calibration_sheet.json
```

### Run Novel Generation with Stateful Engine

```powershell
python inference/novel_builder_v2.py --chapters 5 --title "The Mischief at Blackwood Manor"
```

### Run Experiment 001 Ablation

```powershell
python -m experiments.run_experiment_001
```

---

## Repository Structure

```
├── story_engine/       # Stateful narrative engine & Narrative Type System
│   ├── state/          # Pure WorldState snapshots, characters, objects, spatial graph, checkpoints
│   ├── epistemic/      # Ground truth, character knowledge isolation, reader knowledge
│   ├── events/         # Atomic StoryEvents, StateDelta, immutable EventLedger
│   ├── contracts/      # SceneContract schemas & Narrative Invariant predicates
│   ├── context/        # Knapsack ContextBudgeter enforcing epistemic isolation
│   └── scene_runner.py # Stateful scene execution orchestrator
├── compiler/           # Continuity compiler, symbolic invariant checker, event extractor, repair engine
├── dataset_generator/  # Comedy craft pipeline, factual analyzer, craft annotator, contrast purity, calibration
├── experiments/        # Controlled ablation harness (Experiment 001: Baseline vs Stateful vs BoN)
├── trainer/            # QLoRA fine-tuning & DPO alignment scripts
├── inference/          # Blueprint planner, Story Bible DB, Fiction RAG, Best-of-N selector
├── evaluator/          # Stylometric evaluation suite & composite reward model
├── utils/              # Token sanitizer & manuscript exporter (.docx, .pdf)
├── docs/               # Technical documentation (comedy_craft_taxonomy.md)
├── reports/            # Audit reports & human calibration sheets
├── tests/              # Pytest test suite (106 passing tests)
├── setup_project.py    # Automated book downloader & workspace setup
└── requirements.txt    # Python dependencies
```


# Phase 4B-2 Experiment Report: Contrastive & Counterfactual Supervision

- **Experiment ID**: `sft_experiment_002`
- **Objective**: Test **H4** — Does explicit contrastive/counterfactual supervision ("What would make the joke stop being funny?") enable the model to separate surface prose style from the underlying comedic engine, escaping attractor hubs toward human gold mechanisms?
- **Base Model**: `Qwen2.5-1.5B-Instruct` (4-bit NF4 QLoRA, $r=16, \alpha=32$, $\text{lr}=10^{-4}$, effective batch size 4, 3 epochs)
- **Training Dataset**: `datasets/sft/comedy_contrastive_train.jsonl` (48 records, SHA-256: `65f6ec33...`, 66.7% attractor hubs)
- **DEV Benchmark**: `datasets/sft/comedy_dev.jsonl` (20 records, SHA-256: `18838c6d...`, $\text{sft\_score} \ge 8.0$, 0 leakage)
- **TEST Benchmark**: `datasets/sft/comedy_eval.jsonl` (17 records, SHA-256: `685ad436...`, **SEALED** during selection)

---

## 1. DEV Checkpoint Selection Trajectory (Primary Selection Mechanism)

Checkpoint selection was conducted **exclusively on the frozen 20-record DEV set**. The locked TEST set was not inspected or evaluated during this process.

### Multi-Epoch DEV Scorecard

| Metric | DEV Baseline (Base Qwen) | Epoch 1 | Epoch 2 (Selected) | Epoch 3 | Best Delta (DEV) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Primary Mechanism Accuracy** | 15.0% (3/20) | 15.0% (3/20) | **35.0% (7/20)** | 30.0% (6/20) | **+20.0%** |
| **Exact Record Match** | 0.0% (0/20) | 10.0% (2/20) | **15.0% (3/20)** | **15.0% (3/20)** | **+15.0%** |
| **Secondary Micro F1** | 13.3% | 22.6% | 34.0% | **39.2%** | **+25.9%** |
| **Secondary Macro F1** | 4.2% | 7.5% | 15.3% | **23.2%** | **+19.0%** |
| **Mean Jaccard** | 8.3% | 20.0% | 28.7% | **34.2%** | **+25.9%** |
| **Horizon Accuracy** | 100.0% | 100.0% | 85.0% | 90.0% | -10.0% |
| **Raw JSON Validity** | 0.0% | 100.0% | 85.0% | 90.0% | +85.0% |
| **Taxonomy Violations** | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

### DEV Attractor Analysis: Escape vs. True Causal Success

In the DEV baseline, **13 of 20 records** collapsed onto the false `VERBAL_WIT` attractor (predicted `VERBAL_WIT` when gold was another mechanism). We track the exact fate of these 13 false attractors across training:

| Checkpoint | Stuck in `VERBAL_WIT` | Total Escaped | **True Causal Success (Gold)** | Shifted to Other Error |
| :--- | :---: | :---: | :---: | :---: |
| **Epoch 1** | 12/13 (92.3%) | 1/13 (7.7%) | **0/13 (0.0%)** | 1/13 (7.7%) |
| **Epoch 2 (Selected)** | 4/13 (30.8%) | 9/13 (69.2%) | **5/13 (38.5%)** | 4/13 (30.8%) |
| **Epoch 3** | 3/13 (23.1%) | 10/13 (76.9%) | **4/13 (30.8%)** | 6/13 (46.2%) |

#### Verified True Causal Transitions on DEV (Epoch 2):
1. `audit_073`: `VERBAL_WIT` ➔ **`ESCALATION`** (Gold: `ESCALATION`)
2. `audit_094`: `VERBAL_WIT` ➔ **`DEADPAN_REACTION`** (Gold: `DEADPAN_REACTION`)
3. `audit_118`: `VERBAL_WIT` ➔ **`DEADPAN_REACTION`** (Gold: `DEADPAN_REACTION`)
4. `audit_133`: `VERBAL_WIT` ➔ **`ESCALATION`** (Gold: `ESCALATION`)
5. `audit_170`: `VERBAL_WIT` ➔ **`MISUNDERSTANDING`** (Gold: `MISUNDERSTANDING`)

### Selection Decision

**Epoch 2 (`models/comedy_contrastive_adapter/checkpoint-epoch-2`) is selected as the winning checkpoint** based on:
1. **Primary selection metric**: Peak primary accuracy on DEV (35.0% vs. 15.0% baseline and 30.0% Epoch 3).
2. **Diagnostic metric**: Peak True Causal Success rate (38.5% of baseline false attractors corrected to gold).
3. **Distribution health**: Epoch 2 maintains balanced predictions across 5 distinct mechanisms (`VERBAL_WIT`: 7, `ESCALATION`: 4, `DEADPAN_REACTION`: 4, `MISUNDERSTANDING`: 1, `PHYSICAL_COMPLICATION`: 1), whereas Epoch 3 overfits and collapses heavily onto `DEADPAN_REACTION` (9/20 predictions, 45%).

---

## 2. Unlocked TEST Set Evaluation (Single Evaluation of Best Checkpoint)

Following checkpoint selection, the sealed 17-record TEST benchmark (`datasets/sft/comedy_eval.jsonl`) was unlocked and evaluated once with the selected Epoch 2 adapter under greedy decoding (`do_sample=False`).

### Three-Regime Comparative Scorecard (TEST Set)

| Metric | Phase 4A Base | Phase 4B-1 SFT (Epoch 3) | Phase 4B-2 Contrastive (Epoch 2) | Delta (4B-2 vs. Base) | Delta (4B-2 vs. 4B-1) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Primary Mechanism Accuracy** | 17.6% (3/17) | 17.6% (3/17) | **11.8% (2/17)** | -5.8% | -5.8% |
| **Exact Record Match** | 0.0% (0/17) | 5.9% (1/17) | **0.0% (0/17)** | 0.0% | -5.9% |
| **Secondary Micro F1** | 13.6% | **34.8%** | **26.7%** | **+13.1%** | -8.1% |
| **Secondary Macro F1** | 5.7% | **17.8%** | **9.4%** | **+3.7%** | -8.4% |
| **Mean Jaccard** | 8.3% | **26.7%** | **18.1%** | **+9.8%** | -8.6% |
| **Horizon Accuracy** | 94.1% | 94.1% | **88.2%** | -5.9% | -5.9% |
| **Raw JSON Validity** | 0.0% | 100.0% | **94.1%** | **+94.1%** | -5.9% |
| **Schema Validity** | 100.0% | 100.0% | **94.1%** | -5.9% | -5.9% |
| **Taxonomy Violations** | 0.0% | 0.0% | **0.0%** | 0.0% | 0.0% |

---

## 3. Record-by-Record Transition Matrix (TEST Set)

| Audit ID | Human Gold | Phase 4A Base | Phase 4B-1 SFT | Phase 4B-2 Contrastive (Ep 2) | Status Transition |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `audit_143` | `DEADPAN_REACTION` | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_010` | `DEADPAN_REACTION` | `DIALOGUE_SUBTEXT` (✗) | `DEADPAN_REACTION` (✓) | `VERBAL_WIT` (✗) | 🔴 Regressed |
| `audit_135` | `DIALOGUE_SUBTEXT` | `VERBAL_WIT` (✗) | `DEADPAN_REACTION` (✗) | `MISUNDERSTANDING` (✗) | ⚪ Shifted Error |
| `audit_164` | `DIALOGUE_SUBTEXT` | `DEADPAN_REACTION` (✗) | `DEADPAN_REACTION` (✗) | `DEADPAN_REACTION` (✗) | ⚪ Stuck |
| `audit_083` | `DRAMATIC_IRONY` | `VERBAL_WIT` (✗) | `DEADPAN_REACTION` (✗) | `MISUNDERSTANDING` (✗) | ⚪ Shifted Error |
| `audit_016` | `ESCALATION` | `VERBAL_WIT` (✗) | `DEADPAN_REACTION` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_001` | `ESCALATION` | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_020` | `MISUNDERSTANDING` | `STATUS_REVERSAL` (✗) | `DEADPAN_REACTION` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_004` | `MISUNDERSTANDING` | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_042` | `PHYSICAL_COMPLICATION`| `DIALOGUE_SUBTEXT` (✗) | `DEADPAN_REACTION` (✗) | `UNKNOWN` (Truncated) | ⚪ Truncated |
| `audit_051` | `PHYSICAL_COMPLICATION`| `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_173` | `SOCIAL_EMBARRASSMENT` | `DEADPAN_REACTION` (✗) | `DEADPAN_REACTION` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_076` | `SOCIAL_EMBARRASSMENT` | `VERBAL_WIT` (✗) | `VERBAL_WIT` (✗) | `MISUNDERSTANDING` (✗) | ⚪ Shifted Error |
| `audit_174` | `STATUS_REVERSAL` | `STATUS_REVERSAL` (✓) | `STATUS_REVERSAL` (✓) | `VERBAL_WIT` (✗) | 🔴 Regressed |
| `audit_103` | `STATUS_REVERSAL` | `VERBAL_WIT` (✗) | `DEADPAN_REACTION` (✗) | `VERBAL_WIT` (✗) | ⚪ Stuck |
| `audit_167` | `VERBAL_WIT` | `VERBAL_WIT` (✓) | `DEADPAN_REACTION` (✗) | `VERBAL_WIT` (✓) | 🟢 Preserved / Restored |
| `audit_027` | `VERBAL_WIT` | `VERBAL_WIT` (✓) | `VERBAL_WIT` (✓) | `VERBAL_WIT` (✓) | 🟢 Preserved |

---

## 4. Key Scientific Findings & Attractor Dynamics

### 1. The Discrepancy Between DEV and TEST (The Generalization Gap)
* **On DEV (High-Craft Curated Set, $\text{sft\_score} \ge 8.0$)**: Contrastive supervision produced a **+20.0% primary accuracy increase** (15.0% ➔ 35.0%), an **Attractor Escape Rate of 69.2%**, and a **True Causal Success Rate of 38.5%** (5/13 cases escaping directly to gold `ESCALATION`, `DEADPAN_REACTION`, and `MISUNDERSTANDING`).
* **On TEST (Uncurated Baseline Benchmark)**: The learned behavior failed to generalize. Contrastive supervision reduced primary mechanism accuracy (17.6% ➔ 11.8%). While it suppressed the false `DEADPAN_REACTION` substitute attractor (dropping from 10 predictions in 4B-1 down to 1 in 4B-2), the model defaulted back to `VERBAL_WIT` (12/17) or branched to `MISUNDERSTANDING` (3/17), resulting in **0/9 true causal successes** on baseline false attractor cases.
* **Interpretation**: Training distribution $\rightarrow$ learned contrastive behavior $\rightarrow$ works on similar curated examples; but training distribution $\rightarrow$ unseen/subtler test examples $\rightarrow$ base prior returns.

### 2. Substitute Attractor Dynamics (Intervention Package Effects)
In Phase 4B-1, standard SFT broke the `VERBAL_WIT` attractor by creating a substitute attractor hub on `DEADPAN_REACTION` (10/17 predictions). Phase 4B-2's intervention package reduced this substitute attractor (`DEADPAN_REACTION` fell from 58.8% to 5.9%), **providing evidence that counterfactual supervision can reduce the `DEADPAN_REACTION` attractor under the evaluated conditions**. However, because the intervention package combined multiple elements (new curated data, contrastive schema, causal rationales, counterfactual tests, and `why_primary_wins`), the reduction is attributable to the intervention package as a whole rather than isolated counterfactual pairs.

### 3. Structured Contrastive Reasoning Output vs. Inference Scaffolding
During evaluation, the model exhibited **structured contrastive reasoning behavior** (generating detailed `contrastive_analysis` blocks including `causal_mechanism`, `surface_cue`, `tempting_alternative`, and `counterfactual_test`) despite the evaluation prompt *not explicitly requesting them*. This demonstrates learned structured output generation rather than direct access to internal reasoning. Furthermore, because the evaluation prompt asked for standard classification without explicitly scaffolding the contrastive fields, the model lacked prompt-time encouragement to systematically execute the contrastive sequence before arriving at its final decision on out-of-distribution passages.

### 4. Generation Length Tradeoff & Truncation
On one long passage (`audit_042`), the extensive contrastive generation exhausted the `max_new_tokens=256` budget before completing the JSON object, resulting in an unparsed `UNKNOWN` prediction. This highlights a key engineering tradeoff:
$$\text{More Reasoning Supervision} \longrightarrow \text{Longer Output} \longrightarrow \text{Higher Truncation Risk}$$
For future evaluations with structured contrastive output, output token budgets must be budgeted and monitored explicitly.

### 5. Hypothesis Status: H4
> **H4: Explicit causal/contrastive supervision should reduce the model's tendency to classify prominent witty/deadpan surface cues as the primary mechanism, increasing movement toward the human-labeled causal mechanism.**

* **Verdict**: **PARTIALLY SUPPORTED / DISTRIBUTION-LIMITED (NOT CONFIRMED ON TEST)**
  * **DEV Causal Discrimination**: 🟢 **Supported** (15.0% ➔ 35.0%, +20.0% gain)
  * **DEV Attractor Escape**: 🟢 **Strong Evidence** (69.2% escape, 38.5% true causal success)
  * **TEST Generalization**: 🔴 **Not Supported** (17.6% ➔ 11.8%)
  * **Overall Causal Mechanism Generalization**: 🔴 **Not Demonstrated**

---

## 5. Executive Synthesis & Next Phase

### Scientific Summary
> **Phase 4B-2 demonstrated that a QLoRA-trained Qwen2.5-1.5B model can learn structured contrastive distinctions between comedic mechanisms on a curated development distribution. The model substantially reduced the dominant `VERBAL_WIT` attractor on DEV and converted 5/13 baseline false-attractor cases directly to their human-labeled mechanism at the selected checkpoint. However, this improvement did not generalize to the sealed TEST benchmark, where primary mechanism accuracy declined from 17.6% to 11.8%. The result therefore supports the feasibility of contrastive supervision but indicates a substantial distribution/generalization gap.**

### Project Status Dashboard
* **Phase 4B-2 Execution**: 🟢 Complete & Methodologically Valid
* **DEV Improvement**: 🟢 Demonstrated & Replicated
* **Attractor Shift**: 🟢 Substantially Altered (Substitute attractor suppressed)
* **Causal Reasoning Generalization**: 🟡 Unresolved
* **Primary TEST Accuracy Improvement**: 🔴 Not Achieved (11.8%)
* **Hypothesis H4**: 🔴 Not Confirmed (Distribution-Limited)

### Preservation of Epoch-2 Artifact
The Epoch-2 adapter (`models/comedy_contrastive_adapter/checkpoint-epoch-2`) is preserved as the core experimental artifact. It demonstrated a contrastive behavior that the base model did not reliably exhibit on the curated DEV distribution, providing evidence of a gap between learned contrastive behavior and inference-time generalization.

### Methodological Discipline: 🔒 Freezing TEST
The 17-record benchmark (`comedy_eval.jsonl`) is now **permanently frozen and sealed** with its recorded Phase 4B-2 result (11.8%). It will not be re-evaluated with modified prompts or parameters to avoid converting a sealed benchmark into a development set.

### Next Phase: Phase 4C-1 (Inference-Time Contrastive Scaffolding + Fresh Generalization Benchmark)
1. **Fresh Benchmark**: Construct a new held-out evaluation set (20–30 passages of mixed/unseen craft quality, stratified across mechanisms) prior to designing new prompts.
2. **Controlled Evaluation**: Compare:
   - **Regime A (Standard Inference)**: `passage ➔ classification`
   - **Regime B (Contrastive Scaffolding)**: `passage ➔ causal mechanism ➔ surface cue ➔ tempting alternative ➔ counterfactual test ➔ why primary wins ➔ classification`
3. **Hypothesis Under Test**: Test whether the model already acquired the contrastive discrimination procedure during Phase 4B-2, but requires explicit inference-time scaffolding to reliably activate it on out-of-distribution passages.

# SFT Experiment 1 Comparative Scorecard: Base vs. SFT Checkpoints

- **Evaluation Dataset**: `comedy_eval.jsonl` (Frozen Human Gold, n = 17)
- **Eval SHA-256**: `685ad4369fd731b952801e83ed23f0e3bb7c320876052710abd01c8bd3cb3470`
- **Verdict**: **RED_FAILURE**

## 1. Learning Curve Progression

| Metric | BASE (Zero-Shot) | Epoch 1 | Epoch 2 | Epoch 3 | Best Delta |
|---|:---:|:---:|:---:|:---:|:---:|
| **Primary Accuracy** | 17.6% (3/17) | 11.8% (2/17) | 17.6% (3/17) | 17.6% (3/17) | **+0.0%** |
| **Exact Record Match** | 0.0% (0/17) | 5.9% (1/17) | 5.9% (1/17) | 5.9% (1/17) | **+5.9%** |
| **Secondary Micro F1** | 13.6% | 37.5% | 34.8% | 34.8% | **+21.2%** |
| **Horizon Accuracy** | 94.1% | 94.1% | 94.1% | 94.1% | - |
| **VERBAL_WIT Attractor Rate** | 58.8% (10/17) | 41.2% (7/17) | 35.3% (6/17) | 35.3% (6/17) | **-29.4%** |
| **Schema Validity** | 100.0% | 100.0% | 100.0% | 100.0% | 0.0% |

## 2. VERBAL_WIT Escape Analysis (Best Checkpoint: eval_qwen1.5b_sft_epoch_2)

- **Baseline False Attractor Errors**: 9
- **Corrected to Gold Primary**: **0 / 9 (0.0%)**
- **Changed to Another Wrong Mechanism**: 4
- **Remained Stuck on VERBAL_WIT**: 5

## 3. Individual Transitions Log (All 17 Unseen Eval Passages)

| Audit ID | Gold Primary | Base Prediction | Best SFT Prediction | Status Transition |
|---|---|---|---|:---:|
| `audit_143` | DEADPAN_REACTION | VERBAL_WIT (✗) | VERBAL_WIT (✗) | ⚪ UNRESOLVED |
| `audit_010` | DEADPAN_REACTION | DIALOGUE_SUBTEXT (✗) | DEADPAN_REACTION (✓) | 🟢 IMPROVED |
| `audit_135` | DIALOGUE_SUBTEXT | VERBAL_WIT (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_164` | DIALOGUE_SUBTEXT | DEADPAN_REACTION (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_083` | DRAMATIC_IRONY | VERBAL_WIT (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_016` | ESCALATION | VERBAL_WIT (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_001` | ESCALATION | VERBAL_WIT (✗) | VERBAL_WIT (✗) | ⚪ UNRESOLVED |
| `audit_020` | MISUNDERSTANDING | STATUS_REVERSAL (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_004` | MISUNDERSTANDING | VERBAL_WIT (✗) | VERBAL_WIT (✗) | ⚪ UNRESOLVED |
| `audit_042` | PHYSICAL_COMPLICATION | DIALOGUE_SUBTEXT (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_051` | PHYSICAL_COMPLICATION | VERBAL_WIT (✗) | VERBAL_WIT (✗) | ⚪ UNRESOLVED |
| `audit_173` | SOCIAL_EMBARRASSMENT | DEADPAN_REACTION (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_076` | SOCIAL_EMBARRASSMENT | VERBAL_WIT (✗) | VERBAL_WIT (✗) | ⚪ UNRESOLVED |
| `audit_174` | STATUS_REVERSAL | STATUS_REVERSAL (✓) | STATUS_REVERSAL (✓) | 🟢 PRESERVED |
| `audit_103` | STATUS_REVERSAL | VERBAL_WIT (✗) | DEADPAN_REACTION (✗) | ⚪ UNRESOLVED |
| `audit_167` | VERBAL_WIT | VERBAL_WIT (✓) | DEADPAN_REACTION (✗) | 🔴 REGRESSED |
| `audit_027` | VERBAL_WIT | VERBAL_WIT (✓) | VERBAL_WIT (✓) | 🟢 PRESERVED |

## 4. Hypothesis Status & Scientific Discoveries

- **H1: Primary Mechanism Discrimination**: 🔴 **NOT ACHIEVED** (17.6% Base ➔ 17.6% SFT Best). The 43-example curriculum did not increase primary classification accuracy.
- **H2: Composite Craft Identification**: 🟢 **SUPPORTED / PRELIMINARY EVIDENCE** (Secondary Micro F1: 13.6% Base ➔ 37.5% Epoch 1, 34.8% Epoch 2/3; Jaccard: 10.8% ➔ 28.9%). *Note: Given n=17 frozen eval examples, this is preliminary evidence of composite vocabulary acquisition rather than conclusive proof.*
- **H3: Instruction & Format Preservation**: 🟢 **PASSED** (0.0% taxonomy violations, 94.1% horizon accuracy, 100.0% schema validity).
- **Format Imitation vs. Reasoning**: Raw JSON emission without markdown wrappers reached 100.0% (vs. 0.0% Base), which reflects output format adoption rather than causal reasoning.
- **Discovery of Secondary Attractor**: SFT successfully disrupted the primary `VERBAL_WIT` attractor (58.8% ➔ 35.3%), but partially collapsed onto a second attractor: `DEADPAN_REACTION` (accounting for 4 of 9 transitions).
- **Methodological Constraint & Next Steps**: The 17 frozen eval records were inspected across Epochs 1-3. For subsequent experiments (Phase 4C / 4B-2), establish a separate DEV partition for checkpoint selection before evaluating on the frozen benchmark.

# Phase 4C-1 A/B Experiment Report: Inference-Time Contrastive Scaffolding

- **Benchmark**: `comedy_generalization_test.jsonl` (N = 25, Fresh Sealed Benchmark)
- **Benchmark SHA-256**: `a133d670bb6684a0879b7bd4d16a4ae7cdb62455f7aa2915d0ff5297e5f1c418`
- **Model Under Test**: `Qwen2.5-1.5B-Instruct` + Epoch-2 Contrastive Adapter
- **Objective**: Test **H5** (Primary), **H5a** (Mechanistic Attractors), and **H5b** (Inference Cost/Overhead)

---

## 1. Controlled A/B Comparative Scorecard

| Metric | Regime A (Direct Inference) | Regime B (Contrastive Scaffold) | Delta (B − A) |
| :--- | :---: | :---: | :---: |
| **Primary Mechanism Accuracy** | 8.0% (2/25) | 8.0% (2/25) | **+0.0%** |
| **Exact Record Match** | 0.0% (0/25) | 0.0% (0/25) | **+0.0%** |
| **Secondary Micro F1** | 14.6% | 19.5% | **+4.9%** |
| **Mean Jaccard Index** | 14.0% | 17.3% | **+3.3%** |
| **Horizon Accuracy** | 68.0% | 84.0% | **+16.0%** |
| **Raw JSON Validity** | 84.0% | 100.0% | **+16.0%** |
| **Schema Validity** | 84.0% | 100.0% | **+16.0%** |
| **Taxonomy Violations** | 0.0% | 0.0% | **0.0%** |
| **VERBAL_WIT Attractor Rate** | 44.0% (11/25) | 0.0% (0/25) | **-44.0%** |
| **DEADPAN_REACTION Rate** | 32.0% (8/25) | 100.0% (25/25) | **+68.0%** |

---

## 2. Scaffold Consistency & Causal Reasoning Analysis (Regime B)

- **Causal Mechanism Accuracy**: **8.0%** (2/25)
- **Scaffold Consistency Rate (SCR)**: **100.0%** (25/25)

### Disconnection Matrix (Causal Reasoning vs. Final Classification)
| Causal Analysis | Final Classification | Count | Interpretation |
| :--- | :--- | :---: | :--- |
| **Correct** | **Correct** | 2 | 🟢 Successful causal alignment |
| **Correct** | **Wrong** | 0 | 🟡 Reasoning/classification disconnect |
| **Wrong** | **Correct** | 0 | 🟡 Lucky guess without causal reasoning |
| **Wrong** | **Wrong** | 23 | 🔴 Causal failure & classification failure |

---

## 3. Inference Cost, Latency & Engineering Overhead

| Metric | Regime A (Direct) | Regime B (Scaffold) | Delta (B − A) |
| :--- | :---: | :---: | :---: |
| **Mean Generated Tokens** | 227.4 | 217.2 | -10.2 tok |
| **Median Generated Tokens** | 230 | 221 | -9 tok |
| **Truncation Rate** | 16.0% (4/25) | 0.0% (0/25) | **-16.0%** |

> [!NOTE]
> Setting `max_new_tokens=512` in Regime B completely eliminated the output truncation failure mode (0.0% truncations vs. 16.0% in Regime A), producing 100% schema validity and 100% raw JSON validity.

---

## 4. Record-by-Record Transition Matrix (All 25 Generalization Passages)

| Audit ID | Human Gold | Regime A (Direct) | Regime B (Scaffolded Primary) | Regime B (Causal Mechanism) | Status Transition |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `audit_011` | `ESCALATION` | `UNKNOWN` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_018` | `DEADPAN_REACTION` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | 🟢 IMPROVED |
| `audit_028` | `MISUNDERSTANDING` | `ESCALATION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_032` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_038` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | 🟢 PRESERVED |
| `audit_039` | `STATUS_REVERSAL` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_057` | `MISUNDERSTANDING` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_061` | `MISUNDERSTANDING` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_078` | `DIALOGUE_SUBTEXT` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_084` | `CALLBACK` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_090` | `ESCALATION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_101` | `SOCIAL_EMBARRASSMENT` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_107` | `CALLBACK` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_108` | `VERBAL_WIT` | `UNKNOWN` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_113` | `DIALOGUE_SUBTEXT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_117` | `VERBAL_WIT` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | 🔴 REGRESSED |
| `audit_123` | `DIALOGUE_SUBTEXT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_136` | `SOCIAL_EMBARRASSMENT` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_140` | `CALLBACK` | `ESCALATION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_145` | `ESCALATION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_146` | `PHYSICAL_COMPLICATION` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_157` | `STATUS_REVERSAL` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_159` | `SOCIAL_EMBARRASSMENT` | `UNKNOWN` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_169` | `CALLBACK` | `VERBAL_WIT` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |
| `audit_175` | `ESCALATION` | `UNKNOWN` | `DEADPAN_REACTION` | `DEADPAN_REACTION` | ⚪ UNRESOLVED |

---

## 5. Scientific Findings & Hypothesis Evaluation

### H5 (Primary Hypothesis): Inference-Time Contrastive Scaffolding Improves Accuracy
> **Verdict: NOT SUPPORTED (B ≈ A = 8.0%)**
- Primary mechanism accuracy remained identical: **8.0% (2/25)** in both Regime A and Regime B.
- Contrastive scaffolding did not increase primary classification accuracy on this fresh, uncurated generalization benchmark.

### H5a (Mechanistic Hypothesis): Attractor Disruption & True Causal Selection
> **Verdict: RADICAL ATTRACTOR COLLAPSE RATHER THAN TRUE CAUSAL DISCRIMINATION**
- **Extinction of VERBAL_WIT**: Scaffolding completely extinguished the dominant `VERBAL_WIT` attractor (44.0% ➔ 0.0%).
- **Collapse onto DEADPAN_REACTION**: However, rather than directing predictions to true causal mechanisms, **100% (25/25) of Regime B predictions collapsed onto `DEADPAN_REACTION`**.
- **Scaffold Consistency Rate = 100%**: The model's final classification was not disconnected from its contrastive reasoning. Rather, the contrastive analysis itself systematically convinced the model that the causal mechanism was `DEADPAN_REACTION` across all 25 passages.
- **Outcome B Realized**: Provides decisive evidence that the contrastive procedure acquired during Phase 4B-2 was **distribution-dependent** (tied to the high-craft DEV set) rather than a general, transferable causal reasoning mechanism.

### H5b (Cost & Overhead Hypothesis): Generation Length & Engineering Tradeoffs
> **Verdict: ZERO TRUNCATION AT 512 BUDGET / NO TOKEN INFLATION**
- The expanded `max_new_tokens=512` budget eliminated the truncation failure mode entirely (0% vs. 16% in Regime A).
- Because the scaffold enforced structured fields, the model did not generate runaway conversational text: mean generated tokens were actually slightly lower (217.2 tokens vs. 227.4 tokens in Regime A).
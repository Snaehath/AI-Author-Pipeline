# Comedy Craft Baseline Evaluation Report: Qwen2.5-1.5B-Instruct

- **Model**: `Qwen2.5-1.5B-Instruct`
- **Dataset**: `comedy_eval.jsonl` (Human Gold Truth, n = 17)
- **Eval SHA-256**: `685ad4369fd731b952801e83ed23f0e3bb7c320876052710abd01c8bd3cb3470`

## 1. Core Scorecard

| Metric | Result | Target / Ideal |
|---|:---:|:---:|
| **Primary Mechanism Accuracy** | **17.6%** (3/17) | > 60.0% |
| **Exact Record Accuracy** | **0.0%** (0/17) | > 35.0% |
| **Horizon Accuracy** | **94.1%** | > 80.0% |
| **Secondary Micro F1** | **13.6%** | > 50.0% |
| **Secondary Macro F1** | **5.7%** | > 40.0% |
| **Mean Jaccard Similarity** | **8.3%** | > 50.0% |
| **Combined Coverage (Primary anywhere)** | **35.3%** | > 70.0% |
| **Raw JSON Validity** | **0.0%** | 100.0% |
| **Repairable JSON Validity** | **100.0%** | 100.0% |
| **Schema Validity** | **100.0%** | 100.0% |
| **Taxonomy Violations** | **0.0%** | 0.0% |

## 2. Failure Breakdown

- **JSON Syntax Failures**: 17
- **Schema/Taxonomy Failures**: 0
- **Incorrect Primary Mechanism**: 14
- **Incorrect Mechanism Horizon**: 1
- **Exact Craft Record Failures**: 17
- **Parse Status Breakdown**:
  - `VALID`: 17

## 3. Per-Example Diagnostic Log

| Audit ID | Gold Primary | Predicted Primary | Gold Horizon | Pred Horizon | JSON | Status | Exact |
|---|---|---|---|---|:---:|:---:|:---:|
| `audit_143` | DEADPAN_REACTION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_010` | DEADPAN_REACTION | DIALOGUE_SUBTEXT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_135` | DIALOGUE_SUBTEXT | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_164` | DIALOGUE_SUBTEXT | DEADPAN_REACTION (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_083` | DRAMATIC_IRONY | VERBAL_WIT (✗) | LONG_HORIZON | LOCAL | ✗ | `VALID` | ❌ |
| `audit_016` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_001` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_020` | MISUNDERSTANDING | STATUS_REVERSAL (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_004` | MISUNDERSTANDING | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_042` | PHYSICAL_COMPLICATION | DIALOGUE_SUBTEXT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_051` | PHYSICAL_COMPLICATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_173` | SOCIAL_EMBARRASSMENT | DEADPAN_REACTION (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_076` | SOCIAL_EMBARRASSMENT | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_174` | STATUS_REVERSAL | STATUS_REVERSAL (✓) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_103` | STATUS_REVERSAL | VERBAL_WIT (✗) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_167` | VERBAL_WIT | VERBAL_WIT (✓) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |
| `audit_027` | VERBAL_WIT | VERBAL_WIT (✓) | LOCAL | LOCAL | ✗ | `VALID` | ❌ |

# Comedy Craft Baseline Evaluation Report: Qwen2.5-1.5B-Instruct

- **Model**: `Qwen2.5-1.5B-Instruct`
- **Dataset**: `comedy_dev.jsonl` (Human Gold Truth, n = 20)
- **Eval SHA-256**: `18838c6ddd9bcd89d80df6e223b41bfd68cb25a1ae18976f4dd6ecd2c476829e`

## 1. Core Scorecard

| Metric | Result | Target / Ideal |
|---|:---:|:---:|
| **Primary Mechanism Accuracy** | **15.0%** (3/20) | > 60.0% |
| **Exact Record Accuracy** | **10.0%** (2/20) | > 35.0% |
| **Horizon Accuracy** | **100.0%** | > 80.0% |
| **Secondary Micro F1** | **22.6%** | > 50.0% |
| **Secondary Macro F1** | **7.5%** | > 40.0% |
| **Mean Jaccard Similarity** | **20.0%** | > 50.0% |
| **Combined Coverage (Primary anywhere)** | **30.0%** | > 70.0% |
| **Raw JSON Validity** | **100.0%** | 100.0% |
| **Repairable JSON Validity** | **100.0%** | 100.0% |
| **Schema Validity** | **100.0%** | 100.0% |
| **Taxonomy Violations** | **0.0%** | 0.0% |

## 2. Failure Breakdown

- **JSON Syntax Failures**: 0
- **Schema/Taxonomy Failures**: 0
- **Incorrect Primary Mechanism**: 17
- **Incorrect Mechanism Horizon**: 0
- **Exact Craft Record Failures**: 18
- **Parse Status Breakdown**:
  - `VALID`: 20

## 3. Per-Example Diagnostic Log

| Audit ID | Gold Primary | Predicted Primary | Gold Horizon | Pred Horizon | JSON | Status | Exact |
|---|---|---|---|---|:---:|:---:|:---:|
| `audit_003` | VERBAL_WIT | VERBAL_WIT (✓) | LOCAL | LOCAL | ✓ | `VALID` | ✅ |
| `audit_015` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_041` | MISUNDERSTANDING | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_054` | VERBAL_WIT | VERBAL_WIT (✓) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_062` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_064` | DEADPAN_REACTION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_068` | ESCALATION | DEADPAN_REACTION (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_070` | STATUS_REVERSAL | DEADPAN_REACTION (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_073` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_094` | DEADPAN_REACTION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_095` | PHYSICAL_COMPLICATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_097` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_102` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_116` | PHYSICAL_COMPLICATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_118` | DEADPAN_REACTION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_125` | VERBAL_WIT | VERBAL_WIT (✓) | LOCAL | LOCAL | ✓ | `VALID` | ✅ |
| `audit_126` | SOCIAL_EMBARRASSMENT | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_133` | ESCALATION | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_165` | MISUNDERSTANDING | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |
| `audit_170` | MISUNDERSTANDING | VERBAL_WIT (✗) | LOCAL | LOCAL | ✓ | `VALID` | ❌ |

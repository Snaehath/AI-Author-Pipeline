# Experiment 001: Does a Compiler Make a Small Model Better?

> [!NOTE]
> **Research Invariant:** Small Language Model (1.5B) narrative reliability governed by deterministic external compiler vs unconstrained generation.

## 1. Executive Summary Table

| System | Model | Search | Compiler | Valid Scene Rate (VSR) | Violations / Scene | Fatal Violations | Avg Quality | Tokens / Scene | CAV (Valid/1k Tok) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Baseline (1.5B)** | 1.5B | 1 (Greedy) | No | **20.0%** | 1.2 | 20 | 0.35 | 111.9 | **1.7873** |
| **Stateful (1.5B)** | 1.5B | 1 (Greedy) | Yes | **75.0%** | 0.5 | 4 | 0.35 | 112.2 | **6.6875** |
| **Compiler-Guided BoN (1.5B)** | 1.5B | Best-of-3 | Yes | **80.0%** | 0.25 | 1 | 0.28 | 395.1 | **2.0248** |

---

## 2. Violation Category Breakdown

| System | Epistemic Leaks | Spatial Teleportation | Possession Conflicts | Contract Breaches | Total Violations |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Baseline (1.5B)** | 15 | 0 | 0 | 9 | **24** |
| **Stateful (1.5B)** | 0 | 4 | 4 | 2 | **10** |
| **Compiler-Guided BoN (1.5B)** | 0 | 1 | 1 | 3 | **5** |

---

## 3. Token Economics & Cost-Adjusted Reliability (CAV)

| System | Prompt Tokens | Completion Tokens | Total Tokens | Avg Latency (ms) | CAV (Valid Scenes / 1k Tokens) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Baseline (1.5B)** | 1678 | 560 | 2238 | 0.0ms | **1.7873** |
| **Stateful (1.5B)** | 1964 | 279 | 2243 | 0.0ms | **6.6875** |
| **Compiler-Guided BoN (1.5B)** | 6985 | 917 | 7902 | 0.0ms | **2.0248** |

---

## 4. BoN Search Dynamics & Repair Efficacy

- **Total Candidates Evaluated:** 65
- **Gate 1 & Gate 2 Rejection Rate:** 58.46%
- **Targeted Repair Attempts (Zero Survivors):** 5
- **Targeted Repair Success Rate:** 20.0%
- **Average State Efficiency E(c):** 0.19


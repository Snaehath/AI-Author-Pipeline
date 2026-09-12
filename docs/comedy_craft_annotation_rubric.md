# Phase 3D.2: Human Comedy Craft Annotation Protocol & Evaluation Rubric

> **Target Batch:** 180 Strategic Multi-Work Audits (`reports/comedy_craft_audit_batch_180.json` / `.md`)  
> **Objective:** Establish unshakeable human gold ground-truth to measure detector precision/recall, compute confusion profiles, and partition pristine exemplars for 1.5B Specialist SFT and DPO training.

---

## 1. The Prime Directive: Tripartite Quality Separation

Auditors must strictly decouple three independent dimensions that are frequently conflated:

$$\text{Literary Quality} \neq \text{Craft Clarity} \neq \text{Training Value}$$

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 1. LITERARY QUALITY (1-10)                                                      │
│    Aesthetic, prose, and stylistic polish: diction, cadence, authorial voice,   │
│    period elegance, and readability.                                             │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 2. CRAFT CLARITY (1-10)                                                         │
│    Structural mechanics: how unmistakably does the comic engine function?       │
│    Are Setup, Escalation, Reversal, and Payoff clean and unambiguous?            │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 3. TRAINING VALUE (1-10)                                                        │
│    Pedagogical utility for a 1.5B model: does this teach a clean, reproducible   │
│    craft rule without noise, sprawling context dependencies, or confusing tone? │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### Tripartite Anchor Matrix

| Score | Literary Quality | Craft Clarity | Training Value |
| :---: | :--- | :--- | :--- |
| **1-2** | Garbled OCR, fragmented syntax, or awkward prose. | No identifiable comedic mechanism; register is drama, violence, or dry history. | Harmful to training; introduces noise, hallucinations, or dramatic false positives. |
| **3-4** | Functional but pedestrian or repetitive phrasing. | Comedic intent is vaguely present, but beats are obscured by exposition or clumsy pacing. | Low value; model might learn generic filler rather than the comic beat. |
| **5-6** | Competent narrative prose typical of period novels. | Recognizable mechanism present, but composite interference or weak reversal/payoff weakens it. | Acceptable as auxiliary/composite data, but unsuitable for Foundation SFT. |
| **7-8** | Polished, witty, and distinctive authorial voice (e.g. Jerome K. Jerome, Grossmith). | Mechanism is clearly delineated: clear premise, rising tension, identifiable comic pivot. | High-value exemplar; clearly teaches the intended structural transition. |
| **9-10** | Masterclass English prose (e.g., peak P.G. Wodehouse, Jane Austen). | Textbook execution: setup establishes expectation, escalation compounds pressure, crisp reversal, sharp payoff. | Flawless Gold SFT exemplar; pristine teaching signal for the 1.5B specialist model. |

> [!IMPORTANT]
> **Concrete Example of the Tripartite Distinction:**
> An ornate, beautifully written 19th-century passage describes a gentleman's quiet internal melancholy over dinner.
> * **Literary Quality:** `9/10` (Exquisite prose)
> * **Craft Clarity:** `2/10` (No comedic engine; purely atmospheric/melancholic)
> * **Training Value:** `1/10` (Harmful as a comedy craft exemplar; teaches the model to mistake somber atmosphere for comedy)

---

## 2. Six-Step Audit Decision Workflow

Every passage in `comedy_craft_audit_batch_180.json` must be audited through this sequential protocol:

```text
               ┌───────────────────────────────┐
               │ Passage Excerpt + Context     │
               └───────────────┬───────────────┘
                               │
               [Step 1: Comedic Craft Presence]
                               │
           ┌───────────────────┼───────────────────┐
           ▼                   ▼                   ▼
       NO (Reject)         PARTIAL (Review)    YES (Eligible)
           │                   │                   │
           │           [Step 2: Horizon]           │
           │           LOCAL vs LONG_HORIZON       │
           │                   │                   │
           │           [Step 3: Mechanisms]        │
           │           PRIMARY + SECONDARY[]       │
           │                   │                   │
           │           [Step 4: Stratum]           │
           │           PURE vs COMPOSITE           │
           │                   │                   │
           │           [Step 5: Detector Check]    │
           │           detector_correct: T / F     │
           │                   │                   │
           └───────────────────┼───────────────────┘
                               │
                       [Step 6: Routing]
              KEEP (SFT/DPO) / REVISE / REJECT
```

### Step 1: `craft_presence` (The Hard Eligibility Gate)
* **`YES`**: Passage contains a genuine, functional comedic beat with at least two structural phases (e.g., setup + payoff, or escalation + reversal).
* **`NO`**: Zero comedic craft. The excerpt is genuine drama, horror, academic/historical commentary, or serious emotional conflict.
* **`PARTIAL`**: Contains comedic flavor, irony, or mild amusement, but lacks a complete mechanical arc or is cut off mid-beat.

### Step 2: `mechanism_horizon` (Temporal Scope)
* **`LOCAL`**: The mechanism is completely self-contained and fully decipherable within the excerpt (e.g., dialogue wit, deadpan reaction, immediate situational reversal).
* **`LONG_HORIZON`**: The humor depends on context outside the excerpt—such as a character's secret known from chapter 2, an ongoing running gag (`CALLBACK`), or dramatic irony where the reader knows facts not mentioned in this scene.

### Step 3: `primary_mechanism` & `secondary_mechanisms`
* **Rule:** Do NOT force composite scenes into a single label. Identify the **PRIMARY** structural engine that drives the scene's comedic progression, and list all active **SECONDARY** mechanisms that provide comic color.

### Step 4: `craft_stratum`
* **`PURE_MECHANISM`**: Exactly one dominant mechanism operating cleanly with minimal interference. Required for Foundation SFT.
* **`COMPOSITE_CRAFT`**: Two or more mechanisms working simultaneously (e.g., `ESCALATION` supported by `DEADPAN_REACTION`). Valid for Advanced SFT.
* **`REJECT`**: Failed craft presence or non-functional structure.

### Step 5: `detector_correct` (Detector Evaluation)
* Set to `true` **only if** the automated detector's `primary_mechanism` correctly matches your audited `primary_mechanism`.
* If the detector proposed `MISUNDERSTANDING` but the passage is actually `ESCALATION`, set `detector_correct = false` and note the confusion in `notes`.

### Step 6: `keep_verdict`
* **`KEEP`**: Approved for training (Gold SFT, Composite SFT, or DPO positive).
* **`REJECT`**: Hard negative (used for DPO negative pairs or discarded).
* **`REVISE`**: Borderline snippet that would be valuable if excerpt boundaries were expanded.

---

## 3. The 10 Canonical Mechanisms: Ground-Truth Definitions & Negative Boundaries

### 1. `ESCALATION`
* **Core Definition:** Stakes, complications, or irrational commitments compound iteratively. Each reaction raises the pressure rather than resolving it.
* **Positive Indicator:** Character takes an absurd step to fix a problem, which creates a worse problem, prompting an even more extreme reaction.
* **Negative Boundary:** Normal dialogue back-and-forth or simple sequential plot progression is **NOT** escalation. Escalation requires *exponential* or *compounding irrationality*.

### 2. `MISUNDERSTANDING`
* **Core Definition:** Two or more characters operate on conflicting, mutually orthogonal interpretations of reality while believing they are discussing the same thing.
* **Positive Indicator:** Double-entendre dialogue, cross-purposes conversations where both interpretations are logically sustained.
* **Negative Boundary:** One character simply lying, or a genuine tragic mistake, is **NOT** comic misunderstanding.

### 3. `DEADPAN_REACTION`
* **Core Definition:** A character responds to an outrageous, catastrophic, or bizarre event with flat, mundane, or understated matter-of-factness.
* **Positive Indicator:** The comedic energy arises entirely from the emotional gap between the absurdity of the circumstance and the calmness of the response (e.g., Jeeves' impassive reaction to chaos).
* **Negative Boundary:** Narrator exhaustion, apathy, or normal quietness in a calm scene is **NOT** deadpan.

### 4. `VERBAL_WIT`
* **Core Definition:** Linguistic incongruity, razor-sharp epigrams, disproportionate elevated registers, or absurdly elaborate similes used to describe trivialities.
* **Positive Indicator:** "He looked like a man who had tested an earthquake and found it wanting."
* **Negative Boundary:** Standard pleasant banter or conventional metaphors are **NOT** verbal wit.

### 5. `STATUS_REVERSAL`
* **Core Definition:** The social, intellectual, or power hierarchy between two characters is visibly flipped. The subordinate assumes command while the superior is reduced to helplessness.
* **Positive Indicator:** The valet politely dictating terms to his aristocratic master; the magistrate being interrogated by the tramp.
* **Negative Boundary:** Mere arguments or petulance between equals is **NOT** status reversal.

### 6. `COMIC_IRONY`
* **Core Definition:** Situational outcome directly inverts the character's stated intention, effort, or confident prediction in a way that humorously mocks their pretension.
* **Positive Indicator:** The boastful expert failing catastrophically at the very skill he just lectured on.
* **Negative Boundary:** General misfortune, tragic irony, or random bad luck is **NOT** comic irony.

### 7. `DRAMATIC_IRONY`
* **Core Definition:** The reader (and often one character) possesses vital knowledge that another character is oblivious to, causing the oblivious character's words/actions to carry humorous double meaning.
* **Positive Indicator:** Character confidently walks into a trap or expresses pity for someone who is secretly defrauding them.
* **Temporal Scope:** Typically `LONG_HORIZON` unless the secret is established in the opening lines of the excerpt.

### 8. `DIALOGUE_SUBTEXT`
* **Core Definition:** Ultra-polite, formal social convention concealing intense underlying irritation, hostility, or negotiation.
* **Positive Indicator:** Stiff Victorian courtesy masking murderous mutual hatred over tea.
* **Negative Boundary:** Plain cordial conversation or overt yelling is **NOT** dialogue subtext.

### 9. `PHYSICAL_COMPLICATION`
* **Core Definition:** Inanimate objects, physical geography, or animals actively resisting human competence and intention with comic causality.
* **Positive Indicator:** The struggle to open a tin of pineapple in *Three Men in a Boat*; an umbrella refusing to close.
* **Negative Boundary:** Violent assaults, accidental injuries, or generic physical actions (walking, sitting) are **NOT** physical complications.

### 10. `CALLBACK`
* **Core Definition:** A phrase, object, or bizarre assertion from an earlier situation returns in a completely new context to trigger a comic realization.
* **Positive Indicator:** The unexpected re-emergence of an absurd excuse from three chapters ago.
* **Temporal Scope:** Almost always `LONG_HORIZON`.

---

## 4. Human Review Output JSON Schema

When submitting audits in `reports/comedy_craft_audit_batch_180.json`, each entry's `human_audit` object must conform to:

```json
{
  "craft_presence": "YES",
  "craft_stratum": "PURE_MECHANISM",
  "primary_mechanism": "ESCALATION",
  "secondary_mechanisms": [
    "DEADPAN_REACTION",
    "VERBAL_WIT"
  ],
  "mechanism_horizon": "LOCAL",
  "setup_accurate": true,
  "escalation_accurate": true,
  "reversal_accurate": true,
  "payoff_accurate": true,
  "literary_quality": 9,
  "craft_clarity": 9,
  "training_value": 10,
  "keep_verdict": "KEEP",
  "detector_primary": "MISUNDERSTANDING",
  "detector_correct": false,
  "notes": "Detector confused by polite dialogue turns, but the core engine is compounding social stakes (ESCALATION)."
}
```

---

## 5. Downstream Data Routing (Post-Audit Compilation)

Once the 180 records are annotated, the `GoldAuditEvaluator` will automatically partition them:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. GOLD FOUNDATION SFT                                                      │
│    craft_presence = YES                                                     │
│    craft_stratum = PURE_MECHANISM                                           │
│    mechanism_horizon = LOCAL                                                │
│    craft_clarity >= 8, training_value >= 8                                 │
│    keep_verdict = KEEP                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. GOLD ADVANCED COMPOSITE SFT                                              │
│    craft_presence = YES                                                     │
│    craft_stratum = COMPOSITE_CRAFT                                          │
│    training_value >= 7, keep_verdict = KEEP                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. HELD-OUT LONG-HORIZON BENCHMARK                                          │
│    mechanism_horizon = LONG_HORIZON                                         │
│    Reserved for multi-scene narrative planning and compiler evaluation      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. DPO NEGATIVE CONTROLS                                                    │
│    craft_presence = NO or keep_verdict = REJECT                             │
│    Paired against Foundation positives to train the model what NOT to write │
└─────────────────────────────────────────────────────────────────────────────┘
```

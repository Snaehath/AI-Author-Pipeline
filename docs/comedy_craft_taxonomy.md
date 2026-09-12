# Comedy Craft Taxonomy & Annotation Specification

## 1. Overview & Purpose

The **Comedy Craft Dataset** transforms general prose imitation into a principled training corpus teaching a small language model (1.5B) **how classic comedic fiction works**.

Classic British comedy (Wodehouse, Jerome, Grossmith) derives its comedic power not from superficial period vocabulary, but from **underlying narrative and social mechanisms**: status asymmetry, escalating complications, deadpan restraint, misunderstanding, and dialogue subtext.

---

## 2. Four-Tier Unified Record Architecture

Every record in the Comedy Craft Dataset is strictly anchored to its original source passage across four levels:

```text
SOURCE
  │  (Book, chapter, source ID, and raw unabridged text)
  ▼
FACTS
  │  (Objective reality: characters, location, objects, dialogue ratio, turn count)
  ▼
CRAFT
  │  (Why it works: mechanism, structural beats, confidence score, quality score, tone)
  ▼
OPERATIONS & DPO
     (Active writing tasks: identify, extract, rewrite, continue + audited contrast DPO)
```

### JSON Schema

```json
{
  "source": {
    "source_id": "my_man_jeeves_ch1_00005",
    "source_book": "My Man Jeeves",
    "chapter_index": 1,
    "source_text": "..."
  },
  "facts": {
    "characters": ["Bertie", "Jeeves"],
    "location": "drawing room",
    "objects": ["tea-cup", "telegram"],
    "character_goals": {
      "Bertie": "avert social fallout",
      "Jeeves": "maintain composure and social standing"
    },
    "dialogue_ratio": 0.54,
    "turn_count": 6
  },
  "craft": {
    "primary_mechanism": "STATUS_REVERSAL",
    "secondary_mechanisms": ["DEADPAN_REACTION", "DIALOGUE_SUBTEXT"],
    "confidence": 0.92,
    "quality_score": 0.88,
    "scene_function": "SOCIAL_CONFLICT",
    "tone": "DRY_WIT",
    "setup_summary": "...",
    "escalation_summary": "...",
    "reversal_summary": "...",
    "payoff_summary": "...",
    "surface_style_features": ["right-o", "dash it"],
    "source": "HEURISTIC",
    "review_status": "UNREVIEWED"
  },
  "operations": [
    {
      "task_type": "IDENTIFY_MECHANISM",
      "prompt": "...",
      "expected_output": "...",
      "target_concept": "STATUS_REVERSAL"
    }
  ],
  "dpo_pair": {
    "prompt": "...",
    "chosen": "...",
    "rejected": "...",
    "target_dimension": "COMEDIC_RESTRAINT",
    "purity_report": {
      "purity_score": 0.95,
      "target_dimension_changed": true
    }
  }
}
```

---

## 3. Comedic Mechanism Taxonomy

### Core Mechanisms (Machinery, Not Vocabulary)

1. **`MISUNDERSTANDING`**:
   - Two characters operate under mutually incompatible premises. Neither realizes the discrepancy until tension compounds.
2. **`STATUS_REVERSAL`**:
   - Social hierarchy is inverted. The nominally superior aristocrat/master flails in panic or intellectual incapacity, while the subordinate/valet maintains immaculate calm and control.
3. **`ESCALATION`**:
   - A minor irregularity or trivial deceit is met with an ill-advised remedy, compounding into an uncontrollable cascade of complications.
4. **`DEADPAN_REACTION`**:
   - Emotional understatement and unshakeable placidity in the face of catastrophic social or domestic upheaval.
5. **`SOCIAL_EMBARRASSMENT`**:
   - Acute dread of violating etiquette, incurring scandal, or being unmasked in front of formidable social arbiters (e.g. formidable aunts, clergymen, wealthy benefactors).
6. **`VERBAL_WIT`**:
   - Subtextual parrying, epigrams, ironic formality, and conversational counter-punches.
7. **`DRAMATIC_IRONY`**:
   - The reader and select characters possess knowledge concealed from others, generating anticipation and comedic tension.
8. **`DIALOGUE_SUBTEXT`**:
   - Outwardly civil conversation masking frantic negotiation, suspicion, or deceit.
9. **`CALLBACK`**:
   - Re-introducing a minor detail or running motif with compounded consequence.
10. **`PHYSICAL_COMPLICATION`**:
    - Farce elements: concealment in cupboards, mislaid hats, physical obstacles, and frantic timing.

---

## 4. Decoupling Surface Slang from Comedic Machinery

> [!WARNING]
> Superficial period idioms (e.g., *"By Jove!"*, *"old top"*, *"dash it"*, *"bally"*, *"right-o"*) are **surface style markers**, not comedic craft mechanisms.
> The pipeline records these in `surface_style_features` and forbids them from serving as proof of comedic mechanisms.

---

## 5. Annotation Confidence vs. Literary Quality

- **`confidence` [0.0, 1.0]**: Measures certainty that the labeled comedic mechanism is active in the text.
- **`quality_score` [0.0, 1.0]**: Measures literary execution quality (passage length, syntactic variety, dialogue balance, descriptive richness) independent of annotation confidence.
- Scenes with `confidence < 0.70` are automatically tagged with `ReviewStatus.FLAGGED_LOW_CONFIDENCE`.

---

## 6. Contrast Purity for DPO Pairs

DPO preference learning requires clean comparison boundaries. The `ContrastPurityValidator` audits every candidate pair:
- **`prompt_identical`**: Same context prompt.
- **`characters_same`**: Exact character preservation ($\ge 75\%$ Jaccard overlap).
- **`setting_same`**: Consistent scene location.
- **`plot_events_same`**: Narrative facts preserved ($\ge 60\%$ non-dialogue token overlap).
- **`target_dimension_changed`**: The rejected output specifically exhibits the targeted craft flaw (e.g. over-explaining the joke, exposition dump).
- **Threshold**: Pairs with `purity_score < 0.85` are rejected.

"""
Semantic Comedy Craft Annotator.

Evaluates why a comedic scene works:
- Detects active comedic mechanisms using structural and conversational dynamics
- Computes explicit mechanism confidence scores [0.0, 1.0]
- Computes an independent literary craft quality score [0.0, 1.0]
- Extracts structural beats: setup, escalation, reversal, payoff
- Isolates superficial period slang from true comedic machinery
- Flags low-confidence annotations for human review
"""

import re
from typing import Dict, List, Tuple
from dataset_generator.taxonomy import (
    ComicMechanism,
    SceneFunction,
    ComedicTone,
    AnnotationSource,
    ReviewStatus,
    CraftAnnotation,
    CraftPresence,
    CraftStratum,
    StoryFacts,
)
from dataset_generator.craft_filter import ComedyCraftEligibilityGate


class ComedyCraftAnnotator:
    """
    Annotates scenes with comedic craft principles, structural arcs,
    and confidence scores. Enforces hard eligibility gating and 8-point detector fixes.
    """

    # Surface-level British slang markers (recorded as style features, NOT mechanism evidence)
    SURFACE_SLANG_MARKERS = [
        "by jove", "old top", "old chap", "old bean", "right-o", "right ho",
        "dash it", "deuced", "ripping", "bally", "toodle-oo", "what ho",
        "rummy", "corking", "topping", "stout fellow", "eh what", "my dear fellow"
    ]

    # Refined mechanism semantic cues disambiguated from non-comic actions
    MECHANISM_CUES = {
        ComicMechanism.MISUNDERSTANDING: [
            "thought you meant", "supposed", "understood that", "mistake",
            "at cross-purposes", "different matter", "referring to", "on the contrary",
            "not what i said", "you believed", "talking of something else", "puzzled by"
        ],
        ComicMechanism.STATUS_REVERSAL: [
            "valet", "butler", "submitted respectfully", "venture to suggest",
            "superior intellect", "at his mercy", "condescended", "humble apology",
            "reproved", "master admitted", "tie recommendation", "subordinate",
            "helpless under", "in charge of the situation", "silk tie", "necktie"
        ],
        ComicMechanism.ESCALATION: [
            "worse", "compounded", "furthermore", "on top of that", "disaster",
            "catastrophe", "fresh complication", "multiplied", "hundreds",
            "exponential", "more pigs", "elephant", "rate", "accumulating",
            "doubled", "mounting", "thirty-two", "menagerie", "guinea-pigs"
        ],
        ComicMechanism.DEADPAN_REACTION: [
            "calmly", "mildly", "quietly", "without emotion", "impassively",
            "drily", "gravely", "unmoved", "matter-of-fact", "stoic",
            "hardly the moment", "merely observed", "market opened quietly",
            "casual voice", "unruffled"
        ],
        ComicMechanism.SOCIAL_EMBARRASSMENT: [
            "blushed", "mortified", "social agony", "scandal", "decorum",
            "disgrace", "dreaded", "crimson", "shame", "reputation", "etiquette",
            "frightful awkwardness", "uncomfortable silence"
        ],
        ComicMechanism.VERBAL_WIT: [
            "epigram", "irony", "retorted", "parried", "repartee", "scathing",
            "barb", "quip", "banter", "witticism", "singularly unfortunate",
            "slight overstatement", "scarcely accurate", "make the whole world dirty",
            "pointed observation", "dry irony", "delirium tremens"
        ],
        ComicMechanism.DRAMATIC_IRONY: [
            "unbeknownst", "little did he know", "unaware that", "meanwhile",
            "behind his back", "ignorant of", "confident that", "secure in the belief",
            "had no idea", "kept in the dark"
        ],
        ComicMechanism.DIALOGUE_SUBTEXT: [
            "said pleasantly", "smiling coldly", "sweetly", "polite tone",
            "behind the smile", "feigned indifference", "strained cordiality",
            "surface politeness", "underlying meaning"
        ],
        ComicMechanism.CALLBACK: [
            "as mentioned earlier", "the aforementioned", "remembered the original",
            "once again the", "returning to the subject", "second time today"
        ],
        ComicMechanism.PHYSICAL_COMPLICATION: [
            "behind the screen", "under the sofa", "cupboard", "wardrobe",
            "tripped over", "tea-tray", "scramble under", "tangled in",
            "spilled the", "under the bed", "umbrella held like a hammer"
        ],
    }

    CONFIDENCE_THRESHOLD = 0.65

    def __init__(self):
        self.eligibility_gate = ComedyCraftEligibilityGate()

    def annotate(self, text: str, facts: StoryFacts) -> CraftAnnotation:
        """Produces craft annotation with eligibility gating, confidence scores, and structural breakdown."""
        lower_text = text.lower()

        # 1. Eligibility Gate (Hard filter for genuine comedic presence)
        presence, gate_scores, rationale = self.eligibility_gate.evaluate(text, facts)

        # 2. Surface Style Extraction (decoupled from comedic machinery)
        surface_features = self._extract_surface_features(lower_text)

        # If gate says NO: reject immediately without forcing a false mechanism
        if presence == CraftPresence.NO:
            return CraftAnnotation(
                primary_mechanism=ComicMechanism.MISUNDERSTANDING,
                secondary_mechanisms=[],
                confidence_scores={},
                detector_confidence=0.0,
                linguistic_craft_score=0.10,
                craft_presence=CraftPresence.NO,
                craft_stratum=CraftStratum.REJECT,
                scene_function=SceneFunction.SOCIAL_CONFLICT,
                tone=ComedicTone.DRY_WIT,
                setup_summary="",
                escalation_summary="",
                reversal_summary="",
                payoff_summary="",
                surface_style_features=surface_features,
                source=AnnotationSource.HEURISTIC,
                review_status=ReviewStatus.REJECTED,
            )

        # 3. Mechanism Scoring & Confidence
        scores = self._score_mechanisms(lower_text, facts)
        sorted_mechs = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        primary_mech_name, primary_conf = sorted_mechs[0]
        primary_mech = ComicMechanism(primary_mech_name)

        secondary_mechs = [
            ComicMechanism(name) for name, conf in sorted_mechs[1:4] if conf >= 0.40
        ]

        # 4. Stratum Classification (Pure Mechanism vs Composite Craft vs Review Queue)
        if presence == CraftPresence.PARTIAL:
            # PARTIAL is a human-review state, excluded from automatic SFT
            stratum = CraftStratum.REJECT
            review_status = ReviewStatus.FLAGGED_LOW_CONFIDENCE
        else:
            # Check for Pure vs Composite
            # Pure: single dominant mechanism (top >= 0.60 and gap to 2nd >= 0.15)
            second_conf = sorted_mechs[1][1] if len(sorted_mechs) > 1 else 0.0
            if primary_conf >= 0.60 and (primary_conf - second_conf >= 0.15):
                stratum = CraftStratum.PURE_MECHANISM
            elif primary_conf >= 0.50 and second_conf >= 0.45:
                stratum = CraftStratum.COMPOSITE_CRAFT
            else:
                stratum = CraftStratum.PURE_MECHANISM

            review_status = (
                ReviewStatus.FLAGGED_LOW_CONFIDENCE
                if primary_conf < self.CONFIDENCE_THRESHOLD
                else ReviewStatus.UNREVIEWED
            )

        # 5. Independent Literary Quality Assessment
        quality_score = self._assess_quality(text, facts, primary_conf)

        # 6. Scene Function and Tone
        scene_function = self._determine_scene_function(lower_text, facts, primary_mech)
        tone = self._determine_tone(lower_text, primary_mech)

        # 7. Extract Structural Arc (Setup, Escalation, Reversal, Payoff)
        setup, escalation, reversal, payoff = self._extract_structural_beats(
            text, primary_mech, facts
        )

        return CraftAnnotation(
            primary_mechanism=primary_mech,
            secondary_mechanisms=secondary_mechs,
            confidence_scores={k: round(v, 2) for k, v in scores.items()},
            detector_confidence=round(primary_conf, 2),
            linguistic_craft_score=round(quality_score, 2),
            craft_presence=presence,
            craft_stratum=stratum,
            scene_function=scene_function,
            tone=tone,
            setup_summary=setup,
            escalation_summary=escalation,
            reversal_summary=reversal,
            payoff_summary=payoff,
            surface_style_features=surface_features,
            source=AnnotationSource.HEURISTIC,
            review_status=review_status,
        )

    def _extract_surface_features(self, lower_text: str) -> List[str]:
        """Captures superficial period vernacular to isolate from structural craft."""
        features: List[str] = []
        for marker in self.SURFACE_SLANG_MARKERS:
            if marker in lower_text:
                features.append(marker)
        return features

    def _score_mechanisms(self, lower_text: str, facts: StoryFacts) -> Dict[str, float]:
        """Calculates refined confidence [0.0, 1.0] for each comic mechanism."""
        scores: Dict[str, float] = {}

        for mech, cues in self.MECHANISM_CUES.items():
            base_matches = sum(1 for cue in cues if cue in lower_text)
            structural_boost = 0.0

            if mech == ComicMechanism.STATUS_REVERSAL:
                # Require role inversion or valet dominance, not just "sir"
                has_valet_role = any(c in lower_text for c in ["valet", "jeeves", "butler"])
                has_submission = any(c in lower_text for c in ["submit", "venture to suggest", "reproved", "master admitted", "superior", "respectfully"])
                has_inversion = any(c in lower_text for c in ["at his mercy", "collapsed", "helpless under", "silk tie", "necktie", "tie recommendation"])
                if has_valet_role and (has_submission or has_inversion):
                    structural_boost += 0.45
                elif has_inversion and len(facts.characters) >= 2:
                    structural_boost += 0.30

            elif mech == ComicMechanism.ESCALATION:
                # Compounding stakes or multiplying problem (not merely turn count)
                has_compounding = any(w in lower_text for w in [
                    "worse", "compounded", "furthermore", "fresh complication",
                    "multiplied", "hundreds", "elephant", "thirty-two", "menagerie",
                    "more pigs", "guinea-pigs"
                ])
                if has_compounding and facts.turn_count >= 2:
                    structural_boost += 0.45
                elif has_compounding:
                    structural_boost += 0.35

            elif mech == ComicMechanism.DEADPAN_REACTION:
                # Stoic delivery in crisis/awkward context
                has_stoic = any(w in lower_text for w in ["drily", "calmly", "mildly", "impassively", "observed jeeves", "market opened quietly"])
                if has_stoic and facts.dialogue_ratio >= 0.20:
                    structural_boost += 0.40
                elif has_stoic:
                    structural_boost += 0.25

            elif mech == ComicMechanism.DIALOGUE_SUBTEXT:
                # Surface politeness vs underlying friction
                has_surface_polite = any(w in lower_text for w in ["said pleasantly", "smiling coldly", "sweetly", "polite tone", "statue"])
                if has_surface_polite and facts.dialogue_ratio >= 0.35:
                    structural_boost += 0.40

            elif mech == ComicMechanism.VERBAL_WIT:
                # Retort or pointed wit in conversational turns
                has_retort = any(w in lower_text for w in ["retorted", "parried", "epigram", "quip", "delirium tremens", "make the whole world dirty"])
                if has_retort and facts.dialogue_ratio >= 0.25:
                    structural_boost += 0.40

            elif mech == ComicMechanism.DRAMATIC_IRONY:
                # Asymmetric knowledge
                has_irony = any(w in lower_text for w in ["unbeknownst", "little did he know", "unaware that", "kept in the dark"])
                if has_irony:
                    structural_boost += 0.35

            elif mech == ComicMechanism.MISUNDERSTANDING:
                # Premise mismatch
                has_mismatch = any(w in lower_text for w in ["thought you meant", "misunderstood", "at cross-purposes", "different matter"])
                if has_mismatch and facts.turn_count >= 2:
                    structural_boost += 0.35

            elif mech == ComicMechanism.PHYSICAL_COMPLICATION:
                # Farce mechanics (wardrobe, hiding, tea-tray)
                has_farce = any(w in lower_text for w in ["behind the screen", "under the sofa", "cupboard", "wardrobe", "tripped over", "tea-tray"])
                if has_farce:
                    structural_boost += 0.45

            # If no matches and no structural boost, floor is 0.05
            if base_matches == 0 and structural_boost == 0.0:
                raw_score = 0.05
            else:
                raw_score = (base_matches * 0.25) + structural_boost

            confidence = min(0.98, max(0.05, raw_score))
            scores[mech.value] = confidence

        return scores

    def _assess_quality(self, text: str, facts: StoryFacts, mechanism_confidence: float) -> float:
        """
        Evaluates literary execution quality independently from annotation certainty:
        - Passage length and descriptive variety
        - Balanced dialogue to narrative ratio (ideal around 0.35 - 0.70)
        - Syntactic richness (sentence rhythm, vocabulary breadth)
        """
        words = text.split()
        word_count = len(words)
        if word_count < 25:
            return 0.35  # Fragment or sentence snippet

        quality = 0.50

        # Word count bonus (substantial scenes have room for comedic craft to develop)
        if 80 <= word_count <= 450:
            quality += 0.20
        elif word_count > 450:
            quality += 0.15

        # Dialogue balance bonus
        if 0.30 <= facts.dialogue_ratio <= 0.75:
            quality += 0.15
        elif facts.dialogue_ratio > 0.90 or facts.dialogue_ratio < 0.10:
            quality -= 0.10

        # Sentence rhythm diversity
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip()) > 3]
        if len(sentences) >= 4:
            lengths = [len(s.split()) for s in sentences]
            variance = max(lengths) - min(lengths)
            if variance > 12:  # Alternating short/long cadence
                quality += 0.10

        return min(0.98, max(0.20, quality))

    def _determine_scene_function(
        self, lower_text: str, facts: StoryFacts, primary_mech: ComicMechanism
    ) -> SceneFunction:
        """Maps narrative function from conversational context and mechanisms."""
        if primary_mech == ComicMechanism.STATUS_REVERSAL:
            return SceneFunction.SOCIAL_CONFLICT
        if primary_mech == ComicMechanism.SOCIAL_EMBARRASSMENT:
            return SceneFunction.AWKWARD_ENCOUNTER
        if any(w in lower_text for w in ["plan", "scheme", "idea", "must do", "arrange"]):
            return SceneFunction.SCHEME_EXECUTION
        if any(w in lower_text for w in ["saved", "solved", "settled", "relieved", "escaped"]):
            return SceneFunction.CRISIS_RESOLUTION
        if facts.turn_count >= 2:
            return SceneFunction.SOCIAL_CONFLICT
        return SceneFunction.AWKWARD_ENCOUNTER

    def _determine_tone(self, lower_text: str, primary_mech: ComicMechanism) -> ComedicTone:
        """Determines tonal register."""
        if primary_mech == ComicMechanism.DEADPAN_REACTION:
            return ComedicTone.DEADPAN
        if primary_mech == ComicMechanism.PHYSICAL_COMPLICATION:
            return ComedicTone.FARCE
        if primary_mech in (ComicMechanism.VERBAL_WIT, ComicMechanism.STATUS_REVERSAL):
            return ComedicTone.DRY_WIT
        if any(w in lower_text for w in ["satire", "society", "parliament", "aristocracy"]):
            return ComedicTone.LIGHT_SATIRICAL
        return ComedicTone.DOMESTIC_ABSURDITY

    def _extract_structural_beats(
        self, text: str, primary_mech: ComicMechanism, facts: StoryFacts
    ) -> Tuple[str, str, str, str]:
        """
        Deconstructs passage into 4 structural beats:
        Setup -> Escalation -> Reversal -> Payoff
        """
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
        total_s = len(sentences)

        if total_s < 4:
            # Short passage interpolation
            setup = sentences[0] if total_s > 0 else "Initial status quo established."
            escalation = sentences[1] if total_s > 1 else "Comedic complication introduced."
            reversal = sentences[2] if total_s > 2 else "Expectation upended."
            payoff = sentences[-1] if total_s > 0 else "Deadpan comedic resolution."
            return setup, escalation, reversal, payoff

        # Divide text roughly into 4 quarters
        q1 = sentences[: max(1, total_s // 4)]
        q2 = sentences[max(1, total_s // 4) : max(2, total_s // 2)]
        q3 = sentences[max(2, total_s // 2) : max(3, (3 * total_s) // 4)]
        q4 = sentences[max(3, (3 * total_s) // 4) :]

        setup_summary = f"Characters {', '.join(facts.characters[:2])} establish scene context: '{q1[0][:80]}...'"
        escalation_summary = f"Complication rises around {primary_mech.value.lower()}: '{q2[0][:80]}...'"
        reversal_summary = f"Expectation or status is inverted: '{q3[0][:80]}...'"
        payoff_summary = f"Comedic resolution or deadpan beat lands: '{q4[-1][:80]}...'"

        return setup_summary, escalation_summary, reversal_summary, payoff_summary

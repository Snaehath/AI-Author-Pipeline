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
    StoryFacts,
)


class ComedyCraftAnnotator:
    """
    Annotates scenes with comedic craft principles, structural arcs,
    and confidence scores.
    """

    # Surface-level British slang markers (recorded as style features, NOT mechanism evidence)
    SURFACE_SLANG_MARKERS = [
        "by jove", "old top", "old chap", "old bean", "right-o", "right ho",
        "dash it", "deuced", "ripping", "bally", "toodle-oo", "what ho",
        "rummy", "corking", "topping", "stout fellow", "eh what", "my dear fellow"
    ]

    # Mechanism semantic indicators
    # Note: Evaluated alongside structural cues, dialogue ratio, and speaker contrast
    MECHANISM_CUES = {
        ComicMechanism.MISUNDERSTANDING: [
            "thought you meant", "supposed", "understood that", "mistake",
            "at cross-purposes", "different matter", "referring to", "on the contrary",
            "not what i said", "you believed"
        ],
        ComicMechanism.STATUS_REVERSAL: [
            "sir", "valet", "butler", "master", "master's", "submitted",
            "respectfully", "venture to suggest", "condescended", "humble",
            "dignity", "poise", "collapsed", "at his mercy"
        ],
        ComicMechanism.ESCALATION: [
            "worse", "compounded", "furthermore", "on top of that", "disaster",
            "catastrophe", "culminated", "went from bad to", "fresh complication",
            "plunged deeper", "in addition to"
        ],
        ComicMechanism.DEADPAN_REACTION: [
            "calmly", "mildly", "quietly", "without emotion", "impassively",
            "drily", "gravely", "unmoved", "matter-of-fact", "stoic",
            "hardly the moment", "merely observed"
        ],
        ComicMechanism.SOCIAL_EMBARRASSMENT: [
            "blushed", "awkward", "mortified", "agony", "scandal", "decorum",
            "disgrace", "dreaded", "crimson", "shame", "reputation", "etiquette",
            "good breeding", "horrified"
        ],
        ComicMechanism.VERBAL_WIT: [
            "epigram", "irony", "retorted", "parried", "sarcasm", "repartee",
            "scathing", "barb", "quip", "banter", "witticism"
        ],
        ComicMechanism.DRAMATIC_IRONY: [
            "unbeknownst", "little did he know", "unaware", "meanwhile",
            "behind his back", "ignorant of", "confident that", "secure in the belief"
        ],
        ComicMechanism.DIALOGUE_SUBTEXT: [
            "said pleasantly", "smiling coldly", "sweetly", "polite tone",
            "behind the smile", "feigned indifference", "strained cordiality"
        ],
        ComicMechanism.CALLBACK: [
            "again", "as mentioned", "once more", "inevitable", "haunted by",
            "remembered the", "reappeared", "second time"
        ],
        ComicMechanism.PHYSICAL_COMPLICATION: [
            "tripped", "stumbled", "slipped", "behind the screen", "under the sofa",
            "cupboard", "scramble", "spilled", "dropped", "collision", "fled"
        ],
    }

    CONFIDENCE_THRESHOLD = 0.70

    def annotate(self, text: str, facts: StoryFacts) -> CraftAnnotation:
        """Produces craft annotation with confidence scores, quality score, and structural breakdown."""
        lower_text = text.lower()

        # 1. Surface Style Extraction (decoupled from comedic machinery)
        surface_features = self._extract_surface_features(lower_text)

        # 2. Mechanism Scoring & Confidence
        scores = self._score_mechanisms(lower_text, facts)
        
        # Sort mechanisms by score
        sorted_mechs = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        primary_mech_name, primary_conf = sorted_mechs[0]
        primary_mech = ComicMechanism(primary_mech_name)

        secondary_mechs = [
            ComicMechanism(name) for name, conf in sorted_mechs[1:3] if conf >= 0.40
        ]

        # 3. Independent Literary Quality Assessment
        quality_score = self._assess_quality(text, facts, primary_conf)

        # 4. Determine Scene Function and Tone
        scene_function = self._determine_scene_function(lower_text, facts, primary_mech)
        tone = self._determine_tone(lower_text, primary_mech)

        # 5. Extract Structural Arc (Setup, Escalation, Reversal, Payoff)
        setup, escalation, reversal, payoff = self._extract_structural_beats(
            text, primary_mech, facts
        )

        # 6. Audit Review Status
        review_status = (
            ReviewStatus.FLAGGED_LOW_CONFIDENCE
            if primary_conf < self.CONFIDENCE_THRESHOLD
            else ReviewStatus.UNREVIEWED
        )

        return CraftAnnotation(
            primary_mechanism=primary_mech,
            secondary_mechanisms=secondary_mechs,
            confidence_scores={k: round(v, 2) for k, v in scores.items()},
            confidence=round(primary_conf, 2),
            quality_score=round(quality_score, 2),
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
        """Calculates confidence [0.0, 1.0] for each comic mechanism."""
        scores: Dict[str, float] = {}

        for mech, cues in self.MECHANISM_CUES.items():
            base_matches = sum(1 for cue in cues if cue in lower_text)
            
            # Structural weighting based on objective facts
            structural_boost = 0.0
            if mech == ComicMechanism.STATUS_REVERSAL:
                if len(facts.characters) >= 2 and any(
                    c in lower_text for c in ["sir", "jeeves", "valet", "master"]
                ):
                    structural_boost += 0.35
            elif mech == ComicMechanism.DIALOGUE_SUBTEXT:
                if facts.dialogue_ratio >= 0.40 and len(facts.characters) >= 2:
                    structural_boost += 0.25
            elif mech == ComicMechanism.DEADPAN_REACTION:
                if facts.dialogue_ratio >= 0.30 and any(
                    w in lower_text for w in ["calmly", "drily", "murmured", "observed"]
                ):
                    structural_boost += 0.30
            elif mech == ComicMechanism.ESCALATION:
                if facts.turn_count >= 3:
                    structural_boost += 0.20
            elif mech == ComicMechanism.MISUNDERSTANDING:
                if facts.turn_count >= 2 and "?" in lower_text:
                    structural_boost += 0.20
            elif mech == ComicMechanism.SOCIAL_EMBARRASSMENT:
                if any(w in lower_text for w in ["aunt", "uncle", "reputation", "dread"]):
                    structural_boost += 0.25

            # Confidence calculation bounded in [0.10, 0.98]
            raw_score = (base_matches * 0.22) + structural_boost
            confidence = min(0.98, max(0.12, raw_score))
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

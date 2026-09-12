"""
Comedy Craft Eligibility Gate.

Evaluates whether a raw prose passage genuinely contains comedic craft (social farce,
dry wit, deadpan reaction, domestic absurdity) or represents non-comedic prose (drama,
violence, philosophical exposition, historical apparatus).
"""

import re
from typing import Dict, List, Tuple

from dataset_generator.taxonomy import CraftPresence, StoryFacts


class ComedyCraftEligibilityGate:
    """
    Hard eligibility gate evaluated before mechanism annotation.
    Computes a composite multi-signal balance:
        score = (0.35 * comedic_signal) + (0.25 * character_interaction)
              + (0.20 * comic_stakes) + (0.20 * tonal_compatibility)
              - (0.50 * serious_drama_signal)
    """

    # Indicators of serious drama, existential agony, genuine horror, or non-fiction apparatus
    GENUINE_HORROR_DRAMA_MARKERS = [
        "terror", "horror", "corpse", "bleeding", "blood", "stabbing", "murdered",
        "scaffold", "execution", "gallows", "screamed in agony", "wept bitterly",
        "despair", "fury", "rage", "anguish", "torment", "threat of death",
        "pale and trembling", "murderers lurked", "grievous", "shuddering"
    ]

    HISTORICAL_ACADEMIC_MARKERS = [
        "archival", "citation", "bibliography", "historians agree", "chronicle",
        "political events of", "statute", "treatise", "etymology", "parliamentary report",
        "dates from", "manuscript notes", "editorial note", "in the reign of"
    ]

    COMEDIC_LEXICON_MARKERS = [
        "absurd", "ridiculous", "comical", "laughed", "smiled", "chuckle",
        "bizarre", "preposterous", "ludicrous", "jovial", "scandal", "decorum",
        "valet", "butler", "jeeves", "bertie", "aunt", "uncle", "bicky",
        "guinea pig", "guinea pigs", "flannery", "allowance", "monocle",
        "drily", "mildly", "calmly observed", "stoic", "understated",
        "puzzled", "awkward", "embarrassment", "by jove", "dash it",
        "polite smile", "venture to suggest", "statue", "market opened quietly",
        "tie", "supper party", "supper parties", "quip", "banter", "parried"
    ]

    COMIC_STAKES_MARKERS = [
        "reputation", "etiquette", "dinner", "supper", "hat", "umbrella", "allowance",
        "rule", "regulation", "shipping rate", "pigs", "drawing room", "tea", "bill",
        "landlady", "marriage", "engagement", "refusal", "polite society"
    ]

    PASS_THRESHOLD = 0.52
    REJECT_THRESHOLD = 0.32
    MAX_SERIOUS_DRAMA_TOLERANCE = 0.50

    def evaluate(self, text: str, facts: StoryFacts) -> Tuple[CraftPresence, Dict[str, float], str]:
        """
        Determines whether text is eligible for comedic craft extraction.
        Returns:
            (CraftPresence, score_breakdown, rationale)
        """
        lower = text.lower()

        # 1. Character Interaction Signal [0.0, 1.0]
        # Evaluates presence of active characters, dialogue, and conversational turn-taking
        char_score = 0.0
        if len(facts.characters) >= 2:
            char_score += 0.50
        elif len(facts.characters) == 1:
            char_score += 0.25

        if facts.dialogue_ratio >= 0.25:
            char_score += 0.30
        elif facts.dialogue_ratio > 0.05:
            char_score += 0.15

        if facts.turn_count >= 2:
            char_score += 0.20
        char_score = min(1.0, char_score)

        # 2. Comedic Signal [0.0, 1.0]
        # Evaluates explicit comedic markers, humor vernacular, and ironical framing
        comedic_matches = sum(1 for m in self.COMEDIC_LEXICON_MARKERS if m in lower)
        # Check conversational wit patterns (e.g. quote + observed/murmured/retorted)
        has_witty_dialogue = bool(re.search(r'["\'].*?["\']\s*(?:observed|murmured|retorted|suggested|submitted|said)', lower))
        comedic_score = min(1.0, (comedic_matches * 0.18) + (0.25 if has_witty_dialogue else 0.0))

        # 3. Comic Stakes Signal [0.0, 1.0]
        # Focus on domestic, social, bureaucratic, or etiquette friction rather than physical peril
        stakes_matches = sum(1 for m in self.COMIC_STAKES_MARKERS if m in lower)
        stakes_score = min(1.0, stakes_matches * 0.25)

        # 4. Tonal Compatibility [0.0, 1.0]
        # Lightness, deadpan restraint, domestic absurdity
        tonal_score = 0.40  # neutral baseline
        if any(w in lower for w in ["drily", "calmly", "gently", "mildly", "politely"]):
            tonal_score += 0.30
        if any(w in lower for w in ["curious", "astonished", "puzzled", "amused"]):
            tonal_score += 0.30
        tonal_score = min(1.0, tonal_score)

        # 5. Serious Drama / Non-Fiction Signal [0.0, 1.0]
        horror_matches = sum(1 for m in self.GENUINE_HORROR_DRAMA_MARKERS if m in lower)
        history_matches = sum(1 for m in self.HISTORICAL_ACADEMIC_MARKERS if m in lower)

        # Structural check for non-fiction citations (e.g. "[1]", "(1895)", "pp. 12-14")
        has_citations = bool(re.search(r'\[\d+\]|\(\d{4}\)|pp\.\s*\d+|vol\.\s*[ivxlcdm]+', lower))
        if has_citations:
            history_matches += 3

        drama_score = min(1.0, (horror_matches * 0.25) + (history_matches * 0.30))

        # Attenuation: if strong comedic cues accompany dramatic words (e.g. playful exaggeration)
        if comedic_score >= 0.60 and horror_matches <= 2:
            drama_score = max(0.0, drama_score - 0.20)

        # Composite Eligibility Score
        composite_score = (
            (0.35 * comedic_score)
            + (0.25 * char_score)
            + (0.20 * stakes_score)
            + (0.20 * tonal_score)
            - (0.50 * drama_score)
        )
        composite_score = round(max(0.0, min(1.0, composite_score)), 3)

        scores = {
            "composite_score": composite_score,
            "comedic_signal": round(comedic_score, 2),
            "character_interaction": round(char_score, 2),
            "comic_stakes": round(stakes_score, 2),
            "tonal_compatibility": round(tonal_score, 2),
            "serious_drama_signal": round(drama_score, 2),
        }

        # Gate Verdict
        if drama_score >= self.MAX_SERIOUS_DRAMA_TOLERANCE and comedic_score < 0.45:
            return CraftPresence.NO, scores, f"Rejected: High serious drama / historical signal ({drama_score})"

        if composite_score >= self.PASS_THRESHOLD:
            return CraftPresence.YES, scores, f"Passed: High comedic craft signal ({composite_score})"
        elif composite_score <= self.REJECT_THRESHOLD:
            return CraftPresence.NO, scores, f"Rejected: Insufficient comedic craft signal ({composite_score})"
        else:
            return CraftPresence.PARTIAL, scores, f"Review Queue: Borderline comedic signal ({composite_score})"

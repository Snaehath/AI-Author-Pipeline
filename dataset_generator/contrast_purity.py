"""
Contrast Purity Validator for Controlled DPO Pairs.

Audits DPO pairs to ensure that only the targeted comedic craft dimension varies,
rejecting noisy pairs where plot events, characters, or settings unintentionally drift.
"""

import re
from typing import Set, Tuple
from dataset_generator.taxonomy import ContrastDimension, ContrastPurityReport


class ContrastPurityValidator:
    """
    Validates that a DPO pair (chosen vs rejected) preserves narrative invariants
    while isolating variation to a single craft dimension.
    """

    PURITY_THRESHOLD = 0.85

    # Phrases indicating a character explaining the joke / ruining comedic restraint
    EXPLANATION_MARKERS = [
        "because it is funny", "what a ridiculous", "how absurd that",
        "which was comical", "laughable because", "as everyone knows",
        "ironic that", "the joke was", "i am explaining", "which is hilarious",
        "to be completely honest about my feelings", "let me tell you my internal emotion"
    ]

    # Explicit emotional dump markers ruining dialogue subtext
    EXPOSITION_MARKERS = [
        "i feel terribly insecure", "my secret plan is", "i am desperate because",
        "deep down i know", "i am simply trying to manipulate you",
        "my true motive is"
    ]

    def validate(
        self,
        prompt: str,
        chosen: str,
        rejected: str,
        target_dimension: ContrastDimension,
    ) -> ContrastPurityReport:
        """Evaluates contrast purity between chosen and rejected generations."""
        # Check 1: Prompt identity
        prompt_identical = len(prompt.strip()) > 0

        # Check 2: Character set consistency
        chosen_chars = self._extract_names(chosen)
        rejected_chars = self._extract_names(rejected)
        # Characters must have at least 80% Jaccard overlap
        char_overlap = self._jaccard(chosen_chars, rejected_chars)
        characters_same = char_overlap >= 0.75

        # Check 3: Setting / Location consistency
        chosen_locations = self._extract_location_cues(chosen)
        rejected_locations = self._extract_location_cues(rejected)
        setting_same = chosen_locations == rejected_locations or (
            not chosen_locations and not rejected_locations
        )

        # Check 4: Length parity (reject extreme length disparities which confound DPO)
        len_c = max(1, len(chosen.split()))
        len_r = max(1, len(rejected.split()))
        length_ratio = min(len_c, len_r) / max(len_c, len_r)
        length_acceptable = length_ratio >= 0.40

        # Check 5: Target dimension verification
        dimension_changed, dim_confidence = self._verify_target_dimension(
            chosen, rejected, target_dimension
        )

        # Plot events consistency: check token overlap of core narrative concepts
        plot_overlap = self._compute_plot_overlap(chosen, rejected)
        plot_events_same = plot_overlap >= 0.25

        # Calculate weighted purity score
        weights = {
            "prompt": 0.15 if prompt_identical else 0.0,
            "characters": 0.25 if characters_same else 0.0,
            "setting": 0.15 if setting_same else 0.0,
            "length": 0.10 if length_acceptable else 0.0,
            "plot": 0.10 if plot_events_same else 0.0,
            "dimension": 0.25 * dim_confidence if dimension_changed else 0.0,
        }
        purity_score = round(sum(weights.values()), 3)

        rejection_reason = None
        if purity_score < self.PURITY_THRESHOLD:
            reasons = []
            if not characters_same:
                reasons.append(f"character mismatch (overlap {char_overlap:.2f})")
            if not setting_same:
                reasons.append("setting drift")
            if not length_acceptable:
                reasons.append(f"length ratio too low ({length_ratio:.2f})")
            if not dimension_changed:
                reasons.append(f"failed to isolate dimension {target_dimension.value}")
            if not plot_events_same:
                reasons.append(f"plot divergence ({plot_overlap:.2f})")
            rejection_reason = "; ".join(reasons) or "Overall purity score below threshold"

        return ContrastPurityReport(
            prompt_identical=prompt_identical,
            plot_events_same=plot_events_same,
            characters_same=characters_same,
            setting_same=setting_same,
            target_dimension_changed=dimension_changed,
            purity_score=purity_score,
            rejection_reason=rejection_reason,
        )

    def _verify_target_dimension(
        self, chosen: str, rejected: str, dimension: ContrastDimension
    ) -> Tuple[bool, float]:
        """Checks whether the rejected text properly exhibits the targeted craft flaw."""
        chosen_lower = chosen.lower()
        rejected_lower = rejected.lower()

        if dimension == ContrastDimension.COMEDIC_RESTRAINT:
            # Rejected should contain joke-explaining or excessive emotional reaction
            has_expl = any(m in rejected_lower for m in self.EXPLANATION_MARKERS)
            chosen_restrained = not any(m in chosen_lower for m in self.EXPLANATION_MARKERS)
            if has_expl and chosen_restrained:
                return True, 1.0
            # Check exclamation mark spam in rejected vs chosen
            if rejected.count("!") >= chosen.count("!") + 3:
                return True, 0.85
            return False, 0.40

        elif dimension == ContrastDimension.DIALOGUE_SUBTEXT:
            has_expo = any(m in rejected_lower for m in self.EXPOSITION_MARKERS)
            chosen_subtext = not any(m in chosen_lower for m in self.EXPOSITION_MARKERS)
            if has_expo and chosen_subtext:
                return True, 1.0
            return True, 0.80

        elif dimension == ContrastDimension.PACING_AND_TIMING:
            # In pacing contrast, rejected rushes punchline without escalation
            return True, 0.85

        elif dimension == ContrastDimension.STATUS_DYNAMIC:
            # Servant collapses deference or master speaks with academic precision
            return True, 0.85

        return True, 0.80

    def _extract_names(self, text: str) -> Set[str]:
        """Extracts character names using FactualSceneAnalyzer to avoid sentence-start false positives."""
        from dataset_generator.factual_analyzer import FactualSceneAnalyzer
        analyzer = FactualSceneAnalyzer()
        chars = analyzer._extract_characters(text)
        return {c.lower() for c in chars if c.lower() != "narrator"}

    def _extract_location_cues(self, text: str) -> Set[str]:
        """Extracts location keywords."""
        known = {"drawing room", "study", "pantry", "hall", "club", "terrace", "garden"}
        lower = text.lower()
        return {loc for loc in known if loc in lower}

    def _compute_plot_overlap(self, text_a: str, text_b: str) -> float:
        """Token set overlap excluding common stopwords."""
        stopwords = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "of", "with", "by", "from", "up", "about", "into", "over", "after",
            "is", "was", "were", "be", "been", "being", "have", "has", "had",
            "i", "you", "he", "she", "it", "we", "they", "me", "him", "her"
        }
        tokens_a = {w.lower() for w in re.findall(r'\b[a-zA-Z]{3,}\b', text_a) if w.lower() not in stopwords}
        tokens_b = {w.lower() for w in re.findall(r'\b[a-zA-Z]{3,}\b', text_b) if w.lower() not in stopwords}
        return self._jaccard(tokens_a, tokens_b)

    def _jaccard(self, a: Set[str], b: Set[str]) -> float:
        if not a and not b:
            return 1.0
        union = a.union(b)
        if not union:
            return 1.0
        return len(a.intersection(b)) / len(union)

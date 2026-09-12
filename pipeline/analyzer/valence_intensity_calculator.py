"""
Valence and Intensity Calculator Module.

Calculates emotional polarity (valence from -1.0 to +1.0) and emotional arousal
(intensity from 0.0 to 1.0) for narrative text blocks.
"""

import re
from typing import Dict, Any, Tuple, Optional
from AI_Author.pipeline.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.ValenceIntensity")


class ValenceIntensityCalculator:
    """Calculates valence (-1.0 to +1.0) and intensity (0.0 to 1.0) for narrative blocks."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes ValenceIntensityCalculator.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.positive_words = set(self.config.get(
            "positive_words",
            ["safe", "shone", "glowing", "breath-taking", "light", "dawn", "triumph", "hope", "warm", "peace"]
        ))
        self.negative_words = set(self.config.get(
            "negative_words",
            ["cold", "dark", "stormy", "shadows", "wolves", "danger", "howled", "fear", "grief", "threat"]
        ))
        self.high_intensity_words = set(self.config.get(
            "high_intensity_words",
            ["howled", "shimmered", "shone", "breath-taking", "colossal", "suddenly", "screamed", "climax"]
        ))

    def calculate_valence(self, text: str) -> Tuple[float, KnowledgeItem]:
        """Calculates emotional polarity score between -1.0 and +1.0."""
        words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        pos_count = sum(1 for w in words if w in self.positive_words)
        neg_count = sum(1 for w in words if w in self.negative_words)

        total = pos_count + neg_count
        if total == 0:
            valence = 0.0
            evidence = sentences[0] if sentences else text[:80]
        else:
            valence = round((pos_count - neg_count) / total, 2)

            # Find sentence with strongest match
            evidence = sentences[0] if sentences else text[:80]
            for s in sentences:
                s_words = set(re.findall(r"\b[a-zA-Z]+\b", s.lower()))
                if s_words.intersection(self.positive_words if valence > 0 else self.negative_words):
                    evidence = s
                    break

        item = KnowledgeItem(
            value=f"Valence: {valence:+.2f}",
            confidence=0.85 if total > 0 else 0.60,
            evidence=evidence,
        )

        return valence, item

    def calculate_intensity(self, text: str) -> Tuple[float, KnowledgeItem]:
        """Calculates emotional arousal intensity score between 0.0 and 1.0."""
        words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        match_count = sum(1 for w in words if w in self.high_intensity_words)
        exclamation_cnt = text.count("!")

        raw_score = (match_count * 0.25) + (exclamation_cnt * 0.2) + 0.4
        intensity = min(1.0, round(raw_score, 2))

        evidence = sentences[0] if sentences else text[:80]
        for s in sentences:
            if any(w in s.lower() for w in self.high_intensity_words) or "!" in s:
                evidence = s
                break

        item = KnowledgeItem(
            value=f"Intensity: {intensity:.2f}",
            confidence=0.85,
            evidence=evidence,
        )

        return intensity, item

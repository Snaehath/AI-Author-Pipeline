"""
Foreshadowing, Plot Twist, Cliffhanger, and Theme Detector Module.

Extracts narrative foreshadowing cues, cliffhangers, and core themes
with confidence scores and supporting text snippets.
"""

import re
from typing import List, Dict, Any, Optional
from AI_Author.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.ForeshadowTwist")


class ForeshadowTwistAnalyzer:
    """Detects foreshadowing, plot twists, cliffhangers, and story themes."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes ForeshadowTwistAnalyzer.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.foreshadow_keywords = self.config.get(
            "foreshadow_keywords",
            ["little did he know", "little did she know", "was yet to come", "premonition", "warning", "ominous", "began to stir"]
        )
        self.cliffhanger_keywords = self.config.get(
            "cliffhanger_keywords",
            ["began to stir", "watched from the dark", "it was too late", "shadows", "silence fell", "waiting"]
        )

    def detect_foreshadowing(self, text: str) -> KnowledgeItem:
        """Identifies foreshadowing or premonition cues in chapter text."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        for kw in self.foreshadow_keywords:
            for sentence in sentences:
                if kw in sentence.lower():
                    return KnowledgeItem(
                        value="Explicit Foreshadowing",
                        confidence=0.90,
                        evidence=sentence,
                    )

        # Fallback implicit check
        return KnowledgeItem(
            value="Implicit / Atmospheric Foreshadowing",
            confidence=0.65,
            evidence=sentences[-1] if sentences else text[:80],
        )

    def detect_cliffhanger(self, chapter_text: str) -> KnowledgeItem:
        """Determines if a chapter ends with a unresolved tension cliffhanger."""
        lines = [l.strip() for l in chapter_text.split("\n") if l.strip()]
        if not lines:
            return KnowledgeItem(value="None", confidence=0.5, evidence="Empty text")

        ending_snippet = " ".join(lines[-2:])

        for kw in self.cliffhanger_keywords:
            if kw in ending_snippet.lower():
                return KnowledgeItem(
                    value="Active Cliffhanger",
                    confidence=0.88,
                    evidence=lines[-1],
                )

        return KnowledgeItem(
            value="Standard Scene Resolution",
            confidence=0.75,
            evidence=lines[-1],
        )

    def extract_themes(self, text: str) -> List[KnowledgeItem]:
        """Extracts core story themes present in text."""
        theme_map = {
            "Discovery": ["map", "artifact", "hidden", "runes", "pedestal", "ancient", "secret"],
            "Survival": ["cold", "wind", "wolves", "danger", "dark", "storm", "nightfall"],
            "Courage & Friendship": ["together", "staff", "hand", "walked", "supported", "trusted"],
        }

        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        themes: List[KnowledgeItem] = []

        for theme_name, keywords in theme_map.items():
            count = 0
            best_sentence = ""
            for kw in keywords:
                for s in sentences:
                    if kw in s.lower():
                        count += 1
                        if not best_sentence:
                            best_sentence = s

            if count > 0:
                themes.append(KnowledgeItem(
                    value=theme_name,
                    confidence=min(0.92, round(0.70 + (count * 0.05), 2)),
                    evidence=best_sentence,
                ))

        if not themes:
            themes.append(KnowledgeItem(
                value="General Adventure",
                confidence=0.65,
                evidence=sentences[0] if sentences else text[:80],
            ))

        return themes

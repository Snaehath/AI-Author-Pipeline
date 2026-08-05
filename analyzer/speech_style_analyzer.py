"""
Speech Style, Humor, Vocabulary, and Length Analyzer Module.

Analyzes linguistic metrics, humor, speech style, vocabulary complexity,
and word count categories for dialogue turns.
"""

import re
from typing import Dict, Any, Optional
from AI_Author.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.SpeechStyle")


class SpeechStyleAnalyzer:
    """Analyzes speech style, humor presence, vocabulary level, and length metrics."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes SpeechStyleAnalyzer.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.humor_keywords = set(self.config.get(
            "humor_keywords",
            ["haha", "laugh", "funny", "joke", "brilliant", "great idea", "oh wonderful", "ironic"]
        ))
        self.high_fantasy_vocab = set(self.config.get(
            "high_fantasy_vocab",
            ["pedestal", "threshold", "runes", "artifact", "obsidian", "chamber", "colossal", "shadows"]
        ))

    def analyze_humor(self, spoken_text: str, speech_tag: str) -> KnowledgeItem:
        """Detects presence of humor or sarcasm in dialogue."""
        combined = f"{spoken_text} {speech_tag}".lower()

        for kw in self.humor_keywords:
            if kw in combined:
                return KnowledgeItem(
                    value="Witty / Sarcastic",
                    confidence=0.85,
                    evidence=f'"{spoken_text}"',
                )

        return KnowledgeItem(
            value="None",
            confidence=0.90,
            evidence=f'"{spoken_text}"',
        )

    def analyze_speech_style(self, spoken_text: str) -> KnowledgeItem:
        """Determines speech style classification."""
        words = spoken_text.split()
        word_cnt = len(words)

        if spoken_text.startswith(("Let's", "We should", "Must", "Don't", "Follow", "Look")):
            value = "Imperative / Advice"
            confidence = 0.88
        elif word_cnt <= 4:
            value = "Short / Punchy"
            confidence = 0.90
        elif "," in spoken_text and word_cnt > 12:
            value = "Formal / Ornate"
            confidence = 0.82
        else:
            value = "Casual / Direct"
            confidence = 0.80

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=f'"{spoken_text}"',
        )

    def analyze_vocabulary(self, spoken_text: str) -> KnowledgeItem:
        """Analyzes vocabulary complexity and genre register."""
        words = set(re.findall(r"\b[a-zA-Z]+\b", spoken_text.lower()))
        matched = words.intersection(self.high_fantasy_vocab)

        if matched:
            return KnowledgeItem(
                value="High Fantasy / Formal",
                confidence=0.88,
                evidence=f"Contains specialized terms: {', '.join(matched)}",
            )

        return KnowledgeItem(
            value="Everyday / Direct",
            confidence=0.90,
            evidence=f'"{spoken_text}"',
        )

    def analyze_dialogue_length(self, spoken_text: str) -> KnowledgeItem:
        """Categorizes dialogue length based on word count."""
        word_cnt = len(spoken_text.split())

        if word_cnt <= 5:
            value = f"Brief ({word_cnt} words)"
        elif word_cnt <= 15:
            value = f"Moderate ({word_cnt} words)"
        else:
            value = f"Extended ({word_cnt} words)"

        return KnowledgeItem(
            value=value,
            confidence=1.0,
            evidence=f"{word_cnt} words",
        )

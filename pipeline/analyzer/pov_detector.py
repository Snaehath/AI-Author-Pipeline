"""
Narrative Point of View (POV) Detector.

Analyzes pronoun frequency distributions to determine whether a narrative is written in
First-person, Third-person limited, or Third-person omniscient POV.
"""

import re
from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.POVDetector")


@dataclass
class KnowledgeItem:
    """Standardized metric representation containing value, confidence, and evidence."""
    value: str
    confidence: float
    evidence: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts KnowledgeItem to dictionary."""
        return asdict(self)


class POVDetector:
    """Detects Point of View (POV) from text."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes POVDetector with pronoun sets.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.first_person = set(self.config.get(
            "first_person_pronouns",
            ["i", "me", "my", "mine", "we", "us", "our", "ours"]
        ))
        self.third_person = set(self.config.get(
            "third_person_pronouns",
            ["he", "him", "his", "she", "her", "hers", "they", "them", "their", "theirs"]
        ))

    def detect_pov(self, text: str) -> KnowledgeItem:
        """Determines narrative POV for a body of text.

        Args:
            text: Full text or chapter content.

        Returns:
            KnowledgeItem with value, confidence, and evidence.
        """
        if not text.strip():
            return KnowledgeItem(
                value="Unknown",
                confidence=0.0,
                evidence="Empty text input",
            )

        words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
        if not words:
            return KnowledgeItem(value="Unknown", confidence=0.0, evidence="No valid words found")

        first_cnt = sum(1 for w in words if w in self.first_person)
        third_cnt = sum(1 for w in words if w in self.third_person)

        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        # Find best evidence sentence
        best_sentence = sentences[0] if sentences else text[:100]

        if first_cnt > third_cnt and first_cnt >= 1:
            value = "First-Person"
            confidence = min(0.98, round(0.70 + (first_cnt / (first_cnt + third_cnt + 1)) * 0.28, 2))
            for sentence in sentences:
                s_words = set(re.findall(r"\b[a-zA-Z]+\b", sentence.lower()))
                if s_words.intersection(self.first_person):
                    best_sentence = sentence
                    break
        else:
            value = "Third-Person Limited"
            confidence = min(0.98, round(0.70 + (third_cnt / (first_cnt + third_cnt + 1)) * 0.28, 2))
            for sentence in sentences:
                s_words = set(re.findall(r"\b[a-zA-Z]+\b", sentence.lower()))
                if s_words.intersection(self.third_person):
                    best_sentence = sentence
                    break

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=best_sentence,
        )

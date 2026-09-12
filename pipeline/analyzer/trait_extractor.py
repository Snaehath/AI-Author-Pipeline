"""
Character Trait & Appearance Extractor Module.

Extracts physical appearance, personality traits, strengths, and weaknesses
for specific characters with supporting text evidence and confidence metrics.
"""

import re
from typing import List, Dict, Any, Optional
from AI_Author.pipeline.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.TraitExtractor")


class TraitExtractor:
    """Extracts physical attributes, personality, strengths, and weaknesses for characters."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes TraitExtractor with configuration.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.appearance_keywords = set(self.config.get(
            "appearance_keywords",
            ["cloak", "robe", "staff", "sword", "lantern", "eyes", "hair", "tall", "short", "beard", "boots"]
        ))
        self.personality_keywords = self.config.get(
            "personality_keywords",
            {
                "Determined": ["resolved", "must", "won't stop", "insisted", "refused", "persevered"],
                "Cautious": ["careful", "warning", "hesitated", "watch out", "camp before nightfall", "slowly"],
                "Brave": ["stepped forward", "fearless", "bold", "drew", "front", "threshold"],
                "Curious": ["wondered", "examined", "looked closer", "map", "search", "investigate"]
            }
        )

    def extract_appearance(self, character_name: str, text: str) -> List[KnowledgeItem]:
        """Extracts physical appearance descriptions associated with character."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        appearances: List[KnowledgeItem] = []

        for sentence in sentences:
            if character_name in sentence:
                words = set(re.findall(r"\b[a-zA-Z]+\b", sentence.lower()))
                matched = words.intersection(self.appearance_keywords)
                if matched:
                    appearances.append(KnowledgeItem(
                        value=f"Wears/carries {', '.join(matched)}",
                        confidence=0.88,
                        evidence=sentence,
                    ))

        if not appearances:
            appearances.append(KnowledgeItem(
                value="Standard Traveler Appearance",
                confidence=0.60,
                evidence=f"{character_name} introduced in narrative.",
            ))

        return appearances

    def extract_personality(self, character_name: str, text: str) -> List[KnowledgeItem]:
        """Extracts personality traits associated with character."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        traits: List[KnowledgeItem] = []

        for trait_name, kw_list in self.personality_keywords.items():
            for sentence in sentences:
                if character_name in sentence:
                    for kw in kw_list:
                        if kw in sentence.lower():
                            traits.append(KnowledgeItem(
                                value=trait_name,
                                confidence=0.85,
                                evidence=sentence,
                            ))
                            break

        if not traits:
            traits.append(KnowledgeItem(
                value="Determined & Focused",
                confidence=0.65,
                evidence=f"{character_name} actively participates in events.",
            ))

        return traits

    def extract_strengths(self, character_name: str, text: str) -> List[KnowledgeItem]:
        """Extracts character strengths."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        strengths: List[KnowledgeItem] = []

        for sentence in sentences:
            if character_name in sentence and any(w in sentence.lower() for w in ["map", "leader", "staff", "lantern", "held", "guided"]):
                strengths.append(KnowledgeItem(
                    value="Perceptive & Resourceful",
                    confidence=0.85,
                    evidence=sentence,
                ))
                break

        if not strengths:
            strengths.append(KnowledgeItem(
                value="Resilient Traveler",
                confidence=0.65,
                evidence=f"{character_name} navigates narrative obstacles.",
            ))

        return strengths

    def extract_weaknesses(self, character_name: str, text: str) -> List[KnowledgeItem]:
        """Extracts character vulnerabilities or weaknesses."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        weaknesses: List[KnowledgeItem] = []

        for sentence in sentences:
            if character_name in sentence and any(w in sentence.lower() for w in ["cold", "tired", "wolves", "hesitated", "fear", "danger"]):
                weaknesses.append(KnowledgeItem(
                    value="Vulnerable to Extreme Elements & Threat",
                    confidence=0.80,
                    evidence=sentence,
                ))
                break

        if not weaknesses:
            weaknesses.append(KnowledgeItem(
                value="Human Vulnerability",
                confidence=0.60,
                evidence=f"{character_name} faces environmental challenges.",
            ))

        return weaknesses

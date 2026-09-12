"""
Goal, Motivation, and Pairwise Relationship Mapper Module.

Extracts character goals, underlying motivations, and pairwise relationships
between characters with confidence scores and narrative evidence.
"""

import itertools
from typing import List, Dict, Any, Optional
from AI_Author.pipeline.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.GoalRelationship")


class GoalRelationshipMapper:
    """Extracts character goals, motivations, and inter-character relationship dynamics."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes GoalRelationshipMapper.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.goal_verbs = self.config.get(
            "goal_verbs",
            ["find", "reach", "search", "protect", "defeat", "escape", "claim", "seek", "make camp"]
        )

    def extract_goals(self, character_name: str, text: str) -> List[KnowledgeItem]:
        """Extracts character goals from narrative text."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        goals: List[KnowledgeItem] = []

        for sentence in sentences:
            if character_name in sentence:
                for verb in self.goal_verbs:
                    if verb in sentence.lower():
                        goals.append(KnowledgeItem(
                            value=f"Goal: {verb.title()} target in narrative",
                            confidence=0.85,
                            evidence=sentence,
                        ))
                        break

        if not goals:
            goals.append(KnowledgeItem(
                value="Advance Story Quest",
                confidence=0.65,
                evidence=f"{character_name} participates in narrative events.",
            ))

        return goals

    def extract_motivations(self, character_name: str, text: str) -> List[KnowledgeItem]:
        """Extracts character motivations."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        motivations: List[KnowledgeItem] = []

        for sentence in sentences:
            if character_name in sentence and any(w in sentence.lower() for w in ["safe", "protect", "kingdom", "secret", "artifact", "survive"]):
                motivations.append(KnowledgeItem(
                    value="Protection & Discovery",
                    confidence=0.82,
                    evidence=sentence,
                ))
                break

        if not motivations:
            motivations.append(KnowledgeItem(
                value="Personal Commitment & Safety",
                confidence=0.60,
                evidence=f"{character_name} responds to plot developments.",
            ))

        return motivations

    def map_relationships(self, character_names: List[str], text: str) -> List[Dict[str, Any]]:
        """Maps pairwise relationships between characters appearing together."""
        relationships: List[Dict[str, Any]] = []
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        for name_a, name_b in itertools.combinations(character_names, 2):
            co_occurring = [s for s in sentences if name_a in s and name_b in s]
            if co_occurring:
                relationships.append({
                    "character_a": name_a,
                    "character_b": name_b,
                    "relationship_type": "Traveling Companions / Allies",
                    "confidence": 0.90,
                    "evidence": co_occurring[0],
                })

        return relationships

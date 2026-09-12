"""
Character Knowledge Isolation.

Maintains what individual characters know, suspect, or are completely ignorant of.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Set, List, Optional


@dataclass
class KnowledgeBase:
    character_id: str
    known_fact_ids: Set[str] = field(default_factory=set)
    suspected_fact_ids: Set[str] = field(default_factory=set)
    false_beliefs: Dict[str, str] = field(default_factory=dict)  # topic -> incorrect assertion

    def knows(self, fact_id: str) -> bool:
        return fact_id in self.known_fact_ids

    def suspects(self, fact_id: str) -> bool:
        return fact_id in self.suspected_fact_ids

    def add_known(self, fact_id: str):
        self.known_fact_ids.add(fact_id)
        self.suspected_fact_ids.discard(fact_id)

    def add_suspected(self, fact_id: str):
        if fact_id not in self.known_fact_ids:
            self.suspected_fact_ids.add(fact_id)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "character_id": self.character_id,
            "known_fact_ids": list(self.known_fact_ids),
            "suspected_fact_ids": list(self.suspected_fact_ids),
            "false_beliefs": self.false_beliefs,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "KnowledgeBase":
        return cls(
            character_id=data["character_id"],
            known_fact_ids=set(data.get("known_fact_ids", [])),
            suspected_fact_ids=set(data.get("suspected_fact_ids", [])),
            false_beliefs=dict(data.get("false_beliefs", {})),
        )


class EpistemicTracker:
    """Manages isolated knowledge boundaries for all characters."""

    def __init__(self):
        self.character_knowledge: Dict[str, KnowledgeBase] = {}

    def get_or_create(self, character_id: str) -> KnowledgeBase:
        if character_id not in self.character_knowledge:
            self.character_knowledge[character_id] = KnowledgeBase(character_id=character_id)
        return self.character_knowledge[character_id]

    def character_knows(self, character_id: str, fact_id: str) -> bool:
        kb = self.character_knowledge.get(character_id)
        return kb.knows(fact_id) if kb else False

    def grant_knowledge(self, character_id: str, fact_id: str):
        kb = self.get_or_create(character_id)
        kb.add_known(fact_id)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v.to_dict() for k, v in self.character_knowledge.items()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EpistemicTracker":
        tracker = cls()
        for k, v in data.items():
            tracker.character_knowledge[k] = KnowledgeBase.from_dict(v)
        return tracker

"""
Reader Knowledge & Dramatic Irony Tracking.
"""

from dataclasses import dataclass, field
from typing import Set, Dict, Any, List


class ReaderKnowledge:
    """Tracks what the reader currently knows, enabling dramatic irony modeling."""

    def __init__(self):
        self.known_facts: Set[str] = field(default_factory=set)
        self.revealed_secrets: List[str] = []

    def reveal_to_reader(self, fact_id: str):
        if fact_id not in self.known_facts:
            self.known_facts.add(fact_id)
            self.revealed_secrets.append(fact_id)

    def reader_knows(self, fact_id: str) -> bool:
        return fact_id in self.known_facts

    def has_dramatic_irony(self, character_knows: bool, fact_id: str) -> bool:
        """True if the reader knows the fact, but the character does not."""
        return self.reader_knows(fact_id) and not character_knows

    def to_dict(self) -> Dict[str, Any]:
        return {
            "known_facts": list(self.known_facts),
            "revealed_secrets": self.revealed_secrets,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ReaderKnowledge":
        rk = cls()
        rk.known_facts = set(data.get("known_facts", []))
        rk.revealed_secrets = list(data.get("revealed_secrets", []))
        return rk

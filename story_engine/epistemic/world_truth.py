"""
Ground Truth Fact Base (World Truth).

Maintains all objective truths of the fictional universe, regardless of who knows them.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List, Optional


@dataclass
class Fact:
    id: str
    proposition: str
    category: str = "general"  # secret, revelation, crime, backstory, relationship
    is_public_knowledge: bool = False
    source_event_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Fact":
        return cls(**data)


class WorldTruthBase:
    """Manages ground-truth facts of the story universe."""

    def __init__(self):
        self.facts: Dict[str, Fact] = {}

    def register_fact(
        self,
        fact_id: str,
        proposition: str,
        category: str = "general",
        is_public: bool = False,
        source_event_id: Optional[str] = None,
    ) -> Fact:
        fact = Fact(
            id=fact_id,
            proposition=proposition,
            category=category,
            is_public_knowledge=is_public,
            source_event_id=source_event_id,
        )
        self.facts[fact_id] = fact
        return fact

    def get_fact(self, fact_id: str) -> Optional[Fact]:
        return self.facts.get(fact_id)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v.to_dict() for k, v in self.facts.items()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WorldTruthBase":
        base = cls()
        for k, v in data.items():
            base.facts[k] = Fact.from_dict(v)
        return base

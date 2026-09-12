"""
Character state definitions.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List, Optional


@dataclass
class Character:
    id: str
    name: str
    role: str = "supporting"  # protagonist, companion, antagonist, supporting
    vitality: str = "alive"  # alive, incapacitated, dead
    location: str = "drawing_room"
    mood: str = "neutral"
    current_goal: str = ""
    inventory: List[str] = field(default_factory=list)
    secrets: List[str] = field(default_factory=list)
    traits: List[str] = field(default_factory=list)

    @property
    def is_alive(self) -> bool:
        return self.vitality == "alive"

    @property
    def is_conscious(self) -> bool:
        return self.vitality == "alive"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Character":
        return cls(**data)

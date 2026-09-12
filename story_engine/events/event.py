"""
Atomic Story Event Definitions.

Events represent discrete, immutable symbolic actions extracted from prose or planned by contracts.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import uuid
import time


class EventType(str, Enum):
    # Spatial Events
    MOVE = "MOVE"
    ENTER = "ENTER"
    EXIT = "EXIT"

    # Possession & Physical Interaction
    PICK_UP = "PICK_UP"
    DROP = "DROP"
    TRANSFER = "TRANSFER"
    USE_OBJECT = "USE_OBJECT"

    # Epistemic & Communication
    SAY = "SAY"
    REVEAL_FACT = "REVEAL_FACT"
    OVERHEAR = "OVERHEAR"
    CONCEAL_FACT = "CONCEAL_FACT"

    # Psychological & Relational
    MODIFY_SENTIMENT = "MODIFY_SENTIMENT"
    CHANGE_MOOD = "CHANGE_MOOD"

    # Plot Thread Lifecycle
    OPEN_THREAD = "OPEN_THREAD"
    ADVANCE_THREAD = "ADVANCE_THREAD"
    RESOLVE_THREAD = "RESOLVE_THREAD"

    # Vitality & Physical State
    INCAPACITATE = "INCAPACITATE"
    REVIVE = "REVIVE"
    KILL = "KILL"


@dataclass(frozen=True)
class StoryEvent:
    """An immutable atomic event record in story narrative time."""
    event_id: str = field(default_factory=lambda: f"evt_{uuid.uuid4().hex[:8]}")
    event_type: EventType = EventType.MOVE
    actor: str = ""
    target: Optional[str] = None
    origin: Optional[str] = None
    destination: Optional[str] = None
    payload: Dict[str, Any] = field(default_factory=dict)
    scene_id: str = "scene_0"
    timestamp: int = field(default_factory=lambda: int(time.time()))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value if isinstance(self.event_type, EventType) else self.event_type,
            "actor": self.actor,
            "target": self.target,
            "origin": self.origin,
            "destination": self.destination,
            "payload": self.payload,
            "scene_id": self.scene_id,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StoryEvent":
        return cls(
            event_id=data.get("event_id", f"evt_{uuid.uuid4().hex[:8]}"),
            event_type=EventType(data["event_type"]),
            actor=data.get("actor", ""),
            target=data.get("target"),
            origin=data.get("origin"),
            destination=data.get("destination"),
            payload=data.get("payload", {}),
            scene_id=data.get("scene_id", "scene_0"),
            timestamp=data.get("timestamp", int(time.time())),
        )

"""
StateDelta and CandidateDiff definitions.

Represents atomic mutations to world state and epistemic state resulting from validated events.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from story_engine.events.event import StoryEvent


@dataclass
class StateDelta:
    """Represents the explicit differential changes applied to a state."""
    location_changes: Dict[str, str] = field(default_factory=dict)  # entity -> new_location
    possession_changes: Dict[str, str] = field(default_factory=dict)  # object -> new_holder (character or location)
    knowledge_additions: Dict[str, List[str]] = field(default_factory=dict)  # character -> [fact_ids]
    sentiment_changes: Dict[str, Dict[str, int]] = field(default_factory=dict)  # (char_a, char_b) -> delta
    mood_changes: Dict[str, str] = field(default_factory=dict)  # character -> new_mood
    vitality_changes: Dict[str, str] = field(default_factory=dict)  # character -> status ("alive", "incapacitated", "dead")
    thread_updates: Dict[str, str] = field(default_factory=dict)  # thread_id -> status ("open", "advanced", "resolved")

    def is_empty(self) -> bool:
        return not (
            self.location_changes
            or self.possession_changes
            or self.knowledge_additions
            or self.sentiment_changes
            or self.mood_changes
            or self.vitality_changes
            or self.thread_updates
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "location_changes": self.location_changes,
            "possession_changes": self.possession_changes,
            "knowledge_additions": self.knowledge_additions,
            "sentiment_changes": self.sentiment_changes,
            "mood_changes": self.mood_changes,
            "vitality_changes": self.vitality_changes,
            "thread_updates": self.thread_updates,
        }


@dataclass
class CandidateDiff:
    """A proposed package of events and state delta extracted from scene prose before verification."""
    scene_id: str
    events: List[StoryEvent] = field(default_factory=list)
    delta: StateDelta = field(default_factory=StateDelta)
    extraction_confidence: float = 1.0
    notes: Optional[str] = None

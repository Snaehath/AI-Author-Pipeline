"""
SceneContract schema.

Defines the contract boundaries, required participants, goals, pre-conditions,
required state changes, and forbidden revelations for a single scene.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional


@dataclass
class SceneContract:
    scene_id: str
    chapter_num: int
    scene_num: int
    pov_character: str
    primary_location: str
    allowed_participants: List[str] = field(default_factory=list)
    allowed_props: List[str] = field(default_factory=list)

    # Contractual Pre-conditions (must hold before scene begins)
    required_preconditions: List[Dict[str, Any]] = field(default_factory=list)

    # Contractual Objectives (must occur during scene)
    required_state_changes: List[Dict[str, Any]] = field(default_factory=list)

    # Contractual Prohibitions (must NOT happen)
    forbidden_revelations: List[str] = field(default_factory=list)
    forbidden_thread_resolutions: List[str] = field(default_factory=list)

    # Narrative Guidance
    target_mood: str = "neutral"
    conflict_type: str = "social"
    target_word_count: int = 750

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SceneContract":
        return cls(**data)

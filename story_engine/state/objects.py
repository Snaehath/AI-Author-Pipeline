"""
Physical Object and Prop registry.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional


@dataclass
class StoryObject:
    id: str
    name: str
    description: str = ""
    holder_type: str = "location"  # "character" or "location" or "container"
    holder_id: str = "drawing_room"  # character_id or location_id or container_object_id
    is_portable: bool = True
    is_hidden: bool = False
    state_desc: str = "intact"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StoryObject":
        return cls(**data)

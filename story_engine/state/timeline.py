"""
Story Timeline and Discrete Narrative Clock.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class StoryClock:
    chapter_num: int = 1
    scene_num: int = 1
    story_tick: int = 0
    in_story_time_desc: str = "Morning, Day 1"

    def advance_scene(self, time_desc: str = "") -> None:
        self.scene_num += 1
        self.story_tick += 1
        if time_desc:
            self.in_story_time_desc = time_desc

    def advance_chapter(self, time_desc: str = "") -> None:
        self.chapter_num += 1
        self.scene_num = 1
        self.story_tick += 1
        if time_desc:
            self.in_story_time_desc = time_desc

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StoryClock":
        return cls(**data)

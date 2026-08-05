"""
Evolving Character State Tracker Module.

Tracks dynamic character states (goals, beliefs, secrets, mood, relationship affinity scores)
that evolve scene-by-scene to maintain deep psychological and narrative continuity.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List, Optional
import json


@dataclass
class DynamicCharacterState:
    """Represents the evolving state of a single character in a specific scene."""
    name: str
    current_goal: str
    beliefs: List[str] = field(default_factory=list)
    secrets: List[str] = field(default_factory=list)
    mood: str = "Determined"
    relationship_scores: Dict[str, int] = field(default_factory=dict)
    open_commitments: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class CharacterStateTracker:
    """Manages the evolving narrative state and object continuity across scenes."""

    def __init__(self):
        self.states: Dict[str, DynamicCharacterState] = {}
        self.object_locations: Dict[str, str] = {
            "Silver Teapot": "In drawing-room, safely returned by Barnaby",
            "Letter from Joan": "In Lord Reginald's jacket pocket",
            "Missing Ruby": "Secured inside Professor Thorne's study case",
        }

    def initialize_default_cast(self):
        """Initializes state for default original cast."""
        self.states = {
            "Lord Reginald": DynamicCharacterState(
                name="Lord Reginald",
                current_goal="Attend Blackwood Manor house party and demonstrate social charm",
                beliefs=["Barnaby is the finest valet in England", "Lady Beatrice admires his intellect"],
                secrets=["Accidentally mislaid the family silver teaset earlier"],
                mood="Optimistic & Over-confident",
                relationship_scores={"Barnaby": 85, "Lady Beatrice": 50, "Inspector Higgins": -20},
                open_commitments=["[✓] Return the silver teapot", "[✗] Apologize to Inspector Higgins"],
            ),
            "Barnaby": DynamicCharacterState(
                name="Barnaby",
                current_goal="Prevent Lord Reginald from causing a social disaster",
                beliefs=["Lord Reginald will inevitably misplace important objects", "Discretion is key"],
                secrets=["Already solved the missing teaset location hours ago"],
                mood="Deadpan & Calm",
                relationship_scores={"Lord Reginald": 90, "Lady Beatrice": 60, "Inspector Higgins": -40},
                open_commitments=["[✓] Prepare afternoon coffee", "[✗] Keep Reggie out of trouble"],
            ),
            "Inspector Higgins": DynamicCharacterState(
                name="Inspector Higgins",
                current_goal="Catch anyone breaking Manor rules or causing disturbance",
                beliefs=["Amateur aristocrats are a nuisance to proper police work"],
                secrets=["Has no actual evidence for his accusations"],
                mood="Suspicious & Pompous",
                relationship_scores={"Lord Reginald": -30, "Barnaby": -20, "Lady Beatrice": 40},
                open_commitments=["[✗] Obtain a search warrant for Blackwood Manor"],
            ),
        }

    def update_state_after_scene(self, scene_summary: str, chapter_num: int):
        """Evolves character goals, moods, and relationships after a completed scene/chapter."""
        if not self.states:
            self.initialize_default_cast()

        if chapter_num == 1:
            self.states["Lord Reginald"].current_goal = "Smooth over afternoon tea misadventures with Lady Beatrice"
            self.states["Lord Reginald"].mood = "Mildly Flustered yet Resolute"
            self.states["Barnaby"].relationship_scores["Lord Reginald"] = 88
        elif chapter_num == 2:
            self.states["Lord Reginald"].current_goal = "Resolve the dinner chaos before Higgins makes an arrest"
            self.states["Barnaby"].current_goal = "Discreetly return the mislaid teaset behind the scenes"
            self.states["Inspector Higgins"].mood = "Furious & Outmaneuvered"
            self.states["Inspector Higgins"].relationship_scores["Lord Reginald"] = -45
        elif chapter_num == 3:
            self.states["Lord Reginald"].current_goal = "Take credit for saving the evening while serving coffee"
            self.states["Barnaby"].current_goal = "Ensure dinner concludes peacefully"
            self.states["Lord Reginald"].mood = "Triumphant"

    def format_state_for_prompt(self) -> str:
        """Formats evolving character states into a clean prompt context string."""
        lines = [
            "==================================================",
            "EVOLVING CHARACTER STATES (DYNAMIC NARRATIVE MEMORY)",
            "==================================================",
        ]
        for name, state in self.states.items():
            rel_str = ", ".join([f"{k}: {v}" for k, v in state.relationship_scores.items()])
            lines.extend([
                f"• {name}:",
                f"  - Active Goal: {state.current_goal}",
                f"  - Mood: {state.mood}",
                f"  - Key Beliefs: {'; '.join(state.beliefs)}",
                f"  - Relationship Affinity Scores: [{rel_str}]",
            ])
        lines.append("==================================================")
        return "\n".join(lines)

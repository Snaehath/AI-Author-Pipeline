"""
Selective Memory Retrieval Module.

Filters and retrieves ONLY scene-relevant character states, object locations, and unresolved commitments
for the specific characters present in the active scene, keeping prompt contexts focused and scalable.
"""

from typing import List, Dict, Any
from AI_Author.inference.state_tracker import CharacterStateTracker


class SelectiveMemoryRetriever:
    """Retrieves targeted memory constraints relevant to the active scene's characters and objects."""

    def __init__(self, state_tracker: CharacterStateTracker):
        self.state_tracker = state_tracker

    def retrieve_scene_context(self, characters_present: List[str]) -> str:
        """Retrieves targeted state memory only for characters present in the scene."""
        lines = [
            "==================================================",
            "TARGETED SCENE MEMORY & OBJECT TRACKER",
            "==================================================",
        ]

        # 1. Retrieve Character States
        for char_name in characters_present:
            state = self.state_tracker.states.get(char_name)
            if state:
                commitments_str = "; ".join(state.open_commitments) if state.open_commitments else "None"
                lines.extend([
                    f"• Character: {state.name} (Mood: {state.mood})",
                    f"  - Active Goal: {state.current_goal}",
                    f"  - Open Commitments: {commitments_str}",
                    f"  - Key Secrets: {'; '.join(state.secrets) if state.secrets else 'None'}",
                ])

        # 2. Retrieve Relevant Object Locations
        lines.append("\nOBJECT CONTINUITY STATUS:")
        for obj, loc in self.state_tracker.object_locations.items():
            lines.append(f"  - {obj}: {loc}")

        lines.append("==================================================")
        return "\n".join(lines)

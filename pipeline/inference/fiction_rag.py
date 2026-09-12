"""
Fiction RAG Selective Memory Engine Module (AI Author Studio v2).

Retrieves ONLY scene-relevant character states, epistemic knowledge, and object locations
for characters and objects present in the active scene blueprint, keeping context prompts clean and scalable.
"""

from typing import List
from AI_Author.pipeline.inference.story_bible_db import StoryBibleDB
from AI_Author.pipeline.inference.blueprint_planner import ChapterBlueprint


class FictionRAGEngine:
    """Retrieves targeted memory constraints for active chapter blueprints."""

    def __init__(self, story_db: StoryBibleDB):
        self.story_db = story_db

    def retrieve_scene_memory(self, blueprint: ChapterBlueprint) -> str:
        """Retrieves targeted scene memory matching the blueprint's present characters and objects."""
        lines = [
            "==================================================",
            "FICTION RAG: TARGETED SCENE MEMORY RETRIEVAL",
            "==================================================",
        ]

        # 1. Retrieve Character States & Epistemic Knowledge
        lines.append("ACTIVE CHARACTERS & KNOWLEDGE STATE:")
        for char_name in blueprint.characters_present:
            state_str = self.story_db.query_character_state(char_name)
            if state_str:
                lines.append(state_str)

        # 2. Retrieve Relevant Object Continuity Locations
        lines.append("\nOBJECT CONTINUITY STATUS:")
        for obj_name in blueprint.objects_introduced:
            loc = self.story_db.object_locations.get(obj_name, "Location unrecorded")
            lines.append(f"  - {obj_name}: {loc}")

        lines.append("==================================================")
        return "\n".join(lines)

"""
Blueprint to Contract Mapper.

Transforms high-level narrative chapter blueprints into formal, typed SceneContracts.
Keeps forbidden facts and prohibitions explicit to preserve epistemic boundaries.
"""

from typing import Optional, List, Dict, Any
from story_engine.contracts.scene import SceneContract
try:
    from AI_Author.inference.blueprint_planner import ChapterBlueprint
except ImportError:
    from inference.blueprint_planner import ChapterBlueprint


class BlueprintContractMapper:
    """Deterministically transforms ChapterBlueprints into formal SceneContracts."""

    @staticmethod
    def map_blueprint_to_contract(
        blueprint: ChapterBlueprint,
        scene_num: int = 1,
        forbidden_facts: Optional[List[str]] = None,
        forbidden_threads: Optional[List[str]] = None,
        explicit_required_changes: Optional[List[Dict[str, Any]]] = None,
    ) -> SceneContract:
        """Converts a ChapterBlueprint into a formal SceneContract.

        Args:
            blueprint: The pre-prose chapter blueprint.
            scene_num: Scene number within the chapter (defaults to 1).
            forbidden_facts: Explicitly prohibited fact IDs from being revealed in this scene.
            forbidden_threads: Explicitly prohibited thread IDs from being closed.
            explicit_required_changes: Specific state changes that must be enacted.

        Returns:
            A strongly typed SceneContract.
        """
        # Determine POV character from blueprint or fallback to protagonist
        pov = getattr(blueprint, "pov_character", "Lord Reginald")
        location = getattr(blueprint, "primary_location", "drawing_room")
        if hasattr(blueprint, "location") and blueprint.location:
            location = blueprint.location

        allowed_participants = list(getattr(blueprint, "characters_present", []))
        allowed_props = list(getattr(blueprint, "objects_introduced", []))

        # Explicit required state changes
        required_changes: List[Dict[str, Any]] = []
        if explicit_required_changes:
            required_changes.extend(explicit_required_changes)
        else:
            # If blueprint introduces an object, designate required pick up if specified
            for prop in allowed_props:
                if "Key" in prop or "Letter" in prop:
                    required_changes.append({
                        "type": "PICK_UP",
                        "actor": pov.lower().replace(" ", "_"),
                        "object": prop.lower().replace(" ", "_"),
                    })

        return SceneContract(
            scene_id=f"ch_{blueprint.chapter_num:02d}_sc_{scene_num:02d}",
            chapter_num=blueprint.chapter_num,
            scene_num=scene_num,
            pov_character=pov.lower().replace(" ", "_"),
            primary_location=location.lower().replace(" ", "_"),
            allowed_participants=[p.lower().replace(" ", "_") for p in allowed_participants],
            allowed_props=[p.lower().replace(" ", "_") for p in allowed_props],
            required_state_changes=required_changes,
            forbidden_revelations=list(forbidden_facts or []),
            forbidden_thread_resolutions=list(forbidden_threads or []),
            target_mood=getattr(blueprint, "emotional_arc", "neutral"),
            conflict_type=getattr(blueprint, "conflict", "social_dispute"),
            target_word_count=getattr(blueprint, "target_word_count", 750),
        )

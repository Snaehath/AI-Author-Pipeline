"""
State Extractor Module.

Parses scene prose into candidate symbolic events and structured StateDeltas.
Uses deterministic regex and keyword pattern rules to ground prose in state mutations.
"""

import re
from typing import List, Dict, Any, Optional
from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import CandidateDiff, StateDelta
from story_engine.contracts.scene import SceneContract
from story_engine.state.world import WorldState


class StateExtractor:
    """Extracts candidate symbolic events from generated scene prose."""

    def __init__(self):
        # Action regex patterns
        self.pickup_patterns = [
            re.compile(r"([A-Z][a-zA-Z\s]+?)\s+(?:picked up|took|lifted|grabbed|retrieved)\s+(?:the\s+)?([a-zA-Z\s]+)", re.I),
            re.compile(r"([A-Z][a-zA-Z\s]+?)\s+(?:slipped|pocketed|tucked)\s+(?:the\s+)?([a-zA-Z\s]+?)\s+into", re.I),
        ]
        self.move_patterns = [
            re.compile(r"([A-Z][a-zA-Z\s]+?)\s+(?:entered|walked into|stepped into|hurried to)\s+(?:the\s+)?([a-zA-Z\s]+)", re.I),
            re.compile(r"([A-Z][a-zA-Z\s]+?)\s+(?:departed for|went to)\s+(?:the\s+)?([a-zA-Z\s]+)", re.I),
        ]

    def extract_from_prose(
        self,
        prose: str,
        contract: SceneContract,
        world: WorldState,
    ) -> CandidateDiff:
        """Extracts candidate events and builds a proposed StateDelta from prose text."""
        events: List[StoryEvent] = []
        delta = StateDelta()

        # Build lookup maps for known entities in world
        char_name_map = {c.name.lower(): c.id for c in world.characters.values()}
        obj_name_map = {o.name.lower(): o.id for o in world.objects.values()}
        loc_name_map = {l.name.lower(): l.id for l in world.location_graph.nodes.values()}

        # 1. Extract Movement Events
        for pat in self.move_patterns:
            for match in pat.finditer(prose):
                raw_actor, raw_loc = match.group(1).strip().lower(), match.group(2).strip().lower()
                actor_id = char_name_map.get(raw_actor)
                if not actor_id and raw_actor in ["he", "she", "they", "the valet", "the master"]:
                    actor_id = contract.pov_character
                loc_id = loc_name_map.get(raw_loc)
                if actor_id and loc_id:
                    origin = delta.location_changes.get(actor_id, world.get_character_location(actor_id))
                    evt = StoryEvent(
                        event_type=EventType.MOVE,
                        actor=actor_id,
                        origin=origin,
                        destination=loc_id,
                        scene_id=contract.scene_id,
                    )
                    events.append(evt)
                    delta.location_changes[actor_id] = loc_id

        # 2. Extract Pick Up / Possession Events
        for pat in self.pickup_patterns:
            for match in pat.finditer(prose):
                raw_actor, raw_obj = match.group(1).strip().lower(), match.group(2).strip().lower()
                actor_id = char_name_map.get(raw_actor)
                if not actor_id and raw_actor in ["he", "she", "they", "the valet", "the master"]:
                    actor_id = contract.pov_character
                obj_id = None
                for name, oid in obj_name_map.items():
                    if name in raw_obj or raw_obj in name:
                        obj_id = oid
                        break
                if actor_id and obj_id:
                    obj = world.objects[obj_id]
                    origin = delta.possession_changes.get(obj_id, obj.holder_id)
                    evt = StoryEvent(
                        event_type=EventType.PICK_UP,
                        actor=actor_id,
                        target=obj_id,
                        origin=origin,
                        scene_id=contract.scene_id,
                    )
                    events.append(evt)
                    delta.possession_changes[obj_id] = actor_id

        # 3. Fulfillment of contract required state changes if confirmed in text
        for req in contract.required_state_changes:
            req_type = req.get("type")
            actor = req.get("actor")
            target_obj = req.get("object")
            if req_type == "PICK_UP" and target_obj and actor:
                # If target object is explicitly mentioned in the prose
                obj = world.objects.get(target_obj)
                if obj and (obj.name.lower() in prose.lower() or obj.id.lower() in prose.lower()):
                    if target_obj not in delta.possession_changes:
                        delta.possession_changes[target_obj] = actor
                        events.append(
                            StoryEvent(
                                event_type=EventType.PICK_UP,
                                actor=actor,
                                target=target_obj,
                                origin=obj.holder_id,
                                scene_id=contract.scene_id,
                            )
                        )

        return CandidateDiff(
            scene_id=contract.scene_id,
            events=events,
            delta=delta,
            extraction_confidence=0.9,
            notes=f"Extracted {len(events)} events from prose."
        )

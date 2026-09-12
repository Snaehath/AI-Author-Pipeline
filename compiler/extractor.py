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
        world_truth: Optional[Any] = None,
    ) -> CandidateDiff:
        """Extracts candidate events and builds a proposed StateDelta from prose text."""
        events: List[StoryEvent] = []
        delta = StateDelta()

        # Build lookup maps for known entities in world
        char_name_map = {}
        for c in world.characters.values():
            char_name_map[c.name.lower()] = c.id
            char_name_map[c.id.lower()] = c.id
            for part in c.name.lower().split():
                if part not in ["the", "a", "an", "sir", "lord", "lady", "inspector"]:
                    char_name_map[part] = c.id
            # Also support full lowercase names
            char_name_map[c.name.lower().replace("lord ", "").replace("lady ", "").replace("inspector ", "")] = c.id

        obj_name_map = {o.name.lower(): o.id for o in world.objects.values()}
        for o in world.objects.values():
            obj_name_map[o.id.lower()] = o.id
        loc_name_map = {l.name.lower(): l.id for l in world.location_graph.nodes.values()}
        for l in world.location_graph.nodes.values():
            loc_name_map[l.id.lower()] = l.id

        # 1. Extract Movement Events (anchored to known locations in world)
        for loc_name, loc_id in loc_name_map.items():
            pat = re.compile(
                rf"\b([A-Za-z\s]+?)\s+(?:entered|walked into|stepped into|hurried to|went to)\s+(?:the\s+)?{re.escape(loc_name)}\b",
                re.IGNORECASE,
            )
            for match in pat.finditer(prose):
                raw_actor = match.group(1).strip().lower()
                # Try full raw actor or last word
                actor_id = char_name_map.get(raw_actor) or char_name_map.get(raw_actor.split()[-1] if raw_actor else "")
                if not actor_id and raw_actor in ["he", "she", "they", "the valet", "the master"]:
                    actor_id = contract.pov_character
                if actor_id:
                    origin = delta.location_changes.get(actor_id, world.get_character_location(actor_id))
                    if origin != loc_id:
                        evt = StoryEvent(
                            event_type=EventType.MOVE,
                            actor=actor_id,
                            origin=origin,
                            destination=loc_id,
                            scene_id=contract.scene_id,
                        )
                        events.append(evt)
                        delta.location_changes[actor_id] = loc_id

        # 2. Extract Pick Up / Possession Events (anchored to known objects in world)
        for obj_name, obj_id in obj_name_map.items():
            pat = re.compile(
                rf"\b([A-Za-z\s]+?)\s+(?:picked up|took|lifted|grabbed|retrieved|pocketed|slipped|held)\s+(?:the\s+)?{re.escape(obj_name)}\b",
                re.IGNORECASE,
            )
            for match in pat.finditer(prose):
                raw_actor = match.group(1).strip().lower()
                actor_id = char_name_map.get(raw_actor) or char_name_map.get(raw_actor.split()[-1] if raw_actor else "")
                if not actor_id and raw_actor in ["he", "she", "they", "the valet", "the master"]:
                    actor_id = contract.pov_character
                if actor_id and obj_id in world.objects:
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

        # 4. Extract Epistemic Fact Revelations / Dialogue Leaks
        if world_truth and hasattr(world_truth, "facts"):
            for fact_id, fact in world_truth.facts.items():
                if fact.proposition.lower() in prose.lower():
                    speaker_id = contract.pov_character
                    for char_name, c_id in char_name_map.items():
                        if re.search(rf"\b{re.escape(char_name)}\b[^.!?\n]*(?:shouted|said|exclaimed|whispered|cried)", prose, re.IGNORECASE) or \
                           re.search(rf"(?:shouted|said|exclaimed)\s+\b{re.escape(char_name)}\b", prose, re.IGNORECASE):
                            speaker_id = c_id
                            break
                    evt = StoryEvent(
                        event_type=EventType.SAY,
                        actor=speaker_id,
                        payload={"fact_id": fact_id, "proposition": fact.proposition},
                        scene_id=contract.scene_id,
                    )
                    events.append(evt)

        return CandidateDiff(
            scene_id=contract.scene_id,
            events=events,
            delta=delta,
            extraction_confidence=0.9,
            notes=f"Extracted {len(events)} events from prose."
        )

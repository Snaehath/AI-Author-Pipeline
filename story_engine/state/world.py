"""
WorldState aggregate model.

Maintains complete snapshot of physical and relational story world at any discrete story tick.
"""

from typing import Dict, Any, List, Optional
import copy
import hashlib
import json

from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.state.locations import LocationGraph
from story_engine.state.relationships import RelationshipMatrix
from story_engine.state.timeline import StoryClock


class WorldState:
    """Represents the complete snapshot of physical and relational truth."""

    def __init__(self):
        self.characters: Dict[str, Character] = {}
        self.objects: Dict[str, StoryObject] = {}
        self.location_graph: LocationGraph = LocationGraph()
        self.relationships: RelationshipMatrix = RelationshipMatrix()
        self.clock: StoryClock = StoryClock()

    def clone(self) -> "WorldState":
        """Creates a deep copy of this state snapshot."""
        return copy.deepcopy(self)

    def apply(self, delta: Any) -> "WorldState":
        """Pure functional state transition: returns a new WorldState with delta applied."""
        new_world = self.clone()

        # Apply Location Changes
        for ent_id, new_loc in getattr(delta, "location_changes", {}).items():
            if ent_id in new_world.characters:
                new_world.characters[ent_id].location = new_loc

        # Apply Possession Changes
        for obj_id, holder_id in getattr(delta, "possession_changes", {}).items():
            if obj_id in new_world.objects:
                obj = new_world.objects[obj_id]
                if holder_id in new_world.characters:
                    obj.holder_type = "character"
                    obj.holder_id = holder_id
                    char = new_world.characters[holder_id]
                    if obj.name not in char.inventory:
                        char.inventory.append(obj.name)
                else:
                    obj.holder_type = "location"
                    obj.holder_id = holder_id

        # Apply Sentiment Changes
        for (src, tgt), aff_delta in getattr(delta, "sentiment_changes", {}).items():
            new_world.relationships.modify_affinity(src, tgt, aff_delta)

        # Apply Mood Changes
        for char_id, mood in getattr(delta, "mood_changes", {}).items():
            if char_id in new_world.characters:
                new_world.characters[char_id].mood = mood

        # Apply Vitality Changes
        for char_id, vit in getattr(delta, "vitality_changes", {}).items():
            if char_id in new_world.characters:
                new_world.characters[char_id].vitality = vit

        # Advance Narrative Clock
        new_world.clock.advance_scene()
        return new_world

    def state_hash(self) -> str:
        """Computes a deterministic SHA256 hash of the complete world state."""
        dumped = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(dumped.encode("utf-8")).hexdigest()[:16]

    def add_character(self, char: Character):
        self.characters[char.id] = char

    def add_object(self, obj: StoryObject):
        self.objects[obj.id] = obj

    def get_character_location(self, char_id: str) -> Optional[str]:
        char = self.characters.get(char_id)
        return char.location if char else None

    def get_object_holder(self, obj_id: str) -> Optional[str]:
        obj = self.objects.get(obj_id)
        return obj.holder_id if obj else None

    def get_characters_at_location(self, loc_id: str) -> List[Character]:
        return [c for c in self.characters.values() if c.location == loc_id]

    def get_objects_at_location(self, loc_id: str) -> List[StoryObject]:
        return [o for o in self.objects.values() if o.holder_id == loc_id and o.holder_type == "location"]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "characters": {k: v.to_dict() for k, v in self.characters.items()},
            "objects": {k: v.to_dict() for k, v in self.objects.items()},
            "locations": self.location_graph.to_dict(),
            "relationships": self.relationships.to_dict(),
            "clock": self.clock.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WorldState":
        world = cls()
        world.characters = {k: Character.from_dict(v) for k, v in data.get("characters", {}).items()}
        world.objects = {k: StoryObject.from_dict(v) for k, v in data.get("objects", {}).items()}
        world.location_graph = LocationGraph.from_dict(data.get("locations", {}))
        world.relationships = RelationshipMatrix.from_dict(data.get("relationships", {}))
        world.clock = StoryClock.from_dict(data.get("clock", {}))
        return world

"""
Spatial Locations and Accessibility Graph.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List, Set, Optional


@dataclass
class LocationNode:
    id: str
    name: str
    description: str = ""
    connected_locations: List[str] = field(default_factory=list)
    is_accessible: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LocationNode":
        return cls(**data)


class LocationGraph:
    """Manages spatial locations and connectivity verification."""

    def __init__(self):
        self.nodes: Dict[str, LocationNode] = {}

    def add_location(self, loc_id: str, name: str, connections: Optional[List[str]] = None, desc: str = "") -> LocationNode:
        connections = connections or []
        node = LocationNode(id=loc_id, name=name, description=desc, connected_locations=list(connections))
        self.nodes[loc_id] = node
        # Ensure bidirectional connections
        for neighbor in connections:
            if neighbor in self.nodes:
                if loc_id not in self.nodes[neighbor].connected_locations:
                    self.nodes[neighbor].connected_locations.append(loc_id)
        return node

    def is_connected(self, from_id: str, to_id: str) -> bool:
        if from_id == to_id:
            return True
        node = self.nodes.get(from_id)
        if not node or not node.is_accessible:
            return False
        dest_node = self.nodes.get(to_id)
        if not dest_node or not dest_node.is_accessible:
            return False
        return to_id in node.connected_locations

    def get_node(self, loc_id: str) -> Optional[LocationNode]:
        return self.nodes.get(loc_id)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v.to_dict() for k, v in self.nodes.items()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LocationGraph":
        graph = cls()
        for k, v in data.items():
            graph.nodes[k] = LocationNode.from_dict(v)
        return graph

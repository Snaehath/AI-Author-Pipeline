"""
Pairwise Character Relationships and Affinity Scores.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Tuple


@dataclass
class RelationshipEdge:
    source_id: str
    target_id: str
    affinity: int = 0  # -100 to +100
    trust: int = 0  # -100 to +100
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RelationshipEdge":
        return cls(**data)


class RelationshipMatrix:
    """Tracks directed relationships between characters."""

    def __init__(self):
        self.edges: Dict[Tuple[str, str], RelationshipEdge] = {}

    def set_relationship(self, source: str, target: str, affinity: int, trust: int = 0, notes: str = ""):
        # Clamp between -100 and 100
        affinity = max(-100, min(100, affinity))
        trust = max(-100, min(100, trust))
        self.edges[(source, target)] = RelationshipEdge(
            source_id=source,
            target_id=target,
            affinity=affinity,
            trust=trust,
            notes=notes,
        )

    def modify_affinity(self, source: str, target: str, delta: int) -> int:
        edge = self.edges.get((source, target))
        if not edge:
            edge = RelationshipEdge(source_id=source, target_id=target)
            self.edges[(source, target)] = edge
        edge.affinity = max(-100, min(100, edge.affinity + delta))
        return edge.affinity

    def get_affinity(self, source: str, target: str) -> int:
        edge = self.edges.get((source, target))
        return edge.affinity if edge else 0

    def to_dict(self) -> Dict[str, Any]:
        return {f"{k[0]}->{k[1]}": v.to_dict() for k, v in self.edges.items()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RelationshipMatrix":
        matrix = cls()
        for k, v in data.items():
            src, tgt = k.split("->")
            matrix.edges[(src, tgt)] = RelationshipEdge.from_dict(v)
        return matrix

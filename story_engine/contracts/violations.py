"""
Narrative Violations and Error AST.

Defines the structured reporting hierarchy for narrative invariant failures.
Pure domain definitions with zero dependencies on compiler.
"""

from __future__ import annotations
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


class Severity(str, Enum):
    FATAL = "FATAL"      # Immediate rejection (impossible physics/paradox)
    ERROR = "ERROR"      # Severe penalty, requires rewrite or fallback
    WARNING = "WARNING"  # Minor drift (e.g., mood variance, stylistic drift)


class ViolationType(str, Enum):
    LOCATION_TELEPORTATION = "LOCATION_TELEPORTATION"
    POSSESSION_CONFLICT = "POSSESSION_CONFLICT"
    EPISTEMIC_LEAK = "EPISTEMIC_LEAK"
    VITALITY_BREACH = "VITALITY_BREACH"
    CAUSALITY_VIOLATION = "CAUSALITY_VIOLATION"
    CONTRACT_BREACH = "CONTRACT_BREACH"


@dataclass
class CompilerViolation:
    invariant_id: str
    violation_type: ViolationType
    severity: Severity
    message: str
    scene_id: str
    offending_event: Optional[Any] = None
    involved_entities: List[str] = field(default_factory=list)
    suggested_repair: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "invariant_id": self.invariant_id,
            "violation_type": self.violation_type.value,
            "severity": self.severity.value,
            "message": self.message,
            "scene_id": self.scene_id,
            "offending_event": self.offending_event.to_dict() if (self.offending_event and hasattr(self.offending_event, "to_dict")) else self.offending_event,
            "involved_entities": self.involved_entities,
            "suggested_repair": self.suggested_repair,
        }

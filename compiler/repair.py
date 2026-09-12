"""
Repair and Penalty Engine.

Calculates violation penalty scores, identifies dominant failure patterns across candidates,
and synthesizes targeted AST-driven prompt instructions for model regeneration.
"""

from typing import List, Dict, Any, Tuple, Optional
from collections import Counter
from compiler.violations import CompilerViolation, Severity, ViolationType
from story_engine.contracts.scene import SceneContract


class RepairEngine:
    """Calculates reward penalties and generates AST-guided targeted repairs."""

    def __init__(self):
        self.penalty_weights = {
            Severity.FATAL: -100.0,
            Severity.ERROR: -35.0,
            Severity.WARNING: -10.0,
        }

    def calculate_penalty_score(self, violations: List[CompilerViolation]) -> float:
        """Computes composite reward penalty from compiler violations."""
        penalty = 0.0
        for v in violations:
            penalty += self.penalty_weights.get(v.severity, -10.0)
        return penalty

    def find_dominant_violation(
        self, candidates_violations: List[List[CompilerViolation]]
    ) -> Tuple[Optional[ViolationType], List[CompilerViolation]]:
        """Identifies the dominant failure pattern across multiple failed candidates."""
        all_violations: List[CompilerViolation] = []
        for viols in candidates_violations:
            all_violations.extend(viols)

        if not all_violations:
            return None, []

        # Tally violation types, prioritizing FATAL over ERROR over WARNING
        weighted_counts: Counter = Counter()
        for v in all_violations:
            weight = 3 if v.severity == Severity.FATAL else (2 if v.severity == Severity.ERROR else 1)
            weighted_counts[v.violation_type] += weight

        dominant_type, _ = weighted_counts.most_common(1)[0]
        matching_violations = [v for v in all_violations if v.violation_type == dominant_type]
        return dominant_type, matching_violations

    def generate_targeted_repair_instruction(
        self,
        dominant_type: Optional[ViolationType],
        violations: List[CompilerViolation],
        contract: Optional[SceneContract] = None,
    ) -> str:
        """Synthesizes a precise semantic directive for targeted LLM regeneration."""
        if not violations or not dominant_type:
            return "Ensure all actions respect physical proximity and scene contract objectives."

        # Extract offending entities
        entities = set()
        for v in violations:
            entities.update(v.involved_entities)
        entity_str = ", ".join(sorted(entities)) if entities else "the characters"

        if dominant_type == ViolationType.EPISTEMIC_LEAK:
            return (
                f"### TARGETED COMPILER REPAIR — EPISTEMIC LEAK:\n"
                f"One or more characters asserted confidential facts ({entity_str}) they cannot legitimately know. "
                f"Preserve the scene's emotional tone and dialogue rhythm, but REMOVE or REPLACE the forbidden knowledge assertion. "
                f"The character must remain unaware of this secret."
            )

        elif dominant_type == ViolationType.LOCATION_TELEPORTATION:
            loc = contract.primary_location if contract else "the designated room"
            return (
                f"### TARGETED COMPILER REPAIR — SPATIAL CONTINUITY:\n"
                f"Characters ({entity_str}) moved between disconnected locations without a valid path. "
                f"Confine all interactions strictly to '{loc}' or describe a plausible physical transit before interacting."
            )

        elif dominant_type == ViolationType.POSSESSION_CONFLICT:
            return (
                f"### TARGETED COMPILER REPAIR — OBJECT POSSESSION:\n"
                f"Conflict over physical props ({entity_str}). An object cannot be picked up if it is already held by someone else "
                f"or located in another room. Include a verbal request or physical handoff before possession changes."
            )

        elif dominant_type == ViolationType.CONTRACT_BREACH:
            req_changes = contract.required_state_changes if contract else []
            req_str = str(req_changes) if req_changes else "mandatory objectives"
            return (
                f"### TARGETED COMPILER REPAIR — CONTRACT OBJECTIVES:\n"
                f"The scene failed to fulfill required objectives: {req_str}. "
                f"Ensure this exact state transition takes place clearly in the prose."
            )

        elif dominant_type == ViolationType.VITALITY_BREACH:
            return (
                f"### TARGETED COMPILER REPAIR — VITALITY ERROR:\n"
                f"An incapacitated or deceased character ({entity_str}) attempted physical actions or speech. "
                f"Ensure they remain passive, unconscious, or absent."
            )

        return (
            f"### TARGETED COMPILER REPAIR:\n"
            f"Fix the following continuity errors:\n"
            + "\n".join([f"- {v.message}" for v in violations[:3]])
        )

    def generate_repair_summary(self, violations: List[CompilerViolation]) -> str:
        """Formats human-readable summary for inspection."""
        if not violations:
            return "No continuity violations detected."

        lines = ["Narrative Invariant Violations Detected:"]
        for idx, v in enumerate(violations, start=1):
            lines.append(f"  {idx}. [{v.severity.value}] {v.invariant_id}: {v.message}")
            if v.suggested_repair:
                lines.append(f"     Suggested Repair: {v.suggested_repair}")
        return "\n".join(lines)

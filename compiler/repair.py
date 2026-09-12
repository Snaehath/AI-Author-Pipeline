"""
Targeted AST Repair and Violation Feedback Engine.

Analyzes narrative compiler violations to identify dominant error patterns
and generates precise, context-aware prompt directives for targeted model revision.
"""

from typing import List, Dict, Any, Optional
from collections import Counter
from story_engine.contracts.violations import CompilerViolation, Severity, ViolationType


class RepairEngine:
    """Calculates violation penalty scores and generates targeted AST repair directives."""

    def __init__(self):
        # Penalty weights against composite story reward for soft warnings
        self.penalty_weights = {
            Severity.FATAL: -100.0,
            Severity.ERROR: -35.0,
            Severity.WARNING: -10.0,
        }

    def calculate_penalty_score(self, violations: List[CompilerViolation]) -> float:
        """Computes total reward penalty from compilation violations."""
        penalty = 0.0
        for v in violations:
            penalty += self.penalty_weights.get(v.severity, -10.0)
        return penalty

    def find_dominant_violation_pattern(self, all_candidate_violations: List[List[CompilerViolation]]) -> Optional[ViolationType]:
        """Identifies the most frequent fatal/error violation type across failed candidates."""
        counter: Counter = Counter()
        for v_list in all_candidate_violations:
            for v in v_list:
                if v.severity in (Severity.FATAL, Severity.ERROR):
                    counter[v.violation_type] += 1

        if counter:
            return counter.most_common(1)[0][0]
        return None

    def generate_targeted_repair_directive(self, violations: List[CompilerViolation]) -> str:
        """Constructs an actionable, specific prompt instruction from violation AST."""
        if not violations:
            return ""

        directives = []
        # Group by violation type
        for v in violations:
            if v.violation_type == ViolationType.EPISTEMIC_LEAK:
                fact_desc = v.message
                directives.append(
                    f"• EPISTEMIC CONSTRAINT: {fact_desc} The POV character CANNOT know or speak of this unrevealed secret. "
                    f"Remove any direct assertions or deductive claims about this secret while preserving dialogue."
                )
            elif v.violation_type == ViolationType.LOCATION_TELEPORTATION:
                directives.append(
                    f"• SPATIAL CONSTRAINT: {v.message} Characters cannot instantly appear in disconnected rooms. "
                    f"Include physical transit through connected hallways or maintain the scene strictly in the designated room."
                )
            elif v.violation_type == ViolationType.POSSESSION_CONFLICT:
                directives.append(
                    f"• POSSESSION CONSTRAINT: {v.message} An object already held or out of reach cannot be taken without "
                    f"an explicit handoff or picking it up from its actual location."
                )
            elif v.violation_type == ViolationType.VITALITY_BREACH:
                directives.append(
                    f"• VITALITY CONSTRAINT: {v.message} Deceased or incapacitated characters cannot speak or act physically."
                )
            elif v.violation_type == ViolationType.CONTRACT_BREACH:
                directives.append(
                    f"• SCENE CONTRACT OBJECTIVE: {v.message} Ensure this required interaction is clearly depicted in the scene."
                )
            else:
                if v.suggested_repair:
                    directives.append(f"• CONTINUITY: {v.suggested_repair}")

        return "\n".join(directives)

    def generate_repair_summary(self, violations: List[CompilerViolation]) -> str:
        """Formats human-readable suggestions for multi-agent revision passes."""
        if not violations:
            return "No continuity violations detected."

        lines = ["Narrative Invariant Violations Detected:"]
        for idx, v in enumerate(violations, start=1):
            lines.append(f"  {idx}. [{v.severity.value}] {v.invariant_id}: {v.message}")
            if v.suggested_repair:
                lines.append(f"     Suggested Repair: {v.suggested_repair}")
        return "\n".join(lines)

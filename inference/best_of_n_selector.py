"""
Compiler-Guided Search & Best-of-N Selection Engine.

Implements a 3-Stage Evaluation Pipeline:
  Gate 1: World / State Invariant Validity (V(c) hard gate)
  Gate 2: Scene Contract Objective Validity (V(c) hard gate)
  Gate 3: Multi-Signal Ranking = Q(c) + λ * E(c) - Warnings Penalty

Enforces strict canonical state immutability until ONE winning candidate is selected.
Outputs structured candidate audit records with full token economics.
"""

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import json
import time

try:
    from AI_Author.evaluator.composite_reward_model import CompositeStoryRewardModel, RewardBreakdown
except ImportError:
    from evaluator.composite_reward_model import CompositeStoryRewardModel, RewardBreakdown

try:
    from AI_Author.utils.logger import setup_logger
except ImportError:
    from utils.logger import setup_logger

from story_engine.state.world import WorldState
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.contracts.scene import SceneContract
from story_engine.contracts.violations import CompilerViolation, Severity, ViolationType
from story_engine.events.event import StoryEvent
from story_engine.events.diff import CandidateDiff, StateDelta
from compiler.continuity import ContinuityCompiler, CompilationResult
from compiler.extractor import StateExtractor
from compiler.repair import RepairEngine

logger = setup_logger("AI_Author.Inference.CompilerGuidedSearch")


@dataclass
class CandidateEvaluation:
    candidate_id: str
    prose: str
    gate: str  # "SURVIVOR", "GATE_1_FAILED", "GATE_2_FAILED"
    is_valid: bool
    candidate_diff: CandidateDiff
    violations: List[CompilerViolation]
    quality_score: float = 0.0
    efficiency_score: float = 0.0
    warnings_penalty: float = 0.0
    final_score: float = -float("inf")
    reward_breakdown: Optional[Dict[str, Any]] = None
    token_cost: Dict[str, Any] = field(default_factory=dict)

    def to_summary_dict(self) -> Dict[str, Any]:
        return {
            "id": self.candidate_id,
            "candidate_id": self.candidate_id,
            "gate": "SURVIVOR" if self.is_valid else "REJECTED",
            "rejection_stage": self.gate if not self.is_valid else None,
            "is_valid": self.is_valid,
            "quality": round(self.quality_score, 4),
            "efficiency": round(self.efficiency_score, 4),
            "warnings": sum(1 for v in self.violations if v.severity == Severity.WARNING),
            "final_score": round(self.final_score, 4) if self.final_score != -float("inf") else -999.0,
            "violations": [
                {
                    "type": v.violation_type.value if hasattr(v.violation_type, "value") else str(v.violation_type),
                    "severity": v.severity.value if hasattr(v.severity, "value") else str(v.severity),
                }
                for v in self.violations
            ],
            "token_cost": self.token_cost,
        }


@dataclass
class SearchSelectionResult:
    selected_candidate_id: str
    selected_prose: str
    selected_delta: Optional[StateDelta]
    selected_events: List[StoryEvent]
    candidates: List[CandidateEvaluation]
    gate_summary: Dict[str, int]
    token_economics: Dict[str, Any]
    scene_id: str = "scene_001"
    repair_attempted: bool = False
    repair_dominant_pattern: Optional[str] = None
    audit_file: Optional[Path] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "scene": self.scene_id,
            "num_candidates": len(self.candidates),
            "gate_summary": self.gate_summary,
            "candidates": [c.to_summary_dict() for c in self.candidates],
            "selected": self.selected_candidate_id,
            "repair": {
                "attempted": self.repair_attempted,
                "dominant_pattern": self.repair_dominant_pattern,
            },
            "token_economics": self.token_economics,
        }


class CompilerGuidedSearch:
    """Orchestrates 3-Stage Compiler-Guided Best-of-N Candidate Selection."""

    def __init__(
        self,
        extractor: Optional[StateExtractor] = None,
        repair_engine: Optional[RepairEngine] = None,
        lambda_efficiency: float = 0.25,
    ):
        self.extractor = extractor or StateExtractor()
        self.repair_engine = repair_engine or RepairEngine()
        self.reward_model = CompositeStoryRewardModel()
        self.lambda_eff = lambda_efficiency

    def compute_state_efficiency(
        self,
        delta: StateDelta,
        events: List[StoryEvent],
        contract: SceneContract,
    ) -> float:
        """Calculates Contract-Relevance State Efficiency E(c).

        E(c) = (1.0 + 2.0 * fulfilled_required + 1.0 * supporting) / (1.0 + 3.0 * irrelevant)
        Normalized to [0.0, 1.0].
        """
        fulfilled_required = 0
        supporting_actions = 0
        irrelevant_mutations = 0

        # Allowed entity sets
        allowed_chars = set(contract.allowed_participants)
        allowed_props = set(contract.allowed_props)
        primary_loc = contract.primary_location

        # Check required changes fulfilled
        for req in contract.required_state_changes:
            req_type = req.get("type")
            target_obj = req.get("object")
            actor = req.get("actor")
            if req_type == "PICK_UP" and target_obj and actor:
                if delta.possession_changes.get(target_obj) == actor:
                    fulfilled_required += 1

        # Check all candidate events for contract relevance
        for evt in events:
            is_contract_relevant = False
            # Check actor relevance
            if evt.actor in allowed_chars or evt.actor == contract.pov_character:
                # Supporting moves: movement to contract location
                if evt.event_type.value == "MOVE" and evt.destination == primary_loc:
                    supporting_actions += 1
                    is_contract_relevant = True
                # Supporting object interaction with allowed props
                elif evt.event_type.value in ["PICK_UP", "DROP", "USE_OBJECT"] and evt.target in allowed_props:
                    supporting_actions += 1
                    is_contract_relevant = True

            if not is_contract_relevant:
                # Irrelevant extraneous mutation
                irrelevant_mutations += 1

        # Check uncontracted location changes
        for char_id, loc in delta.location_changes.items():
            if char_id not in allowed_chars and char_id != contract.pov_character:
                irrelevant_mutations += 1

        # Weighted calculation
        raw_score = (1.0 + 2.0 * fulfilled_required + 1.0 * supporting_actions) / (1.0 + 3.0 * irrelevant_mutations)
        # Normalize into [0.1, 1.0]
        return min(1.0, max(0.1, raw_score / (1.0 + 2.0 * max(1, len(contract.required_state_changes)) + 2.0)))

    def evaluate_candidate(
        self,
        candidate_id: str,
        prose: str,
        contract: SceneContract,
        canonical_world: WorldState,
        epistemic: EpistemicTracker,
        world_truth: WorldTruthBase,
        token_cost: Optional[Dict[str, Any]] = None,
    ) -> CandidateEvaluation:
        """Runs the 3-stage gating and ranking evaluation over a single candidate prose."""
        token_cost = token_cost or {}

        # 1. Extract Candidate Diff
        candidate_diff = self.extractor.extract_from_prose(prose, contract, canonical_world, world_truth=world_truth)

        # 2. Gate 1: World / State Invariant Verification (INV_LOCATION, INV_POSSESSION, INV_EPISTEMIC, INV_VITALITY)
        compiler = ContinuityCompiler()
        comp_res: CompilationResult = compiler.compile_scene(
            current_world=canonical_world,
            epistemic=epistemic,
            world_truth=world_truth,
            contract=contract,
            candidate_diff=candidate_diff,
        )

        # Filter violations by gate
        gate1_violations = [
            v for v in comp_res.violations
            if v.violation_type in [
                ViolationType.LOCATION_TELEPORTATION,
                ViolationType.POSSESSION_CONFLICT,
                ViolationType.EPISTEMIC_LEAK,
                ViolationType.VITALITY_BREACH,
                ViolationType.CAUSALITY_VIOLATION,
            ] and v.severity in (Severity.FATAL, Severity.ERROR)
        ]

        if gate1_violations:
            return CandidateEvaluation(
                candidate_id=candidate_id,
                prose=prose,
                gate="GATE_1_FAILED",
                is_valid=False,
                candidate_diff=candidate_diff,
                violations=comp_res.violations,
                final_score=-float("inf"),
                token_cost=token_cost,
            )

        # 3. Gate 2: Scene Contract Validity (Required objectives & forbidden revelations)
        gate2_violations = [
            v for v in comp_res.violations
            if v.violation_type == ViolationType.CONTRACT_BREACH and v.severity in (Severity.FATAL, Severity.ERROR)
        ]

        if gate2_violations:
            return CandidateEvaluation(
                candidate_id=candidate_id,
                prose=prose,
                gate="GATE_2_FAILED",
                is_valid=False,
                candidate_diff=candidate_diff,
                violations=comp_res.violations,
                final_score=-float("inf"),
                token_cost=token_cost,
            )

        # 4. Gate 3: Narrative Quality & Efficiency Ranking (Only Gate 1 + 2 Survivors!)
        # Q(c): Narrative Quality Score (0.0 to 1.0)
        breakdown = self.reward_model.evaluate_scene(
            prose=prose,
            goal=contract.target_mood,
            characters=contract.allowed_participants,
            objects=contract.allowed_props,
        )
        quality_score = min(1.0, max(0.0, breakdown.composite_reward_score / 10.0))

        # E(c): Contract-Relevance State Efficiency (0.0 to 1.0)
        efficiency_score = self.compute_state_efficiency(
            candidate_diff.delta, candidate_diff.events, contract
        )

        # Warnings penalty
        warnings_count = sum(1 for v in comp_res.violations if v.severity == Severity.WARNING)
        warnings_penalty = warnings_count * 0.05

        # Final Score
        final_score = quality_score + (self.lambda_eff * efficiency_score) - warnings_penalty

        return CandidateEvaluation(
            candidate_id=candidate_id,
            prose=prose,
            gate="SURVIVOR",
            is_valid=True,
            candidate_diff=candidate_diff,
            violations=comp_res.violations,
            quality_score=quality_score,
            efficiency_score=efficiency_score,
            warnings_penalty=warnings_penalty,
            final_score=final_score,
            reward_breakdown=breakdown.to_dict(),
            token_cost=token_cost,
        )

    def search_best_candidate(
        self,
        candidate_prose_list: List[str],
        contract: SceneContract,
        canonical_world: WorldState,
        epistemic: EpistemicTracker,
        world_truth: WorldTruthBase,
        generator_fn: Optional[Any] = None,
        candidate_tokens: Optional[List[Dict[str, Any]]] = None,
        output_audit_dir: Optional[Path] = None,
        story_id: str = "default_story",
    ) -> SearchSelectionResult:
        """Executes Compiler-Guided Search over candidate variations.

        Returns SearchSelectionResult with audit log, keeping canonical_world untouched.
        """
        evaluated_candidates: List[CandidateEvaluation] = []
        candidate_tokens = candidate_tokens or [{} for _ in candidate_prose_list]

        # Evaluate initial pool
        for idx, prose in enumerate(candidate_prose_list, 1):
            cand_id = f"candidate_{idx:03d}"
            t_cost = candidate_tokens[idx - 1] if idx - 1 < len(candidate_tokens) else {}
            evaluation = self.evaluate_candidate(
                candidate_id=cand_id,
                prose=prose,
                contract=contract,
                canonical_world=canonical_world,
                epistemic=epistemic,
                world_truth=world_truth,
                token_cost=t_cost,
            )
            evaluated_candidates.append(evaluation)

        # Gate summary counts
        g1_fails = sum(1 for c in evaluated_candidates if c.gate == "GATE_1_FAILED")
        g2_fails = sum(1 for c in evaluated_candidates if c.gate == "GATE_2_FAILED")
        survivors = [c for c in evaluated_candidates if c.gate == "SURVIVOR"]

        repair_attempted = False
        dominant_pattern = None

        # If zero valid candidates survive, trigger Dominant Pattern Targeted Repair
        if not survivors and generator_fn is not None:
            repair_attempted = True
            all_violations = [c.violations for c in evaluated_candidates]
            dominant_pattern = self.repair_engine.find_dominant_violation_pattern(all_violations)

            # Pick the candidate with fewest fatal violations as repair base
            best_failing = min(evaluated_candidates, key=lambda c: len(c.violations))
            repair_directive = self.repair_engine.generate_targeted_repair_directive(best_failing.violations)

            repair_prompt = (
                f"Rewrite this scene resolving the following continuity violations:\n"
                f"{repair_directive}\n\n"
                f"Original Scene Draft:\n{best_failing.prose}"
            )

            t0 = time.time()
            repaired_prose = generator_fn(repair_prompt)
            gen_time = int((time.time() - t0) * 1000)

            rep_id = f"candidate_repaired_{len(evaluated_candidates)+1:03d}"
            rep_cost = {
                "prompt_tokens": len(repair_prompt.split()) * 1.3,
                "completion_tokens": len(repaired_prose.split()) * 1.3,
                "total_tokens": (len(repair_prompt.split()) + len(repaired_prose.split())) * 1.3,
                "generation_time_ms": gen_time,
            }

            repaired_eval = self.evaluate_candidate(
                candidate_id=rep_id,
                prose=repaired_prose,
                contract=contract,
                canonical_world=canonical_world,
                epistemic=epistemic,
                world_truth=world_truth,
                token_cost=rep_cost,
            )
            evaluated_candidates.append(repaired_eval)
            if repaired_eval.gate == "SURVIVOR":
                survivors.append(repaired_eval)

        # Re-compute gate summary
        state_valid = sum(1 for c in evaluated_candidates if c.gate != "GATE_1_FAILED")
        contract_valid = sum(1 for c in evaluated_candidates if c.gate == "SURVIVOR")
        fatal_rejected = sum(1 for c in evaluated_candidates if c.gate in ("GATE_1_FAILED", "GATE_2_FAILED"))

        gate_summary = {
            "total_candidates": len(evaluated_candidates),
            "state_valid": state_valid,
            "contract_valid": contract_valid,
            "fatal_rejected": fatal_rejected,
            "gate_1_failed": sum(1 for c in evaluated_candidates if c.gate == "GATE_1_FAILED"),
            "gate_2_failed": sum(1 for c in evaluated_candidates if c.gate == "GATE_2_FAILED"),
            "survivors": len(survivors),
        }

        # Select winner with deterministic tie-breaking
        if survivors:
            # Sort by: (-final_score, -quality_score, -efficiency_score, candidate_id)
            survivors.sort(key=lambda c: (-c.final_score, -c.quality_score, -c.efficiency_score, c.candidate_id))
            winner = survivors[0]
        else:
            # Fallback if even repair failed: choose candidate with least violations
            evaluated_candidates.sort(key=lambda c: (len(c.violations), c.candidate_id))
            winner = evaluated_candidates[0]

        # Aggregate token economics
        def _to_int(val: Any) -> int:
            try:
                return int(val)
            except (ValueError, TypeError):
                return 0

        total_p_tok = sum(_to_int(c.token_cost.get("prompt_tokens", 0)) for c in evaluated_candidates)
        total_c_tok = sum(_to_int(c.token_cost.get("completion_tokens", 0)) for c in evaluated_candidates)
        total_time_ms = sum(_to_int(c.token_cost.get("generation_time_ms", 0)) for c in evaluated_candidates)

        token_economics = {
            "prompt_tokens": total_p_tok,
            "completion_tokens": total_c_tok,
            "total_tokens": total_p_tok + total_c_tok,
            "generation_time_ms": total_time_ms,
            "repair_tokens": _to_int(evaluated_candidates[-1].token_cost.get("total_tokens", 0)) if repair_attempted else 0,
        }

        result = SearchSelectionResult(
            selected_candidate_id=winner.candidate_id,
            selected_prose=winner.prose,
            selected_delta=winner.candidate_diff.delta if winner.is_valid else None,
            selected_events=winner.candidate_diff.events if winner.is_valid else [],
            candidates=evaluated_candidates,
            gate_summary=gate_summary,
            token_economics=token_economics,
            scene_id=contract.scene_id,
            repair_attempted=repair_attempted,
            repair_dominant_pattern=dominant_pattern.value if dominant_pattern else None,
        )

        # Persist Candidate Audit Directory if path provided
        if output_audit_dir:
            audit_dir = Path(output_audit_dir)
            audit_dir.mkdir(parents=True, exist_ok=True)

            for cand in evaluated_candidates:
                c_dir = audit_dir / cand.candidate_id
                c_dir.mkdir(parents=True, exist_ok=True)
                (c_dir / "prose.md").write_text(cand.prose, encoding="utf-8")
                (c_dir / "candidate_diff.json").write_text(
                    json.dumps({"events": [e.to_dict() for e in cand.candidate_diff.events], "delta": cand.candidate_diff.delta.to_dict()}, indent=2),
                    encoding="utf-8",
                )
                (c_dir / "score.json").write_text(
                    json.dumps(cand.to_summary_dict(), indent=2),
                    encoding="utf-8",
                )

            audit_file = audit_dir / "selection_audit.json"
            audit_file.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")
            result.audit_file = audit_file

        logger.info(
            f"Compiler-Guided Search completed for '{contract.scene_id}': "
            f"{gate_summary['survivors']}/{gate_summary['total_candidates']} survived. "
            f"Winner: '{result.selected_candidate_id}'"
        )
        return result


# Compatibility alias for legacy code
BestOfNCandidateSelector = CompilerGuidedSearch

"""
Stateful Scene Compiler Module.

Orchestrates the pure, immutable state-transition lifecycle for a single scene:
    State_n + SceneContract + CandidateEvents -> State_n+1

Guarantees that prose is merely a proposal for a state transition:
invalid transitions are rejected with zero effect on canonical state.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

from story_engine.state.world import WorldState
from story_engine.state.checkpoints import StoryCheckpointManager
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.contracts.scene import SceneContract
from story_engine.contracts.violations import CompilerViolation, Severity
from story_engine.context.budgeter import ContextBudgeter
from story_engine.events.event import StoryEvent
from story_engine.events.diff import CandidateDiff, StateDelta
from story_engine.events.ledger import EventLedger
from compiler.continuity import ContinuityCompiler, CompilationResult
from compiler.extractor import StateExtractor
from compiler.repair import RepairEngine
try:
    from AI_Author.utils.logger import setup_logger
except ImportError:
    from utils.logger import setup_logger

logger = setup_logger("AI_Author.StoryEngine.SceneCompiler")


@dataclass
class SceneCompilationResult:
    """Explicitly transactional result of a scene compilation."""
    status: str  # "COMMITTED" or "REJECTED"
    prose: str
    candidate_delta: StateDelta
    validated_delta: Optional[StateDelta]
    violations: List[CompilerViolation]
    repair_attempts: int
    previous_state_hash: str
    new_state_hash: str
    committed_events: List[StoryEvent] = field(default_factory=list)
    resulting_world_state: Optional[WorldState] = None
    resulting_epistemic: Optional[EpistemicTracker] = None
    checkpoint_dir: Optional[Path] = None

    @property
    def is_committed(self) -> bool:
        return self.status == "COMMITTED"


class StatefulSceneCompiler:
    """Manages the transactional compilation and execution of a narrative scene."""

    def __init__(
        self,
        ledger: Optional[EventLedger] = None,
        checkpoint_manager: Optional[StoryCheckpointManager] = None,
        context_budgeter: Optional[ContextBudgeter] = None,
        extractor: Optional[StateExtractor] = None,
        repair_engine: Optional[RepairEngine] = None,
    ):
        self.ledger = ledger or EventLedger()
        self.checkpoint_manager = checkpoint_manager
        self.budgeter = context_budgeter or ContextBudgeter()
        self.extractor = extractor or StateExtractor()
        self.repair_engine = repair_engine or RepairEngine()
        self.continuity_compiler = ContinuityCompiler(ledger=self.ledger)

    def compile_scene_candidate(
        self,
        prose: str,
        contract: SceneContract,
        canonical_world: WorldState,
        epistemic: EpistemicTracker,
        world_truth: WorldTruthBase,
        story_id: str = "default_story",
        parent_checkpoint_id: Optional[str] = None,
    ) -> SceneCompilationResult:
        """Compiles generated prose proposal against canonical state.

        Does NOT modify canonical_world in place. Returns a transactional result.
        """
        before_hash = canonical_world.state_hash()
        ledger_count_before = len(self.ledger)

        # 1. Extract Candidate Events & State Delta from prose proposal
        candidate_diff = self.extractor.extract_from_prose(prose, contract, canonical_world, world_truth=world_truth)

        # 2. Evaluate Invariants over candidate proposal
        comp_res: CompilationResult = self.continuity_compiler.compile_scene(
            current_world=canonical_world,
            epistemic=epistemic,
            world_truth=world_truth,
            contract=contract,
            candidate_diff=candidate_diff,
        )

        # 3. Hard-gating: If invalid, abort without mutating canonical state
        if not comp_res.is_valid or comp_res.has_fatal():
            logger.warning(
                f"Scene '{contract.scene_id}' REJECTED: {comp_res.fatal_count} fatal, "
                f"{comp_res.error_count} errors. Canonical state untouched."
            )
            return SceneCompilationResult(
                status="REJECTED",
                prose=prose,
                candidate_delta=candidate_diff.delta,
                validated_delta=None,
                violations=comp_res.violations,
                repair_attempts=0,
                previous_state_hash=before_hash,
                new_state_hash=before_hash,  # MUST equal previous_state_hash
                committed_events=[],
                resulting_world_state=canonical_world,
                resulting_epistemic=epistemic,
                checkpoint_dir=None,
            )

        # 4. Success: Apply validated delta to produce a brand-new WorldState snapshot
        validated_delta = candidate_diff.delta
        new_world = canonical_world.apply(validated_delta)

        # Update Epistemic state copy
        new_epistemic = epistemic  # Already updated inside ContinuityCompiler
        new_hash = new_world.state_hash()

        # 5. Save atomic checkpoint if manager configured
        checkpoint_dir: Optional[Path] = None
        if self.checkpoint_manager:
            checkpoint_dir = self.checkpoint_manager.save_checkpoint(
                story_id=story_id,
                chapter_num=contract.chapter_num,
                scene_num=contract.scene_num,
                contract=contract,
                candidate_diff=candidate_diff,
                validated_delta=validated_delta,
                world_state=new_world,
                epistemic=new_epistemic,
                events=candidate_diff.events,
                prose=prose,
                parent_checkpoint_id=parent_checkpoint_id,
            )

        logger.info(f"Scene '{contract.scene_id}' COMMITTED: State transition {before_hash} -> {new_hash}")

        return SceneCompilationResult(
            status="COMMITTED",
            prose=prose,
            candidate_delta=candidate_diff.delta,
            validated_delta=validated_delta,
            violations=comp_res.violations,
            repair_attempts=0,
            previous_state_hash=before_hash,
            new_state_hash=new_hash,
            committed_events=candidate_diff.events,
            resulting_world_state=new_world,
            resulting_epistemic=new_epistemic,
            checkpoint_dir=checkpoint_dir,
        )

    def execute_and_compile(
        self,
        contract: SceneContract,
        canonical_world: WorldState,
        epistemic: EpistemicTracker,
        world_truth: WorldTruthBase,
        generator_fn: Any,
        story_id: str = "default_story",
        parent_checkpoint_id: Optional[str] = None,
        max_repairs: int = 1,
    ) -> SceneCompilationResult:
        """Full end-to-end loop: Context Budgeting -> LLM Draft -> Compile -> (Optional Repair) -> Commit."""
        # Step 1: Pack strictly POV-isolated prompt context
        context_pack = self.budgeter.build_scene_prompt_context(
            contract=contract,
            world=canonical_world,
            epistemic=epistemic,
            world_truth=world_truth,
        )
        prompt = context_pack["prompt_context"]

        # Step 2: Generate draft prose
        prose = generator_fn(prompt)

        # Step 3: First compilation attempt
        result = self.compile_scene_candidate(
            prose=prose,
            contract=contract,
            canonical_world=canonical_world,
            epistemic=epistemic,
            world_truth=world_truth,
            story_id=story_id,
            parent_checkpoint_id=parent_checkpoint_id,
        )

        # Step 4: If rejected and repairs allowed, attempt targeted rewrite
        repairs_done = 0
        while not result.is_committed and repairs_done < max_repairs:
            repairs_done += 1
            repair_summary = self.repair_engine.generate_repair_summary(result.violations)
            repair_prompt = f"{prompt}\n\n### MANDATORY CONTINUITY FIXES:\n{repair_summary}\n\nRewrite scene avoiding these errors:"
            prose = generator_fn(repair_prompt)
            result = self.compile_scene_candidate(
                prose=prose,
                contract=contract,
                canonical_world=canonical_world,
                epistemic=epistemic,
                world_truth=world_truth,
                story_id=story_id,
                parent_checkpoint_id=parent_checkpoint_id,
            )
            result.repair_attempts = repairs_done

        return result

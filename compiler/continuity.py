"""
Continuity Compiler Module.

Executes narrative invariant checks over CandidateDiffs against WorldState and EpistemicState.
Produces structured StateTransitions and commits sound diffs to the EventLedger.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Dict, Any

from story_engine.state.world import WorldState
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.contracts.scene import SceneContract
from story_engine.contracts.invariants import NarrativeInvariants
from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import CandidateDiff, StateDelta
from story_engine.events.ledger import EventLedger
from compiler.violations import CompilerViolation, Severity


@dataclass
class CompilationResult:
    is_valid: bool
    violations: List[CompilerViolation]
    fatal_count: int
    error_count: int
    warning_count: int
    resulting_world_state: Optional[WorldState] = None
    previous_state_hash: str = ""
    resulting_state_hash: str = ""

    def has_fatal(self) -> bool:
        return self.fatal_count > 0


class ContinuityCompiler:
    """Symbolic narrative compiler enforcing consistency and invariants."""

    def __init__(self, ledger: Optional[EventLedger] = None):
        self.ledger = ledger or EventLedger()

    def compile_scene(
        self,
        current_world: WorldState,
        epistemic: EpistemicTracker,
        world_truth: WorldTruthBase,
        contract: SceneContract,
        candidate_diff: CandidateDiff,
    ) -> CompilationResult:
        """Verifies candidate events against invariants and produces state transitions."""
        violations: List[CompilerViolation] = []
        prev_hash = current_world.state_hash()

        # 1. Evaluate per-event invariants against sequential simulated state
        simulated_world = current_world.clone()
        for event in candidate_diff.events:
            # Spatial Invariant
            loc_viol = NarrativeInvariants.check_location_invariant(simulated_world, event)
            if loc_viol:
                violations.append(loc_viol)

            # Possession Invariant
            pos_viol = NarrativeInvariants.check_possession_invariant(simulated_world, event)
            if pos_viol:
                violations.append(pos_viol)

            # Epistemic Invariant
            epi_viol = NarrativeInvariants.check_epistemic_invariant(
                simulated_world, epistemic, world_truth, event
            )
            if epi_viol:
                violations.append(epi_viol)

            # Vitality Invariant
            vit_viol = NarrativeInvariants.check_vitality_invariant(simulated_world, event)
            if vit_viol:
                violations.append(vit_viol)

            # Advance simulated world so subsequent events within this scene perceive prior actions
            if event.event_type == EventType.MOVE and event.destination and event.actor:
                if event.actor in simulated_world.characters:
                    simulated_world.characters[event.actor].location = event.destination
            elif event.event_type == EventType.PICK_UP and event.target and event.actor:
                if event.target in simulated_world.objects:
                    obj = simulated_world.objects[event.target]
                    obj.holder_type = "character"
                    obj.holder_id = event.actor

        # 2. Evaluate Scene Contract Invariants
        contract_viols = NarrativeInvariants.check_contract_invariants(
            contract, candidate_diff.delta, candidate_diff.events
        )
        violations.extend(contract_viols)

        # 3. Classify violation severity counts
        fatal_count = sum(1 for v in violations if v.severity == Severity.FATAL)
        error_count = sum(1 for v in violations if v.severity == Severity.ERROR)
        warning_count = sum(1 for v in violations if v.severity == Severity.WARNING)

        is_valid = (fatal_count == 0 and error_count == 0)

        # 4. If sound, apply mutations to create next WorldState
        new_world: Optional[WorldState] = None
        new_hash = prev_hash

        if is_valid:
            new_world = current_world.clone()
            delta = candidate_diff.delta

            # Apply Location Changes
            for ent_id, new_loc in delta.location_changes.items():
                if ent_id in new_world.characters:
                    new_world.characters[ent_id].location = new_loc

            # Apply Possession Changes
            for obj_id, holder_id in delta.possession_changes.items():
                if obj_id in new_world.objects:
                    obj = new_world.objects[obj_id]
                    if holder_id in new_world.characters:
                        obj.holder_type = "character"
                        obj.holder_id = holder_id
                        # Add to character inventory if not present
                        char = new_world.characters[holder_id]
                        if obj.name not in char.inventory:
                            char.inventory.append(obj.name)
                    else:
                        obj.holder_type = "location"
                        obj.holder_id = holder_id

            # Apply Knowledge Additions
            for char_id, fact_ids in delta.knowledge_additions.items():
                for fid in fact_ids:
                    epistemic.grant_knowledge(char_id, fid)

            # Apply Sentiment Changes
            for (src, tgt), aff_delta in delta.sentiment_changes.items():
                new_world.relationships.modify_affinity(src, tgt, aff_delta)

            # Apply Mood Changes
            for char_id, mood in delta.mood_changes.items():
                if char_id in new_world.characters:
                    new_world.characters[char_id].mood = mood

            # Apply Vitality Changes
            for char_id, vit in delta.vitality_changes.items():
                if char_id in new_world.characters:
                    new_world.characters[char_id].vitality = vit

            # Advance narrative clock
            new_world.clock.advance_scene()
            new_hash = new_world.state_hash()

            # Commit sound transition to EventLedger
            self.ledger.append(
                scene_id=contract.scene_id,
                events=candidate_diff.events,
                delta=candidate_diff.delta,
                prev_hash=prev_hash,
                new_hash=new_hash,
            )

        return CompilationResult(
            is_valid=is_valid,
            violations=violations,
            fatal_count=fatal_count,
            error_count=error_count,
            warning_count=warning_count,
            resulting_world_state=new_world,
            previous_state_hash=prev_hash,
            resulting_state_hash=new_hash,
        )

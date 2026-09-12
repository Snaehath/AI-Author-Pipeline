"""
Narrative Invariants (Narrative Type System).

Pure mathematical predicates verifying candidate events against WorldState, EpistemicState,
and SceneContracts to guarantee logical, spatial, and narrative soundness.
"""

from typing import List, Optional, Tuple
from story_engine.state.world import WorldState
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.contracts.scene import SceneContract
from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import StateDelta
from story_engine.contracts.violations import CompilerViolation, Severity, ViolationType


class NarrativeInvariants:
    """Evaluates narrative invariants over candidate events and state deltas."""

    @staticmethod
    def check_location_invariant(
        world: WorldState,
        event: StoryEvent,
    ) -> Optional[CompilerViolation]:
        """INV_LOCATION: Verifies spatial connectivity and teleportation prevention."""
        actor = world.characters.get(event.actor)
        if not actor:
            return None

        # 1. Action co-location: Physical actions require being present at the origin/scene location
        if event.event_type in [EventType.PICK_UP, EventType.DROP, EventType.USE_OBJECT]:
            if event.origin and actor.location != event.origin:
                return CompilerViolation(
                    invariant_id="INV_LOCATION_COLOCATION",
                    violation_type=ViolationType.LOCATION_TELEPORTATION,
                    severity=Severity.FATAL,
                    message=f"Actor '{actor.name}' tried to interact at '{event.origin}', but is currently in '{actor.location}'.",
                    scene_id=event.scene_id,
                    offending_event=event,
                    involved_entities=[actor.id, event.origin],
                    suggested_repair=f"Move '{actor.name}' to '{event.origin}' first.",
                )

        # 2. Movement connectivity
        if event.event_type == EventType.MOVE:
            dest = event.destination
            if not dest:
                return None
            if not world.location_graph.is_connected(actor.location, dest):
                return CompilerViolation(
                    invariant_id="INV_LOCATION_CONNECTIVITY",
                    violation_type=ViolationType.LOCATION_TELEPORTATION,
                    severity=Severity.ERROR,
                    message=f"Actor '{actor.name}' teleported from '{actor.location}' to '{dest}' without an accessible connection.",
                    scene_id=event.scene_id,
                    offending_event=event,
                    involved_entities=[actor.id, actor.location, dest],
                    suggested_repair=f"Add transitional movement or connect '{actor.location}' to '{dest}'.",
                )

        return None

    @staticmethod
    def check_possession_invariant(
        world: WorldState,
        event: StoryEvent,
    ) -> Optional[CompilerViolation]:
        """INV_POSSESSION: Verifies object existence, single ownership, and interaction range."""
        if event.event_type == EventType.PICK_UP:
            obj_id = event.target
            obj = world.objects.get(obj_id) if obj_id else None
            actor = world.characters.get(event.actor)

            if not obj or not actor:
                return None

            # Check if object is already held by someone else
            if obj.holder_type == "character" and obj.holder_id != actor.id:
                other_holder = world.characters.get(obj.holder_id)
                other_name = other_holder.name if other_holder else obj.holder_id
                return CompilerViolation(
                    invariant_id="INV_POSSESSION_EXCLUSIVE",
                    violation_type=ViolationType.POSSESSION_CONFLICT,
                    severity=Severity.FATAL,
                    message=f"Actor '{actor.name}' cannot pick up '{obj.name}' because it is currently possessed by '{other_name}'.",
                    scene_id=event.scene_id,
                    offending_event=event,
                    involved_entities=[actor.id, obj.id, obj.holder_id],
                    suggested_repair=f"Transfer '{obj.name}' from '{other_name}' to '{actor.name}' via TRANSFER event.",
                )

            # Check if actor is in the same location as the object
            if obj.holder_type == "location" and actor.location != obj.holder_id:
                return CompilerViolation(
                    invariant_id="INV_POSSESSION_PROXIMITY",
                    violation_type=ViolationType.POSSESSION_CONFLICT,
                    severity=Severity.ERROR,
                    message=f"Actor '{actor.name}' (in '{actor.location}') is not co-located with '{obj.name}' (in '{obj.holder_id}').",
                    scene_id=event.scene_id,
                    offending_event=event,
                    involved_entities=[actor.id, obj.id, actor.location, obj.holder_id],
                    suggested_repair=f"Move '{actor.name}' to '{obj.holder_id}' before picking up.",
                )

        return None

    @staticmethod
    def check_epistemic_invariant(
        world: WorldState,
        epistemic: EpistemicTracker,
        world_truth: WorldTruthBase,
        event: StoryEvent,
    ) -> Optional[CompilerViolation]:
        """INV_EPISTEMIC: Prevents characters from asserting or using secrets they do not know."""
        if event.event_type in [EventType.SAY, EventType.REVEAL_FACT]:
            fact_id = event.payload.get("fact_id")
            if not fact_id:
                return None

            fact = world_truth.get_fact(fact_id)
            if fact and not fact.is_public_knowledge:
                if not epistemic.character_knows(event.actor, fact_id):
                    actor = world.characters.get(event.actor)
                    actor_name = actor.name if actor else event.actor
                    return CompilerViolation(
                        invariant_id="INV_EPISTEMIC_LEAK",
                        violation_type=ViolationType.EPISTEMIC_LEAK,
                        severity=Severity.FATAL,
                        message=f"Epistemic leak: '{actor_name}' asserted secret fact '{fact.proposition}' ({fact_id}) without knowing it.",
                        scene_id=event.scene_id,
                        offending_event=event,
                        involved_entities=[event.actor, fact_id],
                        suggested_repair=f"Introduce revelation event prior to scene, or remove assertion.",
                    )
        return None

    @staticmethod
    def check_vitality_invariant(
        world: WorldState,
        event: StoryEvent,
    ) -> Optional[CompilerViolation]:
        """INV_VITALITY: Dead or incapacitated characters cannot perform physical actions or dialogue."""
        actor = world.characters.get(event.actor)
        if not actor:
            return None

        if not actor.is_alive and event.event_type not in [EventType.REVIVE]:
            return CompilerViolation(
                invariant_id="INV_VITALITY_DEAD_ACTION",
                violation_type=ViolationType.VITALITY_BREACH,
                severity=Severity.FATAL,
                message=f"Dead character '{actor.name}' attempted action '{event.event_type.value}'.",
                scene_id=event.scene_id,
                offending_event=event,
                involved_entities=[actor.id],
                suggested_repair=f"Replace actor with living character or revive '{actor.name}'.",
            )
        return None

    @staticmethod
    def check_contract_invariants(
        contract: SceneContract,
        delta: StateDelta,
        events: List[StoryEvent],
    ) -> List[CompilerViolation]:
        """INV_CONTRACT: Verifies compliance with scene contract objectives and prohibitions."""
        violations: List[CompilerViolation] = []

        # 1. Check forbidden revelations
        for event in events:
            if event.event_type in [EventType.SAY, EventType.REVEAL_FACT]:
                fact_id = event.payload.get("fact_id")
                if fact_id and fact_id in contract.forbidden_revelations:
                    violations.append(
                        CompilerViolation(
                            invariant_id="INV_CONTRACT_FORBIDDEN_REVELATION",
                            violation_type=ViolationType.CONTRACT_BREACH,
                            severity=Severity.FATAL,
                            message=f"Scene contract explicitly forbids revealing '{fact_id}'.",
                            scene_id=contract.scene_id,
                            offending_event=event,
                            involved_entities=[fact_id],
                            suggested_repair=f"Remove revelation of '{fact_id}' from this scene.",
                        )
                    )

        # 2. Check forbidden thread resolutions
        for thread_id, status in delta.thread_updates.items():
            if status == "resolved" and thread_id in contract.forbidden_thread_resolutions:
                violations.append(
                    CompilerViolation(
                        invariant_id="INV_CONTRACT_FORBIDDEN_THREAD_RESOLUTION",
                        violation_type=ViolationType.CONTRACT_BREACH,
                        severity=Severity.FATAL,
                        message=f"Scene contract explicitly forbids resolving thread '{thread_id}'.",
                        scene_id=contract.scene_id,
                        involved_entities=[thread_id],
                        suggested_repair=f"Keep thread '{thread_id}' open or advance without resolving.",
                    )
                )

        # 3. Check required state changes
        for req in contract.required_state_changes:
            req_type = req.get("type")
            if req_type == "PICK_UP":
                target_obj = req.get("object")
                target_char = req.get("actor")
                actual_holder = delta.possession_changes.get(target_obj)
                if actual_holder != target_char:
                    violations.append(
                        CompilerViolation(
                            invariant_id="INV_CONTRACT_REQUIRED_CHANGE_MISSING",
                            violation_type=ViolationType.CONTRACT_BREACH,
                            severity=Severity.ERROR,
                            message=f"Required contract change not fulfilled: '{target_char}' did not pick up '{target_obj}'.",
                            scene_id=contract.scene_id,
                            involved_entities=[target_char, target_obj] if target_char and target_obj else [],
                            suggested_repair=f"Include '{target_char}' picking up '{target_obj}' in scene prose.",
                        )
                    )

        return violations

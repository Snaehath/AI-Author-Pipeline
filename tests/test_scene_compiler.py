"""
Acceptance Test Suite for Stateful Scene Compiler & Checkpoints.

Verifies the central architectural invariants:
1. Valid scene proposal commits a clean state transition.
2. Invalid scene proposal is hard-rejected.
3. Checkpoint manifest, rollback, and event replay work deterministically.
4. Failed scene proposal has EXACTLY zero effect on canonical state.
"""

import tempfile
from pathlib import Path
import pytest

from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.state.checkpoints import StoryCheckpointManager
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.contracts.scene import SceneContract
from story_engine.contracts.mapper import BlueprintContractMapper
from story_engine.scene_compiler import StatefulSceneCompiler
from story_engine.events.event import StoryEvent, EventType
try:
    from AI_Author.pipeline.inference.blueprint_planner import ChapterBlueprint
except ImportError:
    from pipeline.inference.blueprint_planner import ChapterBlueprint


@pytest.fixture
def test_setup():
    world = WorldState()
    world.location_graph.add_location("drawing_room", "Drawing Room", ["library"])
    world.location_graph.add_location("library", "Library", ["drawing_room"])
    world.location_graph.add_location("cellar", "Cellar", [])  # Disconnected

    world.add_character(Character(id="arthur", name="Arthur", location="drawing_room", vitality="alive"))
    world.add_character(Character(id="martha", name="Martha", location="library", vitality="alive"))

    world.add_object(StoryObject(id="silver_key", name="silver key", holder_type="location", holder_id="library"))

    truth = WorldTruthBase()
    truth.register_fact("fact_poison", "Martha poisoned the drink", category="secret")

    epistemic = EpistemicTracker()
    epistemic.grant_knowledge("martha", "fact_poison")

    contract = SceneContract(
        scene_id="ch01_sc001",
        chapter_num=1,
        scene_num=1,
        pov_character="arthur",
        primary_location="library",
        allowed_participants=["arthur", "martha"],
        allowed_props=["silver_key"],
        required_state_changes=[{"type": "PICK_UP", "actor": "arthur", "object": "silver_key"}],
        forbidden_revelations=["fact_poison"],
    )

    return world, truth, epistemic, contract


def test_valid_scene_transition_and_checkpoint(test_setup):
    world, truth, epistemic, contract = test_setup

    with tempfile.TemporaryDirectory() as tmp_dir:
        checkpoint_mgr = StoryCheckpointManager(base_dir=Path(tmp_dir))
        compiler = StatefulSceneCompiler(checkpoint_manager=checkpoint_mgr)

        prose = "Arthur entered the Library. He looked around and picked up the silver key."
        result = compiler.compile_scene_candidate(
            prose=prose,
            contract=contract,
            canonical_world=world,
            epistemic=epistemic,
            world_truth=truth,
            story_id="test_story",
        )

        assert result.is_committed is True
        assert result.status == "COMMITTED"
        assert result.validated_delta is not None
        assert result.validated_delta.possession_changes.get("silver_key") == "arthur"
        assert result.previous_state_hash != result.new_state_hash

        # Checkpoint directory was saved
        assert result.checkpoint_dir is not None
        assert (result.checkpoint_dir / "manifest.json").exists()
        assert (result.checkpoint_dir / "checkpoint_state.json").exists()
        assert (result.checkpoint_dir / "committed_diff.json").exists()


def test_fatal_rejection_for_epistemic_leak(test_setup):
    world, truth, epistemic, contract = test_setup
    compiler = StatefulSceneCompiler()

    # Arthur states the murder secret without knowing it
    prose = "Arthur entered the Library. Arthur picked up the silver key. 'Martha poisoned the drink!' he declared."
    # Inject a candidate SAY event with the secret fact
    candidate_diff = compiler.extractor.extract_from_prose(prose, contract, world)
    candidate_diff.events.append(
        StoryEvent(
            event_type=EventType.SAY,
            actor="arthur",
            payload={"fact_id": "fact_poison"},
            scene_id=contract.scene_id,
        )
    )

    # Compile with the leak
    comp_res = compiler.continuity_compiler.compile_scene(
        current_world=world,
        epistemic=epistemic,
        world_truth=truth,
        contract=contract,
        candidate_diff=candidate_diff,
    )
    assert comp_res.is_valid is False
    assert comp_res.has_fatal() is True


def test_checkpoint_rollback_and_replay(test_setup):
    world, truth, epistemic, contract = test_setup

    with tempfile.TemporaryDirectory() as tmp_dir:
        checkpoint_mgr = StoryCheckpointManager(base_dir=Path(tmp_dir))
        compiler = StatefulSceneCompiler(checkpoint_manager=checkpoint_mgr)

        prose = "Arthur entered the Library. Arthur picked up the silver key."
        result = compiler.compile_scene_candidate(
            prose=prose,
            contract=contract,
            canonical_world=world,
            epistemic=epistemic,
            world_truth=truth,
        )
        assert result.is_committed is True
        checkpoint_dir = result.checkpoint_dir

        # 1. Rollback
        restored_world, restored_epistemic = checkpoint_mgr.rollback(checkpoint_dir)
        assert restored_world.state_hash() == result.new_state_hash

        # 2. Replay events from base
        events_to_replay = [
            StoryEvent(event_type=EventType.MOVE, actor="arthur", destination="library"),
            StoryEvent(event_type=EventType.PICK_UP, actor="arthur", target="silver_key"),
        ]
        replayed_world = checkpoint_mgr.replay(checkpoint_dir, events_to_replay)
        assert replayed_world.characters["arthur"].location == "library"
        assert replayed_world.objects["silver_key"].holder_id == "arthur"


def test_failed_candidate_cannot_mutate_canonical_state(test_setup):
    """Critical Invariant Test: A rejected candidate must have ZERO effect on canonical state."""
    world, truth, epistemic, contract = test_setup
    compiler = StatefulSceneCompiler()

    before_hash = world.state_hash()
    before_ledger_len = len(compiler.ledger)
    before_arthur_location = world.characters["arthur"].location
    before_key_holder = world.objects["silver_key"].holder_id

    # Impossible action: Arthur tries to interact with a non-existent room/disconnected cellar
    impossible_prose = "Arthur entered the cellar without walking. He vanished into thin air."
    # Inject impossible disconnected move
    candidate_diff = compiler.extractor.extract_from_prose(impossible_prose, contract, world)
    candidate_diff.events.append(
        StoryEvent(
            event_type=EventType.MOVE,
            actor="arthur",
            origin="drawing_room",
            destination="cellar",  # Disconnected
            scene_id=contract.scene_id,
        )
    )

    # Manually compile candidate diff
    comp_res = compiler.continuity_compiler.compile_scene(
        current_world=world,
        epistemic=epistemic,
        world_truth=truth,
        contract=contract,
        candidate_diff=candidate_diff,
    )
    assert comp_res.is_valid is False

    # Compile scene candidate via StatefulSceneCompiler
    result = compiler.compile_scene_candidate(
        prose=impossible_prose,
        contract=contract,
        canonical_world=world,
        epistemic=epistemic,
        world_truth=truth,
    )

    # 1. Status is rejected
    assert result.status == "REJECTED"
    assert result.is_committed is False
    assert result.validated_delta is None

    # 2. Canonical state hash is 100% unchanged
    assert world.state_hash() == before_hash
    assert result.previous_state_hash == before_hash
    assert result.new_state_hash == before_hash

    # 3. Canonical objects and characters are completely untouched
    assert world.characters["arthur"].location == before_arthur_location
    assert world.objects["silver_key"].holder_id == before_key_holder

    # 4. Ledger records zero new events
    assert len(compiler.ledger) == before_ledger_len

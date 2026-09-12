import pytest
from compiler.continuity import ContinuityCompiler
from compiler.extractor import StateExtractor
from compiler.repair import RepairEngine
from compiler.violations import Severity
from story_engine.test import run_story_compiler_suite
from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.contracts.scene import SceneContract


def test_story_compiler_cli_suite():
    # Runs the full self-contained story compiler suite
    success = run_story_compiler_suite()
    assert success is True


def test_state_extractor_from_prose():
    world = WorldState()
    world.location_graph.add_location("library", "Library")
    world.add_character(Character(id="arthur", name="Arthur", location="drawing_room"))
    world.add_object(StoryObject(id="silver_key", name="silver key", holder_type="location", holder_id="library"))

    contract = SceneContract(
        scene_id="sc_1",
        chapter_num=1,
        scene_num=1,
        pov_character="arthur",
        primary_location="library",
        required_state_changes=[{"type": "PICK_UP", "actor": "arthur", "object": "silver_key"}]
    )

    prose = "Arthur entered the Library. He glanced around and picked up the silver key."
    extractor = StateExtractor()
    diff = extractor.extract_from_prose(prose, contract, world)

    assert len(diff.events) >= 1
    assert diff.delta.possession_changes.get("silver_key") == "arthur"


def test_repair_engine_penalties():
    engine = RepairEngine()
    from compiler.violations import CompilerViolation, ViolationType
    violations = [
        CompilerViolation(
            invariant_id="INV_POSSESSION",
            violation_type=ViolationType.POSSESSION_CONFLICT,
            severity=Severity.FATAL,
            message="Item conflict",
            scene_id="s1",
        ),
        CompilerViolation(
            invariant_id="INV_CONTRACT",
            violation_type=ViolationType.CONTRACT_BREACH,
            severity=Severity.WARNING,
            message="Minor contract drift",
            scene_id="s1",
        ),
    ]
    penalty = engine.calculate_penalty_score(violations)
    assert penalty == -110.0
    summary = engine.generate_repair_summary(violations)
    assert "FATAL" in summary
    assert "WARNING" in summary

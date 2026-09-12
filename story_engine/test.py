"""
Story Compiler CLI Test Runner.

Usage:
    python -m story_engine.test [novel_dir]
"""

import sys
import os
import argparse
from pathlib import Path
from typing import List

from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.contracts.scene import SceneContract
from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import CandidateDiff, StateDelta
from compiler.continuity import ContinuityCompiler
from compiler.violations import Severity


def run_story_compiler_suite(novel_path: str = ""):
    print("=" * 60)
    print("AI AUTHOR — STORY CONTINUITY COMPILER")
    print("=" * 60)
    novel_name = os.path.basename(novel_path) if novel_path else "The Mischief at Blackwood Manor"
    print(f"Novel:    {novel_name}")
    print(f"Target:   {novel_path if novel_path else 'Default Story State & Invariant Matrix'}")
    print("-" * 60)

    # 1. Setup Standard World
    world = WorldState()
    world.location_graph.add_location("drawing_room", "Drawing Room", ["library", "hallway"])
    world.location_graph.add_location("library", "Library", ["drawing_room"])
    world.location_graph.add_location("cellar", "Cellar", ["hallway"])
    world.location_graph.add_location("hallway", "Hallway", ["drawing_room", "cellar"])

    world.add_character(Character(id="arthur", name="Arthur", location="drawing_room", vitality="alive"))
    world.add_character(Character(id="martha", name="Martha", location="library", vitality="alive"))
    world.add_character(Character(id="higgins", name="Inspector Higgins", location="drawing_room", vitality="alive"))
    world.add_character(Character(id="ghost_sir_hugh", name="Sir Hugh", location="cellar", vitality="dead"))

    world.add_object(StoryObject(id="silver_key", name="Silver Key", holder_type="location", holder_id="library"))
    world.add_object(StoryObject(id="secret_letter", name="Secret Letter", holder_type="character", holder_id="martha"))

    # 2. Epistemic Setup
    truth = WorldTruthBase()
    f_murder = truth.register_fact("fact_murder", "Martha poisoned Sir Hugh", category="secret")
    f_party = truth.register_fact("fact_party", "A party is happening tonight", is_public=True)

    epistemic = EpistemicTracker()
    epistemic.grant_knowledge("martha", "fact_murder")

    compiler = ContinuityCompiler()

    # Define Test Scenarios
    passed_checks = []
    failed_checks = []

    # Check 1: Valid Co-located Pick Up
    contract1 = SceneContract(
        scene_id="ch1_sc1",
        chapter_num=1,
        scene_num=1,
        pov_character="martha",
        primary_location="library",
        allowed_participants=["martha"],
        allowed_props=["silver_key"],
    )
    diff1 = CandidateDiff(
        scene_id="ch1_sc1",
        events=[
            StoryEvent(
                event_type=EventType.PICK_UP,
                actor="martha",
                target="silver_key",
                origin="library",
                scene_id="ch1_sc1",
            )
        ],
        delta=StateDelta(possession_changes={"silver_key": "martha"}),
    )
    res1 = compiler.compile_scene(world, epistemic, truth, contract1, diff1)
    if res1.is_valid:
        passed_checks.append("Object Ownership & Proximity Pick-Up")
    else:
        failed_checks.append("Object Ownership & Proximity Pick-Up")

    # Update world to next state
    if res1.resulting_world_state:
        world = res1.resulting_world_state

    # Check 2: Invalid Disconnected Teleportation (Spatial Invariant)
    contract2 = SceneContract(
        scene_id="ch1_sc2",
        chapter_num=1,
        scene_num=2,
        pov_character="arthur",
        primary_location="cellar",
    )
    diff2 = CandidateDiff(
        scene_id="ch1_sc2",
        events=[
            StoryEvent(
                event_type=EventType.MOVE,
                actor="arthur",
                origin="drawing_room",
                destination="cellar",  # Not directly connected to drawing_room
                scene_id="ch1_sc2",
            )
        ],
        delta=StateDelta(location_changes={"arthur": "cellar"}),
    )
    res2 = compiler.compile_scene(world, epistemic, truth, contract2, diff2)
    if not res2.is_valid and any(v.invariant_id == "INV_LOCATION_CONNECTIVITY" for v in res2.violations):
        passed_checks.append("Spatial Teleportation Prevention (INV_LOCATION)")
    else:
        failed_checks.append("Spatial Teleportation Prevention (INV_LOCATION)")

    # Check 3: Epistemic Leak Prevention (Arthur asserts Martha's secret)
    contract3 = SceneContract(
        scene_id="ch1_sc3",
        chapter_num=1,
        scene_num=3,
        pov_character="arthur",
        primary_location="drawing_room",
    )
    diff3 = CandidateDiff(
        scene_id="ch1_sc3",
        events=[
            StoryEvent(
                event_type=EventType.SAY,
                actor="arthur",
                payload={"fact_id": "fact_murder"},
                scene_id="ch1_sc3",
            )
        ],
    )
    res3 = compiler.compile_scene(world, epistemic, truth, contract3, diff3)
    if not res3.is_valid and any(v.invariant_id == "INV_EPISTEMIC_LEAK" for v in res3.violations):
        passed_checks.append("Epistemic Knowledge Isolation (INV_EPISTEMIC)")
    else:
        failed_checks.append("Epistemic Knowledge Isolation (INV_EPISTEMIC)")

    # Check 4: Dead Character Action Invariant
    contract4 = SceneContract(
        scene_id="ch1_sc4",
        chapter_num=1,
        scene_num=4,
        pov_character="arthur",
        primary_location="cellar",
    )
    diff4 = CandidateDiff(
        scene_id="ch1_sc4",
        events=[
            StoryEvent(
                event_type=EventType.MOVE,
                actor="ghost_sir_hugh",
                origin="cellar",
                destination="hallway",
                scene_id="ch1_sc4",
            )
        ],
    )
    res4 = compiler.compile_scene(world, epistemic, truth, contract4, diff4)
    if not res4.is_valid and any(v.invariant_id == "INV_VITALITY_DEAD_ACTION" for v in res4.violations):
        passed_checks.append("Vitality & Deceased Actor Invariant (INV_VITALITY)")
    else:
        failed_checks.append("Vitality & Deceased Actor Invariant (INV_VITALITY)")

    # Print Report
    print("\nSTATE & NARRATIVE INTEGRITY RESULTS:")
    for check in passed_checks:
        print(f"  \u2713 {check}")
    for check in failed_checks:
        print(f"  \u2717 {check}")

    print("\nSUMMARY:")
    print(f"  Passed Invariants: {len(passed_checks)}/{len(passed_checks) + len(failed_checks)}")
    print(f"  Event Ledger Records: {len(compiler.ledger)}")
    print("=" * 60)
    return len(failed_checks) == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Narrative Story Continuity Compiler Test Suite")
    parser.add_argument("novel_path", nargs="?", default="", help="Path to novel outputs or manuscript")
    args = parser.parse_args()
    success = run_story_compiler_suite(args.novel_path)
    sys.exit(0 if success else 1)

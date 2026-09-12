import pytest
from story_engine.contracts.scene import SceneContract
from story_engine.contracts.invariants import NarrativeInvariants
from story_engine.context.budgeter import ContextBudgeter
from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import StateDelta


def test_scene_contract_prohibitions():
    contract = SceneContract(
        scene_id="sc_1",
        chapter_num=1,
        scene_num=1,
        pov_character="arthur",
        primary_location="library",
        forbidden_revelations=["secret_killer"],
        forbidden_thread_resolutions=["murder_mystery"],
    )

    # 1. Test forbidden revelation violation
    bad_event = StoryEvent(
        event_type=EventType.SAY,
        actor="arthur",
        payload={"fact_id": "secret_killer"},
        scene_id="sc_1",
    )
    violations = NarrativeInvariants.check_contract_invariants(
        contract, StateDelta(), [bad_event]
    )
    assert len(violations) == 1
    assert violations[0].invariant_id == "INV_CONTRACT_FORBIDDEN_REVELATION"

    # 2. Test forbidden thread resolution violation
    bad_delta = StateDelta(thread_updates={"murder_mystery": "resolved"})
    violations_thread = NarrativeInvariants.check_contract_invariants(
        contract, bad_delta, []
    )
    assert len(violations_thread) == 1
    assert violations_thread[0].invariant_id == "INV_CONTRACT_FORBIDDEN_THREAD_RESOLUTION"


def test_context_budgeter_epistemic_isolation():
    world = WorldState()
    world.add_character(Character(id="arthur", name="Arthur", location="library"))

    truth = WorldTruthBase()
    truth.register_fact("fact_public", "Sun rises in east", is_public=True)
    truth.register_fact("fact_secret", "Martha poisoned the drink", category="secret")

    epistemic = EpistemicTracker()
    # Arthur knows nothing about the secret

    contract = SceneContract(
        scene_id="sc_1",
        chapter_num=1,
        scene_num=1,
        pov_character="arthur",
        primary_location="library",
    )

    budgeter = ContextBudgeter(default_token_budget=2000)
    result = budgeter.build_scene_prompt_context(contract, world, epistemic, truth)

    prompt = result["prompt_context"]
    assert "SCENE CONTRACT" in prompt
    assert "Arthur" in prompt
    # Epistemic isolation guarantee: Secret proposition is completely absent from prompt
    assert "Martha poisoned the drink" not in prompt

import pytest
from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.events.event import StoryEvent, EventType
from story_engine.contracts.invariants import NarrativeInvariants
from compiler.violations import ViolationType, Severity


@pytest.fixture
def setup_narrative_context():
    world = WorldState()
    world.location_graph.add_location("room_a", "Room A", ["room_b"])
    world.location_graph.add_location("room_b", "Room B", ["room_a"])
    world.location_graph.add_location("room_c", "Room C", [])  # Disconnected

    world.add_character(Character(id="char_1", name="Arthur", location="room_a", vitality="alive"))
    world.add_character(Character(id="char_2", name="Martha", location="room_b", vitality="alive"))
    world.add_character(Character(id="char_dead", name="Hugh", location="room_a", vitality="dead"))

    world.add_object(StoryObject(id="obj_key", name="Key", holder_type="location", holder_id="room_b"))
    world.add_object(StoryObject(id="obj_ring", name="Ring", holder_type="character", holder_id="char_2"))

    truth = WorldTruthBase()
    truth.register_fact("fact_secret", "Secret treasure exists", category="secret")

    epistemic = EpistemicTracker()
    epistemic.grant_knowledge("char_2", "fact_secret")

    return world, truth, epistemic


def test_location_invariant_teleportation(setup_narrative_context):
    world, _, _ = setup_narrative_context

    # Arthur moves from room_a to room_c (disconnected)
    event = StoryEvent(
        event_type=EventType.MOVE,
        actor="char_1",
        origin="room_a",
        destination="room_c",
    )
    violation = NarrativeInvariants.check_location_invariant(world, event)
    assert violation is not None
    assert violation.violation_type == ViolationType.LOCATION_TELEPORTATION


def test_possession_invariant_exclusive_ownership(setup_narrative_context):
    world, _, _ = setup_narrative_context

    # Arthur tries to pick up the Ring currently held by Martha
    event = StoryEvent(
        event_type=EventType.PICK_UP,
        actor="char_1",
        target="obj_ring",
    )
    violation = NarrativeInvariants.check_possession_invariant(world, event)
    assert violation is not None
    assert violation.violation_type == ViolationType.POSSESSION_CONFLICT
    assert violation.severity == Severity.FATAL


def test_epistemic_invariant_knowledge_leak(setup_narrative_context):
    world, truth, epistemic = setup_narrative_context

    # Arthur states secret fact without knowing it
    event = StoryEvent(
        event_type=EventType.SAY,
        actor="char_1",
        payload={"fact_id": "fact_secret"},
    )
    violation = NarrativeInvariants.check_epistemic_invariant(world, epistemic, truth, event)
    assert violation is not None
    assert violation.violation_type == ViolationType.EPISTEMIC_LEAK
    assert violation.severity == Severity.FATAL

    # Martha states secret fact she knows
    valid_event = StoryEvent(
        event_type=EventType.SAY,
        actor="char_2",
        payload={"fact_id": "fact_secret"},
    )
    assert NarrativeInvariants.check_epistemic_invariant(world, epistemic, truth, valid_event) is None


def test_vitality_invariant_dead_actor(setup_narrative_context):
    world, _, _ = setup_narrative_context

    event = StoryEvent(
        event_type=EventType.MOVE,
        actor="char_dead",
        destination="room_b",
    )
    violation = NarrativeInvariants.check_vitality_invariant(world, event)
    assert violation is not None
    assert violation.violation_type == ViolationType.VITALITY_BREACH

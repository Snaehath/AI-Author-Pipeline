import pytest
from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import StateDelta
from story_engine.events.ledger import EventLedger


def test_world_state_cloning_and_hashing():
    world = WorldState()
    world.add_character(Character(id="c1", name="Reggie", location="drawing_room"))
    world.add_object(StoryObject(id="o1", name="Teapot", holder_type="location", holder_id="drawing_room"))

    hash1 = world.state_hash()
    clone = world.clone()
    assert clone.state_hash() == hash1

    # Mutate clone
    clone.characters["c1"].location = "garden"
    assert clone.state_hash() != hash1
    assert world.characters["c1"].location == "drawing_room"  # Deep copy isolated


def test_event_ledger_append_and_rollback():
    ledger = EventLedger()
    event1 = StoryEvent(event_type=EventType.MOVE, actor="c1", destination="library")
    delta1 = StateDelta(location_changes={"c1": "library"})

    entry = ledger.append(
        scene_id="scene_1",
        events=[event1],
        delta=delta1,
        prev_hash="hash_0",
        new_hash="hash_1",
    )

    assert len(ledger) == 1
    assert entry.scene_id == "scene_1"
    assert ledger.get_events_for_scene("scene_1")[0].destination == "library"

    # Rollback
    discarded = ledger.rollback_to_index(0)
    assert len(discarded) == 1
    assert len(ledger) == 0

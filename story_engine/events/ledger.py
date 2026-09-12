"""
Immutable Event Ledger.

Maintains an append-only transaction history of all state changes across chapters and scenes,
allowing branching, rollback, and inspection of story history.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import json
from story_engine.events.event import StoryEvent
from story_engine.events.diff import StateDelta


@dataclass
class LedgerEntry:
    entry_index: int
    scene_id: str
    events: List[StoryEvent]
    delta: StateDelta
    previous_state_hash: str
    resulting_state_hash: str
    timestamp: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "entry_index": self.entry_index,
            "scene_id": self.scene_id,
            "events": [e.to_dict() for e in self.events],
            "delta": self.delta.to_dict(),
            "previous_state_hash": self.previous_state_hash,
            "resulting_state_hash": self.resulting_state_hash,
            "timestamp": self.timestamp,
        }


class EventLedger:
    """Append-only ledger of narrative events and state diffs."""

    def __init__(self):
        self.entries: List[LedgerEntry] = []
        self._scene_index_map: Dict[str, int] = {}

    def append(
        self,
        scene_id: str,
        events: List[StoryEvent],
        delta: StateDelta,
        prev_hash: str,
        new_hash: str,
    ) -> LedgerEntry:
        """Appends a new verified state transition to the ledger."""
        entry = LedgerEntry(
            entry_index=len(self.entries),
            scene_id=scene_id,
            events=events,
            delta=delta,
            previous_state_hash=prev_hash,
            resulting_state_hash=new_hash,
            timestamp=events[-1].timestamp if events else 0,
        )
        self.entries.append(entry)
        self._scene_index_map[scene_id] = entry.entry_index
        return entry

    def get_events_for_scene(self, scene_id: str) -> List[StoryEvent]:
        """Retrieves all events committed in a specific scene."""
        idx = self._scene_index_map.get(scene_id)
        if idx is not None and 0 <= idx < len(self.entries):
            return self.entries[idx].events
        return []

    def get_all_events(self) -> List[StoryEvent]:
        """Flattens all events in order of occurrence."""
        events = []
        for entry in self.entries:
            events.extend(entry.events)
        return events

    def rollback_to_index(self, target_index: int) -> List[LedgerEntry]:
        """Rolls back the ledger to a prior index, returning discarded entries."""
        if target_index < 0:
            target_index = 0
        discarded = self.entries[target_index:]
        self.entries = self.entries[:target_index]
        self._scene_index_map = {entry.scene_id: entry.entry_index for entry in self.entries}
        return discarded

    def to_json(self) -> str:
        return json.dumps([e.to_dict() for e in self.entries], indent=2)

    def __len__(self) -> int:
        return len(self.entries)

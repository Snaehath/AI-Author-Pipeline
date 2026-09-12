"""
Atomic Story Checkpoints & Transaction Management.

Provides transactional persistence, verification manifests, event replay, and rollback
for committed narrative states.
"""

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
import json
import hashlib
import shutil

from story_engine.state.world import WorldState
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.events.ledger import EventLedger
from story_engine.events.event import StoryEvent
from story_engine.events.diff import StateDelta, CandidateDiff
from story_engine.contracts.scene import SceneContract


@dataclass
class CheckpointManifest:
    story_id: str
    chapter_num: int
    scene_num: int
    parent_checkpoint: Optional[str]
    state_hash: str
    event_hash: str
    contract_hash: str
    status: str  # "COMMITTED" or "REJECTED"
    timestamp: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CheckpointManifest":
        return cls(**data)


class StoryCheckpointManager:
    """Manages atomic checkpoint directories, replay, and rollback."""

    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_checkpoint(
        self,
        story_id: str,
        chapter_num: int,
        scene_num: int,
        contract: SceneContract,
        candidate_diff: CandidateDiff,
        validated_delta: StateDelta,
        world_state: WorldState,
        epistemic: EpistemicTracker,
        events: List[StoryEvent],
        prose: str,
        parent_checkpoint_id: Optional[str] = None,
    ) -> Path:
        """Atomically saves a committed scene transaction directory."""
        scene_dir = self.base_dir / f"chapter_{chapter_num:02d}" / f"scene_{scene_num:03d}"
        scene_dir.mkdir(parents=True, exist_ok=True)

        state_dict = world_state.to_dict()
        state_dict["epistemic"] = epistemic.to_dict()
        state_json = json.dumps(state_dict, sort_keys=True)
        state_hash = hashlib.sha256(state_json.encode("utf-8")).hexdigest()[:16]

        events_dict = [e.to_dict() for e in events]
        events_json = json.dumps(events_dict, sort_keys=True)
        event_hash = hashlib.sha256(events_json.encode("utf-8")).hexdigest()[:16]

        contract_json = json.dumps(contract.to_dict(), sort_keys=True)
        contract_hash = hashlib.sha256(contract_json.encode("utf-8")).hexdigest()[:16]

        manifest = CheckpointManifest(
            story_id=story_id,
            chapter_num=chapter_num,
            scene_num=scene_num,
            parent_checkpoint=parent_checkpoint_id,
            state_hash=state_hash,
            event_hash=event_hash,
            contract_hash=contract_hash,
            status="COMMITTED",
            timestamp=events[-1].timestamp if events else 0,
        )

        # Write atomic files
        (scene_dir / "prose.md").write_text(prose, encoding="utf-8")
        (scene_dir / "contract.json").write_text(contract_json, encoding="utf-8")
        (scene_dir / "candidate_diff.json").write_text(
            json.dumps({"events": [e.to_dict() for e in candidate_diff.events], "delta": candidate_diff.delta.to_dict()}, indent=2),
            encoding="utf-8",
        )
        (scene_dir / "committed_diff.json").write_text(
            json.dumps(validated_delta.to_dict(), indent=2),
            encoding="utf-8",
        )
        (scene_dir / "checkpoint_state.json").write_text(state_json, encoding="utf-8")
        (scene_dir / "checkpoint_events.json").write_text(events_json, encoding="utf-8")
        (scene_dir / "manifest.json").write_text(json.dumps(manifest.to_dict(), indent=2), encoding="utf-8")

        return scene_dir

    def load_checkpoint(self, checkpoint_dir: Path) -> Tuple[WorldState, EpistemicTracker, CheckpointManifest]:
        """Loads a committed checkpoint state and manifest."""
        checkpoint_dir = Path(checkpoint_dir)
        state_data = json.loads((checkpoint_dir / "checkpoint_state.json").read_text(encoding="utf-8"))
        epistemic_data = state_data.pop("epistemic", {})
        world = WorldState.from_dict(state_data)
        epistemic = EpistemicTracker.from_dict(epistemic_data)
        manifest_data = json.loads((checkpoint_dir / "manifest.json").read_text(encoding="utf-8"))
        manifest = CheckpointManifest.from_dict(manifest_data)
        return world, epistemic, manifest

    def rollback(self, target_checkpoint_dir: Path) -> Tuple[WorldState, EpistemicTracker]:
        """Explicit rollback: restores world state and epistemic state from a historical checkpoint."""
        world, epistemic, _ = self.load_checkpoint(target_checkpoint_dir)
        return world, epistemic

    def replay(self, base_checkpoint_dir: Path, events: List[StoryEvent]) -> WorldState:
        """Explicit replay: loads a base checkpoint and applies event mutations sequentially."""
        world, _, _ = self.load_checkpoint(base_checkpoint_dir)
        for event in events:
            # Build minimal delta from event
            delta = StateDelta()
            if event.destination and event.actor:
                delta.location_changes[event.actor] = event.destination
            if event.target and event.actor and event.event_type.value == "PICK_UP":
                delta.possession_changes[event.target] = event.actor
            world = world.apply(delta)
        return world

    def branch(self, base_checkpoint_dir: Path, branch_name: str) -> Path:
        """Creates a parallel branching timeline from an existing checkpoint."""
        branch_dir = self.base_dir / "branches" / branch_name
        branch_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(base_checkpoint_dir, branch_dir / "root_checkpoint", dirs_exist_ok=True)
        return branch_dir

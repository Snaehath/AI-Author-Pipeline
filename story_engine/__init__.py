"""
Story Engine: Stateful Narrative Generation Operating System.
"""

from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.state.locations import LocationGraph
from story_engine.state.relationships import RelationshipMatrix
from story_engine.state.timeline import StoryClock

from story_engine.epistemic.world_truth import Fact, WorldTruthBase
from story_engine.epistemic.character_knowledge import KnowledgeBase, EpistemicTracker
from story_engine.epistemic.reader_knowledge import ReaderKnowledge

from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import StateDelta, CandidateDiff
from story_engine.events.ledger import EventLedger, LedgerEntry

from story_engine.state.checkpoints import StoryCheckpointManager, CheckpointManifest
from story_engine.contracts.scene import SceneContract
from story_engine.contracts.invariants import NarrativeInvariants
from story_engine.contracts.mapper import BlueprintContractMapper
from story_engine.context.budgeter import ContextBudgeter
def __getattr__(name: str):
    if name in ("StatefulSceneCompiler", "SceneCompilationResult"):
        from story_engine.scene_compiler import StatefulSceneCompiler, SceneCompilationResult
        return locals()[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "WorldState",
    "Character",
    "StoryObject",
    "LocationGraph",
    "RelationshipMatrix",
    "StoryClock",
    "StoryCheckpointManager",
    "CheckpointManifest",
    "Fact",
    "WorldTruthBase",
    "KnowledgeBase",
    "EpistemicTracker",
    "ReaderKnowledge",
    "StoryEvent",
    "EventType",
    "StateDelta",
    "CandidateDiff",
    "EventLedger",
    "LedgerEntry",
    "SceneContract",
    "NarrativeInvariants",
    "BlueprintContractMapper",
    "ContextBudgeter",
    "StatefulSceneCompiler",
    "SceneCompilationResult",
]

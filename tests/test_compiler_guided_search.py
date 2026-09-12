"""
Acceptance Test Suite for Path 2: Compiler-Guided Search & Selection.

Verifies:
1. Gate 1 Hard Gating: Fatal world violations disqualify candidates regardless of prose score.
2. Gate 2 Hard Gating: Contract breaches disqualify candidates.
3. Gate 3 Ranking & Contract-Relevance State Efficiency E(c).
4. Dominant Pattern Targeted Repair when zero candidates survive initial pool.
5. Full Candidate Audit Directory & Token Economics logging.
6. Zero Canonical State Mutation during candidate search.
"""

import tempfile
import json
from pathlib import Path
import pytest

from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.contracts.scene import SceneContract
from story_engine.events.event import StoryEvent, EventType
from story_engine.events.diff import StateDelta
from pipeline.inference.best_of_n_selector import CompilerGuidedSearch, CandidateEvaluation


@pytest.fixture
def search_context():
    world = WorldState()
    world.location_graph.add_location("drawing_room", "Drawing Room", ["library"])
    world.location_graph.add_location("library", "Library", ["drawing_room"])

    world.add_character(Character(id="arthur", name="Arthur", location="drawing_room", vitality="alive"))
    world.add_character(Character(id="martha", name="Martha", location="library", vitality="alive"))

    world.add_object(StoryObject(id="silver_key", name="silver key", holder_type="location", holder_id="library"))
    world.add_object(StoryObject(id="unrelated_cup", name="unrelated cup", holder_type="location", holder_id="library"))

    truth = WorldTruthBase()
    truth.register_fact("fact_murder", "Martha poisoned Sir Hugh", category="secret")

    epistemic = EpistemicTracker()
    epistemic.grant_knowledge("martha", "fact_murder")

    contract = SceneContract(
        scene_id="ch01_sc001",
        chapter_num=1,
        scene_num=1,
        pov_character="arthur",
        primary_location="library",
        allowed_participants=["arthur", "martha"],
        allowed_props=["silver_key"],
        required_state_changes=[{"type": "PICK_UP", "actor": "arthur", "object": "silver_key"}],
        forbidden_revelations=["fact_murder"],
    )

    return world, truth, epistemic, contract


def test_gate_1_hard_gating_fatal_disqualification(search_context):
    """Gate 1: Fatal violation (secret leak) is hard-rejected even if prose is long and fluent."""
    world, truth, epistemic, contract = search_context
    search = CompilerGuidedSearch()

    # Candidate A: Beautiful writing, but leaks murder secret
    cand_a_prose = "Arthur entered the Library. Arthur picked up the silver key. 'Martha poisoned Sir Hugh!' Arthur shouted suddenly."
    # Candidate B: Simple writing, 100% valid
    cand_b_prose = "Arthur entered the Library. Arthur picked up the silver key. 'A lovely afternoon,' said Arthur politely."

    result = search.search_best_candidate(
        candidate_prose_list=[cand_a_prose, cand_b_prose],
        contract=contract,
        canonical_world=world,
        epistemic=epistemic,
        world_truth=truth,
    )

    # Candidate A must fail Gate 1 (epistemic leak) or Gate 2
    # Candidate B must survive and win
    assert result.gate_summary["survivors"] >= 1
    assert result.selected_candidate_id == "candidate_002"
    assert result.selected_prose == cand_b_prose


def test_gate_2_contract_breach_disqualification(search_context):
    """Gate 2: Candidate that omits mandatory contract objective is disqualified."""
    world, truth, epistemic, contract = search_context
    search = CompilerGuidedSearch()

    # Candidate A: Forgets to pick up silver key (contract objective missing)
    cand_a_prose = "Arthur entered the Library. Arthur glanced around at the bookshelves and sighed quietly."
    # Candidate B: Fulfills pick up
    cand_b_prose = "Arthur entered the Library. Arthur picked up the silver key with a smile."

    result = search.search_best_candidate(
        candidate_prose_list=[cand_a_prose, cand_b_prose],
        contract=contract,
        canonical_world=world,
        epistemic=epistemic,
        world_truth=truth,
    )

    # Candidate A fails Gate 2
    eval_a = next(c for c in result.candidates if c.candidate_id == "candidate_001")
    assert eval_a.gate == "GATE_2_FAILED"

    # Candidate B is the survivor and selected winner
    assert result.selected_candidate_id == "candidate_002"


def test_contract_relevance_state_efficiency(search_context):
    """Gate 3: Between two valid candidates, relevant actions beat noisy irrelevant mutations."""
    world, truth, epistemic, contract = search_context
    search = CompilerGuidedSearch(lambda_efficiency=0.5)

    # Candidate A: Clean, relevant contract actions
    cand_a_prose = "Arthur entered the Library. Arthur picked up the silver key."
    # Candidate B: Relevant actions PLUS irrelevant actions touching uncontracted objects
    cand_b_prose = "Arthur entered the Library. Arthur picked up the silver key. Arthur took the unrelated cup from the table."

    result = search.search_best_candidate(
        candidate_prose_list=[cand_a_prose, cand_b_prose],
        contract=contract,
        canonical_world=world,
        epistemic=epistemic,
        world_truth=truth,
    )

    eval_a = next(c for c in result.candidates if c.candidate_id == "candidate_001")
    eval_b = next(c for c in result.candidates if c.candidate_id == "candidate_002")

    # Both survived Gates 1 and 2
    assert eval_a.gate == "SURVIVOR"
    assert eval_b.gate == "SURVIVOR"

    # Candidate A has higher state efficiency E(c)
    assert eval_a.efficiency_score >= eval_b.efficiency_score


def test_dominant_pattern_targeted_repair(search_context):
    """Targeted Repair: When all candidates fail, identifies dominant violation pattern and repairs."""
    world, truth, epistemic, contract = search_context
    search = CompilerGuidedSearch()

    # All initial candidates fail due to missing required key pickup
    failing_prose_list = [
        "Arthur entered the Library and admired the portraits.",
        "Arthur walked into the Library and opened a dusty volume.",
    ]

    # Mock generator function that produces a valid scene when given the repair prompt
    def mock_generator(prompt: str) -> str:
        assert "SCENE CONTRACT OBJECTIVE" in prompt or "silver_key" in prompt or "PICK_UP" in prompt
        return "Arthur entered the Library and picked up the silver key."

    result = search.search_best_candidate(
        candidate_prose_list=failing_prose_list,
        contract=contract,
        canonical_world=world,
        epistemic=epistemic,
        world_truth=truth,
        generator_fn=mock_generator,
    )

    assert result.repair_attempted is True
    # The repaired candidate survived and was selected
    assert "candidate_repaired" in result.selected_candidate_id
    assert "picked up the silver key" in result.selected_prose


def test_candidate_audit_logging_and_token_economics(search_context):
    """Audit Logging: Verifies full directory structure and selection_audit.json persistence."""
    world, truth, epistemic, contract = search_context
    search = CompilerGuidedSearch()

    candidates = [
        "Arthur entered the Library. Arthur picked up the silver key.",
        "Arthur entered the Library. Arthur picked up the silver key. 'Splendid day!' he said.",
    ]
    tokens = [
        {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150, "generation_time_ms": 500},
        {"prompt_tokens": 100, "completion_tokens": 60, "total_tokens": 160, "generation_time_ms": 600},
    ]

    with tempfile.TemporaryDirectory() as tmp_dir:
        audit_path = Path(tmp_dir) / "audit_scene_001"
        result = search.search_best_candidate(
            candidate_prose_list=candidates,
            contract=contract,
            canonical_world=world,
            epistemic=epistemic,
            world_truth=truth,
            candidate_tokens=tokens,
            output_audit_dir=audit_path,
        )

        assert audit_path.exists()
        assert (audit_path / "selection_audit.json").exists()
        assert (audit_path / "candidate_001" / "prose.md").exists()
        assert (audit_path / "candidate_001" / "score.json").exists()
        assert (audit_path / "candidate_002" / "prose.md").exists()

        audit_data = json.loads((audit_path / "selection_audit.json").read_text(encoding="utf-8"))
        assert audit_data["selected"] in ["candidate_001", "candidate_002"]
        assert audit_data["gate_summary"]["survivors"] >= 1
        assert audit_data["token_economics"]["total_tokens"] == 310
        assert audit_data["token_economics"]["generation_time_ms"] == 1100


def test_zero_canonical_mutation_during_search(search_context):
    """Search Invariant: Canonical state remains 100% untouched during multi-candidate evaluation."""
    world, truth, epistemic, contract = search_context
    search = CompilerGuidedSearch()

    before_hash = world.state_hash()
    before_arthur_loc = world.characters["arthur"].location
    before_key_holder = world.objects["silver_key"].holder_id

    candidates = [
        "Arthur entered the Library. Arthur picked up the silver key.",
        "Arthur entered the Library and spoke with Martha.",
        "Arthur entered the cellar without walking.",
    ]

    result = search.search_best_candidate(
        candidate_prose_list=candidates,
        contract=contract,
        canonical_world=world,
        epistemic=epistemic,
        world_truth=truth,
    )

    # Canonical world must NOT be mutated by search
    assert world.state_hash() == before_hash
    assert world.characters["arthur"].location == before_arthur_loc
    assert world.objects["silver_key"].holder_id == before_key_holder

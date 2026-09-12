"""
Experiment 001 Tri-System Deterministic Runner Harness.

Runs:
- System A: Baseline (1.5B Unconstrained Generation + Post-hoc Compiler Audit)
- System B: Stateful (1.5B + Context Budgeter + Stateful Scene Compiler, 1 Candidate)
- System C: Compiler-Guided BoN (1.5B + Context Budgeter + Best-of-3 + 3-Stage Gate + Targeted Repair)
"""

import copy
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Callable

from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.state.checkpoints import StoryCheckpointManager
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.contracts.scene import SceneContract
from story_engine.context.budgeter import ContextBudgeter
from story_engine.scene_compiler import StatefulSceneCompiler, SceneCompilationResult
from compiler.continuity import ContinuityCompiler, CompilationResult
from compiler.extractor import StateExtractor
from inference.best_of_n_selector import CompilerGuidedSearch, SearchSelectionResult
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Experiments.Runner")


class ExperimentHarness:
    """Manages frozen initial state and executes comparative experiment arms."""

    def __init__(
        self,
        config_path: Path,
        generator_fn: Optional[Callable[[str, str], str]] = None,
        mock_mode: bool = False,
    ):
        self.config_path = Path(config_path)
        with open(self.config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.mock_mode = mock_mode
        self.generator_fn = generator_fn or self._create_generator_fn()
        self.extractor = StateExtractor()
        self.budgeter = ContextBudgeter()
        self.search_engine = CompilerGuidedSearch(
            lambda_efficiency=self.config.get("search", {}).get("lambda_efficiency", 0.15)
        )

    def _create_generator_fn(self) -> Callable[[str, str], str]:
        """Loads StoryGenerator for live inference or provides fallback."""
        if self.mock_mode:
            return self._mock_generator

        try:
            from AI_Author.inference.generator import StoryGenerator
            generator = StoryGenerator()

            def _live_gen(sys_p: str, user_p: str) -> str:
                return generator._generate_response(sys_p, user_p)

            self._story_gen_ref = generator
            return _live_gen
        except Exception as e:
            logger.warning(f"Could not load live generator ({e}). Falling back to mock generator.")
            self.mock_mode = True
            return self._mock_generator

    def _mock_generator(self, sys_p: str, user_p: str) -> str:
        """Deterministic mock generator for tests and fast verification."""
        # Check if this is a naive baseline prompt with stuffed secrets
        if "PRIVATE SECRETS:" in user_p and "fact_teapot_mislaid" in user_p:
            return (
                "Lord Reginald paced the drawing room. 'The teapot was mislaid behind books by Professor Thorne!' "
                "he blurted out recklessly to Inspector Higgins."
            )

        # Check for repair prompt
        if "SCENE CONTRACT OBJECTIVE" in user_p or "Rewrite this scene" in sys_p or "repairing scenes" in sys_p:
            if "silver_teapot" in user_p:
                return "Lord Reginald entered the Library. He picked up the Prized Silver Teapot from behind the books."
            return "Lord Reginald entered the Library and carefully picked up the silver key."

        # Check for contract hints in prompt
        if "PICK_UP silver_teapot" in user_p or "silver_teapot" in user_p:
            if "library" in user_p.lower():
                return "Lord Reginald entered the Library and picked up the Prized Silver Teapot."
            return "Lord Reginald picked up the Prized Silver Teapot from the parlor table."
        elif "MOVE to library" in user_p or "library" in user_p.lower():
            return "Lord Reginald walked into the Library. He examined the high mahogany shelves."
        elif "MOVE to hallway" in user_p or "hallway" in user_p.lower():
            return "Barnaby entered the Hallway with silent, measured steps."
        elif "MOVE to study" in user_p or "study" in user_p.lower():
            return "Inspector Higgins walked into the Study and examined the ledger."
        elif "MOVE to dining_room" in user_p or "dining_room" in user_p.lower():
            return "Lady Beatrice entered the Dining Room with elegant composure."
        elif "MOVE to cellar" in user_p or "cellar" in user_p.lower():
            return "Barnaby entered the Cellar holding a dim brass lantern."

        return "Lord Reginald Finch observed Blackwood Manor. 'A splendid morning, Barnaby,' he remarked calmly."

    def build_initial_environment(self) -> tuple[WorldState, WorldTruthBase, EpistemicTracker]:
        """Creates the identical, frozen canonical baseline environment."""
        world = WorldState()

        # 1. Location Graph
        world.location_graph.add_location("drawing_room", "Drawing Room", ["library", "hallway", "dining_room"])
        world.location_graph.add_location("library", "Library", ["drawing_room", "study"])
        world.location_graph.add_location("study", "Study", ["library"])
        world.location_graph.add_location("hallway", "Hallway", ["drawing_room", "cellar"])
        world.location_graph.add_location("dining_room", "Dining Room", ["drawing_room"])
        world.location_graph.add_location("cellar", "Cellar", ["hallway"])

        # 2. Characters
        world.add_character(Character(id="lord_reginald", name="Lord Reginald", location="drawing_room", role="protagonist"))
        world.add_character(Character(id="barnaby", name="Barnaby", location="drawing_room", role="companion"))
        world.add_character(Character(id="inspector_higgins", name="Inspector Higgins", location="drawing_room", role="antagonist"))
        world.add_character(Character(id="lady_beatrice", name="Lady Beatrice", location="drawing_room", role="supporting"))

        # 3. Objects
        world.add_object(StoryObject(id="silver_teapot", name="Prized Silver Teapot", holder_type="location", holder_id="drawing_room"))
        world.add_object(StoryObject(id="urgent_blue_envelope", name="Urgent Blue Envelope", holder_type="character", holder_id="lord_reginald"))
        world.add_object(StoryObject(id="scotland_yard_badge", name="Scotland Yard Badge", holder_type="character", holder_id="inspector_higgins"))
        world.add_object(StoryObject(id="silver_key", name="silver key", holder_type="location", holder_id="library"))

        # 4. Truth & Epistemic Base
        truth = WorldTruthBase()
        truth.register_fact("fact_teapot_mislaid", "The teapot was mislaid behind books by Professor Thorne", category="secret")

        epistemic = EpistemicTracker()
        epistemic.grant_knowledge("barnaby", "fact_teapot_mislaid")

        return world, truth, epistemic

    def run_baseline_scene(
        self,
        scene_def: Dict[str, Any],
        canonical_world: WorldState,
        truth: WorldTruthBase,
        epistemic: EpistemicTracker,
    ) -> Dict[str, Any]:
        """System A: Unconstrained baseline generation with post-hoc compiler verification."""
        contract = SceneContract(**scene_def["contract"])

        # Naive prompt stuffing: stuff all characters, locations, and registered secrets indiscriminately
        naive_context = (
            f"MANOR CHARACTERS: Lord Reginald, Barnaby, Inspector Higgins, Lady Beatrice.\n"
            f"LOCATIONS: Drawing Room, Library, Study, Hallway, Dining Room, Cellar.\n"
            f"PRIVATE SECRETS: The teapot was mislaid behind books by Professor Thorne (fact_teapot_mislaid).\n"
            f"SCENE GOAL: {scene_def['description']}\n"
        )
        sys_p = "You are an AI author writing continuous fiction prose. Write the full scene prose."
        user_p = f"Write Scene: {scene_def['title']}\n{naive_context}"

        t0 = time.time()
        prose = self.generator_fn(sys_p, user_p)
        gen_time = int((time.time() - t0) * 1000)

        p_tok = int(len((sys_p + user_p).split()) * 1.3)
        c_tok = int(len(prose.split()) * 1.3)
        token_cost = {
            "prompt_tokens": p_tok,
            "completion_tokens": c_tok,
            "total_tokens": p_tok + c_tok,
            "generation_time_ms": gen_time,
            "repair_tokens": 0,
        }

        # Post-hoc evaluation via ContinuityCompiler
        candidate_diff = self.extractor.extract_from_prose(prose, contract, canonical_world, world_truth=truth)
        compiler = ContinuityCompiler()
        comp_res: CompilationResult = compiler.compile_scene(
            current_world=canonical_world,
            epistemic=epistemic,
            world_truth=truth,
            contract=contract,
            candidate_diff=candidate_diff,
        )

        quality_breakdown = self.search_engine.reward_model.evaluate_scene(
            prose=prose,
            goal=contract.target_mood,
            characters=contract.allowed_participants,
            objects=contract.allowed_props,
        )
        q_score = min(1.0, max(0.0, quality_breakdown.composite_reward_score / 10.0))

        return {
            "scene_id": contract.scene_id,
            "system_id": "baseline",
            "is_valid": comp_res.is_valid and not comp_res.has_fatal(),
            "prose": prose,
            "violations": [v.to_dict() for v in comp_res.violations],
            "quality_score": round(q_score, 4),
            "efficiency_score": 0.5,
            "token_economics": token_cost,
            "gate_summary": {
                "total_candidates": 1,
                "survivors": 1 if comp_res.is_valid and not comp_res.has_fatal() else 0,
                "fatal_rejected": 1 if (not comp_res.is_valid or comp_res.has_fatal()) else 0,
            },
            "repair": {"attempted": False},
        }

    def run_stateful_scene(
        self,
        scene_def: Dict[str, Any],
        canonical_world: WorldState,
        truth: WorldTruthBase,
        epistemic: EpistemicTracker,
        checkpoint_manager: Optional[StoryCheckpointManager] = None,
    ) -> tuple[Dict[str, Any], WorldState]:
        """System B: Single-candidate generation with Context Budgeter and StatefulSceneCompiler."""
        contract = SceneContract(**scene_def["contract"])
        compiler = StatefulSceneCompiler(checkpoint_manager=checkpoint_manager)

        # Context Budgeting: strictly POV-isolated context
        context_pack = self.budgeter.build_scene_prompt_context(
            contract=contract,
            world=canonical_world,
            epistemic=epistemic,
            world_truth=truth,
        )

        sys_p = "You are an AI author writing stateful continuous fiction prose."
        user_p = f"{context_pack['prompt_context']}\n\nSCENE GOAL: {scene_def['description']}"

        t0 = time.time()
        prose = self.generator_fn(sys_p, user_p)
        gen_time = int((time.time() - t0) * 1000)

        p_tok = int(len((sys_p + user_p).split()) * 1.3)
        c_tok = int(len(prose.split()) * 1.3)
        token_cost = {
            "prompt_tokens": p_tok,
            "completion_tokens": c_tok,
            "total_tokens": p_tok + c_tok,
            "generation_time_ms": gen_time,
            "repair_tokens": 0,
        }

        # Stateful Scene Compilation
        comp_result: SceneCompilationResult = compiler.compile_scene_candidate(
            prose=prose,
            contract=contract,
            canonical_world=canonical_world,
            epistemic=epistemic,
            world_truth=truth,
            story_id="experiment_001",
        )

        quality_breakdown = self.search_engine.reward_model.evaluate_scene(
            prose=prose,
            goal=contract.target_mood,
            characters=contract.allowed_participants,
            objects=contract.allowed_props,
        )
        q_score = min(1.0, max(0.0, quality_breakdown.composite_reward_score / 10.0))

        resulting_world = comp_result.resulting_world_state if comp_result.is_committed else canonical_world

        record = {
            "scene_id": contract.scene_id,
            "system_id": "stateful",
            "is_valid": comp_result.is_committed,
            "prose": prose,
            "violations": [v.to_dict() for v in comp_result.violations],
            "quality_score": round(q_score, 4),
            "efficiency_score": 0.5,
            "token_economics": token_cost,
            "gate_summary": {
                "total_candidates": 1,
                "survivors": 1 if comp_result.is_committed else 0,
                "fatal_rejected": 1 if not comp_result.is_committed else 0,
            },
            "repair": {"attempted": False},
        }
        return record, resulting_world

    def run_bon_scene(
        self,
        scene_def: Dict[str, Any],
        canonical_world: WorldState,
        truth: WorldTruthBase,
        epistemic: EpistemicTracker,
        output_audit_dir: Optional[Path] = None,
        checkpoint_manager: Optional[StoryCheckpointManager] = None,
    ) -> tuple[Dict[str, Any], WorldState]:
        """System C: Best-of-3 with 3-Stage Gating, State Efficiency, and Targeted Repair."""
        contract = SceneContract(**scene_def["contract"])
        compiler = StatefulSceneCompiler(checkpoint_manager=checkpoint_manager)

        context_pack = self.budgeter.build_scene_prompt_context(
            contract=contract,
            world=canonical_world,
            epistemic=epistemic,
            world_truth=truth,
        )

        variation_hints = [
            "Authoritative and precise narrative style.",
            "Suspenseful and atmospheric pacing.",
            "Fast-paced dialogue with sharp character turns.",
        ]

        candidate_prose_list = []
        candidate_tokens = []

        sys_p = "You are an AI author generating continuous publication-grade prose."

        for idx in range(3):
            hint = variation_hints[idx]
            user_p = (
                f"{context_pack['prompt_context']}\n"
                f"STYLE HINT: {hint}\n"
                f"SCENE GOAL: {scene_def['description']}\n"
            )
            t0 = time.time()
            prose = self.generator_fn(sys_p, user_p)
            gen_time = int((time.time() - t0) * 1000)

            p_tok = int(len((sys_p + user_p).split()) * 1.3)
            c_tok = int(len(prose.split()) * 1.3)
            cand_token = {
                "prompt_tokens": p_tok,
                "completion_tokens": c_tok,
                "total_tokens": p_tok + c_tok,
                "generation_time_ms": gen_time,
            }
            candidate_prose_list.append(prose)
            candidate_tokens.append(cand_token)

        search_result: SearchSelectionResult = self.search_engine.search_best_candidate(
            candidate_prose_list=candidate_prose_list,
            contract=contract,
            canonical_world=canonical_world,
            epistemic=epistemic,
            world_truth=truth,
            generator_fn=lambda prompt: self.generator_fn("You are a fiction continuity editor repairing scenes.", prompt),
            candidate_tokens=candidate_tokens,
            output_audit_dir=output_audit_dir,
            story_id="experiment_001",
        )

        winning_eval = next((c for c in search_result.candidates if c.candidate_id == search_result.selected_candidate_id), None)
        is_valid = winning_eval.is_valid if winning_eval else False

        # Atomic Commit of ONE Winner
        comp_result = compiler.compile_scene_candidate(
            prose=search_result.selected_prose,
            contract=contract,
            canonical_world=canonical_world,
            epistemic=epistemic,
            world_truth=truth,
            story_id="experiment_001",
        )

        resulting_world = comp_result.resulting_world_state if comp_result.is_committed else canonical_world

        record = {
            "scene_id": contract.scene_id,
            "system_id": "bon",
            "is_valid": comp_result.is_committed,
            "selected_candidate": search_result.selected_candidate_id,
            "prose": search_result.selected_prose,
            "violations": [v.to_dict() for v in comp_result.violations],
            "quality_score": round(winning_eval.quality_score, 4) if winning_eval else 0.0,
            "efficiency_score": round(winning_eval.efficiency_score, 4) if winning_eval else 0.0,
            "token_economics": search_result.token_economics,
            "gate_summary": search_result.gate_summary,
            "repair": {
                "attempted": search_result.repair_attempted,
                "dominant_pattern": search_result.repair_dominant_pattern,
            },
        }
        return record, resulting_world

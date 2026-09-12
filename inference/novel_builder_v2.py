"""
v2 Master Novel Builder Orchestrator (AI Author Studio v2).

Integrates:
- BlueprintPlanner (Pre-prose structured blueprints)
- BlueprintContractMapper (Maps blueprints to formal SceneContracts)
- StatefulSceneCompiler (Pure immutable state transitions & invariant verification)
- StoryCheckpointManager (Atomic checkpoint directories with manifests)
- MultiAgentEditingCrew (Multi-agent specialized revision crew)
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure project root and AI_Author directory are in sys.path
AI_AUTHOR_DIR = Path(__file__).resolve().parent.parent
ML_DIR = AI_AUTHOR_DIR.parent

for p in (AI_AUTHOR_DIR, ML_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from AI_Author.inference.generator import StoryGenerator
from AI_Author.inference.blueprint_planner import BlueprintPlanner
from AI_Author.inference.multi_agent_crew import MultiAgentEditingCrew
from AI_Author.inference.best_of_n_selector import CompilerGuidedSearch
from story_engine.state.world import WorldState
from story_engine.state.characters import Character
from story_engine.state.objects import StoryObject
from story_engine.state.checkpoints import StoryCheckpointManager
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.contracts.mapper import BlueprintContractMapper
from story_engine.scene_compiler import StatefulSceneCompiler, SceneCompilationResult
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.NovelBuilderV2")


class NovelBuilderV2:
    """Master orchestrator for AI Author Studio v2 stateful novel generation."""

    def __init__(self, generator: StoryGenerator = None, lambda_efficiency: float = 0.25):
        self.generator = generator or StoryGenerator()
        self.planner = BlueprintPlanner()
        self.crew = MultiAgentEditingCrew(self.generator)
        self.search_engine = CompilerGuidedSearch(lambda_efficiency=lambda_efficiency)

        # Initialize Canonical World & Invariant Graph
        self.world = WorldState()
        self._init_world_cast()

        self.truth = WorldTruthBase()
        self.epistemic = EpistemicTracker()
        self._init_epistemic_base()

    def _init_world_cast(self):
        """Builds spatial layout and initial character/prop registry."""
        # Spatial Graph
        self.world.location_graph.add_location("drawing_room", "Drawing Room", ["library", "hallway", "dining_room"])
        self.world.location_graph.add_location("library", "Library", ["drawing_room", "study"])
        self.world.location_graph.add_location("study", "Study", ["library"])
        self.world.location_graph.add_location("hallway", "Hallway", ["drawing_room", "cellar"])
        self.world.location_graph.add_location("dining_room", "Dining Room", ["drawing_room"])
        self.world.location_graph.add_location("cellar", "Cellar", ["hallway"])

        # Characters
        self.world.add_character(Character(id="lord_reginald", name="Lord Reginald", location="drawing_room", role="protagonist"))
        self.world.add_character(Character(id="barnaby", name="Barnaby", location="drawing_room", role="companion"))
        self.world.add_character(Character(id="inspector_higgins", name="Inspector Higgins", location="drawing_room", role="antagonist"))
        self.world.add_character(Character(id="lady_beatrice", name="Lady Beatrice", location="drawing_room", role="supporting"))

        # Props
        self.world.add_object(StoryObject(id="silver_teapot", name="Prized Silver Teapot", holder_type="location", holder_id="drawing_room"))
        self.world.add_object(StoryObject(id="urgent_blue_envelope", name="Urgent Blue Envelope", holder_type="character", holder_id="lord_reginald"))
        self.world.add_object(StoryObject(id="scotland_yard_badge", name="Scotland Yard Badge", holder_type="character", holder_id="inspector_higgins"))

        # Pairwise Relationships
        self.world.relationships.set_relationship("lord_reginald", "barnaby", affinity=85, trust=90)
        self.world.relationships.set_relationship("barnaby", "lord_reginald", affinity=90, trust=95)
        self.world.relationships.set_relationship("inspector_higgins", "lord_reginald", affinity=-30, trust=-40)

    def _init_epistemic_base(self):
        """Registers secrets and initializes private knowledge bases."""
        f1 = self.truth.register_fact("fact_teapot_mislaid", "The teapot was mislaid behind books by Professor Thorne", category="secret")
        self.epistemic.grant_knowledge("barnaby", "fact_teapot_mislaid")

    def generate_novel_v2(
        self,
        title: str = "The Mischief at Blackwood Manor",
        num_chapters: int = 5,
        output_dir: str = "outputs/generated_novel",
        num_candidates: int = 3,
    ) -> Path:
        """Generates a multi-chapter novel using Compiler-Guided Search & Stateful Scene Compiler."""
        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        chap_dir = out_path / "chapters"
        chap_dir.mkdir(parents=True, exist_ok=True)
        checkpoints_dir = out_path / "checkpoints"

        checkpoint_mgr = StoryCheckpointManager(base_dir=checkpoints_dir)
        compiler = StatefulSceneCompiler(checkpoint_manager=checkpoint_mgr)

        logger.info("==================================================")
        logger.info(f"Starting AI Author Studio v2 Master Orchestration: '{title}'")
        logger.info(f"Generating Pre-Prose Blueprints, Stateful Checkpoints, Best-of-{num_candidates} Search & {num_chapters} Chapters...")

        # 1. Generate Pre-Prose Blueprints
        blueprints = self.planner.create_novel_blueprints(title, num_chapters)
        logger.info(f"Generated {len(blueprints)} Pre-Prose Chapter Blueprints.")

        with open(out_path / "chapter_blueprints.json", "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in blueprints], f, indent=2)

        full_manuscript_lines = [
            f"# {title}\n\n*By AI Author Studio v2 Stateful Engine*\n\n---\n\n",
            "## Story Outline & Blueprint Architecture\n\n",
        ]

        for b in blueprints:
            full_manuscript_lines.append(
                f"### Chapter {b.chapter_num}: {b.title}\n"
                f"- **Goal:** {b.goal}\n"
                f"- **Conflict:** {b.conflict}\n"
                f"- **Emotional Arc:** {b.emotional_arc}\n"
                f"- **Characters:** {', '.join(b.characters_present)}\n\n"
            )
        full_manuscript_lines.append("---\n\n")

        prev_context = ""
        parent_ckpt_id: str = "root"

        variation_hints = [
            "Standard crisp narrative, witty banter, atmospheric 1920s manor setting.",
            "Dramatic tension and escalating suspicion, highlighting character secrets.",
            "Rapid dialogue-driven pacing and sharp comedic irony between Reginald and Barnaby.",
        ]

        for idx, blueprint in enumerate(blueprints, 1):
            logger.info(f"--- Generating Chapter {idx}/{num_chapters}: '{blueprint.title}' ---")

            # 2. Map Blueprint to formal SceneContract
            contract = BlueprintContractMapper.map_blueprint_to_contract(
                blueprint=blueprint,
                scene_num=1,
                forbidden_facts=["fact_teapot_mislaid"] if idx < 3 else [],
            )

            # 3. Context Budgeter: Build strictly isolated POV prompt
            context_pack = compiler.budgeter.build_scene_prompt_context(
                contract=contract,
                world=self.world,
                epistemic=self.epistemic,
                world_truth=self.truth,
            )

            # 4. Generate Candidate Variations
            candidate_prose_list = []
            candidate_tokens = []
            for c_idx in range(max(1, num_candidates)):
                hint = variation_hints[c_idx % len(variation_hints)]
                logger.info(f"Generating Candidate {c_idx + 1}/{num_candidates} (Variation: '{hint[:40]}...')")
                cand_prose = self.crew.generate_masterpiece_chapter(
                    book_title=title,
                    blueprint=blueprint,
                    previous_context=prev_context,
                    rag_prompt=context_pack["prompt_context"],
                    variation_hint=hint,
                )
                candidate_prose_list.append(cand_prose)
                candidate_tokens.append(getattr(self.crew, "last_crew_stats", {}))

            # 5. Compiler-Guided Search & Best-of-N Evaluation (3-Stage Gating, Canonical State Untouched)
            scene_audit_dir = checkpoints_dir / f"chapter_{idx:02d}" / "scene_001"
            search_result = self.search_engine.search_best_candidate(
                candidate_prose_list=candidate_prose_list,
                contract=contract,
                canonical_world=self.world,
                epistemic=self.epistemic,
                world_truth=self.truth,
                generator_fn=lambda prompt: self.generator._generate_response(
                    "You are an expert fiction continuity editor repairing scenes.",
                    "Repair and rewrite the following scene:",
                    prompt,
                ),
                candidate_tokens=candidate_tokens,
                output_audit_dir=scene_audit_dir,
                story_id=title.lower().replace(" ", "_"),
            )

            winning_prose = search_result.selected_prose
            logger.info(
                f"✓ Selected winning candidate '{search_result.selected_candidate_id}' for Chapter {idx} "
                f"(Survivors: {search_result.gate_summary['survivors']}/{search_result.gate_summary['total_candidates']})"
            )

            # 6. Stateful Scene Compiler (Prose Proposal -> Candidate Delta -> Invariants -> Commit ONE winner)
            comp_result: SceneCompilationResult = compiler.compile_scene_candidate(
                prose=winning_prose,
                contract=contract,
                canonical_world=self.world,
                epistemic=self.epistemic,
                world_truth=self.truth,
                story_id=title.lower().replace(" ", "_"),
                parent_checkpoint_id=parent_ckpt_id,
            )

            if comp_result.is_committed:
                # Atomically update canonical state snapshot
                self.world = comp_result.resulting_world_state
                parent_ckpt_id = f"chapter_{idx:02d}_scene_001"
                logger.info(f"✓ Chapter {idx} committed to EventLedger (Hash: {comp_result.new_state_hash})")
            else:
                logger.warning(f"⚠ Chapter {idx} had violations: {len(comp_result.violations)}. Canonical state untouched.")

            # Save Chapter JSON & Committed State Diff
            chap_data = {
                "chapter_index": idx,
                "title": blueprint.title,
                "word_count": len(winning_prose.split()),
                "blueprint": blueprint.to_dict(),
                "contract": contract.to_dict(),
                "state_hash": self.world.state_hash(),
                "is_committed": comp_result.is_committed,
                "selected_candidate": search_result.selected_candidate_id,
                "gate_summary": search_result.gate_summary,
                "token_economics": search_result.token_economics,
                "content": winning_prose,
            }
            with open(chap_dir / f"chapter_{idx:02d}.json", "w", encoding="utf-8") as f:
                json.dump(chap_data, f, indent=2)

            if comp_result.validated_delta:
                with open(chap_dir / f"chapter_{idx:02d}_diff.json", "w", encoding="utf-8") as f:
                    json.dump(comp_result.validated_delta.to_dict(), f, indent=2)

            full_manuscript_lines.append(f"## Chapter {idx}: {blueprint.title}\n\n{winning_prose}\n\n")

            # Context memory for next chapter
            paras = [p.strip() for p in winning_prose.split("\n\n") if p.strip()]
            prev_context = "\n\n".join(paras[-2:]) if len(paras) >= 2 else winning_prose

        # 7. Save final event ledger and state dump
        with open(out_path / "event_ledger.json", "w", encoding="utf-8") as f:
            f.write(compiler.ledger.to_json())

        with open(out_path / "canonical_world_state.json", "w", encoding="utf-8") as f:
            json.dump(self.world.to_dict(), f, indent=2)

        # Write Master Manuscript Markdown File
        manuscript_path = out_path / "generated_novel_manuscript.md"
        manuscript_path.write_text("".join(full_manuscript_lines), encoding="utf-8")
        logger.info(f"Exported full stateful manuscript to: '{manuscript_path}'")
        logger.info("==================================================")
        return manuscript_path


def main():
    parser = argparse.ArgumentParser(description="AI Author Studio v2 Stateful Novel Generator")
    parser.add_argument("--chapters", type=int, default=5, help="Number of chapters to generate (default: 5)")
    parser.add_argument("--candidates", type=int, default=3, help="Number of candidate variations per scene (default: 3)")
    parser.add_argument("--title", type=str, default="The Mischief at Blackwood Manor", help="Novel title")
    parser.add_argument("--output_dir", type=str, default="outputs/generated_novel", help="Output directory")

    args = parser.parse_args()

    builder = NovelBuilderV2()
    builder.generate_novel_v2(
        title=args.title,
        num_chapters=args.chapters,
        output_dir=args.output_dir,
        num_candidates=args.candidates,
    )


if __name__ == "__main__":
    main()

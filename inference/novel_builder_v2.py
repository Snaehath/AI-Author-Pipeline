"""
v2 Master Novel Builder Orchestrator (AI Author Studio v2).

Integrates:
- BlueprintPlanner (Pre-prose structured blueprints)
- StoryBibleDB (Persistent state, goals, inventories & trust scores)
- FictionRAGEngine (Targeted memory retrieval per scene)
- ContinuityCheckerV2 (Post-generation verification & name sanitizer)
- MultiAgentEditingCrew (Multi-agent specialized revision crew)
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.inference.generator import StoryGenerator
from AI_Author.inference.blueprint_planner import BlueprintPlanner
from AI_Author.inference.story_bible_db import StoryBibleDB
from AI_Author.inference.fiction_rag import FictionRAGEngine
from AI_Author.inference.continuity_checker_v2 import ContinuityCheckerV2
from AI_Author.inference.multi_agent_crew import MultiAgentEditingCrew
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.NovelBuilderV2")


class NovelBuilderV2:
    """Master orchestrator for AI Author Studio v2 novel generation."""

    def __init__(self, generator: StoryGenerator = None):
        self.generator = generator or StoryGenerator()
        self.planner = BlueprintPlanner()
        self.story_db = StoryBibleDB()
        self.story_db.initialize_default_db()
        self.rag_engine = FictionRAGEngine(self.story_db)
        self.continuity_checker = ContinuityCheckerV2()
        self.crew = MultiAgentEditingCrew(self.generator)

    def generate_novel_v2(
        self,
        title: str = "The Mischief at Blackwood Manor",
        num_chapters: int = 5,
        output_dir: str = "outputs/generated_novel",
    ) -> Path:
        """Generates a multi-chapter novel using AI Author Studio v2 architecture."""

        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        chap_dir = out_path / "chapters"
        chap_dir.mkdir(parents=True, exist_ok=True)

        logger.info("==================================================")
        logger.info(f"Starting AI Author Studio v2 Master Orchestration: '{title}'")
        logger.info(f"Generating Pre-Prose Blueprints, Story Bible DB & {num_chapters} Chapters...")

        # 1. Generate Pre-Prose Blueprints
        blueprints = self.planner.create_novel_blueprints(title, num_chapters)
        logger.info(f"Generated {len(blueprints)} Pre-Prose Chapter Blueprints.")

        # Save Blueprints and Story Bible DB to output dir
        with open(out_path / "chapter_blueprints.json", "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in blueprints], f, indent=2)

        with open(out_path / "story_bible_db.json", "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.story_db.characters.items()}, f, indent=2)

        full_manuscript_lines = [
            f"# {title}\n\n*By AI Author Studio v2 Engine*\n\n---\n\n",
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

        for idx, blueprint in enumerate(blueprints, 1):
            logger.info(f"--- Generating Chapter {idx}/{num_chapters}: '{blueprint.title}' ---")

            # 2. Fiction RAG Memory Retrieval
            rag_prompt = self.rag_engine.retrieve_scene_memory(blueprint)

            # 3. Multi-Agent Revision Crew Pass
            chap_prose = self.crew.generate_masterpiece_chapter(
                book_title=title,
                blueprint=blueprint,
                previous_context=prev_context,
                rag_prompt=rag_prompt,
            )

            # 4. Continuity Checker Pass
            check_res = self.continuity_checker.verify_and_clean(chap_prose, blueprint)
            chap_prose = check_res["cleaned_prose"]
            if check_res["warnings"]:
                logger.info(f"Continuity Checker Warnings on Ch.{idx}: {check_res['warnings']}")

            # Save individual chapter JSON
            chap_data = {
                "chapter_index": idx,
                "title": blueprint.title,
                "word_count": check_res["word_count"],
                "blueprint": blueprint.to_dict(),
                "content": chap_prose,
            }
            with open(chap_dir / f"chapter_{idx:02d}.json", "w", encoding="utf-8") as f:
                json.dump(chap_data, f, indent=2)

            logger.info(f"Saved Chapter {idx} ({check_res['word_count']} words) to: 'chapter_{idx:02d}.json'")

            full_manuscript_lines.append(f"## Chapter {idx}: {blueprint.title}\n\n{chap_prose}\n\n")

            # Context memory for next chapter
            paras = [p.strip() for p in chap_prose.split("\n\n") if p.strip()]
            prev_context = "\n\n".join(paras[-2:]) if len(paras) >= 2 else chap_prose

        # Write Master Manuscript Markdown File
        manuscript_path = out_path / "generated_novel_manuscript.md"
        manuscript_path.write_text("".join(full_manuscript_lines), encoding="utf-8")
        logger.info(f"Exported full v2 manuscript to: '{manuscript_path}'")
        logger.info("==================================================")
        return manuscript_path


def main():
    parser = argparse.ArgumentParser(description="AI Author Studio v2 Novel Generator")
    parser.add_argument("--chapters", type=int, default=5, help="Number of chapters to generate (default: 5)")
    parser.add_argument("--title", type=str, default="The Mischief at Blackwood Manor", help="Novel title")
    parser.add_argument("--output_dir", type=str, default="outputs/generated_novel", help="Output directory")

    args = parser.parse_args()

    builder = NovelBuilderV2()
    manuscript = builder.generate_novel_v2(
        title=args.title,
        num_chapters=args.chapters,
        output_dir=args.output_dir,
    )
    print(f"\n✓ Successfully generated v2 novel '{args.title}' at: {manuscript}")


if __name__ == "__main__":
    main()

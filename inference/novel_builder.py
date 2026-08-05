"""
Automated Novel Builder Module.

Automatically generates a complete multi-chapter novel using Qwen 2.5 1.5B Instruct
+ fine-tuned LoRA adapter, saving chapters and full manuscript to outputs/generated_novel/.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.inference.generator import StoryGenerator
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.NovelBuilder")


class NovelBuilder:
    """Automates complete multi-chapter novel generation and workspace compilation."""

    def __init__(self, generator: Optional[StoryGenerator] = None):
        """Initializes NovelBuilder with StoryGenerator instance.

        Args:
            generator: Optional StoryGenerator instance.
        """
        self.root_dir = Path(__file__).resolve().parent.parent
        self.generator = generator or StoryGenerator()

    def generate_complete_novel(
        self,
        title: str = "The Chronicles of Eldoria: The Lost Artifact",
        genre: str = "Fantasy / Adventure",
        premise: str = "Two travelers search for an ancient lost artifact hidden inside a dangerous mountain cavern.",
        num_chapters: int = 3,
        output_dir: Optional[Path] = None,
    ) -> Dict[str, Any]:
        """Generates a complete multi-chapter novel and saves outputs.

        Args:
            title: Novel title.
            genre: Novel genre.
            premise: Story premise.
            num_chapters: Number of chapters to generate.
            output_dir: Output directory (defaults to outputs/generated_novel).

        Returns:
            Dictionary containing generation summary and file paths.
        """
        out_path = output_dir or (self.root_dir / "outputs" / "generated_novel")
        chap_dir = out_path / "chapters"
        chap_dir.mkdir(parents=True, exist_ok=True)

        from AI_Author.inference.character_bible import CharacterBible
        from AI_Author.inference.state_tracker import CharacterStateTracker
        from AI_Author.inference.consistency_checker import ConsistencyChecker
        from AI_Author.inference.critic_engine import MultiPassCriticEngine

        logger.info(f"==================================================")
        logger.info(f"Starting Automated 3-Pass Novel Generation: '{title}'")
        logger.info(f"Generating Character Bible, Dynamic State Memory & {num_chapters} Chapters...")

        # Step 1: Initialize Original Character Bible & Dynamic State Tracker
        bible = CharacterBible.create_default_comedy_mystery(title=title)
        bible_context = bible.to_prompt_context()

        state_tracker = CharacterStateTracker()
        state_tracker.initialize_default_cast()

        consistency_checker = ConsistencyChecker()
        critic_engine = MultiPassCriticEngine(generator=self.generator)

        logger.info(f"Initialized Character Bible & Evolving State Tracker for: {bible.protagonist.name}")

        # Save Character Bible to output dir
        with open(out_path / "character_bible.json", "w", encoding="utf-8") as f:
            json.dump(bible.to_dict(), f, indent=2)

        # Step 2: Structured 3-Act Outline & Setting Anchors
        outline = (
            "## Story Outline: The Misadventures of Lord Reginald Finch\n\n"
            "**Setting:** Blackwood Manor, 1920s Country Estate, England\n"
            "**POV:** Third-Person Limited (following Lord Reginald Finch)\n\n"
            "• **Act I (Chapter 1):** Lord Reginald receives an urgent letter at Blackwood Manor.\n"
            "• **Act II (Chapters 2-3):** Afternoon tea turns to chaos when a silver teapot disappears, and Inspector Higgins accuses the wrong guest.\n"
            "• **Act III (Chapters 4-5):** Barnaby quietly uncovers the real culprit, restoring order before dinner concludes."
        )
        logger.info("Generated Structured 3-Act Story Outline with Setting & POV Anchors.")

        # Step 3: Strict Cause-and-Effect Scene Plans (Anchored at Blackwood Manor)
        scene_plans = [
            f"LOCATION: Blackwood Manor Drawing-Room. POV: Lord Reginald Finch.\nSCENE GOAL: Lord Reginald receives an urgent letter from Lady Beatrice inviting him to Blackwood Manor. Barnaby warns him to be careful, but Reggie insists on demonstrating his charm.",
            f"LOCATION: Blackwood Manor Garden Terrace. POV: Lord Reginald Finch.\nSCENE GOAL: At afternoon tea, Lord Reginald attempts to impress Lady Beatrice and Professor Thorne, but a prized silver teapot disappears under mysterious circumstances.",
            f"LOCATION: Blackwood Manor Library. POV: Lord Reginald Finch.\nSCENE GOAL: Inspector Higgins arrives at the manor, pompously accusing Lord Reginald of stealing the teapot. Reggie blusters while Barnaby observes quietly.",
            f"LOCATION: Blackwood Manor Study. POV: Lord Reginald Finch.\nSCENE GOAL: Barnaby investigates the study, discovering that the teapot was merely mislaid behind a book stack by Professor Thorne during a heated argument.",
            f"LOCATION: Blackwood Manor Dining Room. POV: Lord Reginald Finch.\nSCENE GOAL: Barnaby discreetly returns the teapot before dinner. Lord Reginald triumphantly takes full credit for solving the mystery, and the guests celebrate."
        ]

        from AI_Author.inference.memory_retrieval import SelectiveMemoryRetriever
        memory_retriever = SelectiveMemoryRetriever(state_tracker=state_tracker)

        chapters = []
        full_manuscript_lines = [f"# {title}\n\n*By AI Author Studio*\n\n---\n\n"]
        full_manuscript_lines.append(f"## Story Outline\n\n{outline}\n\n---\n\n")

        prev_context = ""

        for idx in range(1, num_chapters + 1):
            summary = scene_plans[(idx - 1) % len(scene_plans)]
            chap_title = f"Chapter {idx}"

            # Evolve dynamic character state & retrieve targeted memory for characters present
            state_tracker.update_state_after_scene(summary, idx)
            chars_present = ["Lord Reginald", "Barnaby", "Inspector Higgins"]
            dynamic_state_prompt = memory_retriever.retrieve_scene_context(chars_present)
            combined_prompt = f"{bible_context}\n\n{dynamic_state_prompt}"

            logger.info(f"Generating Chapter {idx}/{num_chapters} (3-Pass Revision with Selective State Memory)...")
            chap_prose = critic_engine.generate_polished_chapter(
                book_title=title,
                chapter_num=idx,
                summary=summary,
                previous_context=prev_context,
                character_bible_prompt=combined_prompt,
            )

            # Pass 4: Run Consistency & Teleportation Verification
            check_res = consistency_checker.verify_and_clean_chapter(chap_prose, idx)
            chap_prose = check_res["cleaned_text"]
            if check_res["warnings"]:
                logger.info(f"Consistency Checker Warnings on Ch.{idx}: {check_res['warnings']}")

            # Extract last 200 words as context memory for the next chapter
            paras = [p.strip() for p in chap_prose.split("\n\n") if p.strip()]
            prev_context = "\n\n".join(paras[-2:]) if len(paras) >= 2 else chap_prose

            words = chap_prose.split()
            chap_data = {
                "book_title": title,
                "chapter_index": idx,
                "chapter_title": chap_title,
                "total_scenes": 1,
                "total_paragraphs": len(chap_prose.split("\n\n")),
                "total_dialogues": chap_prose.count('"') // 2,
                "word_count": len(words),
                "narration_ratio": 0.8,
                "dialogue_ratio": 0.2,
                "scenes": [
                    {
                        "scene_index": 1,
                        "word_count": len(words),
                        "paragraphs": [
                            {
                                "paragraph_index": i + 1,
                                "text": p.strip(),
                                "type": "dialogue" if '"' in p else "narration",
                                "word_count": len(p.split()),
                                "has_dialogue": '"' in p,
                                "dialogues": []
                            }
                            for i, p in enumerate(chap_prose.split("\n\n")) if p.strip()
                        ]
                    }
                ]
            }

            chap_filepath = chap_dir / f"chapter_{idx:02d}.json"
            with open(chap_filepath, "w", encoding="utf-8") as f:
                json.dump(chap_data, f, indent=2, ensure_ascii=False)

            chapters.append(chap_data)
            full_manuscript_lines.append(f"## {chap_title}\n\n{chap_prose}\n\n")
            logger.info(f"Saved Chapter {idx} ({len(words)} words) to: '{chap_filepath.name}'")

        # Save Metadata
        metadata = {
          "title": title,
          "genre": genre,
          "author": "AI Author Studio",
          "total_chapters": num_chapters,
          "total_words": sum(c["word_count"] for c in chapters),
        }
        with open(out_path / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        # Save Full Manuscript (.md & .txt)
        md_file = out_path / "generated_novel_manuscript.md"
        txt_file = out_path / "generated_novel_manuscript.txt"

        with open(md_file, "w", encoding="utf-8") as f:
            f.writelines(full_manuscript_lines)

        with open(txt_file, "w", encoding="utf-8") as f:
            f.writelines(full_manuscript_lines)

        logger.info(f"Exported full manuscript to: '{md_file}'")
        logger.info(f"==================================================")

        return {
            "title": title,
            "total_chapters": num_chapters,
            "total_words": metadata["total_words"],
            "output_dir": str(out_path),
            "manuscript_md": str(md_file),
            "manuscript_txt": str(txt_file),
        }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Automated Novel Builder")
    parser.add_argument("--chapters", type=int, default=5, help="Number of chapters to generate (default: 5)")
    parser.add_argument("--title", type=str, default="The Comedy of Errors & Mysteries", help="Novel title")
    parser.add_argument("--genre", type=str, default="Humorous Mystery / Comedy", help="Novel genre")
    parser.add_argument("--premise", type=str, default="A hilarious detective investigation involving eccentric aristocrats and mysterious occurrences.", help="Novel premise")

    args = parser.parse_args()
    builder = NovelBuilder()
    res = builder.generate_complete_novel(
        title=args.title,
        genre=args.genre,
        premise=args.premise,
        num_chapters=args.chapters
    )
    print(f"Successfully generated full novel '{res['title']}' ({res['total_words']} words, {res['total_chapters']} chapters) in {res['output_dir']}.")

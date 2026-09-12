"""
Chapter Parser Orchestrator Module.

Loads ingested book outputs from Module 1 (metadata.json and cleaned.txt),
parses each chapter into scenes, paragraphs, and dialogue units,
and writes structured outputs to outputs/<book_slug>/chapters/chapter_XX.json.
"""

import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any, Optional

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from .scene_parser import SceneParser, Scene
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Parser.ChapterParser")


@dataclass
class ParsedChapter:
    """Represents a fully parsed chapter containing scene & paragraph breakdown."""
    book_title: str
    chapter_index: int
    chapter_title: str
    total_scenes: int
    total_paragraphs: int
    total_dialogues: int
    word_count: int
    narration_ratio: float
    dialogue_ratio: float
    scenes: List[Scene]

    def to_dict(self) -> Dict[str, Any]:
        """Converts ParsedChapter object to dictionary."""
        data = asdict(self)
        data["scenes"] = [s.to_dict() for s in self.scenes]
        return data


class ChapterParser:
    """Orchestrates scene, paragraph, and dialogue parsing across book chapters."""

    def __init__(
        self,
        config_path: Optional[Path] = None,
        scene_parser: Optional[SceneParser] = None,
    ):
        """Initializes ChapterParser.

        Args:
            config_path: Path to parser_config.json.
            scene_parser: Optional SceneParser instance.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "parser_config.json")
        self.config = self._load_config()
        self.scene_parser = scene_parser or SceneParser(self.config.get("scene_parser"))

    def _load_config(self) -> Dict[str, Any]:
        """Loads configuration JSON file if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded parser config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read parser config file ({e}). Using defaults.")
        return {}

    def parse_book_directory(self, book_dir: Path) -> List[ParsedChapter]:
        """Parses all chapters inside a processed book directory from Module 1.

        Args:
            book_dir: Path to book output directory (e.g. outputs/sample_novel).

        Returns:
            List of ParsedChapter objects.
        """
        book_path = Path(book_dir).resolve()
        metadata_file = book_path / "metadata.json"
        cleaned_txt_file = book_path / "cleaned.txt"

        if not metadata_file.exists():
            raise FileNotFoundError(f"Missing metadata.json at: {metadata_file}")
        if not cleaned_txt_file.exists():
            raise FileNotFoundError(f"Missing cleaned.txt at: {cleaned_txt_file}")

        with open(metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)

        book_title = metadata.get("title", "Untitled Book")
        raw_chapters = metadata.get("chapters", [])

        logger.info(f"==================================================")
        logger.info(f"Starting Chapter Parsing for Book: '{book_title}'")
        logger.info(f"Processing {len(raw_chapters)} chapter sections...")

        parsed_chapters: List[ParsedChapter] = []
        chapters_out_dir = book_path / "chapters"
        chapters_out_dir.mkdir(parents=True, exist_ok=True)

        for chap_data in raw_chapters:
            chap_idx = chap_data["chapter_index"]
            chap_title = chap_data["title"]
            chap_content = chap_data["content"]

            parsed_chap = self.parse_single_chapter(
                book_title=book_title,
                chapter_index=chap_idx,
                chapter_title=chap_title,
                chapter_content=chap_content,
            )

            parsed_chapters.append(parsed_chap)

            # Save individual chapter_XX.json file
            out_filename = f"chapter_{chap_idx:02d}.json"
            out_filepath = chapters_out_dir / out_filename

            with open(out_filepath, "w", encoding="utf-8") as f:
                json.dump(parsed_chap.to_dict(), f, indent=2, ensure_ascii=False)

            logger.info(f"Saved parsed chapter to: '{out_filepath}'")

        # Write parsing summary
        summary = {
            "book_title": book_title,
            "total_chapters": len(parsed_chapters),
            "total_scenes": sum(c.total_scenes for c in parsed_chapters),
            "total_paragraphs": sum(c.total_paragraphs for c in parsed_chapters),
            "total_dialogues": sum(c.total_dialogues for c in parsed_chapters),
            "total_words": sum(c.word_count for c in parsed_chapters),
        }
        summary_filepath = book_path / "parsing_summary.json"
        with open(summary_filepath, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        logger.info(f"Parsing summary saved to: '{summary_filepath}'")
        logger.info(f"Chapter parsing complete for '{book_title}'.")
        logger.info(f"==================================================")

        return parsed_chapters

    def parse_single_chapter(
        self,
        book_title: str,
        chapter_index: int,
        chapter_title: str,
        chapter_content: str,
    ) -> ParsedChapter:
        """Parses raw text of a single chapter into a ParsedChapter object.

        Args:
            book_title: Title of the book.
            chapter_index: 1-based index.
            chapter_title: Title string of the chapter.
            chapter_content: Raw chapter narrative text string.

        Returns:
            ParsedChapter object.
        """
        scenes: List[Scene] = self.scene_parser.parse_scenes(chapter_content)

        total_paragraphs = sum(len(s.paragraphs) for s in scenes)
        total_dialogues = sum(
            sum(len(p.dialogues) for p in s.paragraphs) for s in scenes
        )
        total_words = sum(s.word_count for s in scenes)

        dialogue_words = sum(
            sum(
                sum(d.word_count for d in p.dialogues)
                for p in s.paragraphs
            )
            for s in scenes
        )

        narration_words = max(0, total_words - dialogue_words)

        n_ratio = round(narration_words / total_words, 3) if total_words > 0 else 1.0
        d_ratio = round(dialogue_words / total_words, 3) if total_words > 0 else 0.0

        return ParsedChapter(
            book_title=book_title,
            chapter_index=chapter_index,
            chapter_title=chapter_title,
            total_scenes=len(scenes),
            total_paragraphs=total_paragraphs,
            total_dialogues=total_dialogues,
            word_count=total_words,
            narration_ratio=n_ratio,
            dialogue_ratio=d_ratio,
            scenes=scenes,
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Chapter Parser")
    parser.add_argument("book_dir", type=str, help="Path to processed book directory (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    chapter_parser = ChapterParser()
    res = chapter_parser.parse_book_directory(Path(args.book_dir))
    print(f"Successfully parsed {len(res)} chapters.")

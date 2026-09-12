"""
Ingestion Pipeline Orchestrator.

Combines format extraction, text normalization, header cleaning, and chapter splitting
into a unified pipeline that outputs cleaned.txt and metadata.json.
"""

import json
import re
import sys
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, List, Optional

# Ensure project root (containing AI_Author package) is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from .extractors import extract_text_from_file
from .normalizer import TextNormalizer
from .header_cleaner import HeaderCleaner
from .chapter_splitter import ChapterSplitter, Chapter
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Ingestion.Pipeline")


@dataclass
class IngestionResult:
    """Dataclass holding ingestion output references and metrics."""
    book_slug: str
    cleaned_text_path: Path
    metadata_path: Path
    total_words: int
    total_chapters: int
    format: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts result to dictionary representation."""
        data = asdict(self)
        data["cleaned_text_path"] = str(self.cleaned_text_path)
        data["metadata_path"] = str(self.metadata_path)
        return data


class IngestionPipeline:
    """Orchestrates end-to-end book ingestion."""

    def __init__(self, config_path: Optional[Path] = None, output_base_dir: Optional[Path] = None):
        """Initializes the ingestion pipeline.

        Args:
            config_path: Path to ingestion_config.json.
            output_base_dir: Directory where processed book subfolders will be written.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "ingestion_config.json")
        self.output_base_dir = output_base_dir or (self.root_dir / "outputs")
        self.config = self._load_config()

        self.normalizer = TextNormalizer(self.config.get("normalizer"))
        self.header_cleaner = HeaderCleaner(self.config.get("header_cleaner"))
        self.chapter_splitter = ChapterSplitter(self.config.get("chapter_splitter"))

    def _load_config(self) -> Dict[str, Any]:
        """Loads configuration JSON file if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read config file ({e}). Using default settings.")
        return {}

    def _slugify(self, text: str) -> str:
        """Converts string into filesystem-friendly slug."""
        text = text.lower().strip()
        text = re.sub(r"[^\w\s-]", "", text)
        return re.sub(r"[-\s]+", "_", text)

    def _strip_gutenberg_preamble(self, text: str) -> str:
        """Strips Project Gutenberg legal headers and footers from raw text."""
        start_markers = [
            "*** START OF THE PROJECT GUTENBERG EBOOK",
            "*** START OF THIS PROJECT GUTENBERG EBOOK",
        ]
        for marker in start_markers:
            if marker in text:
                text = text.split(marker, 1)[-1]
                # Strip header title block up to first main chapter
                lines = text.splitlines()
                for i, l in enumerate(lines[:100]):
                    if any(l.strip().startswith(kw) for kw in ["CHAPTER", "Chapter", "Contents", "LEAVE IT TO JEEVES", "PSMITH IN THE CITY"]):
                        text = "\n".join(lines[i:])
                        break
                break

        end_markers = [
            "*** END OF THE PROJECT GUTENBERG EBOOK",
            "*** END OF THIS PROJECT GUTENBERG EBOOK",
        ]
        for marker in end_markers:
            if marker in text:
                text = text.split(marker, 1)[0]
                break

        return text.strip()

    def run(
        self,
        input_file: Path,
        title: Optional[str] = None,
        author: Optional[str] = None,
    ) -> IngestionResult:
        """Executes full book ingestion pipeline.

        Args:
            input_file: Path to input book file (.txt, .pdf, .epub, .docx).
            title: Optional title override. Defaults to file stem.
            author: Optional author name.

        Returns:
            IngestionResult object containing output paths and metadata.
        """
        input_path = Path(input_file).resolve()
        logger.info(f"==================================================")
        logger.info(f"Starting Book Ingestion Pipeline for: {input_path.name}")

        book_title = title or input_path.stem.replace("_", " ").title()
        book_author = author or "Unknown Author"
        book_slug = self._slugify(book_title)

        # Step 1: Extract Raw Text
        raw_text = extract_text_from_file(input_path)

        # Step 1b: Strip Gutenberg Legal Preamble Header/Footer
        raw_text = self._strip_gutenberg_preamble(raw_text)

        # Step 2: Normalize Text
        normalized_text = self.normalizer.process(raw_text)

        # Step 3: Remove Headers, Footers, Page Numbers
        cleaned_text = self.header_cleaner.process(normalized_text)

        # Step 4: Split into Chapters
        chapters: List[Chapter] = self.chapter_splitter.split(cleaned_text)

        # Step 5: Compute Metadata & Metrics
        char_count = len(cleaned_text)
        word_count = len(cleaned_text.split())
        line_count = len(cleaned_text.splitlines())

        chapter_data = [chap.to_dict() for chap in chapters]

        metadata = {
          "title": book_title,
          "author": book_author,
          "original_filename": input_path.name,
          "format": input_path.suffix.upper().lstrip("."),
          "character_count": char_count,
          "word_count": word_count,
          "line_count": line_count,
          "chapter_count": len(chapters),
          "chapters": chapter_data,
          "ingestion_timestamp": datetime.now(timezone.utc).isoformat(),
        }

        # Step 6: Write Output Files
        book_output_dir = self.output_base_dir / book_slug
        book_output_dir.mkdir(parents=True, exist_ok=True)

        cleaned_txt_path = book_output_dir / "cleaned.txt"
        metadata_json_path = book_output_dir / "metadata.json"

        with open(cleaned_txt_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        with open(metadata_json_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        logger.info(f"Cleaned text saved to: '{cleaned_txt_path}'")
        logger.info(f"Metadata saved to: '{metadata_json_path}'")
        logger.info(f"Ingestion complete: {word_count} words across {len(chapters)} chapters.")
        logger.info(f"==================================================")

        return IngestionResult(
            book_slug=book_slug,
            cleaned_text_path=cleaned_txt_path,
            metadata_path=metadata_json_path,
            total_words=word_count,
            total_chapters=len(chapters),
            format=input_path.suffix.upper().lstrip("."),
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Book Ingestion Pipeline")
    parser.add_argument("file", type=str, help="Path to input book file (.txt, .pdf, .epub, .docx)")
    parser.add_argument("--title", type=str, default=None, help="Book title override")
    parser.add_argument("--author", type=str, default=None, help="Book author override")

    args = parser.parse_args()

    pipeline = IngestionPipeline()
    res = pipeline.run(Path(args.file), title=args.title, author=args.author)
    print(json.dumps(res.to_dict(), indent=2))

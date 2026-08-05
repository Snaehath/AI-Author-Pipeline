"""
Chapter Segmentation and Boundary Detection Module.

Identifies chapter headings, prologues, epilogues, and scene dividers,
splitting raw text into structured chapter units with character offsets and word counts.
"""

import re
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Ingestion.ChapterSplitter")


@dataclass
class Chapter:
    """Represents a parsed chapter block within a book."""
    chapter_index: int
    title: str
    content: str
    start_char: int
    end_char: int
    word_count: int

    def to_dict(self) -> Dict[str, Any]:
        """Converts Chapter object to dictionary."""
        return asdict(self)


class ChapterSplitter:
    """Detects chapter headings and splits book text into structured chapters."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes ChapterSplitter with regex patterns and fallback parameters.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        default_heading_patterns = [
            r"^\s*(?:CHAPTER|Chapter|CH|Ch\.)\s+(?:[0-9]+|[IVXLCDM]+|[A-Za-z]+)(?::.*|\s+.*)?$",
            r"^\s*(?:PROLOGUE|Prologue|EPILOGUE|Epilogue|PREFACE|Preface|BOOK|Book|PART|Part)\s*(?:[0-9]+|[IVXLCDM]+)?(?::.*|\s+.*)?$",
            r"^\s*\b(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|Seventeen|Eighteen|Nineteen|Twenty)\b\s*$",
        ]
        heading_patterns = self.config.get("heading_patterns", default_heading_patterns)
        self.compiled_heading_patterns = [re.compile(pat, re.MULTILINE) for pat in heading_patterns]
        self.fallback_chunk_words = self.config.get("fallback_chunk_words", 3000)

    def is_chapter_heading(self, line: str) -> bool:
        """Checks if a given line matches any chapter heading regex pattern."""
        line_str = line.strip()
        if not line_str or len(line_str) > 120:
            return False

        for pattern in self.compiled_heading_patterns:
            if pattern.match(line_str):
                return True
        return False

    def split(self, text: str) -> List[Chapter]:
        """Segments text into a list of Chapter objects.

        Args:
            text: Cleaned narrative text string.

        Returns:
            List of Chapter objects.
        """
        logger.info("Starting chapter segmentation...")
        lines = text.split("\n")
        chapter_matches = []

        current_char = 0
        for i, line in enumerate(lines):
            line_len = len(line) + 1  # includes newline character
            if self.is_chapter_heading(line):
                chapter_matches.append({
                    "line_index": i,
                    "title": line.strip(),
                    "char_start": current_char,
                })
            current_char += line_len

        # Fallback if no chapter headings were found
        if not chapter_matches:
            logger.warning("No explicit chapter headings detected. Applying single/fallback chunking strategy.")
            return self._fallback_split(text)

        chapters: List[Chapter] = []

        # Preamble/Intro text before Chapter 1 if present
        first_match_start = chapter_matches[0]["char_start"]
        if first_match_start > 0:
            preamble_content = text[:first_match_start].strip()
            if preamble_content:
                word_cnt = len(preamble_content.split())
                chapters.append(Chapter(
                    chapter_index=1,
                    title="Preamble",
                    content=preamble_content,
                    start_char=0,
                    end_char=first_match_start,
                    word_count=word_cnt,
                ))

        for idx, match in enumerate(chapter_matches):
            chap_num = len(chapters) + 1
            title = match["title"]
            start_pos = match["char_start"]

            if idx + 1 < len(chapter_matches):
                end_pos = chapter_matches[idx + 1]["char_start"]
            else:
                end_pos = len(text)

            chap_content = text[start_pos:end_pos].strip()
            word_cnt = len(chap_content.split())

            chapters.append(Chapter(
                chapter_index=chap_num,
                title=title,
                content=chap_content,
                start_char=start_pos,
                end_char=end_pos,
                word_count=word_cnt,
            ))

        logger.info(f"Successfully segmented text into {len(chapters)} chapters.")
        return chapters

    def _fallback_split(self, text: str) -> List[Chapter]:
        """Fallback chunking method when no explicit chapter headings exist."""
        words = text.split()
        if not words:
            return []

        total_words = len(words)
        chapters: List[Chapter] = []

        # Split into fixed word blocks
        chunk_size = self.fallback_chunk_words
        chunks = [words[i:i + chunk_size] for i in range(0, total_words, chunk_size)]

        current_char = 0
        for idx, chunk in enumerate(chunks, start=1):
            content_str = " ".join(chunk)
            word_cnt = len(chunk)
            end_pos = current_char + len(content_str)

            chapters.append(Chapter(
                chapter_index=idx,
                title=f"Section {idx}",
                content=content_str,
                start_char=current_char,
                end_char=end_pos,
                word_count=word_cnt,
            ))
            current_char = end_pos + 1

        return chapters

"""
Scene Parser Module.

Detects scene transition indicators (***, ---, ###, extra line gaps)
and divides chapters into distinct scenes composed of classified paragraphs.
"""

import re
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional

from AI_Author.parser.paragraph_parser import ParagraphParser, Paragraph
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Parser.SceneParser")


@dataclass
class Scene:
    """Represents a single scene unit within a chapter."""
    scene_index: int
    word_count: int
    paragraphs: List[Paragraph]

    def to_dict(self) -> Dict[str, Any]:
        """Converts Scene object to dictionary."""
        data = asdict(self)
        data["paragraphs"] = [p.to_dict() for p in self.paragraphs]
        return data


class SceneParser:
    """Segments chapter text into structured Scene objects."""

    def __init__(
        self,
        config: Optional[Dict[str, Any]] = None,
        paragraph_parser: Optional[ParagraphParser] = None,
    ):
        """Initializes SceneParser.

        Args:
            config: Optional configuration dictionary.
            paragraph_parser: Optional ParagraphParser instance.
        """
        self.config = config or {}
        default_divider_patterns = [
            r"^\s*[*\-_=#]{3,}\s*$",
            r"^\s*\*\s+\*\s+\*\s*$",
        ]
        divider_patterns = self.config.get("divider_patterns", default_divider_patterns)
        self.compiled_dividers = [re.compile(pat, re.MULTILINE) for pat in divider_patterns]
        self.paragraph_parser = paragraph_parser or ParagraphParser()

    def parse_scenes(self, chapter_text: str) -> List[Scene]:
        """Splits chapter text into scenes and parses paragraph structure.

        Args:
            chapter_text: Full text content of a chapter.

        Returns:
            List of Scene objects.
        """
        raw_scenes = self._split_by_dividers(chapter_text)
        scenes: List[Scene] = []

        for idx, scene_text in enumerate(raw_scenes, start=1):
            paragraphs = self.paragraph_parser.parse_paragraphs(scene_text)
            scene_word_cnt = sum(p.word_count for p in paragraphs)

            scenes.append(Scene(
                scene_index=idx,
                word_count=scene_word_cnt,
                paragraphs=paragraphs,
            ))

        return scenes

    def _split_by_dividers(self, chapter_text: str) -> List[str]:
        """Splits chapter text by matching explicit scene dividers."""
        lines = chapter_text.split("\n")
        scene_blocks = []
        current_block = []

        for line in lines:
            if self._is_scene_divider(line):
                block_str = "\n".join(current_block).strip()
                if block_str:
                    scene_blocks.append(block_str)
                current_block = []
            else:
                current_block.append(line)

        final_str = "\n".join(current_block).strip()
        if final_str:
            scene_blocks.append(final_str)

        return scene_blocks if scene_blocks else [chapter_text.strip()]

    def _is_scene_divider(self, line: str) -> bool:
        """Checks if a single line acts as an explicit scene divider."""
        line_str = line.strip()
        if not line_str:
            return False
        for pattern in self.compiled_dividers:
            if pattern.match(line_str):
                return True
        return False

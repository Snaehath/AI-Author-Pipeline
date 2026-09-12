"""
Paragraph Parser Module.

Segments text blocks into individual paragraphs and classifies each paragraph
as pure narration, pure dialogue, or mixed narrative text.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional

from .dialogue_extractor import DialogueExtractor, DialogueItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Parser.ParagraphParser")


@dataclass
class Paragraph:
    """Represents a single paragraph unit within a scene."""
    paragraph_index: int
    text: str
    type: str  # "narration", "dialogue", or "mixed"
    word_count: int
    has_dialogue: bool
    dialogues: List[DialogueItem]

    def to_dict(self) -> Dict[str, Any]:
        """Converts Paragraph object to dictionary."""
        data = asdict(self)
        data["dialogues"] = [d.to_dict() for d in self.dialogues]
        return data


class ParagraphParser:
    """Parses text blocks into classified Paragraph objects."""

    def __init__(self, dialogue_extractor: Optional[DialogueExtractor] = None):
        """Initializes ParagraphParser.

        Args:
            dialogue_extractor: Optional DialogueExtractor instance.
        """
        self.dialogue_extractor = dialogue_extractor or DialogueExtractor()

    def parse_paragraphs(self, text_block: str) -> List[Paragraph]:
        """Splits text block into paragraphs and extracts dialogue metadata.

        Args:
            text_block: Raw text content of a scene or chapter.

        Returns:
            List of classified Paragraph objects.
        """
        raw_paragraphs = [p.strip() for p in text_block.split("\n\n") if p.strip()]
        paragraphs: List[Paragraph] = []

        for idx, p_text in enumerate(raw_paragraphs, start=1):
            dialogue_items = self.dialogue_extractor.extract_dialogue_items(p_text)
            has_dialogue = len(dialogue_items) > 0
            word_cnt = len(p_text.split())

            # Classify paragraph type
            if not has_dialogue:
                p_type = "narration"
            else:
                # Check if paragraph is purely dialogue inside quotes
                stripped = p_text.strip()
                if stripped.startswith('"') and stripped.endswith('"') and len(dialogue_items) == 1:
                    if len(dialogue_items[0].spoken_text.split()) == word_cnt:
                        p_type = "dialogue"
                    else:
                        p_type = "mixed"
                else:
                    p_type = "mixed"

            paragraphs.append(Paragraph(
                paragraph_index=idx,
                text=p_text,
                type=p_type,
                word_count=word_cnt,
                has_dialogue=has_dialogue,
                dialogues=dialogue_items,
            ))

        return paragraphs

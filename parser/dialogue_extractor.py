"""
Dialogue Extractor Module.

Identifies spoken dialogue inside quotes, isolates speech tags,
and extracts potential speaker hints.
"""

import re
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Parser.DialogueExtractor")


@dataclass
class DialogueItem:
    """Represents a single spoken dialogue element inside a paragraph."""
    spoken_text: str
    speech_tag: str
    speaker_hint: Optional[str]
    quote_char_start: int
    quote_char_end: int
    word_count: int

    def to_dict(self) -> Dict[str, Any]:
        """Converts DialogueItem to dictionary."""
        return asdict(self)


class DialogueExtractor:
    """Parses spoken dialogue and speech tags from text."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes DialogueExtractor.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        default_speech_verbs = [
            "said", "asked", "replied", "whispered", "shouted", "yelled",
            "muttered", "murmured", "exclaimed", "bellowed", "added", "continued",
            "responded", "called", "spoke", "snapped", "grunted", "nodded"
        ]
        self.speech_verbs = set(self.config.get("speech_verbs", default_speech_verbs))
        # Regex matching text enclosed in double quotes: "dialogue text"
        self.double_quote_pattern = re.compile(r'"([^"\n]+)"')

    def extract_dialogue_items(self, paragraph_text: str) -> List[DialogueItem]:
        """Finds all spoken dialogue quotes in a paragraph and extracts metadata.

        Args:
            paragraph_text: Raw text of a single paragraph.

        Returns:
            List of DialogueItem objects.
        """
        dialogue_items: List[DialogueItem] = []

        for match in self.double_quote_pattern.finditer(paragraph_text):
            raw_spoken = match.group(1).strip()
            if not raw_spoken:
                continue

            # Strip trailing clause punctuation (commas, periods) from spoken dialogue text
            spoken_text = raw_spoken.rstrip(",.").strip()

            start_idx = match.start()
            end_idx = match.end()
            word_cnt = len(spoken_text.split())

            # Isolate surrounding speech tag
            speech_tag, speaker_hint = self._extract_speech_tag(paragraph_text, start_idx, end_idx)

            dialogue_items.append(DialogueItem(
                spoken_text=spoken_text,
                speech_tag=speech_tag,
                speaker_hint=speaker_hint,
                quote_char_start=start_idx,
                quote_char_end=end_idx,
                word_count=word_cnt,
            ))

        return dialogue_items

    def _extract_speech_tag(self, text: str, quote_start: int, quote_end: int) -> tuple[str, Optional[str]]:
        """Extracts the non-dialogue sentence context (speech tag) near a quote and infers speaker."""
        tag_parts = []
        # Check text after quote up to clause end
        after_text = text[quote_end:].split(".")[0].strip()
        if after_text.startswith((",", " -", "-")):
            after_text = after_text.lstrip(", -")

        # Check text before quote
        before_text = text[:quote_start].split(".")[-1].strip()

        combined_context = f"{before_text} {after_text}".strip()
        speaker_hint = self._infer_speaker(combined_context)

        return combined_context, speaker_hint

    def _infer_speaker(self, context_text: str) -> Optional[str]:
        """Infers candidate speaker name from speech tag context."""
        words = re.findall(r"\b[A-Z][a-z]+\b", context_text)
        # Filter out common sentence starters if any
        candidates = [w for w in words if w.lower() not in {"the", "a", "an", "they", "he", "she", "it"}]
        if candidates:
            return candidates[0]
        return None

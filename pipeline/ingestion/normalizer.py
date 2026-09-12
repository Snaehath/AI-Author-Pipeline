"""
Text Normalization & Cleanup Module.

Provides Unicode standardization, smart quote normalization, whitespace cleanup,
and OCR hyphenation/error correction.
"""

import re
import unicodedata
from typing import Dict, Any, Optional
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Ingestion.Normalizer")


class TextNormalizer:
    """Normalizes raw text into clean, standardized narrative text."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes normalizer with options.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.unicode_form = self.config.get("unicode_form", "NFKC")
        self.normalize_unicode_enabled = self.config.get("normalize_unicode", True)
        self.normalize_quotes_enabled = self.config.get("normalize_quotes", True)
        self.fix_ocr_hyphenation_enabled = self.config.get("fix_ocr_hyphenation", True)
        self.max_blank_lines = self.config.get("max_consecutive_blank_lines", 2)

    def normalize_unicode(self, text: str) -> str:
        """Standardizes Unicode characters to NFKC representation."""
        if not self.normalize_unicode_enabled:
            return text
        return unicodedata.normalize(self.unicode_form, text)

    def normalize_quotes_and_punctuation(self, text: str) -> str:
        """Converts curly/smart quotes and special typography into standard characters."""
        if not self.normalize_quotes_enabled:
            return text

        replacements = {
            "“": '"',
            "”": '"',
            "„": '"',
            "«": '"',
            "»": '"',
            "‘": "'",
            "’": "'",
            "`": "'",
            "´": "'",
            "–": "-",  # en dash
            "—": " - ", # em dash normalized with spacing for clean reading
            "…": "...",  # ellipsis
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    def fix_ocr_hyphenation(self, text: str) -> str:
        """Fixes word hyphens split across line endings caused by OCR or PDF page wrapping.

        Example:
            'develo-\npment' -> 'development'
        """
        if not self.fix_ocr_hyphenation_enabled:
            return text

        # Regex matches lowercase word ending with hyphen, newline, and starting lowercase word
        pattern = re.compile(r"([a-z]+)-\s*\n\s*([a-z]+)")
        return pattern.sub(r"\1\2", text)

    def normalize_whitespace(self, text: str) -> str:
        """Normalizes tabs, line endings, trailing spaces, and excessive line breaks."""
        # Standardize line endings to \n
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Replace non-breaking spaces with standard space
        text = text.replace("\u00a0", " ")

        # Remove trailing spaces from each line
        lines = [re.sub(r"[ \t]+$", "", line) for line in text.split("\n")]
        text = "\n".join(lines)

        # Collapse 3 or more consecutive newlines into double newlines (paragraph boundary)
        max_newlines = "\n" * (self.max_blank_lines + 1)
        target_newlines = "\n" * 2
        text = re.sub(rf"\n{{{self.max_blank_lines + 1},}}", target_newlines, text)

        return text.strip()

    def process(self, raw_text: str) -> str:
        """Executes full normalization pipeline on raw text input.

        Args:
            raw_text: The input text to normalize.

        Returns:
            Fully cleaned and normalized text string.
        """
        logger.info("Starting text normalization...")
        text = self.normalize_unicode(raw_text)
        text = self.normalize_quotes_and_punctuation(text)
        text = self.fix_ocr_hyphenation(text)
        text = self.normalize_whitespace(text)
        logger.info("Text normalization completed.")
        return text

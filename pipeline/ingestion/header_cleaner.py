"""
Header, Footer, and Page Number Cleaner.

Detects and strips standalone page numbers, running headers, and running footers
from ingested book text.
"""

import re
from typing import List, Dict, Any, Optional
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Ingestion.HeaderCleaner")


class HeaderCleaner:
    """Strips headers, footers, and page numbers from document text."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes cleaner settings.

        Args:
            config: Configuration dictionary.
        """
        self.config = config or {}
        self.remove_page_numbers_enabled = self.config.get("remove_page_numbers", True)
        self.remove_headers_footers_enabled = self.config.get("remove_headers_footers", True)

        # Regex patterns for standalone page numbers
        self.page_number_patterns = [
            re.compile(r"^\s*-\s*\d+\s*-\s*$"),               # - 45 -
            re.compile(r"^\s*Page\s+\d+\s*$", re.IGNORECASE), # Page 45
            re.compile(r"^\s*Page\s+\d+\s+of\s+\d+\s*$", re.IGNORECASE), # Page 45 of 300
            re.compile(r"^\s*\d+\s*$"),                       # Standalone 45
            re.compile(r"^\s*[IVXLCDM]+\s*$"),                # Standalone Roman numeral IV
        ]

    def is_page_number_line(self, line: str) -> bool:
        """Determines whether a single line is a page number indicator."""
        line_str = line.strip()
        if not line_str:
            return False

        for pattern in self.page_number_patterns:
            if pattern.match(line_str):
                return True
        return False

    def remove_repeating_headers_footers(self, text: str) -> str:
        """Finds lines that repeat across pages and removes them if they act as headers/footers."""
        if not self.remove_headers_footers_enabled:
            return text

        lines = text.split("\n")
        line_counts: Dict[str, int] = {}
        candidate_lines = []

        # Count frequencies of short lines (potential headers/footers are usually < 80 chars)
        for line in lines:
            stripped = line.strip()
            if 3 <= len(stripped) <= 80:
                line_counts[stripped] = line_counts.get(stripped, 0) + 1

        # High frequency lines relative to overall length (e.g. repeated 5+ times)
        threshold = max(4, len(lines) // 200)
        repeating_headers = {
            line_text for line_text, count in line_counts.items()
            if count >= threshold and not self._is_legitimate_prose(line_text)
        }

        if repeating_headers:
            logger.info(f"Identified {len(repeating_headers)} repeating header/footer patterns.")

        cleaned_lines = []
        for line in lines:
            if line.strip() in repeating_headers:
                continue
            cleaned_lines.append(line)

        return "\n".join(cleaned_lines)

    def _is_legitimate_prose(self, line: str) -> bool:
        """Checks if a line looks like normal prose (e.g. ends with punctuation or starts dialogue)."""
        stripped = line.strip()
        if stripped.endswith((".", "?", "!", '"', "'", ";")):
            return True
        if stripped.startswith(('"', "'", "“", "‘", "- ")):
            return True
        return False

    def process(self, text: str) -> str:
        """Cleans headers, footers, and page numbers from text string.

        Args:
            text: Normalized book text string.

        Returns:
            Text string with header/footer artifacts removed.
        """
        logger.info("Starting header/footer and page number removal...")
        lines = text.split("\n")
        filtered_lines = []

        for line in lines:
            if self.remove_page_numbers_enabled and self.is_page_number_line(line):
                continue
            filtered_lines.append(line)

        cleaned_text = "\n".join(filtered_lines)
        cleaned_text = self.remove_repeating_headers_footers(cleaned_text)

        logger.info("Header/footer removal completed.")
        return cleaned_text

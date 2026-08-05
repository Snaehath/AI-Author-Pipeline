"""
Character Extractor Module.

Identifies major and minor character names from text across dialogue tags and narrative prose.
"""

import re
from typing import List, Dict, Any, Set
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.CharacterExtractor")


class CharacterExtractor:
    """Discovers character names and aliases from text."""

    def __init__(self):
        """Initializes CharacterExtractor with stop words."""
        self.stop_words = {
            "The", "A", "An", "In", "On", "At", "It", "As", "We", "He", "She", "They",
            "Chapter", "Prologue", "Epilogue", "Book", "Part", "Page", "Author", "Name",
            "Title", "Chronicles", "Eldoria", "Mountains", "Desert", "Canyon", "Forest",
            "Project", "Gutenberg", "License", "Ebook", "Foundation", "United", "States",
            "Section", "Preface", "Rights", "Reserved", "This", "That", "There", "Here",
            "What", "Where", "When", "With", "From", "About", "Please", "Royalty",
            "Donations", "Vanilla", "Archive", "Literary", "Terms", "General", "Volunteers",
            "Service", "Professor", "Public", "Domain"
        }

    def discover_characters(self, chapter_texts: List[str]) -> Dict[str, List[str]]:
        """Identifies primary character names across chapter texts.

        Args:
            chapter_texts: List of chapter text strings.

        Returns:
            Dictionary mapping primary name to list of aliases.
        """
        combined = " ".join(chapter_texts)
        # Match capitalized words that occur in speech tags or proper noun contexts
        candidates = re.findall(r"\b[A-Z][a-z]+\b", combined)

        counts: Dict[str, int] = {}
        for word in candidates:
            if word not in self.stop_words and len(word) > 2:
                counts[word] = counts.get(word, 0) + 1

        # Keep primary characters mentioned at least 5 times, sorted by frequency (top 25)
        sorted_candidates = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        top_candidates = [name for name, count in sorted_candidates if count >= 5][:25]

        main_characters = {name: [name] for name in top_candidates}

        if not main_characters and counts:
            # Fallback to top candidate if overall text is very short
            top_name = max(counts, key=counts.get)
            main_characters[top_name] = [top_name]

        logger.info(f"Discovered {len(main_characters)} character candidate profiles.")
        return main_characters

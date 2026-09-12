"""
Character Analyzer Orchestrator Module.

Loads parsed chapter outputs from Module 2 (outputs/<book_slug>/chapters/chapter_XX.json),
executes comprehensive character profile & arc analysis, and outputs outputs/<book_slug>/character_analysis.json.
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

from AI_Author.pipeline.analyzer.pov_detector import KnowledgeItem
from AI_Author.pipeline.analyzer.character_extractor import CharacterExtractor
from AI_Author.pipeline.analyzer.trait_extractor import TraitExtractor
from AI_Author.pipeline.analyzer.goal_relationship_mapper import GoalRelationshipMapper
from AI_Author.pipeline.analyzer.arc_tracker import ArcTracker
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.CharacterAnalyzer")


@dataclass
class CharacterProfile:
    """Represents a complete character analysis profile."""
    name: str
    aliases: List[str]
    appearance: List[KnowledgeItem]
    personality: List[KnowledgeItem]
    goals: List[KnowledgeItem]
    motivations: List[KnowledgeItem]
    character_arc: KnowledgeItem
    growth: KnowledgeItem
    strengths: List[KnowledgeItem]
    weaknesses: List[KnowledgeItem]

    def to_dict(self) -> Dict[str, Any]:
        """Converts CharacterProfile to dictionary."""
        return {
            "name": self.name,
            "aliases": self.aliases,
            "appearance": [a.to_dict() for a in self.appearance],
            "personality": [p.to_dict() for p in self.personality],
            "goals": [g.to_dict() for g in self.goals],
            "motivations": [m.to_dict() for m in self.motivations],
            "character_arc": self.character_arc.to_dict(),
            "growth": self.growth.to_dict(),
            "strengths": [s.to_dict() for s in self.strengths],
            "weaknesses": [w.to_dict() for w in self.weaknesses],
        }


class CharacterAnalyzer:
    """Orchestrates complete character profile and arc analysis."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initializes CharacterAnalyzer with sub-analyzers.

        Args:
            config_path: Path to character_config.json.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "character_config.json")
        self.config = self._load_config()

        self.character_extractor = CharacterExtractor()
        self.trait_extractor = TraitExtractor(self.config)
        self.goal_mapper = GoalRelationshipMapper(self.config)
        self.arc_tracker = ArcTracker()

    def _load_config(self) -> Dict[str, Any]:
        """Loads character configuration JSON if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded character config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read character config file ({e}). Using defaults.")
        return {}

    def analyze_book_directory(self, book_dir: Path) -> Dict[str, Any]:
        """Analyzes all characters across a book directory.

        Args:
            book_dir: Path to book output directory (e.g. outputs/sample_novel).

        Returns:
            Dictionary containing full character_analysis.json content.
        """
        book_path = Path(book_dir).resolve()
        chapters_dir = book_path / "chapters"

        if not chapters_dir.exists():
            raise FileNotFoundError(f"Missing parsed chapters directory at: {chapters_dir}")

        chapter_files = sorted(list(chapters_dir.glob("chapter_*.json")))
        if not chapter_files:
            raise FileNotFoundError(f"No chapter_XX.json files found in: {chapters_dir}")

        logger.info(f"==================================================")
        logger.info(f"Starting Character Analysis for: '{book_path.name}'")

        # Blacklist of common non-character words and Gutenberg legal header terms
        IGNORE_NAMES = {
            "project", "gutenberg", "license", "ebook", "foundation", "united", "states",
            "section", "chapter", "preface", "title", "author", "rights", "reserved",
            "this", "that", "there", "here", "what", "where", "when", "with", "from",
            "about", "please", "royalty", "donations", "vanilla", "archive", "literary",
            "terms", "general", "volunteers", "service", "professor", "public", "domain"
        }

        chapter_texts: List[str] = []
        for c_file in chapter_files:
            with open(c_file, "r", encoding="utf-8") as f:
                chap_json = json.load(f)
            c_text_parts = []
            for scene in chap_json.get("scenes", []):
                for p in scene.get("paragraphs", []):
                    c_text_parts.append(p["text"])
            chapter_texts.append("\n\n".join(c_text_parts))

        entire_text = "\n\n".join(chapter_texts)

        # Step 1: Discover Characters
        character_map = self.character_extractor.discover_characters(chapter_texts)

        # Step 2: Build Character Profiles
        profiles: List[CharacterProfile] = []
        char_names = list(character_map.keys())

        for name, aliases in character_map.items():
            appearance = self.trait_extractor.extract_appearance(name, entire_text)
            personality = self.trait_extractor.extract_personality(name, entire_text)
            goals = self.goal_mapper.extract_goals(name, entire_text)
            motivations = self.goal_mapper.extract_motivations(name, entire_text)
            arc, growth = self.arc_tracker.track_character_arc(name, chapter_texts)
            strengths = self.trait_extractor.extract_strengths(name, entire_text)
            weaknesses = self.trait_extractor.extract_weaknesses(name, entire_text)

            profiles.append(CharacterProfile(
                name=name,
                aliases=aliases,
                appearance=appearance,
                personality=personality,
                goals=goals,
                motivations=motivations,
                character_arc=arc,
                growth=growth,
                strengths=strengths,
                weaknesses=weaknesses,
            ))
            logger.info(f"Built character profile for: '{name}'")

        # Step 3: Map Relationships
        relationships = self.goal_mapper.map_relationships(char_names, entire_text)

        output_data = {
            "book_title": book_path.name.replace("_", " ").title(),
            "total_characters_identified": len(profiles),
            "relationships": relationships,
            "characters": [p.to_dict() for p in profiles],
        }

        # Write output file
        out_filepath = book_path / "character_analysis.json"
        with open(out_filepath, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Character Analysis saved to: '{out_filepath}'")
        logger.info(f"==================================================")

        return output_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Character Analyzer")
    parser.add_argument("book_dir", type=str, help="Path to processed book output directory (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    analyzer = CharacterAnalyzer()
    res = analyzer.analyze_book_directory(Path(args.book_dir))
    print(f"Successfully analyzed {res['total_characters_identified']} characters.")

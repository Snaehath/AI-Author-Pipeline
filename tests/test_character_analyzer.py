"""
Unit and Integration Tests for Module 4 (Character Analyzer).

Executes automated checks on character discovery, trait extraction, goal/relationship mapping,
arc tracking, and end-to-end character_analysis.json generation.
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.pipeline.analyzer.character_extractor import CharacterExtractor
from AI_Author.pipeline.analyzer.trait_extractor import TraitExtractor
from AI_Author.pipeline.analyzer.goal_relationship_mapper import GoalRelationshipMapper
from AI_Author.pipeline.analyzer.arc_tracker import ArcTracker
from AI_Author.pipeline.analyzer.character_analyzer import CharacterAnalyzer
from AI_Author.pipeline.ingestion.pipeline import IngestionPipeline
from AI_Author.pipeline.parser.chapter_parser import ChapterParser


class TestCharacterExtractor(unittest.TestCase):
    """Unit tests for CharacterExtractor."""

    def setUp(self):
        self.extractor = CharacterExtractor()

    def test_discover_characters(self):
        chapters = [
            "Aria adjusted her leather cloak. Kane stood beside Aria.",
            "Kane said to Aria, 'We must find the hidden key.'"
        ]
        chars = self.extractor.discover_characters(chapters)
        self.assertIn("Aria", chars)
        self.assertIn("Kane", chars)


class TestTraitExtractor(unittest.TestCase):
    """Unit tests for TraitExtractor."""

    def setUp(self):
        self.extractor = TraitExtractor()

    def test_appearance_extraction(self):
        text = "Aria adjusted her leather cloak and held her brass lantern."
        items = self.extractor.extract_appearance("Aria", text)
        self.assertGreater(len(items), 0)
        self.assertEqual(items[0].confidence, 0.88)
        self.assertIn("Aria", items[0].evidence)

    def test_personality_extraction(self):
        text = "Kane carefully warned her, 'We should make camp before nightfall.'"
        items = self.extractor.extract_personality("Kane", text)
        self.assertGreater(len(items), 0)
        self.assertEqual(items[0].value, "Cautious")


class TestGoalRelationshipMapper(unittest.TestCase):
    """Unit tests for GoalRelationshipMapper."""

    def setUp(self):
        self.mapper = GoalRelationshipMapper()

    def test_relationship_mapping(self):
        text = "Aria and Kane walked together past the twin pillars."
        rel = self.mapper.map_relationships(["Aria", "Kane"], text)
        self.assertEqual(len(rel), 1)
        self.assertEqual(rel[0]["character_a"], "Aria")
        self.assertEqual(rel[0]["character_b"], "Kane")
        self.assertEqual(rel[0]["relationship_type"], "Traveling Companions / Allies")


class TestCharacterAnalyzerIntegration(unittest.TestCase):
    """Integration test for full CharacterAnalyzer pipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"

        # Step 1: Run Ingestion
        self.ingestion_pipeline = IngestionPipeline(output_base_dir=self.output_dir)
        sample_book = Path(self.temp_dir.name) / "sample.txt"
        sample_content = (
            "The Legend of Kane\nBy Jane Doe\n\n"
            "CHAPTER 1: The Trail\n\n"
            "Aria adjusted her leather cloak while Kane prepared the lantern.\n\n"
            '"We must reach the twin pillars," Aria said.\n\n'
            "CHAPTER 2: The Chamber\n\n"
            "Inside the ancient room, Kane found the artifact."
        )
        with open(sample_book, "w", encoding="utf-8") as f:
            f.write(sample_content)

        ingestion_res = self.ingestion_pipeline.run(sample_book, title="The Legend of Kane", author="Jane Doe")
        self.book_dir = ingestion_res.cleaned_text_path.parent

        # Step 2: Run Chapter Parser
        self.chapter_parser = ChapterParser()
        self.chapter_parser.parse_book_directory(self.book_dir)

        # Step 3: Character Analyzer
        self.character_analyzer = CharacterAnalyzer()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_character_analysis(self):
        analysis_json = self.character_analyzer.analyze_book_directory(self.book_dir)

        self.assertIn("characters", analysis_json)
        self.assertIn("relationships", analysis_json)
        self.assertGreater(analysis_json["total_characters_identified"], 0)

        char_analysis_file = self.book_dir / "character_analysis.json"
        self.assertTrue(char_analysis_file.exists())

        # Verify contract schema compliance: value, confidence, evidence
        char_aria = analysis_json["characters"][0]
        self.assertIn("name", char_aria)
        self.assertIn("character_arc", char_aria)
        self.assertIn("value", char_aria["character_arc"])
        self.assertIn("confidence", char_aria["character_arc"])
        self.assertIn("evidence", char_aria["character_arc"])


if __name__ == "__main__":
    unittest.main()

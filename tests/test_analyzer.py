"""
Unit and Integration Tests for Module 3 (Story Analyzer).

Executes automated checks on POV detectors, tone/mood analyzers, conflict classifiers,
foreshadowing detectors, and end-to-end story_analysis.json generation.
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

from AI_Author.pipeline.analyzer.pov_detector import POVDetector
from AI_Author.pipeline.analyzer.tone_mood_analyzer import ToneMoodAnalyzer
from AI_Author.pipeline.analyzer.conflict_scene_analyzer import ConflictSceneAnalyzer
from AI_Author.pipeline.analyzer.foreshadow_twist_analyzer import ForeshadowTwistAnalyzer
from AI_Author.pipeline.analyzer.story_analyzer import StoryAnalyzer
from AI_Author.pipeline.ingestion.pipeline import IngestionPipeline
from AI_Author.pipeline.parser.chapter_parser import ChapterParser


class TestPOVDetector(unittest.TestCase):
    """Unit tests for POVDetector."""

    def setUp(self):
        self.detector = POVDetector()

    def test_first_person_pov(self):
        text = "I adjusted my heavy cloak as I walked into the dark forest."
        item = self.detector.detect_pov(text)
        self.assertEqual(item.value, "First-Person")
        self.assertGreater(item.confidence, 0.70)
        self.assertIn("cloak", item.evidence)

    def test_third_person_pov(self):
        text = "Aria adjusted her leather cloak as she walked into the canyon."
        item = self.detector.detect_pov(text)
        self.assertEqual(item.value, "Third-Person Limited")
        self.assertGreater(item.confidence, 0.70)
        self.assertIn("Aria", item.evidence)


class TestToneMoodAnalyzer(unittest.TestCase):
    """Unit tests for ToneMoodAnalyzer."""

    def setUp(self):
        self.analyzer = ToneMoodAnalyzer()

    def test_tone_detection(self):
        text = "The cold mountain wind howled through the canyon as danger lurked in the dark shadows."
        item = self.analyzer.analyze_tone(text)
        self.assertEqual(item.value, "Suspenseful")
        self.assertGreater(item.confidence, 0.70)
        self.assertIsNotNone(item.evidence)

    def test_pacing_detection(self):
        text = "He ran. She jumped. They hid. Quick action."
        item = self.analyzer.analyze_pacing(text, dialogue_ratio=0.5)
        self.assertEqual(item.value, "Fast-Paced")


class TestConflictSceneAnalyzer(unittest.TestCase):
    """Unit tests for ConflictSceneAnalyzer."""

    def setUp(self):
        self.analyzer = ConflictSceneAnalyzer()

    def test_conflict_nature(self):
        text = "The freezing blizzard and mountain storm threatened to sweep them off the cliff."
        item = self.analyzer.analyze_conflict(text)
        self.assertEqual(item.value, "Person vs Nature")
        self.assertGreater(item.confidence, 0.70)

    def test_character_introductions(self):
        text = "Kane looked up at the mountains while Aria checked her map."
        intros = self.analyzer.extract_character_introductions(text)
        names = [i.value for i in intros]
        self.assertIn("Kane", names)
        self.assertIn("Aria", names)


class TestForeshadowTwistAnalyzer(unittest.TestCase):
    """Unit tests for ForeshadowTwistAnalyzer."""

    def setUp(self):
        self.analyzer = ForeshadowTwistAnalyzer()

    def test_foreshadowing_detection(self):
        text = "Little did he know, a dark shadow was yet to come."
        item = self.analyzer.detect_foreshadowing(text)
        self.assertEqual(item.value, "Explicit Foreshadowing")
        self.assertGreater(item.confidence, 0.80)

    def test_theme_extraction(self):
        text = "They searched for the ancient artifact marked on the map."
        themes = self.analyzer.extract_themes(text)
        theme_names = [t.value for t in themes]
        self.assertIn("Discovery", theme_names)


class TestStoryAnalyzerIntegration(unittest.TestCase):
    """Integration test for full StoryAnalyzer pipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"

        # Step 1: Run Ingestion
        self.ingestion_pipeline = IngestionPipeline(output_base_dir=self.output_dir)
        sample_book = Path(self.temp_dir.name) / "sample.txt"
        sample_content = (
            "The Crystal of Shadows\nBy Jane Doe\n\n"
            "CHAPTER 1: The Canyon\n\n"
            "Aria adjusted her leather cloak as the cold mountain wind howled through the canyon.\n\n"
            '"We should make camp," Kane said.\n\n'
            "CHAPTER 2: The Temple\n\n"
            "Inside the ancient ruins, glowing runes shimmered on the pedestal."
        )
        with open(sample_book, "w", encoding="utf-8") as f:
            f.write(sample_content)

        ingestion_res = self.ingestion_pipeline.run(sample_book, title="The Crystal of Shadows", author="Jane Doe")
        self.book_dir = ingestion_res.cleaned_text_path.parent

        # Step 2: Run Chapter Parser
        self.chapter_parser = ChapterParser()
        self.chapter_parser.parse_book_directory(self.book_dir)

        # Step 3: Story Analyzer
        self.story_analyzer = StoryAnalyzer()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_story_analysis(self):
        analysis_json = self.story_analyzer.analyze_book_directory(self.book_dir)

        self.assertIn("overall_narrative_pov", analysis_json)
        self.assertIn("chapter_analyses", analysis_json)
        self.assertEqual(len(analysis_json["chapter_analyses"]), 3)

        story_analysis_file = self.book_dir / "story_analysis.json"
        self.assertTrue(story_analysis_file.exists())

        # Verify contract schema compliance: value, confidence, evidence
        chap_1 = analysis_json["chapter_analyses"][1]
        self.assertIn("value", chap_1["tone"])
        self.assertIn("confidence", chap_1["tone"])
        self.assertIn("evidence", chap_1["tone"])


if __name__ == "__main__":
    unittest.main()

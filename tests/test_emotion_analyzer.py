"""
Unit and Integration Tests for Module 6 (Emotion Analyzer).

Executes automated checks on valence & intensity calculators, emotion timeline trackers,
and end-to-end emotion_analysis.json generation.
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

from AI_Author.analyzer.valence_intensity_calculator import ValenceIntensityCalculator
from AI_Author.analyzer.emotion_timeline_tracker import EmotionTimelineTracker
from AI_Author.analyzer.emotion_analyzer import EmotionAnalyzer
from AI_Author.ingestion.pipeline import IngestionPipeline
from AI_Author.parser.chapter_parser import ChapterParser


class TestValenceIntensityCalculator(unittest.TestCase):
    """Unit tests for ValenceIntensityCalculator."""

    def setUp(self):
        self.calculator = ValenceIntensityCalculator()

    def test_positive_valence(self):
        text = "The glowing light brought hope, triumph, and peace to the safe kingdom."
        val, item = self.calculator.calculate_valence(text)
        self.assertGreater(val, 0.0)
        self.assertGreater(item.confidence, 0.70)

    def test_negative_valence(self):
        text = "The dark stormy night brought cold shadows, danger, and fear."
        val, item = self.calculator.calculate_valence(text)
        self.assertLess(val, 0.0)
        self.assertGreater(item.confidence, 0.70)

    def test_high_intensity(self):
        text = "The blizzard howled frantically as the colossal creature attacked!"
        intensity, item = self.calculator.calculate_intensity(text)
        self.assertGreater(intensity, 0.60)


class TestEmotionTimelineTracker(unittest.TestCase):
    """Unit tests for EmotionTimelineTracker."""

    def setUp(self):
        self.tracker = EmotionTimelineTracker()

    def test_dominant_emotion_classification(self):
        text = "The glowing artifact shone brightly upon the pedestal."
        item = self.tracker.classify_dominant_emotion(valence=0.8, intensity=0.9, text=text)
        self.assertEqual(item.value, "Wonder / Awe & Triumph")

    def test_shift_trigger(self):
        text = "Suddenly, they reached the glowing pedestal of the artifact."
        item = self.tracker.detect_shift_trigger(text)
        self.assertIn("Narrative Trigger", item.value)


class TestEmotionAnalyzerIntegration(unittest.TestCase):
    """Integration test for full EmotionAnalyzer pipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"

        # Step 1: Run Ingestion
        self.ingestion_pipeline = IngestionPipeline(output_base_dir=self.output_dir)
        sample_book = Path(self.temp_dir.name) / "sample.txt"
        sample_content = (
            "The Emotional Journey\nBy Jane Doe\n\n"
            "CHAPTER 1: The Storm\n\n"
            "The cold wind howled and dark shadows threatened danger.\n\n"
            "CHAPTER 2: The Triumph\n\n"
            "The glowing light of the artifact brought peace, hope, and victory to the kingdom."
        )
        with open(sample_book, "w", encoding="utf-8") as f:
            f.write(sample_content)

        ingestion_res = self.ingestion_pipeline.run(sample_book, title="The Emotional Journey", author="Jane Doe")
        self.book_dir = ingestion_res.cleaned_text_path.parent

        # Step 2: Run Chapter Parser
        self.chapter_parser = ChapterParser()
        self.chapter_parser.parse_book_directory(self.book_dir)

        # Step 3: Emotion Analyzer
        self.emotion_analyzer = EmotionAnalyzer()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_emotion_analysis(self):
        analysis_json = self.emotion_analyzer.analyze_book_directory(self.book_dir)

        self.assertIn("emotion_timeline", analysis_json)
        self.assertIn("overall_emotional_arc", analysis_json)
        self.assertEqual(analysis_json["total_timeline_points"], 3)

        emotion_file = self.book_dir / "emotion_analysis.json"
        self.assertTrue(emotion_file.exists())

        # Verify contract schema compliance: value, confidence, evidence
        first_point = analysis_json["emotion_timeline"][0]
        self.assertIn("dominant_emotion", first_point)
        self.assertIn("value", first_point["dominant_emotion"])
        self.assertIn("confidence", first_point["dominant_emotion"])
        self.assertIn("evidence", first_point["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()

"""
Unit and Integration Tests for Module 5 (Dialogue Analyzer).

Executes automated checks on dialogue emotion classifiers, conflict detectors,
speech style analyzers, and end-to-end dialogue_analysis.json generation.
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

from AI_Author.pipeline.analyzer.dialogue_emotion_analyzer import DialogueEmotionAnalyzer
from AI_Author.pipeline.analyzer.speech_style_analyzer import SpeechStyleAnalyzer
from AI_Author.pipeline.analyzer.dialogue_analyzer import DialogueAnalyzer
from AI_Author.pipeline.ingestion.pipeline import IngestionPipeline
from AI_Author.pipeline.parser.chapter_parser import ChapterParser


class TestDialogueEmotionAnalyzer(unittest.TestCase):
    """Unit tests for DialogueEmotionAnalyzer."""

    def setUp(self):
        self.analyzer = DialogueEmotionAnalyzer()

    def test_emotion_urgent(self):
        spoken = "We should make camp before nightfall"
        tag = "Kane said"
        item = self.analyzer.analyze_dialogue_emotion(spoken, tag)
        self.assertEqual(item.value, "Urgent / Cautious")
        self.assertGreater(item.confidence, 0.70)

    def test_conflict_inquiry(self):
        spoken = "Is anyone inside?"
        tag = "Kane asked"
        item = self.analyzer.analyze_dialogue_conflict(spoken, tag)
        self.assertEqual(item.value, "Inquiry / Questioning")
        self.assertGreater(item.confidence, 0.85)


class TestSpeechStyleAnalyzer(unittest.TestCase):
    """Unit tests for SpeechStyleAnalyzer."""

    def setUp(self):
        self.analyzer = SpeechStyleAnalyzer()

    def test_speech_style_imperative(self):
        spoken = "Follow me through the tunnel"
        item = self.analyzer.analyze_speech_style(spoken)
        self.assertEqual(item.value, "Imperative / Advice")

    def test_dialogue_length_brief(self):
        spoken = "Let us proceed"
        item = self.analyzer.analyze_dialogue_length(spoken)
        self.assertEqual(item.value, "Brief (3 words)")


class TestDialogueAnalyzerIntegration(unittest.TestCase):
    """Integration test for full DialogueAnalyzer pipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"

        # Step 1: Run Ingestion
        self.ingestion_pipeline = IngestionPipeline(output_base_dir=self.output_dir)
        sample_book = Path(self.temp_dir.name) / "sample.txt"
        sample_content = (
            "The Dialogue Quest\nBy Jane Doe\n\n"
            "CHAPTER 1: The Encounter\n\n"
            '"We must find the hidden entrance," Aria said.\n\n'
            '"Are you sure it is safe?" Kane asked.'
        )
        with open(sample_book, "w", encoding="utf-8") as f:
            f.write(sample_content)

        ingestion_res = self.ingestion_pipeline.run(sample_book, title="The Dialogue Quest", author="Jane Doe")
        self.book_dir = ingestion_res.cleaned_text_path.parent

        # Step 2: Run Chapter Parser
        self.chapter_parser = ChapterParser()
        self.chapter_parser.parse_book_directory(self.book_dir)

        # Step 3: Dialogue Analyzer
        self.dialogue_analyzer = DialogueAnalyzer()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_dialogue_analysis(self):
        analysis_json = self.dialogue_analyzer.analyze_book_directory(self.book_dir)

        self.assertIn("dialogues", analysis_json)
        self.assertIn("dialogue_metrics_summary", analysis_json)
        self.assertEqual(analysis_json["total_dialogues_analyzed"], 2)

        dialogue_file = self.book_dir / "dialogue_analysis.json"
        self.assertTrue(dialogue_file.exists())

        # Verify contract schema compliance: value, confidence, evidence
        first_turn = analysis_json["dialogues"][0]
        self.assertIn("speaker", first_turn)
        self.assertIn("emotion", first_turn)
        self.assertIn("value", first_turn["emotion"])
        self.assertIn("confidence", first_turn["emotion"])
        self.assertIn("evidence", first_turn["emotion"])


if __name__ == "__main__":
    unittest.main()

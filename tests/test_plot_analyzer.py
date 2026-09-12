"""
Unit and Integration Tests for Module 7 (Plot Analyzer).

Executes automated checks on 8-point story structure classifiers, milestone mappers,
and end-to-end plot_analysis.json generation.
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

from AI_Author.pipeline.analyzer.plot_point_classifier import PlotPointClassifier
from AI_Author.pipeline.analyzer.plot_analyzer import PlotAnalyzer
from AI_Author.pipeline.ingestion.pipeline import IngestionPipeline
from AI_Author.pipeline.parser.chapter_parser import ChapterParser


class TestPlotPointClassifier(unittest.TestCase):
    """Unit tests for PlotPointClassifier."""

    def setUp(self):
        self.classifier = PlotPointClassifier()

    def test_milestone_classification(self):
        chapters = [
            {"scenes": [{"paragraphs": [{"text": "Beginning in the cold canyon."}]}]},
            {"scenes": [{"paragraphs": [{"text": "Entering the ancient cavern arches."}]}]},
            {"scenes": [{"paragraphs": [{"text": "Finding the glowing artifact on the pedestal."}]}]},
            {"scenes": [{"paragraphs": [{"text": "Securing victory for the kingdom safe once more."}]}]},
            {"scenes": [{"paragraphs": [{"text": "EPILOGUE: But a new shadow stirs in the dark."}]}]},
        ]
        milestones = self.classifier.classify_plot_milestones(chapters)

        self.assertIn("hook", milestones)
        self.assertIn("midpoint", milestones)
        self.assertIn("climax", milestones)
        self.assertIn("resolution", milestones)
        self.assertIn("epilogue", milestones)
        self.assertEqual(milestones["epilogue"].confidence, 0.95)


class TestPlotAnalyzerIntegration(unittest.TestCase):
    """Integration test for full PlotAnalyzer pipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"

        # Step 1: Run Ingestion
        self.ingestion_pipeline = IngestionPipeline(output_base_dir=self.output_dir)
        sample_book = Path(self.temp_dir.name) / "sample.txt"
        sample_content = (
            "The Plot Quest\nBy Jane Doe\n\n"
            "CHAPTER 1: The Trail\n\n"
            "Cold wind howled as Aria started her quest.\n\n"
            "CHAPTER 2: The Pedestal\n\n"
            "Inside the ancient chamber, Kane found the glowing artifact on the obsidian pedestal.\n\n"
            "EPILOGUE\n\n"
            "A new shadow began to stir in the dark."
        )
        with open(sample_book, "w", encoding="utf-8") as f:
            f.write(sample_content)

        ingestion_res = self.ingestion_pipeline.run(sample_book, title="The Plot Quest", author="Jane Doe")
        self.book_dir = ingestion_res.cleaned_text_path.parent

        # Step 2: Run Chapter Parser
        self.chapter_parser = ChapterParser()
        self.chapter_parser.parse_book_directory(self.book_dir)

        # Step 3: Plot Analyzer
        self.plot_analyzer = PlotAnalyzer()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_plot_analysis(self):
        analysis_json = self.plot_analyzer.analyze_book_directory(self.book_dir)

        self.assertIn("plot_points", analysis_json)
        self.assertIn("hook", analysis_json["plot_points"])
        self.assertIn("midpoint", analysis_json["plot_points"])
        self.assertIn("climax", analysis_json["plot_points"])

        plot_file = self.book_dir / "plot_analysis.json"
        self.assertTrue(plot_file.exists())

        # Verify contract schema compliance: value, confidence, evidence
        hook_point = analysis_json["plot_points"]["hook"]
        self.assertIn("value", hook_point)
        self.assertIn("confidence", hook_point)
        self.assertIn("evidence", hook_point)


if __name__ == "__main__":
    unittest.main()

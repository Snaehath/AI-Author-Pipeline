"""
Unit and Integration Tests for Module 8 (Dataset Generator).

Executes automated checks on prompt formatting, SFT synthesizers, train/val splitters,
and end-to-end datasets/train.jsonl & val.jsonl generation.
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

from AI_Author.dataset_generator.prompt_templates import PromptTemplates
from AI_Author.dataset_generator.sft_synthesizer import SFTSynthesizer, SFTExample
from AI_Author.dataset_generator.dataset_pipeline import DatasetPipeline
from AI_Author.pipeline.ingestion.pipeline import IngestionPipeline
from AI_Author.pipeline.parser.chapter_parser import ChapterParser
from AI_Author.pipeline.analyzer.story_analyzer import StoryAnalyzer
from AI_Author.pipeline.analyzer.character_analyzer import CharacterAnalyzer
from AI_Author.pipeline.analyzer.dialogue_analyzer import DialogueAnalyzer
from AI_Author.pipeline.analyzer.emotion_analyzer import EmotionAnalyzer
from AI_Author.pipeline.analyzer.plot_analyzer import PlotAnalyzer


class TestPromptTemplates(unittest.TestCase):
    """Unit tests for PromptTemplates."""

    def setUp(self):
        self.templates = PromptTemplates()

    def test_system_prompt(self):
        sys_prompt = self.templates.get_system_prompt()
        self.assertIn("author", sys_prompt.lower())

    def test_format_instruction(self):
        formatted = self.templates.format_instruction("scene_writing", "Chapter 1")
        self.assertIn("Chapter 1", formatted)


class TestSFTSynthesizer(unittest.TestCase):
    """Unit tests for SFTSynthesizer."""

    def setUp(self):
        self.synthesizer = SFTSynthesizer()

    def test_synthesis_example(self):
        example = SFTExample(
            system="System Prompt",
            instruction="Write a scene",
            input="POV: Third-Person",
            output="Prose text...",
            task_type="scene_writing",
            source_book="Sample Book",
        )
        data = example.to_dict()
        self.assertEqual(data["task_type"], "scene_writing")
        self.assertEqual(data["system"], "System Prompt")


class TestDatasetPipelineIntegration(unittest.TestCase):
    """Integration test for full DatasetPipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"
        self.dataset_dir = Path(self.temp_dir.name) / "datasets"

        # Step 1: Run Ingestion
        self.ingestion_pipeline = IngestionPipeline(output_base_dir=self.output_dir)
        sample_book = Path(self.temp_dir.name) / "sample.txt"
        sample_content = (
            "The Dataset Story\nBy Jane Doe\n\n"
            "CHAPTER 1: The Trail\n\n"
            "Aria adjusted her leather cloak as the cold wind howled.\n\n"
            '"We must reach the twin pillars," Aria said.\n\n'
            '"Are you sure?" Kane asked.'
        )
        with open(sample_book, "w", encoding="utf-8") as f:
            f.write(sample_content)

        ingestion_res = self.ingestion_pipeline.run(sample_book, title="The Dataset Story", author="Jane Doe")
        self.book_dir = ingestion_res.cleaned_text_path.parent

        # Step 2: Run Parser & Analyzers (Modules 2-7)
        ChapterParser().parse_book_directory(self.book_dir)
        StoryAnalyzer().analyze_book_directory(self.book_dir)
        CharacterAnalyzer().analyze_book_directory(self.book_dir)
        DialogueAnalyzer().analyze_book_directory(self.book_dir)
        EmotionAnalyzer().analyze_book_directory(self.book_dir)
        PlotAnalyzer().analyze_book_directory(self.book_dir)

        # Step 3: Dataset Pipeline
        self.dataset_pipeline = DatasetPipeline(output_dataset_dir=self.dataset_dir)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_dataset_generation(self):
        summary = self.dataset_pipeline.run_pipeline([self.book_dir])

        self.assertGreater(summary["total_examples"], 0)
        self.assertTrue((self.dataset_dir / "train.jsonl").exists())
        self.assertTrue((self.dataset_dir / "val.jsonl").exists())
        self.assertTrue((self.dataset_dir / "dataset_summary.json").exists())

        # Verify JSONL lines schema
        with open(self.dataset_dir / "train.jsonl", "r", encoding="utf-8") as f:
            first_line = json.loads(f.readline())

        self.assertIn("system", first_line)
        self.assertIn("instruction", first_line)
        self.assertIn("input", first_line)
        self.assertIn("output", first_line)
        self.assertIn("task_type", first_line)


if __name__ == "__main__":
    unittest.main()

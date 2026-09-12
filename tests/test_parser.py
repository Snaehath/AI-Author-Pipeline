"""
Unit and Integration Tests for Module 2 (Chapter Parser).

Executes automated checks on dialogue extractors, paragraph parsers,
scene parsers, and end-to-end chapter parsing execution.
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

from AI_Author.pipeline.parser.dialogue_extractor import DialogueExtractor
from AI_Author.pipeline.parser.paragraph_parser import ParagraphParser
from AI_Author.pipeline.parser.scene_parser import SceneParser
from AI_Author.pipeline.parser.chapter_parser import ChapterParser, ParsedChapter
from AI_Author.pipeline.ingestion.pipeline import IngestionPipeline


class TestDialogueExtractor(unittest.TestCase):
    """Unit tests for DialogueExtractor."""

    def setUp(self):
        self.extractor = DialogueExtractor()

    def test_extract_dialogue_and_speech_tag(self):
        text = '"We should make camp before nightfall," Kane said, leaning on his wooden staff.'
        items = self.extractor.extract_dialogue_items(text)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].spoken_text, "We should make camp before nightfall")
        self.assertIn("Kane said", items[0].speech_tag)
        self.assertEqual(items[0].speaker_hint, "Kane")

    def test_no_dialogue(self):
        text = "Aria adjusted her cloak as the mountain wind blew."
        items = self.extractor.extract_dialogue_items(text)
        self.assertEqual(len(items), 0)


class TestParagraphParser(unittest.TestCase):
    """Unit tests for ParagraphParser."""

    def setUp(self):
        self.parser = ParagraphParser()

    def test_narration_paragraph(self):
        text = "The cold mountain wind howled through the canyon."
        paragraphs = self.parser.parse_paragraphs(text)
        self.assertEqual(len(paragraphs), 1)
        self.assertEqual(paragraphs[0].type, "narration")
        self.assertFalse(paragraphs[0].has_dialogue)

    def test_mixed_paragraph(self):
        text = '"Follow me," Aria whispered, turning toward the dark tunnel.'
        paragraphs = self.parser.parse_paragraphs(text)
        self.assertEqual(len(paragraphs), 1)
        self.assertEqual(paragraphs[0].type, "mixed")
        self.assertTrue(paragraphs[0].has_dialogue)


class TestSceneParser(unittest.TestCase):
    """Unit tests for SceneParser."""

    def setUp(self):
        self.parser = SceneParser()

    def test_scene_splitting(self):
        chapter_text = (
            "Paragraph one of scene one.\n\n"
            "***\n\n"
            "Paragraph one of scene two."
        )
        scenes = self.parser.parse_scenes(chapter_text)
        self.assertEqual(len(scenes), 2)
        self.assertEqual(scenes[0].scene_index, 1)
        self.assertEqual(scenes[1].scene_index, 2)


class TestChapterParserIntegration(unittest.TestCase):
    """Integration tests for ChapterParser."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"

        # Run Module 1 Pipeline to generate sample book outputs
        self.ingestion_pipeline = IngestionPipeline(output_base_dir=self.output_dir)

        sample_book_path = Path(self.temp_dir.name) / "test_book.txt"
        sample_content = (
            "The Mystery of Oak Manor\nBy Jane Doe\n\n"
            "CHAPTER 1: The Gate\n\n"
            "The iron gate creaked as Aria pushed it open.\n\n"
            '"Is anyone inside?" Kane asked.\n\n'
            "***\n\n"
            "Inside the manor, shadows danced across the wall."
        )
        with open(sample_book_path, "w", encoding="utf-8") as f:
            f.write(sample_content)

        self.ingestion_result = self.ingestion_pipeline.run(
            sample_book_path, title="The Mystery of Oak Manor", author="Jane Doe"
        )
        self.chapter_parser = ChapterParser()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_chapter_parsing(self):
        book_output_dir = self.ingestion_result.cleaned_text_path.parent
        parsed_chapters = self.chapter_parser.parse_book_directory(book_output_dir)

        self.assertGreater(len(parsed_chapters), 0)

        chapters_dir = book_output_dir / "chapters"
        self.assertTrue(chapters_dir.exists())

        chapter_01_file = chapters_dir / "chapter_01.json"
        summary_file = book_output_dir / "parsing_summary.json"

        self.assertTrue(chapter_01_file.exists())
        self.assertTrue(summary_file.exists())

        # Verify contents of parsed chapter JSON
        with open(chapter_01_file, "r", encoding="utf-8") as f:
            chap_data = json.load(f)

        self.assertEqual(chap_data["book_title"], "The Mystery of Oak Manor")
        self.assertIn("scenes", chap_data)
        self.assertGreater(chap_data["total_paragraphs"], 0)


if __name__ == "__main__":
    unittest.main()

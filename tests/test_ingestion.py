"""
Unit and Integration Tests for Module 1 (Book Ingestion).

Executes automated checks on text extractors, normalizers, header cleaners,
chapter splitters, and end-to-end pipeline execution.
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Add project root (containing AI_Author package) to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.ingestion.extractors import extract_text_from_file, extract_from_txt
from AI_Author.ingestion.normalizer import TextNormalizer
from AI_Author.ingestion.header_cleaner import HeaderCleaner
from AI_Author.ingestion.chapter_splitter import ChapterSplitter, Chapter
from AI_Author.ingestion.pipeline import IngestionPipeline


class TestTextNormalizer(unittest.TestCase):
    """Unit tests for TextNormalizer."""

    def setUp(self):
        self.normalizer = TextNormalizer()

    def test_unicode_normalization(self):
        # Test compatibility character normalization
        raw = "caf\u00e9" # café
        normalized = self.normalizer.normalize_unicode(raw)
        self.assertEqual(normalized, "café")

    def test_smart_quote_normalization(self):
        raw = '“It’s a secret,” she whispered, ‘indeed’.'
        expected = '"It\'s a secret," she whispered, \'indeed\'.'
        result = self.normalizer.normalize_quotes_and_punctuation(raw)
        self.assertEqual(result, expected)

    def test_ocr_hyphenation_fix(self):
        raw = "This is a develo-\npment in AI storytelling."
        expected = "This is a development in AI storytelling."
        result = self.normalizer.fix_ocr_hyphenation(raw)
        self.assertEqual(result, expected)

    def test_whitespace_normalization(self):
        raw = "Line 1   \nLine 2\t\n\n\n\nLine 3"
        result = self.normalizer.normalize_whitespace(raw)
        self.assertNotIn("   \n", result)
        self.assertNotIn("\n\n\n\n", result)
        self.assertIn("\n\nLine 3", result)


class TestHeaderCleaner(unittest.TestCase):
    """Unit tests for HeaderCleaner."""

    def setUp(self):
        self.cleaner = HeaderCleaner()

    def test_page_number_detection(self):
        self.assertTrue(self.cleaner.is_page_number_line("- 42 -"))
        self.assertTrue(self.cleaner.is_page_number_line("Page 105"))
        self.assertTrue(self.cleaner.is_page_number_line("Page 12 of 300"))
        self.assertTrue(self.cleaner.is_page_number_line("123"))
        self.assertTrue(self.cleaner.is_page_number_line("IV"))
        self.assertFalse(self.cleaner.is_page_number_line("Chapter 1: The Dark Forest"))
        self.assertFalse(self.cleaner.is_page_number_line("He ran 12 miles yesterday."))

    def test_repeating_header_removal(self):
        lines = []
        for i in range(10):
            lines.append("STORY TITLE - FOR INTERNAL USE")
            lines.append(f"Paragraph text number {i} in the chapter.")
            lines.append("- 1 -")

        text = "\n".join(lines)
        cleaned = self.cleaner.process(text)

        self.assertNotIn("STORY TITLE - FOR INTERNAL USE", cleaned)
        self.assertNotIn("- 1 -", cleaned)
        self.assertIn("Paragraph text number 0 in the chapter.", cleaned)


class TestChapterSplitter(unittest.TestCase):
    """Unit tests for ChapterSplitter."""

    def setUp(self):
        self.splitter = ChapterSplitter()

    def test_chapter_heading_detection(self):
        self.assertTrue(self.splitter.is_chapter_heading("Chapter 1"))
        self.assertTrue(self.splitter.is_chapter_heading("CHAPTER IV: THE DISCOVERY"))
        self.assertTrue(self.splitter.is_chapter_heading("PROLOGUE"))
        self.assertTrue(self.splitter.is_chapter_heading("Epilogue"))
        self.assertTrue(self.splitter.is_chapter_heading("Three"))
        self.assertFalse(self.splitter.is_chapter_heading("The dragon flew across the sky."))

    def test_chapter_splitting(self):
        sample_text = (
            "PROLOGUE\n\nIn the beginning, there was shadow.\n\n"
            "Chapter 1: The Awakening\n\nJohn woke up in a dark room.\n\n"
            "Chapter 2: The Journey\n\nThey traveled north towards the mountains."
        )

        chapters = self.splitter.split(sample_text)
        self.assertEqual(len(chapters), 3)
        self.assertEqual(chapters[0].title, "PROLOGUE")
        self.assertEqual(chapters[1].title, "Chapter 1: The Awakening")
        self.assertEqual(chapters[2].title, "Chapter 2: The Journey")
        self.assertGreater(chapters[1].word_count, 0)

    def test_fallback_split(self):
        text = "word " * 7000  # 7000 words with no headings
        chapters = self.splitter.split(text.strip())
        self.assertGreater(len(chapters), 1)
        self.assertEqual(chapters[0].title, "Section 1")


class TestIngestionPipeline(unittest.TestCase):
    """Integration test for full IngestionPipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name) / "outputs"
        self.pipeline = IngestionPipeline(output_base_dir=self.output_dir)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_txt_ingestion(self):
        # Create temporary book file
        sample_book_path = Path(self.temp_dir.name) / "test_novel.txt"
        sample_content = (
            "“The Secret Passage”\nby Author Name\n\n"
            "PROLOGUE\n\nIt was a dark and stormy night.\n\n"
            "Chapter 1\n\nAria found the hidden key under the floorboards.\n"
            "Page 1\n\n"
            "Chapter 2\n\nThe doorway opened into an ancient hall."
        )
        with open(sample_book_path, "w", encoding="utf-8") as f:
            f.write(sample_content)

        result = self.pipeline.run(sample_book_path, title="The Secret Passage", author="Author Name")

        self.assertTrue(result.cleaned_text_path.exists())
        self.assertTrue(result.metadata_path.exists())
        self.assertGreater(result.total_words, 0)
        # Expected 4 chapters: Preamble (title page), PROLOGUE, Chapter 1, Chapter 2
        self.assertEqual(result.total_chapters, 4)

        # Read metadata.json
        with open(result.metadata_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

        self.assertEqual(meta["title"], "The Secret Passage")
        self.assertEqual(meta["author"], "Author Name")
        self.assertEqual(meta["format"], "TXT")
        self.assertEqual(meta["chapter_count"], 4)
        self.assertEqual(len(meta["chapters"]), 4)


if __name__ == "__main__":
    unittest.main()

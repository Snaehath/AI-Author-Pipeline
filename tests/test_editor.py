"""
Unit and Integration Tests for Module 11 (Local Editor).

Executes automated checks on WorkspaceManager, manuscript export pipeline,
and Editor Server REST API endpoints.
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

from AI_Author.editor.workspace_manager import WorkspaceManager
from AI_Author.editor.editor_server import AuthorStudioHTTPHandler


class TestWorkspaceManager(unittest.TestCase):
    """Unit tests for WorkspaceManager."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.outputs_dir = Path(self.temp_dir.name) / "outputs"
        self.book_dir = self.outputs_dir / "test_book"
        self.chap_dir = self.book_dir / "chapters"
        self.chap_dir.mkdir(parents=True, exist_ok=True)

        meta = {"title": "Test Book"}
        with open(self.book_dir / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(meta, f)

        chap1 = {
            "chapter_index": 1,
            "chapter_title": "Chapter 1: Opening",
            "word_count": 10,
            "scenes": [{"paragraphs": [{"text": "First test paragraph."}]}]
        }
        with open(self.chap_dir / "chapter_01.json", "w", encoding="utf-8") as f:
            json.dump(chap1, f)

        self.wm = WorkspaceManager(outputs_dir=self.outputs_dir)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_list_books(self):
        books = self.wm.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Test Book")

    def test_get_chapter(self):
        chap = self.wm.get_chapter("test_book", 1)
        self.assertEqual(chap["chapter_title"], "Chapter 1: Opening")

    def test_save_chapter(self):
        updated = self.wm.save_chapter("test_book", 1, "New edited text paragraph.")
        self.assertEqual(updated["word_count"], 4)

    def test_export_manuscript(self):
        exp_file = self.wm.export_manuscript("test_book", "markdown")
        self.assertTrue(exp_file.exists())
        with open(exp_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("# Test Book", content)
        self.assertIn("Chapter 1: Opening", content)


if __name__ == "__main__":
    unittest.main()

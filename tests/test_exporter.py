"""
Unit and Integration Tests for Manuscript Exporter Utility.

Executes automated checks on DOCX and PDF manuscript generation.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.utils.manuscript_exporter import export_to_docx, export_to_pdf, export_book_workspace


class TestManuscriptExporter(unittest.TestCase):
    """Unit tests for manuscript exporter."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.book_dir = Path(self.temp_dir.name) / "generated_novel"
        self.book_dir.mkdir(parents=True, exist_ok=True)

        self.md_file = self.book_dir / "generated_novel_manuscript.md"
        with open(self.md_file, "w", encoding="utf-8") as f:
            f.write("# Test Novel\n\n## Chapter 1\n\nAria looked at the horizon.")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_export_to_docx(self):
        docx_file = self.book_dir / "test.docx"
        out = export_to_docx(self.md_file, docx_file)
        self.assertTrue(out.exists())

    def test_export_to_pdf(self):
        pdf_file = self.book_dir / "test.pdf"
        out = export_to_pdf(self.md_file, pdf_file)
        self.assertTrue(out.exists())

    def test_export_book_workspace(self):
        res = export_book_workspace(self.book_dir)
        self.assertIn("docx_path", res)
        self.assertIn("pdf_path", res)


if __name__ == "__main__":
    unittest.main()

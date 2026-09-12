"""
Unit and Integration Tests for Automated Novel Builder.

Executes automated checks on multi-chapter novel generation and workspace file exports.
"""

import json
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.pipeline.inference.novel_builder import NovelBuilder


class TestNovelBuilder(unittest.TestCase):
    """Unit tests for NovelBuilder."""

    def setUp(self):
        self.mock_generator = MagicMock()
        self.mock_generator.create_novel.return_value = "3-Act Outline"
        self.mock_generator.create_chapter.return_value = "Chapter 1 prose paragraph text."
        self.mock_generator._generate_response.return_value = "Chapter 1 prose paragraph text."

        self.builder = NovelBuilder(generator=self.mock_generator)

    def test_generate_complete_novel(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "generated_novel"
            res = self.builder.generate_complete_novel(
                title="Test Novel",
                genre="Fantasy",
                premise="Premise",
                num_chapters=2,
                output_dir=out_path
            )

            self.assertEqual(res["total_chapters"], 2)
            self.assertTrue((out_path / "metadata.json").exists())
            self.assertTrue((out_path / "generated_novel_manuscript.md").exists())
            self.assertTrue((out_path / "chapters" / "chapter_01.json").exists())
            self.assertTrue((out_path / "chapters" / "chapter_02.json").exists())


from AI_Author.pipeline.inference.novel_builder_v2 import NovelBuilderV2


class TestNovelBuilderV2(unittest.TestCase):
    """Unit tests for stateful NovelBuilderV2."""

    def setUp(self):
        self.mock_generator = MagicMock()
        self.mock_generator._generate_response.return_value = (
            "Lord Reginald entered the Library. He looked across the room and picked up the Prized Silver Teapot."
        )
        self.builder = NovelBuilderV2(generator=self.mock_generator)

    def test_generate_novel_v2_with_checkpoints(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "generated_novel_v2"
            res_path = self.builder.generate_novel_v2(
                title="The Test Mystery",
                num_chapters=2,
                output_dir=out_path,
            )
            self.assertTrue(res_path.exists())
            self.assertTrue((out_path / "chapter_blueprints.json").exists())
            self.assertTrue((out_path / "event_ledger.json").exists())
            self.assertTrue((out_path / "canonical_world_state.json").exists())
            self.assertTrue((out_path / "chapters" / "chapter_01.json").exists())
            self.assertTrue((out_path / "checkpoints" / "chapter_01" / "scene_001" / "manifest.json").exists())
            self.assertTrue((out_path / "checkpoints" / "chapter_01" / "scene_001" / "selection_audit.json").exists())


if __name__ == "__main__":
    unittest.main()

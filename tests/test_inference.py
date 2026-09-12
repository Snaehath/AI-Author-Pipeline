"""
Unit and Mock Tests for Module 10 (Inference Engine).

Executes automated checks on model loading resolution and 10 core novel generation APIs.
"""

import os
import sys
import unittest
from unittest.mock import MagicMock
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.pipeline.inference.generator import StoryGenerator


class TestStoryGeneratorMock(unittest.TestCase):
    """Unit test for StoryGenerator using mock model and tokenizer."""

    def setUp(self):
        self.mock_model = MagicMock()
        self.mock_tokenizer = MagicMock()

        self.mock_tokenizer.return_value = {"input_ids": MagicMock()}
        self.mock_tokenizer.pad_token_id = 0
        self.mock_tokenizer.decode.return_value = "<|im_start|>assistant\nGenerated Story Text<|im_end|>"

        self.generator = StoryGenerator(model=self.mock_model, tokenizer=self.mock_tokenizer)

    def test_create_novel(self):
        res = self.generator.create_novel("Title", "Fantasy", "Premise")
        self.assertEqual(res, "Generated Story Text")

    def test_create_chapter(self):
        res = self.generator.create_chapter("Title", 1, "Summary")
        self.assertEqual(res, "Generated Story Text")

    def test_continue_story(self):
        res = self.generator.continue_story("Text snippet")
        self.assertEqual(res, "Generated Story Text")

    def test_rewrite_scene(self):
        res = self.generator.rewrite_scene("Scene", "Darker tone")
        self.assertEqual(res, "Generated Story Text")

    def test_improve_dialogue(self):
        res = self.generator.improve_dialogue("Dialogue", "Angry")
        self.assertEqual(res, "Generated Story Text")

    def test_increase_suspense(self):
        res = self.generator.increase_suspense("Draft")
        self.assertEqual(res, "Generated Story Text")

    def test_improve_pacing(self):
        res = self.generator.improve_pacing("Draft", "Fast")
        self.assertEqual(res, "Generated Story Text")

    def test_emotional_impact(self):
        res = self.generator.emotional_impact("Draft", "Awe")
        self.assertEqual(res, "Generated Story Text")

    def test_generate_character_world(self):
        res = self.generator.generate_character_world("Prompt")
        self.assertEqual(res, "Generated Story Text")

    def test_generate_ending(self):
        res = self.generator.generate_ending("Context")
        self.assertEqual(res, "Generated Story Text")


if __name__ == "__main__":
    unittest.main()

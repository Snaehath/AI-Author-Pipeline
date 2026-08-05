"""
Unit and Integration Tests for Module 9 (Training).

Executes automated checks on ChatML prompt formatters, SFT dataset loaders,
and training pipeline path resolution.
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

from AI_Author.trainer.dataset_loader import format_chatml_prompt, load_sft_jsonl_raw
from AI_Author.trainer.train_pipeline import TrainingPipeline


class TestDatasetLoader(unittest.TestCase):
    """Unit tests for dataset loader."""

    def test_format_chatml_prompt(self):
        example = {
            "system": "You are an author.",
            "instruction": "Write a scene.",
            "input": "POV: First-Person",
            "output": "I stepped into the forest."
        }
        prompt = format_chatml_prompt(example)
        self.assertIn("<|im_start|>system\nYou are an author.<|im_end|>", prompt)
        self.assertIn("<|im_start|>user\nWrite a scene.\n\nPOV: First-Person<|im_end|>", prompt)
        self.assertIn("<|im_start|>assistant\nI stepped into the forest.<|im_end|>", prompt)

    def test_load_sft_jsonl_raw(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            jsonl_path = Path(tmp_dir) / "test.jsonl"
            with open(jsonl_path, "w", encoding="utf-8") as f:
                f.write(json.dumps({"instruction": "hi", "output": "hello"}) + "\n")

            entries = load_sft_jsonl_raw(jsonl_path)
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0]["instruction"], "hi")


class TestTrainingPipeline(unittest.TestCase):
    """Unit tests for TrainingPipeline resolution."""

    def setUp(self):
        self.pipeline = TrainingPipeline()

    def test_pipeline_config_loaded(self):
        self.assertIsNotNone(self.pipeline.config)
        self.assertIn("base_model_path", self.pipeline.config)


if __name__ == "__main__":
    unittest.main()

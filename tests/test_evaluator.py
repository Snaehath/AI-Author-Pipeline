"""
Unit and Integration Tests for Module 12 (Evaluation Suite).

Executes automated checks on BLEU, ROUGE, and Author Style Consistency metrics.
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

from AI_Author.evaluator.bleu_rouge_evaluator import calculate_bleu_rouge
from AI_Author.evaluator.style_consistency import calculate_style_consistency
from AI_Author.evaluator.eval_pipeline import EvaluationPipeline


class TestBLEUROUGEEvaluator(unittest.TestCase):
    """Unit tests for BLEU and ROUGE metrics."""

    def test_bleu_rouge_calculation(self):
        hyp = "Aria adjusted her leather cloak as the cold wind howled."
        ref = "Aria adjusted her cloak in the cold wind."

        res = calculate_bleu_rouge(hyp, ref)

        self.assertIn("bleu_scores", res)
        self.assertIn("rouge_scores", res)
        self.assertGreater(res["bleu_scores"]["bleu_1"], 0.0)
        self.assertGreater(res["rouge_scores"]["rouge_1"]["precision"], 0.0)


class TestStyleConsistency(unittest.TestCase):
    """Unit tests for Author Style Consistency metrics."""

    def test_style_consistency_calculation(self):
        hyp = 'Aria looked up. "We must go," she said.'
        ref = 'Kane looked down. "We must hurry," he replied.'

        res = calculate_style_consistency(hyp, ref)

        self.assertIn("overall_style_consistency", res)
        self.assertGreater(res["overall_style_consistency"], 0.50)


class TestEvaluationPipelineIntegration(unittest.TestCase):
    """Integration test for full EvaluationPipeline."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.gen_dir = Path(self.temp_dir.name) / "generated"
        self.ref_dir = Path(self.temp_dir.name) / "reference"

        self.gen_dir.mkdir(parents=True, exist_ok=True)
        self.ref_dir.mkdir(parents=True, exist_ok=True)

        with open(self.gen_dir / "generated_novel_manuscript.md", "w", encoding="utf-8") as f:
            f.write("# Generated Story\n\nCold wind howled in the canyon.")

        with open(self.ref_dir / "cleaned.txt", "w", encoding="utf-8") as f:
            f.write("Cold wind howled in the mountain canyon.")

        self.pipeline = EvaluationPipeline()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_end_to_end_evaluation(self):
        report = self.pipeline.evaluate_book_directory(self.gen_dir, self.ref_dir)

        self.assertIn("bleu_scores", report)
        self.assertIn("rouge_scores", report)
        self.assertIn("author_style_consistency", report)
        self.assertTrue((self.gen_dir / "evaluation_report.json").exists())
        self.assertTrue((self.gen_dir / "evaluation_summary.md").exists())


if __name__ == "__main__":
    unittest.main()

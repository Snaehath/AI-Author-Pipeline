"""
Evaluation Pipeline Orchestrator Module.

Loads generated manuscripts and reference human books, executes BLEU, ROUGE,
and Author Style Consistency evaluations, and outputs outputs/generated_novel/evaluation_report.json.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.pipeline.evaluator.bleu_rouge_evaluator import calculate_bleu_rouge
from AI_Author.pipeline.evaluator.style_consistency import calculate_style_consistency
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Evaluator.Pipeline")


class EvaluationPipeline:
    """Orchestrates end-to-end evaluation suite execution."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initializes EvaluationPipeline.

        Args:
            config_path: Path to eval_config.json.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "eval_config.json")
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Loads evaluation configuration JSON if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded evaluation config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read eval config file ({e}). Using defaults.")
        return {}

    def evaluate_book_directory(
        self,
        generated_dir: Path,
        reference_dir: Optional[Path] = None,
    ) -> Dict[str, Any]:
        """Runs evaluation suite on a generated novel directory against a reference book.

        Args:
            generated_dir: Directory of generated novel (e.g. outputs/generated_novel).
            reference_dir: Optional directory of reference book (e.g. outputs/sample_novel).

        Returns:
            Dictionary containing evaluation metrics.
        """
        g_path = Path(generated_dir).resolve()
        if not g_path.exists():
            raise FileNotFoundError(f"Generated novel directory not found at: '{g_path}'")

        # Locate generated text
        hyp_text = self._extract_text(g_path)

        # Locate reference text
        r_path = Path(reference_dir).resolve() if reference_dir else (self.root_dir / "outputs" / "sample_novel")
        ref_text = self._extract_text(r_path) if r_path.exists() else hyp_text

        logger.info(f"==================================================")
        logger.info(f"Starting AI Author Studio Evaluation Suite...")
        logger.info(f"Generated Book: '{g_path.name}' vs Reference: '{r_path.name if r_path.exists() else 'Self'}'")

        # 1. BLEU & ROUGE
        bleu_rouge_res = calculate_bleu_rouge(hyp_text, ref_text)

        # 2. Style Consistency
        style_res = calculate_style_consistency(hyp_text, ref_text)

        # Build Full Report
        report = {
            "book_title": g_path.name.replace("_", " ").title(),
            "reference_book": r_path.name.replace("_", " ").title() if r_path.exists() else "Self Reference",
            "evaluation_timestamp": datetime.now(timezone.utc).isoformat(),
            "bleu_scores": bleu_rouge_res["bleu_scores"],
            "rouge_scores": bleu_rouge_res["rouge_scores"],
            "author_style_consistency": style_res,
        }

        # Write evaluation_report.json
        out_json = g_path / "evaluation_report.json"
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Write evaluation_summary.md
        summary_md_lines = [
            f"# Evaluation Report — {report['book_title']}\n\n",
            f"- **Reference Book**: {report['reference_book']}\n",
            f"- **Overall BLEU Score**: {report['bleu_scores']['overall_bleu']}\n",
            f"- **ROUGE-L F1 Score**: {report['rouge_scores']['rouge_l']['f1']}\n",
            f"- **Style Consistency Score**: {style_res['overall_style_consistency']}\n\n",
            "## Metric Breakdown\n\n",
            f"- **Vocabulary Richness (TTR)**: Generated={style_res['generated_ttr']} vs Ref={style_res['reference_ttr']}\n",
            f"- **Avg Sentence Length**: Generated={style_res['generated_avg_sentence_length']} words vs Ref={style_res['reference_avg_sentence_length']} words\n",
            f"- **Dialogue Ratio**: Generated={style_res['generated_dialogue_ratio']} vs Ref={style_res['reference_dialogue_ratio']}\n"
        ]

        out_md = g_path / "evaluation_summary.md"
        with open(out_md, "w", encoding="utf-8") as f:
            f.writelines(summary_md_lines)

        logger.info(f"Evaluation report saved to: '{out_json}'")
        logger.info(f"Evaluation summary saved to: '{out_md}'")
        logger.info(f"==================================================")

        return report

    def _extract_text(self, book_dir: Path) -> str:
        """Helper to extract clean text from manuscript files or chapter JSONs."""
        md_file = book_dir / "generated_novel_manuscript.md"
        txt_file = book_dir / "cleaned.txt"

        if md_file.exists():
            with open(md_file, "r", encoding="utf-8") as f:
                return f.read()

        if txt_file.exists():
            with open(txt_file, "r", encoding="utf-8") as f:
                return f.read()

        chap_dir = book_dir / "chapters"
        if chap_dir.exists():
            c_files = sorted(list(chap_dir.glob("chapter_*.json")))
            paragraphs = []
            for c_file in c_files:
                with open(c_file, "r", encoding="utf-8") as f:
                    c_json = json.load(f)
                for scene in c_json.get("scenes", []):
                    for p in scene.get("paragraphs", []):
                        paragraphs.append(p["text"])
            return "\n\n".join(paragraphs)

        return "Empty text."


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Evaluation Suite")
    parser.add_argument("generated_dir", type=str, help="Path to generated novel directory (e.g. outputs/generated_novel)")
    parser.add_argument("--reference_dir", type=str, help="Optional path to reference book directory (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    pipeline = EvaluationPipeline()
    ref = Path(args.reference_dir) if args.reference_dir else None
    res = pipeline.evaluate_book_directory(Path(args.generated_dir), ref)
    print(f"Evaluation Complete for {res['book_title']} (Overall Style Consistency: {res['author_style_consistency']['overall_style_consistency']}).")

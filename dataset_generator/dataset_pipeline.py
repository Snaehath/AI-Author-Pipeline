"""
Dataset Pipeline Orchestrator Module.

Loads extracted book knowledge from Modules 1-7, calls SFTSynthesizer,
splits examples into train/val datasets (90/10 ratio), and writes datasets/train.jsonl,
datasets/val.jsonl, and datasets/dataset_summary.json.
"""

import json
import random
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.dataset_generator.prompt_templates import PromptTemplates
from AI_Author.dataset_generator.sft_synthesizer import SFTSynthesizer, SFTExample
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.DatasetGenerator.DatasetPipeline")


class DatasetPipeline:
    """Orchestrates end-to-end dataset synthesis and train/val generation."""

    def __init__(self, config_path: Optional[Path] = None, output_dataset_dir: Optional[Path] = None):
        """Initializes DatasetPipeline.

        Args:
            config_path: Path to dataset_config.json.
            output_dataset_dir: Directory where train.jsonl and val.jsonl will be saved.
        """
        self.root_dir = Path(__file__).resolve().parent.parent
        self.config_path = config_path or (self.root_dir / "config" / "dataset_config.json")
        self.output_dataset_dir = output_dataset_dir or (self.root_dir / "datasets")
        self.config = self._load_config()

        self.split_ratio = self.config.get("train_val_split_ratio", 0.90)
        self.templates = PromptTemplates(self.config)
        self.synthesizer = SFTSynthesizer(self.templates)

    def _load_config(self) -> Dict[str, Any]:
        """Loads dataset configuration JSON file if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded dataset config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read dataset config file ({e}). Using defaults.")
        return {}

    def run_pipeline(self, book_dirs: List[Path]) -> Dict[str, Any]:
        """Executes dataset synthesis across one or multiple processed book directories.

        Args:
            book_dirs: List of paths to book output directories.

        Returns:
            Dictionary summary of generated datasets.
        """
        logger.info(f"==================================================")
        logger.info(f"Starting Dataset Generation Pipeline...")

        all_examples: List[SFTExample] = []

        for b_dir in book_dirs:
            book_path = Path(b_dir).resolve()
            if not book_path.exists():
                logger.warning(f"Skipping missing book directory: {book_path}")
                continue

            knowledge = self._load_book_knowledge(book_path)
            book_examples = self.synthesizer.synthesize_all(book_path, knowledge)
            all_examples.extend(book_examples)

        if not all_examples:
            logger.error("No SFT examples synthesized. Check input book directories.")
            return {"total_examples": 0}

        # Apply Character Anonymization to generalize style learning
        from AI_Author.dataset_generator.character_anonymizer import CharacterAnonymizer
        anonymizer = CharacterAnonymizer()
        for ex in all_examples:
            ex.instruction = anonymizer.anonymize_text(ex.instruction)
            ex.input = anonymizer.anonymize_text(ex.input)
            ex.output = anonymizer.anonymize_text(ex.output)

        # Shuffle examples deterministically
        random.seed(42)
        random.shuffle(all_examples)

        # Split into Train and Validation sets
        split_idx = max(1, int(len(all_examples) * self.split_ratio))
        train_examples = all_examples[:split_idx]
        val_examples = all_examples[split_idx:] if split_idx < len(all_examples) else all_examples[:1]

        # Write datasets/train.jsonl and val.jsonl
        self.output_dataset_dir.mkdir(parents=True, exist_ok=True)

        train_path = self.output_dataset_dir / "train.jsonl"
        val_path = self.output_dataset_dir / "val.jsonl"
        summary_path = self.output_dataset_dir / "dataset_summary.json"

        self._write_jsonl(train_path, train_examples)
        self._write_jsonl(val_path, val_examples)

        # Task breakdown distribution
        task_dist: Dict[str, int] = {}
        for ex in all_examples:
            task_dist[ex.task_type] = task_dist.get(ex.task_type, 0) + 1

        summary = {
            "total_examples": len(all_examples),
            "train_examples": len(train_examples),
            "val_examples": len(val_examples),
            "train_val_split_ratio": self.split_ratio,
            "task_type_distribution": task_dist,
            "train_path": str(train_path),
            "val_path": str(val_path),
        }

        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved {len(train_examples)} train examples to: '{train_path}'")
        logger.info(f"Saved {len(val_examples)} val examples to: '{val_path}'")
        logger.info(f"Dataset summary saved to: '{summary_path}'")
        logger.info(f"==================================================")

        return summary

    def _load_book_knowledge(self, book_path: Path) -> Dict[str, Any]:
        """Helper to load all JSON analysis files for a book."""
        knowledge: Dict[str, Any] = {}

        for key, filename in [
            ("metadata", "metadata.json"),
            ("story_analysis", "story_analysis.json"),
            ("character_analysis", "character_analysis.json"),
            ("dialogue_analysis", "dialogue_analysis.json"),
            ("emotion_analysis", "emotion_analysis.json"),
            ("plot_analysis", "plot_analysis.json"),
        ]:
            fpath = book_path / filename
            if fpath.exists():
                with open(fpath, "r", encoding="utf-8") as f:
                    knowledge[key] = json.load(f)

        # Load parsed chapter files
        chapters_dir = book_path / "chapters"
        if chapters_dir.exists():
            chap_files = sorted(list(chapters_dir.glob("chapter_*.json")))
            chap_list = []
            for c_file in chap_files:
                with open(c_file, "r", encoding="utf-8") as f:
                    chap_list.append(json.load(f))
            knowledge["chapters"] = chap_list

        return knowledge

    def _write_jsonl(self, filepath: Path, examples: List[SFTExample]) -> None:
        """Writes SFTExample objects to JSONL file."""
        with open(filepath, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex.to_dict(), ensure_ascii=False) + "\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Dataset Generator")
    parser.add_argument("book_dirs", nargs="+", type=str, help="Path to one or more book output directories (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    pipeline = DatasetPipeline()
    dirs = [Path(d) for d in args.book_dirs]
    res = pipeline.run_pipeline(dirs)
    print(f"Dataset Generation Complete: {res['total_examples']} total SFT examples ({res['train_examples']} train, {res['val_examples']} val).")

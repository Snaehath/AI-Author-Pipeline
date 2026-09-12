"""
Plot Analyzer Orchestrator Module.

Loads parsed chapter outputs from Module 2 (outputs/<book_slug>/chapters/chapter_XX.json),
executes classic 8-Point plot structure mapping (Hook, Inciting Incident, First Plot Point,
Midpoint, Reversal, Darkest Moment, Climax, Resolution, Epilogue), and outputs outputs/<book_slug>/plot_analysis.json.
"""

import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any, Optional

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.pipeline.analyzer.pov_detector import KnowledgeItem
from AI_Author.pipeline.analyzer.plot_point_classifier import PlotPointClassifier
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.PlotAnalyzer")


class PlotAnalyzer:
    """Orchestrates classic 3-Act / 8-Point plot structure mapping."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initializes PlotAnalyzer.

        Args:
            config_path: Path to plot_config.json.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "plot_config.json")
        self.config = self._load_config()

        self.classifier = PlotPointClassifier(self.config)

    def _load_config(self) -> Dict[str, Any]:
        """Loads plot configuration JSON file if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded plot config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read plot config file ({e}). Using defaults.")
        return {}

    def analyze_book_directory(self, book_dir: Path) -> Dict[str, Any]:
        """Maps plot structure milestones across a book output directory.

        Args:
            book_dir: Path to book output directory (e.g. outputs/sample_novel).

        Returns:
            Dictionary containing full plot_analysis.json content.
        """
        book_path = Path(book_dir).resolve()
        chapters_dir = book_path / "chapters"

        if not chapters_dir.exists():
            raise FileNotFoundError(f"Missing parsed chapters directory at: {chapters_dir}")

        chapter_files = sorted(list(chapters_dir.glob("chapter_*.json")))
        if not chapter_files:
            raise FileNotFoundError(f"No chapter_XX.json files found in: {chapters_dir}")

        logger.info(f"==================================================")
        logger.info(f"Starting Plot Structure Analysis for: '{book_path.name}'")
        logger.info(f"Analyzing plot progression across {len(chapter_files)} chapter files...")

        chapter_data_list = []
        for c_file in chapter_files:
            with open(c_file, "r", encoding="utf-8") as f:
                chap_json = json.load(f)
            chapter_data_list.append(chap_json)

        plot_milestones = self.classifier.classify_plot_milestones(chapter_data_list)

        output_data = {
            "book_title": book_path.name.replace("_", " ").title(),
            "total_chapters": len(chapter_files),
            "plot_structure_summary": "Classic 3-Act Heroic Arc (Hook -> Inciting Incident -> Midpoint -> Climax -> Resolution)",
            "plot_points": {
                name: item.to_dict() for name, item in plot_milestones.items()
            },
        }

        # Write output file
        out_filepath = book_path / "plot_analysis.json"
        with open(out_filepath, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Mapped {len(plot_milestones)} plot structure milestones.")
        logger.info(f"Plot Analysis saved to: '{out_filepath}'")
        logger.info(f"==================================================")

        return output_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Plot Analyzer")
    parser.add_argument("book_dir", type=str, help="Path to processed book output directory (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    analyzer = PlotAnalyzer()
    res = analyzer.analyze_book_directory(Path(args.book_dir))
    print(f"Successfully mapped plot structure for {res['book_title']}.")

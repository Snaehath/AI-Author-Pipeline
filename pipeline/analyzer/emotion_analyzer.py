"""
Emotion Analyzer Orchestrator Module.

Loads parsed chapter outputs from Module 2 (outputs/<book_slug>/chapters/chapter_XX.json),
executes emotional progression tracking (Valence, Intensity, Dominant Emotion, Shift Triggers,
Emotion Timeline), and outputs outputs/<book_slug>/emotion_analysis.json.
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
from AI_Author.pipeline.analyzer.valence_intensity_calculator import ValenceIntensityCalculator
from AI_Author.pipeline.analyzer.emotion_timeline_tracker import EmotionTimelineTracker
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.EmotionAnalyzer")


@dataclass
class TimelinePoint:
    """Represents a single checkpoint in the story emotion timeline."""
    chapter_index: int
    chapter_title: str
    dominant_emotion: KnowledgeItem
    valence: float
    intensity: float
    emotional_shift_trigger: KnowledgeItem

    def to_dict(self) -> Dict[str, Any]:
        """Converts TimelinePoint to dictionary."""
        return {
            "chapter_index": self.chapter_index,
            "chapter_title": self.chapter_title,
            "dominant_emotion": self.dominant_emotion.to_dict(),
            "valence": self.valence,
            "intensity": self.intensity,
            "emotional_shift_trigger": self.emotional_shift_trigger.to_dict(),
        }


class EmotionAnalyzer:
    """Orchestrates emotion progression tracking and timeline generation."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initializes EmotionAnalyzer with sub-calculators.

        Args:
            config_path: Path to emotion_config.json.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "emotion_config.json")
        self.config = self._load_config()

        self.calculator = ValenceIntensityCalculator(self.config)
        self.tracker = EmotionTimelineTracker()

    def _load_config(self) -> Dict[str, Any]:
        """Loads emotion configuration JSON file if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded emotion config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read emotion config file ({e}). Using defaults.")
        return {}

    def analyze_book_directory(self, book_dir: Path) -> Dict[str, Any]:
        """Tracks emotional progression across a book output directory.

        Args:
            book_dir: Path to book output directory (e.g. outputs/sample_novel).

        Returns:
            Dictionary containing full emotion_analysis.json content.
        """
        book_path = Path(book_dir).resolve()
        chapters_dir = book_path / "chapters"

        if not chapters_dir.exists():
            raise FileNotFoundError(f"Missing parsed chapters directory at: {chapters_dir}")

        chapter_files = sorted(list(chapters_dir.glob("chapter_*.json")))
        if not chapter_files:
            raise FileNotFoundError(f"No chapter_XX.json files found in: {chapters_dir}")

        logger.info(f"==================================================")
        logger.info(f"Starting Emotion Progression Analysis for: '{book_path.name}'")

        timeline_points: List[TimelinePoint] = []

        for c_file in chapter_files:
            with open(c_file, "r", encoding="utf-8") as f:
                chap_json = json.load(f)

            chap_idx = chap_json["chapter_index"]
            chap_title = chap_json["chapter_title"]

            c_text_parts = []
            for scene in chap_json.get("scenes", []):
                for p in scene.get("paragraphs", []):
                    c_text_parts.append(p["text"])
            chap_text = "\n\n".join(c_text_parts)

            valence, v_item = self.calculator.calculate_valence(chap_text)
            intensity, i_item = self.calculator.calculate_intensity(chap_text)
            dom_emotion = self.tracker.classify_dominant_emotion(valence, intensity, chap_text)
            trigger = self.tracker.detect_shift_trigger(chap_text)

            point = TimelinePoint(
                chapter_index=chap_idx,
                chapter_title=chap_title,
                dominant_emotion=dom_emotion,
                valence=valence,
                intensity=intensity,
                emotional_shift_trigger=trigger,
            )

            timeline_points.append(point)
            logger.info(f"Chapter {chap_idx} Emotion: {dom_emotion.value} (Valence: {valence:+.2f}, Intensity: {intensity:.2f})")

        # Book-level aggregate statistics
        avg_valence = round(sum(p.valence for p in timeline_points) / max(1, len(timeline_points)), 2)
        avg_intensity = round(sum(p.intensity for p in timeline_points) / max(1, len(timeline_points)), 2)

        overall_arc = KnowledgeItem(
            value=f"Emotional Arc Trajectory ({timeline_points[0].dominant_emotion.value} -> {timeline_points[-1].dominant_emotion.value})",
            confidence=0.90,
            evidence=f"Overall Book Average Valence: {avg_valence:+.2f}, Average Intensity: {avg_intensity:.2f}",
        )

        output_data = {
            "book_title": book_path.name.replace("_", " ").title(),
            "total_timeline_points": len(timeline_points),
            "overall_emotional_arc": overall_arc.to_dict(),
            "average_book_valence": avg_valence,
            "average_book_intensity": avg_intensity,
            "emotion_timeline": [p.to_dict() for p in timeline_points],
        }

        # Write output file
        out_filepath = book_path / "emotion_analysis.json"
        with open(out_filepath, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Emotion Timeline saved to: '{out_filepath}'")
        logger.info(f"==================================================")

        return output_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Emotion Analyzer")
    parser.add_argument("book_dir", type=str, help="Path to processed book output directory (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    analyzer = EmotionAnalyzer()
    res = analyzer.analyze_book_directory(Path(args.book_dir))
    print(f"Successfully generated emotion timeline for {res['book_title']}.")

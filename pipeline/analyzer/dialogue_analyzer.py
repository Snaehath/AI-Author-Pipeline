"""
Dialogue Analyzer Orchestrator Module.

Loads parsed chapter outputs from Module 2 (outputs/<book_slug>/chapters/chapter_XX.json),
executes detailed dialogue analysis per spoken turn (Speaker, Emotion, Conflict, Humor,
Speech Style, Vocabulary, Dialogue Length), and outputs outputs/<book_slug>/dialogue_analysis.json.
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
from AI_Author.pipeline.analyzer.dialogue_emotion_analyzer import DialogueEmotionAnalyzer
from AI_Author.pipeline.analyzer.speech_style_analyzer import SpeechStyleAnalyzer
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.DialogueAnalyzer")


@dataclass
class SpokenTurnAnalysis:
    """Represents full dialogue analysis for a single spoken turn."""
    chapter_index: int
    scene_index: int
    speaker: KnowledgeItem
    spoken_text: str
    speech_tag: str
    emotion: KnowledgeItem
    conflict: KnowledgeItem
    humor: KnowledgeItem
    speech_style: KnowledgeItem
    vocabulary: KnowledgeItem
    dialogue_length: KnowledgeItem

    def to_dict(self) -> Dict[str, Any]:
        """Converts SpokenTurnAnalysis to dictionary."""
        return {
            "chapter_index": self.chapter_index,
            "scene_index": self.scene_index,
            "speaker": self.speaker.to_dict(),
            "spoken_text": self.spoken_text,
            "speech_tag": self.speech_tag,
            "emotion": self.emotion.to_dict(),
            "conflict": self.conflict.to_dict(),
            "humor": self.humor.to_dict(),
            "speech_style": self.speech_style.to_dict(),
            "vocabulary": self.vocabulary.to_dict(),
            "dialogue_length": self.dialogue_length.to_dict(),
        }


class DialogueAnalyzer:
    """Orchestrates comprehensive analysis across all dialogue turns in a book."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initializes DialogueAnalyzer with sub-analyzers.

        Args:
            config_path: Path to dialogue_config.json.
        """
        self.root_dir = PROJECT_ROOT
        self.config_path = config_path or (self.root_dir / "config" / "dialogue_config.json")
        self.config = self._load_config()

        self.emotion_analyzer = DialogueEmotionAnalyzer(self.config)
        self.style_analyzer = SpeechStyleAnalyzer(self.config)

    def _load_config(self) -> Dict[str, Any]:
        """Loads dialogue configuration JSON file if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded dialogue config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read dialogue config file ({e}). Using defaults.")
        return {}

    def analyze_book_directory(self, book_dir: Path) -> Dict[str, Any]:
        """Analyzes all spoken dialogue lines in a book output directory.

        Args:
            book_dir: Path to book output directory (e.g. outputs/sample_novel).

        Returns:
            Dictionary containing full dialogue_analysis.json content.
        """
        book_path = Path(book_dir).resolve()
        chapters_dir = book_path / "chapters"

        if not chapters_dir.exists():
            raise FileNotFoundError(f"Missing parsed chapters directory at: {chapters_dir}")

        chapter_files = sorted(list(chapters_dir.glob("chapter_*.json")))
        if not chapter_files:
            raise FileNotFoundError(f"No chapter_XX.json files found in: {chapters_dir}")

        logger.info(f"==================================================")
        logger.info(f"Starting Dialogue Analysis for: '{book_path.name}'")

        dialogue_turns: List[SpokenTurnAnalysis] = []

        for c_file in chapter_files:
            with open(c_file, "r", encoding="utf-8") as f:
                chap_json = json.load(f)

            chap_idx = chap_json["chapter_index"]
            scenes = chap_json.get("scenes", [])

            for scene in scenes:
                s_idx = scene["scene_index"]
                for p in scene.get("paragraphs", []):
                    for d_item in p.get("dialogues", []):
                        spoken_text = d_item["spoken_text"]
                        speech_tag = d_item.get("speech_tag", "")
                        speaker_name = d_item.get("speaker_hint") or "Unknown"

                        speaker = KnowledgeItem(
                            value=speaker_name,
                            confidence=0.90 if speaker_name != "Unknown" else 0.60,
                            evidence=f'"{spoken_text}" {speech_tag}'.strip(),
                        )

                        emotion = self.emotion_analyzer.analyze_dialogue_emotion(spoken_text, speech_tag)
                        conflict = self.emotion_analyzer.analyze_dialogue_conflict(spoken_text, speech_tag)
                        humor = self.style_analyzer.analyze_humor(spoken_text, speech_tag)
                        speech_style = self.style_analyzer.analyze_speech_style(spoken_text)
                        vocab = self.style_analyzer.analyze_vocabulary(spoken_text)
                        length = self.style_analyzer.analyze_dialogue_length(spoken_text)

                        turn = SpokenTurnAnalysis(
                            chapter_index=chap_idx,
                            scene_index=s_idx,
                            speaker=speaker,
                            spoken_text=spoken_text,
                            speech_tag=speech_tag,
                            emotion=emotion,
                            conflict=conflict,
                            humor=humor,
                            speech_style=speech_style,
                            vocabulary=vocab,
                            dialogue_length=length,
                        )

                        dialogue_turns.append(turn)

        # Summary statistics
        total_dialogues = len(dialogue_turns)
        total_words = sum(len(t.spoken_text.split()) for t in dialogue_turns)
        avg_words = round(total_words / max(1, total_dialogues), 1)

        conflict_dist: Dict[str, int] = {}
        for t in dialogue_turns:
            c_val = t.conflict.value
            conflict_dist[c_val] = conflict_dist.get(c_val, 0) + 1

        output_data = {
            "book_title": book_path.name.replace("_", " ").title(),
            "total_dialogues_analyzed": total_dialogues,
            "dialogue_metrics_summary": {
                "average_words_per_dialogue": avg_words,
                "dialogue_conflict_distribution": conflict_dist,
            },
            "dialogues": [t.to_dict() for t in dialogue_turns],
        }

        # Write output file
        out_filepath = book_path / "dialogue_analysis.json"
        with open(out_filepath, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Analyzed {total_dialogues} dialogue turns across {len(chapter_files)} chapters.")
        logger.info(f"Dialogue Analysis saved to: '{out_filepath}'")
        logger.info(f"==================================================")

        return output_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Dialogue Analyzer")
    parser.add_argument("book_dir", type=str, help="Path to processed book output directory (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    analyzer = DialogueAnalyzer()
    res = analyzer.analyze_book_directory(Path(args.book_dir))
    print(f"Successfully analyzed {res['total_dialogues_analyzed']} dialogue turns.")

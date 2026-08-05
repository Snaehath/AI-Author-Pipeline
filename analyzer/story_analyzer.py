"""
Story Analyzer Orchestrator Module.

Loads parsed chapter outputs from Module 2 (outputs/<book_slug>/chapters/chapter_XX.json),
executes story knowledge extraction (POV, Tone, Mood, Pacing, Conflict, Scene Purpose,
Character Introductions, Foreshadowing, Twists, Cliffhangers, and Themes),
and outputs outputs/<book_slug>/story_analysis.json.
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

from AI_Author.analyzer.pov_detector import POVDetector, KnowledgeItem
from AI_Author.analyzer.tone_mood_analyzer import ToneMoodAnalyzer
from AI_Author.analyzer.conflict_scene_analyzer import ConflictSceneAnalyzer
from AI_Author.analyzer.foreshadow_twist_analyzer import ForeshadowTwistAnalyzer
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.StoryAnalyzer")


@dataclass
class ChapterAnalysis:
    """Represents full storytelling knowledge breakdown for a single chapter."""
    chapter_index: int
    chapter_title: str
    word_count: int
    narrative_pov: KnowledgeItem
    tone: KnowledgeItem
    mood: KnowledgeItem
    pacing: KnowledgeItem
    conflict: KnowledgeItem
    scene_purposes: List[Dict[str, Any]]
    character_introductions: List[KnowledgeItem]
    foreshadowing: KnowledgeItem
    cliffhanger: KnowledgeItem

    def to_dict(self) -> Dict[str, Any]:
        """Converts ChapterAnalysis to dictionary."""
        return {
            "chapter_index": self.chapter_index,
            "chapter_title": self.chapter_title,
            "word_count": self.word_count,
            "narrative_pov": self.narrative_pov.to_dict(),
            "tone": self.tone.to_dict(),
            "mood": self.mood.to_dict(),
            "pacing": self.pacing.to_dict(),
            "conflict": self.conflict.to_dict(),
            "scene_purposes": self.scene_purposes,
            "character_introductions": [c.to_dict() for c in self.character_introductions],
            "foreshadowing": self.foreshadowing.to_dict(),
            "cliffhanger": self.cliffhanger.to_dict(),
        }


class StoryAnalyzer:
    """Orchestrates comprehensive storytelling knowledge extraction."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initializes StoryAnalyzer with sub-analyzers.

        Args:
            config_path: Path to analyzer_config.json.
        """
        self.root_dir = Path(__file__).resolve().parent.parent
        self.config_path = config_path or (self.root_dir / "config" / "analyzer_config.json")
        self.config = self._load_config()

        self.pov_detector = POVDetector(self.config.get("pov_detector"))
        self.tone_mood_analyzer = ToneMoodAnalyzer(self.config.get("tone_mood_analyzer"))
        self.conflict_scene_analyzer = ConflictSceneAnalyzer(self.config.get("conflict_scene_analyzer"))
        self.foreshadow_twist_analyzer = ForeshadowTwistAnalyzer(self.config.get("foreshadow_twist_analyzer"))

    def _load_config(self) -> Dict[str, Any]:
        """Loads analyzer configuration JSON file if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded analyzer config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read analyzer config file ({e}). Using defaults.")
        return {}

    def analyze_book_directory(self, book_dir: Path) -> Dict[str, Any]:
        """Analyzes all parsed chapter JSON files in a book output directory.

        Args:
            book_dir: Path to book output directory (e.g. outputs/sample_novel).

        Returns:
            Dictionary containing full story_analysis.json content.
        """
        book_path = Path(book_dir).resolve()
        chapters_dir = book_path / "chapters"

        if not chapters_dir.exists():
            raise FileNotFoundError(f"Missing parsed chapters directory at: {chapters_dir}")

        chapter_files = sorted(list(chapters_dir.glob("chapter_*.json")))
        if not chapter_files:
            raise FileNotFoundError(f"No chapter_XX.json files found in: {chapters_dir}")

        logger.info(f"==================================================")
        logger.info(f"Starting Story Knowledge Analysis for: '{book_path.name}'")
        logger.info(f"Analyzing {len(chapter_files)} chapter files...")

        chapter_analyses: List[ChapterAnalysis] = []
        combined_text_snippets = []

        for c_file in chapter_files:
            with open(c_file, "r", encoding="utf-8") as f:
                chap_json = json.load(f)

            chap_idx = chap_json["chapter_index"]
            chap_title = chap_json["chapter_title"]
            dialogue_ratio = chap_json.get("dialogue_ratio", 0.0)

            # Reconstruct chapter text from scenes & paragraphs
            scenes = chap_json.get("scenes", [])
            chapter_text_parts = []
            scene_purposes = []

            for s_idx, scene in enumerate(scenes, start=1):
                scene_text = " ".join([p["text"] for p in scene.get("paragraphs", [])])
                chapter_text_parts.append(scene_text)

                s_purpose = self.conflict_scene_analyzer.analyze_scene_purpose(
                    scene_text, s_idx, len(scenes)
                )
                scene_purposes.append({
                    "scene_index": s_idx,
                    "purpose": s_purpose.value,
                    "confidence": s_purpose.confidence,
                    "evidence": s_purpose.evidence,
                })

            full_chapter_text = "\n\n".join(chapter_text_parts)
            combined_text_snippets.append(full_chapter_text)

            # Analyze storytelling dimensions
            pov = self.pov_detector.detect_pov(full_chapter_text)
            tone = self.tone_mood_analyzer.analyze_tone(full_chapter_text)
            mood = self.tone_mood_analyzer.analyze_mood(full_chapter_text)
            pacing = self.tone_mood_analyzer.analyze_pacing(full_chapter_text, dialogue_ratio)
            conflict = self.conflict_scene_analyzer.analyze_conflict(full_chapter_text)
            char_intros = self.conflict_scene_analyzer.extract_character_introductions(full_chapter_text)
            foreshadowing = self.foreshadow_twist_analyzer.detect_foreshadowing(full_chapter_text)
            cliffhanger = self.foreshadow_twist_analyzer.detect_cliffhanger(full_chapter_text)

            analysis = ChapterAnalysis(
                chapter_index=chap_idx,
                chapter_title=chap_title,
                word_count=chap_json.get("word_count", 0),
                narrative_pov=pov,
                tone=tone,
                mood=mood,
                pacing=pacing,
                conflict=conflict,
                scene_purposes=scene_purposes,
                character_introductions=char_intros,
                foreshadowing=foreshadowing,
                cliffhanger=cliffhanger,
            )

            chapter_analyses.append(analysis)
            logger.info(f"Completed analysis for Chapter {chap_idx}: '{chap_title}' (Tone: {tone.value}, POV: {pov.value})")

        # Book-level aggregate knowledge
        entire_book_text = "\n\n".join(combined_text_snippets)
        overall_pov = self.pov_detector.detect_pov(entire_book_text)
        overall_tone = self.tone_mood_analyzer.analyze_tone(entire_book_text)
        overall_themes = self.foreshadow_twist_analyzer.extract_themes(entire_book_text)

        full_analysis = {
            "book_title": book_path.name.replace("_", " ").title(),
            "total_chapters_analyzed": len(chapter_analyses),
            "overall_narrative_pov": overall_pov.to_dict(),
            "overall_tone": overall_tone.to_dict(),
            "primary_themes": [t.to_dict() for t in overall_themes],
            "chapter_analyses": [c.to_dict() for c in chapter_analyses],
        }

        # Write story_analysis.json
        out_analysis_path = book_path / "story_analysis.json"
        with open(out_analysis_path, "w", encoding="utf-8") as f:
            json.dump(full_analysis, f, indent=2, ensure_ascii=False)

        logger.info(f"Story Analysis output saved to: '{out_analysis_path}'")
        logger.info(f"Knowledge extraction complete for: '{book_path.name}'")
        logger.info(f"==================================================")

        return full_analysis


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Author Studio — Story Analyzer")
    parser.add_argument("book_dir", type=str, help="Path to processed book output directory (e.g. outputs/sample_novel)")

    args = parser.parse_args()

    analyzer = StoryAnalyzer()
    res = analyzer.analyze_book_directory(Path(args.book_dir))
    print(f"Successfully analyzed story knowledge for {res['book_title']}.")

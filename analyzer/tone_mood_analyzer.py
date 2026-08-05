"""
Tone, Mood, and Pacing Analyzer Module.

Extracts narrative tone, emotional mood, and structural pacing metrics
with confidence scores and text evidence.
"""

import re
from typing import Dict, Any, Optional
from AI_Author.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.ToneMood")


class ToneMoodAnalyzer:
    """Analyzes tone, mood, and pacing across narrative chapters and scenes."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes ToneMoodAnalyzer with keyword dictionaries.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        default_tones = {
            "Suspenseful": ["dark", "shadow", "cold", "whisper", "creak", "footstep", "silence", "danger", "stalk", "hidden"],
            "Somber": ["grief", "loss", "mourn", "grave", "sorrow", "tear", "despair", "empty", "lonely"],
            "Adventurous": ["journey", "mountain", "canyon", "explore", "path", "map", "artifact", "quest", "horizon"],
            "Humorous": ["laugh", "chuckle", "smile", "joke", "grin", "amused", "witty", "ironic"],
            "Dramatic": ["conflict", "confront", "truth", "climax", "fate", "destiny", "desperate", "betrayal"]
        }
        default_moods = {
            "Tense": ["howl", "sharp", "warning", "frost", "obsidian", "threshold", "echo", "nightfall"],
            "Mysterious": ["legend", "ancient", "runes", "hidden", "star", "pedestal", "secret", "shadows"],
            "Hopeful": ["sun", "glowing", "safe", "light", "dawn", "promise", "warmth", "bright"]
        }
        self.tone_keywords = self.config.get("tone_keywords", default_tones)
        self.mood_keywords = self.config.get("mood_keywords", default_moods)

    def analyze_tone(self, text: str) -> KnowledgeItem:
        """Determines narrative tone."""
        return self._evaluate_keyword_categories(text, self.tone_keywords, default_value="Neutral / Objective")

    def analyze_mood(self, text: str) -> KnowledgeItem:
        """Determines narrative mood."""
        return self._evaluate_keyword_categories(text, self.mood_keywords, default_value="Atmospheric")

    def analyze_pacing(self, text: str, dialogue_ratio: float = 0.0) -> KnowledgeItem:
        """Determines scene pacing (Fast, Moderate, Slow/Reflective).

        Args:
            text: Narrative text string.
            dialogue_ratio: Ratio of dialogue words to total words.

        Returns:
            KnowledgeItem object.
        """
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        avg_sentence_len = sum(len(s.split()) for s in sentences) / max(1, len(sentences))

        evidence = sentences[0] if sentences else text[:80]

        # Fast pacing: high dialogue OR short punchy sentences (< 10 words)
        if dialogue_ratio > 0.4 or avg_sentence_len < 10:
            value = "Fast-Paced"
            confidence = 0.88
            evidence_str = f"Average sentence length of {avg_sentence_len:.1f} words with {dialogue_ratio*100:.1f}% dialogue ratio."
        elif avg_sentence_len > 22 or dialogue_ratio < 0.1:
            value = "Slow / Descriptive"
            confidence = 0.85
            evidence_str = f"Descriptive prose with average sentence length of {avg_sentence_len:.1f} words."
        else:
            value = "Moderate"
            confidence = 0.82
            evidence_str = f"Balanced narrative flow with average sentence length of {avg_sentence_len:.1f} words."

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=evidence_str,
        )

    def _evaluate_keyword_categories(
        self, text: str, categories: Dict[str, list], default_value: str
    ) -> KnowledgeItem:
        """Helper method to match keyword categories and compute confidence/evidence."""
        words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        scores: Dict[str, int] = {}
        category_evidences: Dict[str, str] = {}

        for category, kw_list in categories.items():
            count = 0
            found_sentence = ""
            for kw in kw_list:
                for s in sentences:
                    if kw in s.lower():
                        count += 1
                        if not found_sentence:
                            found_sentence = s
            scores[category] = count
            category_evidences[category] = found_sentence

        best_category = max(scores, key=scores.get) if scores else default_value
        max_score = scores.get(best_category, 0)

        if max_score > 0:
            confidence = min(0.95, round(0.65 + (max_score * 0.08), 2))
            evidence = category_evidences[best_category] or text[:100]
            value = best_category
        else:
            confidence = 0.60
            evidence = sentences[0] if sentences else text[:80]
            value = default_value

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=evidence,
        )

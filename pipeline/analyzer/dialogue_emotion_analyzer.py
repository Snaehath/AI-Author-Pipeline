"""
Dialogue Emotion and Conflict Analyzer Module.

Analyzes emotional state and sub-conflict levels for individual spoken dialogue lines.
"""

import re
from typing import Dict, Any, Optional
from AI_Author.pipeline.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.DialogueEmotion")


class DialogueEmotionAnalyzer:
    """Classifies emotion and sub-conflict in dialogue turns."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes DialogueEmotionAnalyzer.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        default_emotions = {
            "Urgent / Cautious": ["must", "should", "quickly", "careful", "nightfall", "hurry", "danger", "wolves", "watch out", "run"],
            "Fearful": ["scared", "terrified", "afraid", "no", "please", "hide", "dark", "monsters", "trap"],
            "Hopeful / Reassuring": ["safe", "light", "found", "good", "hope", "will make it", "trust me", "look"],
            "Angry / Hostile": ["fool", "liar", "never", "stop", "curse", "die", "shut up", "get out", "back off"],
            "Sarcastic / Witty": ["oh great", "wonderful", "brilliant", "surely", "of course", "obviously", "as if"],
            "Calm / Analytical": ["according to", "marks", "indicates", "entrance", "pillars", "pedestal", "study"]
        }
        default_conflicts = {
            "Warning / Friction": ["should", "cannot", "don't", "must not", "careful", "danger", "wolves", "stop"],
            "Direct Disagreement": ["no", "never", "wrong", "false", "disagree", "refuse", "impossible"],
            "Cooperative / Harmonious": ["yes", "agreed", "together", "let's", "all right", "understand"],
            "Inquiry / Questioning": ["what", "where", "why", "who", "how", "when", "?"]
        }
        self.emotion_keywords = self.config.get("emotion_keywords", default_emotions)
        self.conflict_keywords = self.config.get("conflict_keywords", default_conflicts)

    def analyze_dialogue_emotion(self, spoken_text: str, speech_tag: str) -> KnowledgeItem:
        """Determines emotional tone of a dialogue line."""
        combined = f"{spoken_text} {speech_tag}".lower()

        scores: Dict[str, int] = {}
        for emotion, keywords in self.emotion_keywords.items():
            cnt = sum(1 for kw in keywords if kw in combined)
            scores[emotion] = cnt

        best_emotion = max(scores, key=scores.get) if scores else "Calm / Conversational"
        max_score = scores.get(best_emotion, 0)

        if max_score > 0:
            confidence = min(0.95, round(0.70 + (max_score * 0.08), 2))
            value = best_emotion
        else:
            confidence = 0.65
            value = "Calm / Conversational"

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=f'"{spoken_text}"',
        )

    def analyze_dialogue_conflict(self, spoken_text: str, speech_tag: str) -> KnowledgeItem:
        """Determines conflict level in dialogue."""
        combined = f"{spoken_text} {speech_tag}".lower()

        if "?" in spoken_text:
            return KnowledgeItem(
                value="Inquiry / Questioning",
                confidence=0.92,
                evidence=f'"{spoken_text}"',
            )

        scores: Dict[str, int] = {}
        for conflict_type, keywords in self.conflict_keywords.items():
            cnt = sum(1 for kw in keywords if kw in combined)
            scores[conflict_type] = cnt

        best_conflict = max(scores, key=scores.get) if scores else "Cooperative / Harmonious"
        max_score = scores.get(best_conflict, 0)

        if max_score > 0:
            confidence = min(0.95, round(0.70 + (max_score * 0.08), 2))
            value = best_conflict
        else:
            confidence = 0.70
            value = "Cooperative / Harmonious"

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=f'"{spoken_text}"',
        )

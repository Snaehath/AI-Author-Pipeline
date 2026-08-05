"""
Emotion Timeline Tracker Module.

Classifies dominant emotion states and identifies narrative shift triggers
for emotion timeline points.
"""

from typing import Dict, Any, Optional
from AI_Author.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.EmotionTimelineTracker")


class EmotionTimelineTracker:
    """Classifies dominant emotion states and tracks transition triggers."""

    def classify_dominant_emotion(self, valence: float, intensity: float, text: str) -> KnowledgeItem:
        """Determines primary emotion state based on valence and intensity."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        first_sentence = sentences[0] if sentences else text[:80]

        if valence > 0.3 and intensity > 0.7:
            value = "Wonder / Awe & Triumph"
            confidence = 0.90
        elif valence > 0.2:
            value = "Hopeful / Reassuring"
            confidence = 0.85
        elif valence < -0.3 and intensity > 0.6:
            value = "Fear / Dread & Tension"
            confidence = 0.88
        elif valence < 0.0:
            value = "Anticipation / Caution"
            confidence = 0.82
        else:
            value = "Reflective / Calm"
            confidence = 0.75

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=first_sentence,
        )

    def detect_shift_trigger(self, text: str) -> KnowledgeItem:
        """Identifies narrative event triggering emotional shift."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        for s in sentences:
            if any(w in s.lower() for w in ["artifact", "pedestal", "runes", "wolves", "wind", "canyon", "secured"]):
                return KnowledgeItem(
                    value=f"Narrative Trigger: {s[:60]}...",
                    confidence=0.88,
                    evidence=s,
                )

        return KnowledgeItem(
            value="Scene Environment & Progression",
            confidence=0.70,
            evidence=sentences[0] if sentences else text[:80],
        )

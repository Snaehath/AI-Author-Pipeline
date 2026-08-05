"""
Reader Experience and Scene Beat Validation Engine Module (AI Author Studio v3).

Focuses on reader-centric narrative engagement:
1. Expanded Scene Beat Planner (Objective, Hidden Agenda, Expectation, Reversal, Ending Image, Reader Question).
2. Emotional RAG Memory (Running Gags, Promises Made, Misconceptions, Emotional Wounds).
3. Reader Agent Evaluator ("Was I bored?", "Was anything surprising?", "What am I curious about?").
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any
from pathlib import Path
import json


@dataclass
class ExpandedSceneBeat:
    """Rich pre-scene beat structure for reader-centric dramatic progression."""
    chapter_num: int
    scene_objective: str
    hidden_agenda: str
    character_expectation: str
    reversal_twist: str
    ending_image: str
    reader_question: str
    characters_present: List[str] = field(default_factory=list)
    running_gags: List[str] = field(default_factory=list)
    promises_made: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_prompt_context(self) -> str:
        return (
            f"=== EXPANDED DRAMATIC SCENE BEAT (CH.{self.chapter_num}) ===\n"
            f"• Scene Objective: {self.scene_objective}\n"
            f"• Hidden Agenda: {self.hidden_agenda}\n"
            f"• Character Expectation: {self.character_expectation}\n"
            f"• Reversal / Twist: {self.reversal_twist}\n"
            f"• Ending Image: {self.ending_image}\n"
            f"• Reader Question: {self.reader_question}\n"
            f"• Running Gags: {'; '.join(self.running_gags) if self.running_gags else 'None'}\n"
            f"• Promises Made: {'; '.join(self.promises_made) if self.promises_made else 'None'}\n"
            f"=================================================="
        )


class ReaderAgentEvaluator:
    """Simulates a human reader evaluating emotional tension, surprise, and curiosity."""

    def evaluate_scene_engagement(self, prose: str) -> Dict[str, Any]:
        """Evaluates narrative engagement from a reader's perspective."""
        word_count = len(prose.split())
        has_dialogue = '"' in prose
        has_reversal = any(w in prose.lower() for w in ["suddenly", "however", "unexpectedly", "surprised"])
        
        boredom_risk = "Low" if (word_count >= 500 and has_dialogue) else "High"
        curiosity_score = 8.5 if has_reversal else 6.0

        return {
            "was_bored": boredom_risk == "High",
            "was_surprising": has_reversal,
            "curiosity_score": curiosity_score,
            "reader_feedback": (
                "Scene maintains strong engagement and dialogue timing." if not boredom_risk == "High"
                " else Scene requires stronger emotional tension and conflict resolution."
            )
        }

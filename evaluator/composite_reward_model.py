"""
Composite Story Quality Reward Model (AI Author Studio v3 / RLHF & DPO Alignment).

Computes a multi-signal story quality reward score (0.0 to 10.0) combining:
+ Story Coherence (+2.0)
+ Character Voice Consistency (+1.5)
+ Object Continuity (+1.5)
+ Goal Completion (+2.0)
+ Comedy Timing & Dialogue Brevity (+1.5)
+ Reader Curiosity (+1.5)
- Repetition & Drift Penalties (-2.0)
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any, List
import re


@dataclass
class RewardBreakdown:
    story_coherence: float
    character_voice: float
    object_continuity: float
    goal_completion: float
    comedy_timing: float
    reader_curiosity: float
    repetition_penalty: float
    composite_reward_score: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class CompositeStoryRewardModel:
    """Evaluates story scenes against composite multi-signal quality objectives."""

    def evaluate_scene(self, prose: str, goal: str, characters: List[str], objects: List[str]) -> RewardBreakdown:
        """Calculates multi-signal reward score for candidate prose."""
        words = prose.split()
        word_count = len(words)

        # 1. Story Coherence & Goal Completion
        goal_words = [w.lower() for w in goal.split() if len(w) > 3]
        goal_matches = sum(1 for w in goal_words if w in prose.lower())
        goal_completion = min(2.0, (goal_matches / max(1, len(goal_words))) * 2.0)
        coherence = 2.0 if word_count >= 500 else 1.0

        # 2. Character Voice & Dialogue Brevity
        dialogue_turns = re.findall(r'"([^"]*)"', prose)
        avg_dialogue_len = sum(len(d.split()) for d in dialogue_turns) / max(1, len(dialogue_turns))
        # Reward deadpan brevity under 15 words per turn
        char_voice = 1.5 if (avg_dialogue_len <= 15 and len(dialogue_turns) >= 4) else 0.8

        # 3. Object Continuity
        obj_found = sum(1 for o in objects if o.lower() in prose.lower())
        obj_continuity = min(1.5, (obj_found / max(1, len(objects))) * 1.5)

        # 4. Comedy Timing & Reader Curiosity
        has_punchline = any(w in prose.lower() for w in ["suddenly", "however", "unexpectedly", "by jove"])
        comedy_timing = 1.5 if has_punchline else 0.8
        reader_curiosity = 1.5 if (word_count >= 650 and '"' in prose) else 0.9

        # 5. Repetition & Drift Penalties
        unique_ratio = len(set(w.lower() for w in words)) / max(1, word_count)
        rep_penalty = 0.0 if unique_ratio >= 0.35 else -2.0

        # Total Composite Reward Score out of 10.0
        total_score = round(
            max(0.0, min(10.0, coherence + char_voice + obj_continuity + goal_completion + comedy_timing + reader_curiosity + rep_penalty)),
            2
        )

        return RewardBreakdown(
            story_coherence=round(coherence, 2),
            character_voice=round(char_voice, 2),
            object_continuity=round(obj_continuity, 2),
            goal_completion=round(goal_completion, 2),
            comedy_timing=round(comedy_timing, 2),
            reader_curiosity=round(reader_curiosity, 2),
            repetition_penalty=round(rep_penalty, 2),
            composite_reward_score=total_score,
        )

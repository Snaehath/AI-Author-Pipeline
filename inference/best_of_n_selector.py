"""
Best-of-N Candidate Selector Module (AI Author Studio v3 / RLHF & Preference Sampling).

Generates N candidate scene variations per chapter, scores each candidate using the Composite
Story Quality Reward Model, and selects the winning candidate with the highest reward score.
"""

from typing import List, Dict, Any
from AI_Author.evaluator.composite_reward_model import CompositeStoryRewardModel, RewardBreakdown
from AI_Author.inference.blueprint_planner import ChapterBlueprint
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.BestOfNSelector")


class BestOfNCandidateSelector:
    """Orchestrates Best-of-N candidate scene generation and reward model selection."""

    def __init__(self):
        self.reward_model = CompositeStoryRewardModel()

    def select_best_candidate(
        self,
        candidates: List[str],
        blueprint: ChapterBlueprint,
    ) -> Dict[str, Any]:
        """Scores candidate scenes and selects the variation with the highest reward score."""
        logger.info(f"Evaluating {len(candidates)} candidate scene variations against Composite Reward Model...")
        
        scored_candidates = []
        for idx, prose in enumerate(candidates, 1):
            breakdown = self.reward_model.evaluate_scene(
                prose=prose,
                goal=blueprint.goal,
                characters=blueprint.characters_present,
                objects=blueprint.objects_introduced,
            )
            scored_candidates.append({
                "candidate_idx": idx,
                "reward_score": breakdown.composite_reward_score,
                "breakdown": breakdown.to_dict(),
                "prose": prose,
            })
            logger.info(f"  • Candidate #{idx}: Composite Reward Score = {breakdown.composite_reward_score}/10.0")

        # Sort by reward score descending
        scored_candidates.sort(key=lambda x: x["reward_score"], reverse=True)
        winner = scored_candidates[0]

        logger.info(f"✓ Selected Candidate #{winner['candidate_idx']} (Reward: {winner['reward_score']}/10.0) as Chapter Masterpiece!")
        return winner

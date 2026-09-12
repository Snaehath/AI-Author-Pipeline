"""
Context Budgeter Module.

Allocates and optimizes prompt context under strict token budgets using knapsack-style packing.
Enforces epistemic isolation by excluding facts unknown to the POV character.
"""

from typing import Dict, Any, List, Optional
from story_engine.state.world import WorldState
from story_engine.epistemic.character_knowledge import EpistemicTracker
from story_engine.epistemic.world_truth import WorldTruthBase
from story_engine.contracts.scene import SceneContract


class ContextBudgeter:
    """Knapsack-style token context builder enforcing epistemic boundaries."""

    def __init__(self, default_token_budget: int = 3500):
        self.default_token_budget = default_token_budget

    def estimate_tokens(self, text: str) -> int:
        """Heuristic estimation: ~1.3 tokens per word."""
        return int(len(text.split()) * 1.3) + 2

    def build_scene_prompt_context(
        self,
        contract: SceneContract,
        world: WorldState,
        epistemic: EpistemicTracker,
        world_truth: WorldTruthBase,
        active_threads: Optional[List[Dict[str, Any]]] = None,
        token_budget: Optional[int] = None,
    ) -> Dict[str, Any]:
        budget = token_budget or self.default_token_budget
        active_threads = active_threads or []

        pov_char = world.characters.get(contract.pov_character)
        pov_name = pov_char.name if pov_char else contract.pov_character

        sections: List[str] = []
        total_tokens = 0

        # 1. Mandatory Scene Contract Section
        contract_str = (
            f"### SCENE CONTRACT [{contract.scene_id}]\n"
            f"Location: {contract.primary_location}\n"
            f"POV: {pov_name}\n"
            f"Target Mood: {contract.target_mood} | Conflict: {contract.conflict_type}\n"
            f"Required Participants: {', '.join(contract.allowed_participants)}\n"
            f"Allowed Props: {', '.join(contract.allowed_props)}\n"
        )
        sections.append(contract_str)
        total_tokens += self.estimate_tokens(contract_str)

        # 2. POV Character State & Knowledge Section (Epistemic Isolation!)
        pov_kb = epistemic.get_or_create(contract.pov_character)
        known_propositions = []
        for fid in pov_kb.known_fact_ids:
            fact = world_truth.get_fact(fid)
            if fact:
                known_propositions.append(f"- {fact.proposition}")

        knowledge_str = (
            f"### POV KNOWLEDGE ({pov_name})\n"
            f"Current Mood: {pov_char.mood if pov_char else 'neutral'}\n"
            f"Inventory: {', '.join(pov_char.inventory) if (pov_char and pov_char.inventory) else 'empty'}\n"
            f"Known Facts:\n" + ("\n".join(known_propositions) if known_propositions else "- None") + "\n"
        )
        sections.append(knowledge_str)
        total_tokens += self.estimate_tokens(knowledge_str)

        # 3. Co-located Characters and Objects
        co_located_chars = [
            c.name for c in world.get_characters_at_location(contract.primary_location)
            if c.id != contract.pov_character and c.is_alive
        ]
        co_located_objects = [
            o.name for o in world.get_objects_at_location(contract.primary_location)
            if not o.is_hidden
        ]
        presence_str = (
            f"### PRESENT IN ROOM ({contract.primary_location})\n"
            f"Characters: {', '.join(co_located_chars) if co_located_chars else 'None'}\n"
            f"Visible Objects: {', '.join(co_located_objects) if co_located_objects else 'None'}\n"
        )
        sections.append(presence_str)
        total_tokens += self.estimate_tokens(presence_str)

        # 4. Active Plot Threads (fitted within budget)
        if active_threads:
            thread_lines = ["### ACTIVE PLOT THREADS"]
            for th in active_threads:
                line = f"- [{th.get('id', 'T')}] {th.get('question', '')} (Status: {th.get('status', 'open')})"
                line_tokens = self.estimate_tokens(line)
                if total_tokens + line_tokens < budget - 200:
                    thread_lines.append(line)
                    total_tokens += line_tokens
                else:
                    break
            if len(thread_lines) > 1:
                sections.append("\n".join(thread_lines) + "\n")

        full_prompt = "\n".join(sections)
        return {
            "prompt_context": full_prompt,
            "estimated_tokens": self.estimate_tokens(full_prompt),
            "token_budget": budget,
            "pov_character": pov_name,
        }

"""
Craft Operation & Controlled DPO Builder.

Synthesizes:
- Level 3 Writing Operations: QA tasks that train the model to analyze, deconstruct,
  rewrite with comedic restraint, and continue scenes.
- Level 4 Controlled DPO Pairs: Single-dimension contrast pairs validated by ContrastPurityValidator.
"""

import re
from typing import List, Optional
from dataset_generator.taxonomy import (
    ComicMechanism,
    ContrastDimension,
    CraftAnnotation,
    CraftOperationTask,
    ControlledDPOPair,
    StoryFacts,
    TaskType,
)
from dataset_generator.contrast_purity import ContrastPurityValidator


class CraftOperationBuilder:
    """Builds interactive training operations and audited contrast pairs from annotated scenes."""

    def __init__(self):
        self.purity_validator = ContrastPurityValidator()

    def build_operations(
        self, text: str, facts: StoryFacts, craft: CraftAnnotation
    ) -> List[CraftOperationTask]:
        """Generates Level 3 craft operations for a scene."""
        tasks: List[CraftOperationTask] = []
        if len(facts.characters) >= 2:
            char_desc = f"{facts.characters[0]} and {facts.characters[1]}"
        elif len(facts.characters) == 1:
            char_desc = f"{facts.characters[0]}"
        else:
            char_desc = "the characters"

        # Task 1: Identify Mechanism
        tasks.append(
            CraftOperationTask(
                task_type=TaskType.IDENTIFY_MECHANISM,
                prompt=(
                    f"Analyze the comedic craft in the following scene involving {char_desc}.\n\n"
                    f"Passage:\n\"\"\"\n{text}\n\"\"\"\n\n"
                    f"Question: What is the primary comic mechanism driving this scene, "
                    f"and what secondary dynamics support it?"
                ),
                expected_output=(
                    f"Primary Mechanism: {craft.primary_mechanism.value}.\n"
                    f"Supporting Dynamics: {', '.join(m.value for m in craft.secondary_mechanisms) or 'Subtextual banter'}.\n\n"
                    f"Craft Explanation: The comedic tension is driven by {craft.primary_mechanism.value.lower()}, "
                    f"where {craft.setup_summary} The effect is heightened because the characters maintain "
                    f"a {craft.tone.value.lower()} posture despite the escalating social absurdity."
                ),
                target_concept=craft.primary_mechanism.value,
            )
        )

        # Task 2: Extract Structure
        tasks.append(
            CraftOperationTask(
                task_type=TaskType.EXTRACT_STRUCTURE,
                prompt=(
                    f"Deconstruct the four-part comedic structure of this passage into "
                    f"Setup, Escalation, Reversal, and Payoff.\n\n"
                    f"Passage:\n\"\"\"\n{text}\n\"\"\""
                ),
                expected_output=(
                    f"1. Setup: {craft.setup_summary}\n"
                    f"2. Escalation: {craft.escalation_summary}\n"
                    f"3. Reversal: {craft.reversal_summary}\n"
                    f"4. Payoff: {craft.payoff_summary}"
                ),
                target_concept="FOUR_PART_STRUCTURE",
            )
        )

        # Task 3: Rewrite with Restraint
        tasks.append(
            CraftOperationTask(
                task_type=TaskType.REWRITE_RESTRAINT,
                prompt=(
                    f"The following scene hinges on {craft.primary_mechanism.value.lower()}.\n"
                    f"Rewrite the excerpt to maximize deadpan restraint, avoiding any explanatory "
                    f"narrative commentary that tells the reader why the situation is ridiculous.\n\n"
                    f"Original Excerpt:\n\"\"\"\n{text[:300]}...\n\"\"\""
                ),
                expected_output=(
                    f"A refined version emphasizing understated comedic timing:\n\n"
                    f"{self._synthesize_restrained_rewrite(text, craft)}"
                ),
                target_concept="COMEDIC_RESTRAINT",
            )
        )

        # Task 4: Continue Tension
        tasks.append(
            CraftOperationTask(
                task_type=TaskType.CONTINUE_TENSION,
                prompt=(
                    f"Continue the scene below for another conversational exchange involving {char_desc}. "
                    f"Maintain the unresolved comedic tension of {craft.primary_mechanism.value.lower()} "
                    f"and preserve the {craft.tone.value.lower()} tone without prematurely resolving the crisis.\n\n"
                    f"Context:\n\"\"\"\n{text[-350:] if len(text) > 350 else text}\n\"\"\""
                ),
                expected_output=(
                    self._synthesize_continuation(facts, craft)
                ),
                target_concept="UNRESOLVED_TENSION",
            )
        )

        return tasks

    def build_contrast_dpo_pair(
        self, text: str, facts: StoryFacts, craft: CraftAnnotation
    ) -> Optional[ControlledDPOPair]:
        """
        Synthesizes a controlled DPO pair targeting COMEDIC_RESTRAINT or DIALOGUE_SUBTEXT,
        and validates that contrast purity >= 0.85.
        """
        dimension = (
            ContrastDimension.COMEDIC_RESTRAINT
            if craft.primary_mechanism == ComicMechanism.DEADPAN_REACTION
            else ContrastDimension.DIALOGUE_SUBTEXT
        )

        prompt = (
            f"Write the concluding exchange of a scene where {', '.join(facts.characters[:2])} "
            f"face a {craft.primary_mechanism.value.lower()} in the {facts.location.replace('_', ' ')}."
        )

        # Chosen: Masterful comedic restraint / dry subtext
        chosen = self._synthesize_chosen_sample(text, facts, craft)

        # Rejected: Violates restraint by explaining the joke or dumping exposition
        rejected = self._synthesize_rejected_flawed_sample(text, facts, craft, dimension)

        # Audit with purity validator
        report = self.purity_validator.validate(prompt, chosen, rejected, dimension)
        if report.purity_score < ContrastPurityValidator.PURITY_THRESHOLD:
            return None

        return ControlledDPOPair(
            prompt=prompt,
            chosen=chosen,
            rejected=rejected,
            target_dimension=dimension,
            purity_report=report,
        )

    def _synthesize_restrained_rewrite(self, text: str, craft: CraftAnnotation) -> str:
        """Strips explanatory adjectives and enhances deadpan tone."""
        # Clean text of excessive exclamation points and over-explanatory adverbs
        cleaned = re.sub(r'!(?=\s|$)', '.', text[:250].strip())
        cleaned = re.sub(r'\b(hilariously|ridiculously|absurdly|comically)\b\s*', '', cleaned, flags=re.IGNORECASE)
        return cleaned + "."

    def _synthesize_continuation(self, facts: StoryFacts, craft: CraftAnnotation) -> str:
        """Synthesizes a valid continuation respecting character restraint."""
        c1 = facts.characters[0] if facts.characters else "Bertie"
        c2 = facts.characters[1] if len(facts.characters) > 1 else "Jeeves"
        
        return (
            f'"{c2}," said {c1}, staring fixedly at the carpet, "there are moments when one feels '
            f'that the universe has taken a distinct dislike to one."\n\n'
            f'"The contingency is not uncommon, sir," observed {c2} impassively. '
            f'"Shall I bring the tea?"'
        )

    def _synthesize_chosen_sample(self, text: str, facts: StoryFacts, craft: CraftAnnotation) -> str:
        c1 = facts.characters[0] if facts.characters else "Arthur"
        c2 = facts.characters[1] if len(facts.characters) > 1 else "James"
        return (
            f'{c1} cleared his throat with great care. "It would appear," he murmured, '
            f'"that our minor miscalculation regarding the {facts.objects[0] if facts.objects else "matter"} '
            f'has reached the ears of the authorities."\n\n'
            f'{c2} placed his teacup down without a sound. "Precisely, sir. The situation offers '
            f'ample scope for fortitude."'
        )

    def _synthesize_rejected_flawed_sample(
        self, text: str, facts: StoryFacts, craft: CraftAnnotation, dimension: ContrastDimension
    ) -> str:
        c1 = facts.characters[0] if facts.characters else "Arthur"
        c2 = facts.characters[1] if len(facts.characters) > 1 else "James"
        if dimension == ContrastDimension.COMEDIC_RESTRAINT:
            return (
                f'{c1} burst out in frantic exasperation! "It is so laughable because we are in complete '
                f'disaster over the {facts.objects[0] if facts.objects else "matter"}! How absurd that '
                f'the authorities know everything! This is pure comedy!"\n\n'
                f'{c2} laughed loudly. "Yes, because it is funny how foolish we look right now!"'
            )
        else:
            return (
                f'{c1} sighed heavily. "I feel terribly insecure and my secret plan is falling apart because '
                f'I am desperate to avoid public shame regarding the {facts.objects[0] if facts.objects else "matter"}."\n\n'
                f'{c2} replied bluntly. "My true motive is to judge your poor decisions because you have '
                f'no dignity left."'
            )

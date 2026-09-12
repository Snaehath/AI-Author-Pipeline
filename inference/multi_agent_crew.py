"""
Multi-Agent 7-Pass Editing Crew Module (AI Author Studio v2).

Orchestrates 7 specialized revision passes:
Pass 1: Writer Raw Expansion
Pass 2: Character Voice & Identity Reviewer
Pass 3: Dialogue Brevity & Monologue Reviewer
Pass 4: Pacing & Scene Goal Resolution Reviewer
Pass 5: Comedy & Punchline Editor
Pass 6: Subplot & Foreshadowing Weaver
Pass 7: Final Prose Rhythm Polish
"""

from typing import Optional
from AI_Author.inference.generator import StoryGenerator
from AI_Author.inference.blueprint_planner import ChapterBlueprint
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.MultiAgentCrew")


class MultiAgentEditingCrew:
    """Orchestrates multi-agent specialized revision passes over chapter prose."""

    def __init__(self, generator: Optional[StoryGenerator] = None):
        self.generator = generator or StoryGenerator()

    def generate_masterpiece_chapter(
        self,
        book_title: str,
        blueprint: ChapterBlueprint,
        previous_context: str = "",
        rag_prompt: str = "",
    ) -> str:
        """Runs multi-agent revision crew passes to produce publication-grade chapter prose."""

        # PASS 1: Writer Agent (Raw Chapter Expansion)
        logger.info(f"[Pass 1/7] Writer Agent expanding raw draft for Ch.{blueprint.chapter_num}...")
        raw_draft = self.generator.create_chapter(
            book_title=book_title,
            chapter_num=blueprint.chapter_num,
            summary=blueprint.goal,
            previous_chapter_context=previous_context,
            character_bible_prompt=f"{blueprint.to_prompt_context()}\n\n{rag_prompt}",
        )

        # PASS 2 & 3: Character & Dialogue Reviewer Agent
        logger.info(f"[Pass 2-3/7] Character & Dialogue Reviewer evaluating voice contrast...")
        review_prompt = (
            "You are a Senior Dialogue & Character Voice Editor.\n"
            "Evaluate this draft:\n"
            "1. Barnaby Voice: Must speak in deadpan under-15-word turns ('Very good, my Lord').\n"
            "2. Reginald Voice: Must speak in over-excited British slang ('By Jove!', 'Old top!').\n"
            "3. Monologue Check: Eliminate any long speeches. Enforce rapid back-and-forth exchanges.\n"
            "Output 2 concise revision instructions."
        )
        voice_critique = self.generator._generate_response(review_prompt, "Review draft voice:", raw_draft[:1000])

        # PASS 4 & 5: Comedy & Pacing Editor Agent
        logger.info(f"[Pass 4-5/7] Comedy & Pacing Editor evaluating setup/punchline timing...")
        comedy_prompt = (
            "You are a Master Comedy & Pacing Editor.\n"
            "1. Joke Setup/Punchline: Ensure ironic contrast is clear.\n"
            "2. Obstacle Pacing: Ensure the scene conflict is not resolved prematurely.\n"
            "Output 2 concise comedy polish notes."
        )
        comedy_notes = self.generator._generate_response(comedy_prompt, "Review comedy timing:", raw_draft[:1000])

        # PASS 6 & 7: Final Master Polish Editor Agent (Enforce 10-12 word sentence cadence & 45-50% dialogue)
        logger.info(f"[Pass 6-7/7] Master Editor applying final prose rhythm polish & blueprint adherence...")
        final_sys_p = (
            "You are a Master Fiction Editor performing the final publication polish.\n"
            "STRICT SENTENCE CADENCE: Keep sentences short, crisp, and energetic (average 10-12 words per sentence). Avoid run-on sentences.\n"
            "STRICT DIALOGUE RATIO: Enforce 45-50% spoken dialogue across the chapter.\n"
            "STRICT LENGTH MANDATE: DO NOT condense or summarize. Write a full, detailed, expansive multi-paragraph scene (700-800 words).\n"
            "STRICT NEGATIVE CONSTRAINT: DO NOT output historical court-martial text, legal letters, footnotes, or hyphenated dictionary lists.\n"
            "STRICT BLUEPRINT COMPLIANCE MANDATE:\n"
            f"• GOAL: You MUST advance the goal: {blueprint.goal}\n"
            f"• CONFLICT: You MUST include the conflict: {blueprint.conflict}\n"
            f"• CHARACTERS PRESENT: ONLY use [{', '.join(blueprint.characters_present)}]. DO NOT introduce new characters.\n"
            f"• OBJECTS INTRODUCED: You MUST include [{', '.join(blueprint.objects_introduced)}]. DO NOT introduce random ungrounded objects.\n"
            f"• VOICE REVISION NOTES: {voice_critique[:250]}\n"
            f"• COMEDY REVISION NOTES: {comedy_notes[:250]}\n"
            "STRICT POV LOCK: Third-Person Limited following Lord Reginald Finch at Blackwood Manor.\n"
            "• Barnaby MUST speak in deadpan under-15-word turns ('Very good, my Lord. If I might suggest...').\n"
            "• Lord Reginald MUST speak in over-excited British slang ('By Jove!', 'Old top!').\n"
            "Output ONLY the final, polished continuous publication prose."
        )

        polished_prose = self.generator._generate_response(
            final_sys_p,
            f"Write the full revised publication prose for Chapter {blueprint.chapter_num} of '{book_title}' (Goal: {blueprint.goal}):",
            raw_draft,
        )

        logger.info(f"✓ Chapter {blueprint.chapter_num} Multi-Agent Crew Revision Complete!")
        return polished_prose

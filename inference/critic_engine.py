"""
Multi-Pass Literary Critic and Revision Engine Module.

Implements a 3-Pass Generation Pipeline:
- Pass 1 (Drafting): Generate raw chapter prose.
- Pass 2 (Critique): Evaluate chapter pacing, voice contrast, and comedic timing.
- Pass 3 (Revision): Polish and rewrite the chapter incorporating editor feedback.
"""

from typing import Dict, Any, Optional
from AI_Author.inference.generator import StoryGenerator
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.CriticEngine")


class MultiPassCriticEngine:
    """Orchestrates 3-pass draft -> critique -> revision generation."""

    def __init__(self, generator: Optional[StoryGenerator] = None):
        self.generator = generator or StoryGenerator()

    def generate_polished_chapter(
        self,
        book_title: str,
        chapter_num: int,
        summary: str,
        previous_context: str = "",
        character_bible_prompt: str = "",
    ) -> str:
        """Executes a 3-pass generation pipeline for maximum literary quality."""

        # PASS 1: Raw Draft Generation
        logger.info(f"[Pass 1/3] Generating raw draft for Chapter {chapter_num}...")
        raw_draft = self.generator.create_chapter(
            book_title=book_title,
            chapter_num=chapter_num,
            summary=summary,
            previous_chapter_context=previous_context,
            character_bible_prompt=character_bible_prompt,
        )

        # PASS 2: Specific Line-Editor Critique Pass
        logger.info(f"[Pass 2/3] Running Specific Line-Editor Critique on Chapter {chapter_num}...")
        critique_prompt = (
            "You are a senior line editor reviewing a comedic novel draft.\n"
            "Identify specific line issues:\n"
            "1. Joke Repetition: Check if any paragraph repeats the same joke or idea twice.\n"
            "2. Voice Contrast: Ensure Barnaby speaks in concise deadpan sentences (under 15 words) while Lord Reginald uses excited upper-class banter.\n"
            "3. Pacing: Ensure the scene obstacle is not resolved too quickly or abruptly.\n"
            "Provide 2 specific line-editing instructions for the rewrite pass."
        )
        critique = self.generator._generate_response(critique_prompt, "Critique this draft prose:", raw_draft[:1200])

        # PASS 3: Polished Revision Pass (Enforce 600-800 word standardized depth + POV/Location Lock)
        logger.info(f"[Pass 3/3] Polishing and revising Chapter {chapter_num} with Line-Editor Feedback...")
        revision_sys_p = (
            "You are a master fiction editor performing a final polish.\n"
            "STRICT POV LOCK: Third-Person Limited following Lord Reginald Finch. DO NOT switch narrator identity.\n"
            "STRICT LOCATION LOCK: 1920s Blackwood Manor, England. DO NOT introduce random foreign cities (Chicago, Troy, Montreal).\n"
            f"• SPECIFIC LINE-EDITOR NOTES: {critique[:350]}\n"
            "• Barnaby MUST speak in deadpan, concise sentences under 15 words per turn ('Very good, my Lord').\n"
            "• Lord Reginald MUST speak in over-excited upper-class slang ('By Jove!', 'Old top!').\n"
            "• Enforce rapid back-and-forth dialogue exchanges. Eliminate long monologues.\n"
            "• Write a full, detailed, multi-paragraph scene covering the exact scene goal.\n"
            "Output ONLY the final, polished continuous story prose."
        )
        polished_prose = self.generator._generate_response(
            revision_sys_p,
            f"Write the full revised continuous prose for Chapter {chapter_num} of '{book_title}' (Scene Goal: {summary}):",
            raw_draft,
        )

        logger.info(f"✓ Chapter {chapter_num} 3-Pass Revision Complete!")
        return polished_prose

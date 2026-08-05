"""
SFT Synthesizer Module.

Converts extracted storytelling knowledge from Modules 1-7 into structured
Supervised Fine-Tuning instruction-response training pairs across 8 task categories.
"""

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any, Optional

from AI_Author.dataset_generator.prompt_templates import PromptTemplates
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.DatasetGenerator.SFTSynthesizer")


@dataclass
class SFTExample:
    """Represents a single Supervised Fine-Tuning (SFT) training pair."""
    system: str
    instruction: str
    input: str
    output: str
    task_type: str
    source_book: str
    chapter_index: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        """Converts SFTExample object to dictionary."""
        return asdict(self)


class SFTSynthesizer:
    """Synthesizes SFT instruction-response pairs from book knowledge JSON outputs."""

    def __init__(self, templates: Optional[PromptTemplates] = None):
        """Initializes SFTSynthesizer.

        Args:
            templates: Optional PromptTemplates instance.
        """
        self.templates = templates or PromptTemplates()

    def synthesize_all(self, book_dir: Path, knowledge: Dict[str, Any]) -> List[SFTExample]:
        """Synthesizes SFT training examples across all 8 writing task categories.

        Args:
            book_dir: Path to book output directory.
            knowledge: Dictionary containing all loaded analysis JSON outputs.

        Returns:
            List of SFTExample objects.
        """
        book_title = knowledge.get("metadata", {}).get("title", book_dir.name)
        examples: List[SFTExample] = []

        # Category 1: Story Planning
        examples.extend(self._synthesize_story_planning(book_title, knowledge))

        # Category 2: Character Writing
        examples.extend(self._synthesize_character_writing(book_title, knowledge))

        # Category 3: Dialogue Generation
        examples.extend(self._synthesize_dialogue_generation(book_title, knowledge))

        # Category 4: Scene Writing
        examples.extend(self._synthesize_scene_writing(book_title, knowledge))

        # Category 5: Pacing Control
        examples.extend(self._synthesize_pacing_control(book_title, knowledge))

        # Category 6: Prose Polish & Editing
        examples.extend(self._synthesize_prose_editing(book_title, knowledge))

        # Category 7: Emotional Writing
        examples.extend(self._synthesize_emotional_writing(book_title, knowledge))

        # Category 8: Revision & Conflict Escalation
        examples.extend(self._synthesize_revision_conflict(book_title, knowledge))

        logger.info(f"Synthesized {len(examples)} SFT instruction pairs for '{book_title}'.")
        return examples

    def _synthesize_story_planning(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        plot_info = k.get("plot_analysis", {}).get("plot_points", {})
        if not plot_info:
            return []

        hook_ev = plot_info.get("hook", {}).get("evidence", "")
        mid_ev = plot_info.get("midpoint", {}).get("evidence", "")
        climax_ev = plot_info.get("climax", {}).get("evidence", "")

        instruction = self.templates.format_instruction("story_planning", f"for '{book_title}'")
        input_str = self.templates.format_input({
            "book_title": book_title,
            "target_arc": "3-Act Heroic Arc",
        })
        output_str = (
            f"**Story Outline for {book_title}**\n\n"
            f"- **Hook**: {hook_ev}\n"
            f"- **Midpoint**: {mid_ev}\n"
            f"- **Climax**: {climax_ev}"
        )

        return [SFTExample(
            system=self.templates.get_system_prompt(),
            instruction=instruction,
            input=input_str,
            output=output_str,
            task_type="story_planning",
            source_book=book_title,
        )]

    def _synthesize_character_writing(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        chars = k.get("character_analysis", {}).get("characters", [])
        examples = []
        for char in chars:
            name = char.get("name")
            app = char.get("appearance", [{}])[0].get("evidence", "")
            pers = char.get("personality", [{}])[0].get("value", "Determined")

            instruction = self.templates.format_instruction("character_writing", f"Character: {name}")
            input_str = self.templates.format_input({"name": name, "personality": pers})
            output_str = app if app else f"{name} stepped forward with quiet determination."

            examples.append(SFTExample(
                system=self.templates.get_system_prompt(),
                instruction=instruction,
                input=input_str,
                output=output_str,
                task_type="character_writing",
                source_book=book_title,
            ))
        return examples

    def _synthesize_dialogue_generation(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        dialogues = k.get("dialogue_analysis", {}).get("dialogues", [])
        examples = []
        for d in dialogues:
            speaker = d.get("speaker", {}).get("value", "Character")
            spoken = d.get("spoken_text", "")
            tag = d.get("speech_tag", "")
            emotion = d.get("emotion", {}).get("value", "Calm")

            instruction = self.templates.format_instruction("dialogue_generation", f"Speaker: {speaker}")
            input_str = self.templates.format_input({"speaker": speaker, "target_emotion": emotion})
            output_str = f'"{spoken}," {tag}.'.replace("..", ".")

            examples.append(SFTExample(
                system=self.templates.get_system_prompt(),
                instruction=instruction,
                input=input_str,
                output=output_str,
                task_type="dialogue_generation",
                source_book=book_title,
                chapter_index=d.get("chapter_index"),
            ))
        return examples

    def _synthesize_scene_writing(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        chaps = k.get("chapters", [])
        examples = []
        for chap in chaps:
            c_idx = chap.get("chapter_index", 1)
            c_title = chap.get("chapter_title", "")
            scenes = chap.get("scenes", [])
            if scenes:
                scene_text = " ".join([p["text"] for p in scenes[0].get("paragraphs", [])])
                instruction = self.templates.format_instruction("scene_writing", f"Chapter {c_idx}: {c_title}")
                input_str = self.templates.format_input({"chapter": c_title, "pov": "Third-Person Limited"})

                examples.append(SFTExample(
                    system=self.templates.get_system_prompt(),
                    instruction=instruction,
                    input=input_str,
                    output=scene_text,
                    task_type="scene_writing",
                    source_book=book_title,
                    chapter_index=c_idx,
                ))
        return examples

    def _synthesize_pacing_control(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        story_ans = k.get("story_analysis", {}).get("chapter_analyses", [])
        examples = []
        for chap_an in story_ans:
            c_idx = chap_an.get("chapter_index", 1)
            pacing_val = chap_an.get("pacing", {}).get("value", "Moderate")
            evidence = chap_an.get("pacing", {}).get("evidence", "")

            instruction = self.templates.format_instruction("pacing_control", f"Pacing: {pacing_val}")
            input_str = self.templates.format_input({"target_pacing": pacing_val})

            examples.append(SFTExample(
                system=self.templates.get_system_prompt(),
                instruction=instruction,
                input=input_str,
                output=evidence if len(evidence) > 20 else f"Narrative pacing executed at {pacing_val} speed.",
                task_type="pacing_control",
                source_book=book_title,
                chapter_index=c_idx,
            ))
        return examples

    def _synthesize_prose_editing(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        chaps = k.get("chapters", [])
        examples = []
        for chap in chaps:
            c_idx = chap.get("chapter_index", 1)
            scenes = chap.get("scenes", [])
            if scenes:
                paragraphs = scenes[0].get("paragraphs", [])
                if paragraphs:
                    raw = paragraphs[0].get("text", "")
                    instruction = self.templates.format_instruction("prose_editing", "Enhance flow & sensory detail")
                    input_str = self.templates.format_input({"raw_draft": raw})

                    examples.append(SFTExample(
                        system=self.templates.get_system_prompt(),
                        instruction=instruction,
                        input=input_str,
                        output=raw,
                        task_type="prose_editing",
                        source_book=book_title,
                        chapter_index=c_idx,
                    ))
        return examples

    def _synthesize_emotional_writing(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        timeline = k.get("emotion_analysis", {}).get("emotion_timeline", [])
        examples = []
        for point in timeline:
            c_idx = point.get("chapter_index", 1)
            dom_em = point.get("dominant_emotion", {}).get("value", "Calm")
            ev = point.get("dominant_emotion", {}).get("evidence", "")

            instruction = self.templates.format_instruction("emotional_writing", f"Emotion: {dom_em}")
            input_str = self.templates.format_input({"target_emotion": dom_em, "valence": point.get("valence")})

            examples.append(SFTExample(
                system=self.templates.get_system_prompt(),
                instruction=instruction,
                input=input_str,
                output=ev if len(ev) > 15 else f"Scene written with {dom_em} emotional resonance.",
                task_type="emotional_writing",
                source_book=book_title,
                chapter_index=c_idx,
            ))
        return examples

    def _synthesize_revision_conflict(self, book_title: str, k: Dict[str, Any]) -> List[SFTExample]:
        chaps = k.get("chapters", [])
        examples = []
        for chap in chaps:
            c_idx = chap.get("chapter_index", 1)
            scenes = chap.get("scenes", [])
            if len(scenes) > 0:
                paragraphs = scenes[0].get("paragraphs", [])
                if len(paragraphs) > 1:
                    draft = paragraphs[0]["text"]
                    revised = f"{paragraphs[0]['text']}\n\n{paragraphs[1]['text']}"
                    instruction = self.templates.format_instruction("revision_conflict", "Escalate scene tension")
                    input_str = self.templates.format_input({"draft": draft})

                    examples.append(SFTExample(
                        system=self.templates.get_system_prompt(),
                        instruction=instruction,
                        input=input_str,
                        output=revised,
                        task_type="revision_conflict",
                        source_book=book_title,
                        chapter_index=c_idx,
                    ))
        return examples

"""
Story Generator Module for Inference.

Implements 10 specialized storytelling commands utilizing the base model
and fine-tuned LoRA adapter.
"""

import json
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.inference.model_loader import load_inference_model_and_tokenizer
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.Generator")


class StoryGenerator:
    """Provides 10 core novel generation and author editing commands."""

    def __init__(
        self,
        model: Optional[Any] = None,
        tokenizer: Optional[Any] = None,
        config_path: Optional[Path] = None,
    ):
        """Initializes StoryGenerator.

        Args:
            model: Pre-loaded PEFT model instance.
            tokenizer: Pre-loaded AutoTokenizer instance.
            config_path: Path to inference_config.json.
        """
        self.root_dir = Path(__file__).resolve().parent.parent
        self.config_path = config_path or (self.root_dir / "config" / "inference_config.json")
        self.config = self._load_config()

        gen_cfg = self.config.get("generation", {})
        self.temperature = gen_cfg.get("temperature", 0.7)
        self.top_p = gen_cfg.get("top_p", 0.9)
        self.repetition_penalty = gen_cfg.get("repetition_penalty", 1.1)
        self.max_new_tokens = gen_cfg.get("max_new_tokens", 512)

        if model is not None and tokenizer is not None:
            self.model = model
            self.tokenizer = tokenizer
        else:
            base_p = self.config.get("base_model_path", "models/Qwen2.5-1.5B-Instruct")
            lora_p = self.config.get("lora_adapter_path", "models/story_lora_adapter")
            self.model, self.tokenizer = load_inference_model_and_tokenizer(
                str(self.root_dir / base_p),
                str(self.root_dir / lora_p),
            )

    def _load_config(self) -> Dict[str, Any]:
        """Loads inference configuration JSON if present."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    logger.info(f"Loaded inference config from '{self.config_path.name}'")
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not read inference config file ({e}). Using defaults.")
        return {}

    def _generate_response(self, system_prompt: str, user_instruction: str, user_input: str = "") -> str:
        """Helper to format ChatML prompt and run model generation."""
        import torch

        user_content = f"{user_instruction}\n\n{user_input}".strip() if user_input else user_instruction
        chatml_prompt = (
            f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
            f"<|im_start|>user\n{user_content}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )

        inputs = self.tokenizer(chatml_prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k, v in inputs.items()}

        t0 = time.time()
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                temperature=self.temperature,
                top_p=self.top_p,
                repetition_penalty=self.repetition_penalty,
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id,
            )
        gen_time_ms = int((time.time() - t0) * 1000)

        prompt_len = int(inputs["input_ids"].shape[-1])
        total_len = int(outputs[0].shape[-1])
        self.last_generation_stats = {
            "prompt_tokens": prompt_len,
            "completion_tokens": max(0, total_len - prompt_len),
            "total_tokens": total_len,
            "generation_time_ms": gen_time_ms,
        }

        full_decoded = self.tokenizer.decode(outputs[0], skip_special_tokens=False)
        assistant_part = full_decoded.split("<|im_start|>assistant\n")[-1]

        # Stop strictly at the first EOS / ChatML end token to prevent post-generation hallucination
        for stop_tok in ["<|im_end|>", "<|endoftext|>", "</s>"]:
            if stop_tok in assistant_part:
                assistant_part = assistant_part.split(stop_tok)[0]

        clean_response = assistant_part.strip()

        # Clean Gutenberg illustration, stage direction tags, and legal disclaimers
        from AI_Author.utils.text_sanitizer import sanitize_generated_prose
        return sanitize_generated_prose(clean_response)

    # 1. Create Novel
    def create_novel(self, title: str, genre: str, premise: str, character_bible_prompt: str = "") -> str:
        sys_p = "You are a professional AI novel author specializing in 3-Act story planning."
        if character_bible_prompt:
            sys_p = f"{sys_p}\n\n{character_bible_prompt}"
        inst = f"Create a 3-Act story outline with 8-point plot structure for a novel titled '{title}'."
        inp = f"Genre: {genre} | Premise: {premise}"
        return self._generate_response(sys_p, inst, inp)

    # 2. Create Chapter with Sequential Continuity & Character Bible Constraint
    def create_chapter(
        self,
        book_title: str,
        chapter_num: int,
        summary: str,
        previous_chapter_context: str = "",
        character_bible_prompt: str = "",
    ) -> str:
        sys_p = (
            "You are a professional AI novel author writing an ongoing continuous novel.\n"
            "STRICT POV LOCK: Third-Person Limited following Lord Reginald Finch. DO NOT switch narrator identity.\n"
            "STRICT LOCATION LOCK: 1920s Blackwood Manor, England. DO NOT introduce random foreign cities (Chicago, Troy, Montreal).\n"
            "Write continuous fiction paragraphs with rich narration and rapid back-and-forth dialogue exchanges.\n"
            "DO NOT allow long monologues. Limit character speech turns to 1-3 crisp sentences per speaker.\n"
            "Do NOT output scene breakdowns, bullet points, play script directions, or illustration tags."
        )
        if character_bible_prompt:
            sys_p = f"{sys_p}\n\n{character_bible_prompt}"

        inst = (
            f"Write the full continuous narrative prose for Chapter {chapter_num} of '{book_title}'.\n"
            f"MANDATORY SCENE CHECKLIST (You MUST advance the plot through these exact cause-and-effect events):\n"
            f"{summary}"
        )
        if previous_chapter_context:
            inp = f"Previous Chapter Ending Context:\n{previous_chapter_context}\n\nChapter {chapter_num} Scene Goals:\n{summary}"
        else:
            inp = f"Chapter {chapter_num} Opening Scene Goals:\n{summary}"
        return self._generate_response(sys_p, inst, inp)

    # 3. Continue Story
    def continue_story(self, text_snippet: str, continuation_goal: str = "") -> str:
        sys_p = "You are a professional AI novel author continuing narrative prose seamlessly."
        inst = "Continue writing the story smoothly from the text snippet below."
        inp = f"Goal: {continuation_goal}\n\nExisting Draft:\n{text_snippet}" if continuation_goal else f"Existing Draft:\n{text_snippet}"
        return self._generate_response(sys_p, inst, inp)

    # 4. Rewrite Scene
    def rewrite_scene(self, original_scene: str, direction: str) -> str:
        sys_p = "You are a professional novel editor revising scenes according to creative directions."
        inst = f"Rewrite the following scene according to direction: {direction}"
        inp = f"Original Scene:\n{original_scene}"
        return self._generate_response(sys_p, inst, inp)

    # 5. Improve Dialogue
    def improve_dialogue(self, dialogue_scene: str, target_emotion: str = "Urgent / Cautious") -> str:
        sys_p = "You are a master dialogue coach enhancing character interactions, subtext, and emotion."
        inst = f"Rewrite the dialogue in this scene to express emotion: {target_emotion} with sharp subtext."
        inp = f"Dialogue Scene:\n{dialogue_scene}"
        return self._generate_response(sys_p, inst, inp)

    # 6. Increase Suspense
    def increase_suspense(self, scene_draft: str) -> str:
        sys_p = "You are a thriller and suspense fiction editor specializing in mounting tension."
        inst = "Escalate narrative conflict, environmental threats, and suspense in this scene draft."
        inp = f"Draft:\n{scene_draft}"
        return self._generate_response(sys_p, inst, inp)

    # 7. Improve Pacing
    def improve_pacing(self, scene_draft: str, target_pacing: str = "Fast-Paced Action") -> str:
        sys_p = "You are a fiction pacing editor tailoring sentence lengths and narrative speed."
        inst = f"Adjust sentence structures and sentence flow to achieve target pacing: {target_pacing}."
        inp = f"Draft:\n{scene_draft}"
        return self._generate_response(sys_p, inst, inp)

    # 8. Emotional Impact
    def emotional_impact(self, scene_draft: str, target_emotion: str = "Wonder & Awe") -> str:
        sys_p = "You are a literary novel editor enhancing emotional resonance and sensory details."
        inst = f"Enhance emotional resonance to evoke {target_emotion} in the reader."
        inp = f"Draft:\n{scene_draft}"
        return self._generate_response(sys_p, inst, inp)

    # 9. Character & World Generation
    def generate_character_world(self, prompt: str) -> str:
        sys_p = "You are a worldbuilding and character designer creating rich lore and character profiles."
        inst = "Generate a detailed character profile and world lore entry based on the requirements below."
        inp = f"Requirements: {prompt}"
        return self._generate_response(sys_p, inst, inp)

    # 10. Ending Generation
    def generate_ending(self, story_context: str) -> str:
        sys_p = "You are a fiction author crafting climactic endings and satisfying resolutions."
        inst = "Write a compelling climactic ending and resolution for the story context below."
        inp = f"Story Context:\n{story_context}"
        return self._generate_response(sys_p, inst, inp)

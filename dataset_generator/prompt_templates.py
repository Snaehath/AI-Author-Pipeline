"""
Prompt Templates Module.

Provides system prompt definitions and instruction formatting utilities
for SFT dataset generation.
"""

from typing import Dict, Any, Optional


class PromptTemplates:
    """Formats system prompts, instructions, and context inputs for SFT pairs."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes PromptTemplates.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        self.system_prompt = self.config.get(
            "system_prompt",
            "You are a professional AI novel author specializing in immersive fiction, rich character development, engaging dialogue, and balanced pacing."
        )
        self.templates = self.config.get("task_templates", {})

    def get_system_prompt(self) -> str:
        """Returns central system prompt."""
        return self.system_prompt

    def format_instruction(self, task_type: str, detail_str: str) -> str:
        """Formats instruction query string for a given task type."""
        prefix = self.templates.get(task_type, "Write a high-quality storytelling response for:")
        return f"{prefix} {detail_str}".strip()

    def format_input(self, context_dict: Dict[str, Any]) -> str:
        """Converts key-value context dictionary into readable prompt input string."""
        items = [f"{k.replace('_', ' ').title()}: {v}" for k, v in context_dict.items() if v]
        return " | ".join(items)

"""
Character and World Bible Module.

Defines and manages original character profiles, world settings, and prompt constraints
to prevent text collage leakage and enforce consistent character identities.
"""

from typing import Dict, Any, List, Optional
import json


class CharacterSpec:
    """Defines an original character specification."""

    def __init__(
        self,
        name: str,
        role: str,
        personality: str,
        speech_style: str,
        aliases: Optional[List[str]] = None,
    ):
        self.name = name
        self.role = role
        self.personality = personality
        self.speech_style = speech_style
        self.aliases = aliases or [name]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "role": self.role,
            "personality": self.personality,
            "speech_style": self.speech_style,
            "aliases": self.aliases,
        }


class CharacterBible:
    """Manages the complete character cast and world setting for a novel."""

    def __init__(
        self,
        novel_title: str,
        genre: str,
        setting: str,
        protagonist: CharacterSpec,
        sidekick: CharacterSpec,
        antagonist: CharacterSpec,
        supporting: Optional[List[CharacterSpec]] = None,
    ):
        self.novel_title = novel_title
        self.genre = genre
        self.setting = setting
        self.protagonist = protagonist
        self.sidekick = sidekick
        self.antagonist = antagonist
        self.supporting = supporting or []

    @classmethod
    def create_default_comedy_mystery(cls, title: str = "The Great Comedy of Errors & Mysteries") -> "CharacterBible":
        """Creates an original 1920s Humorous Mystery character cast."""
        return cls(
            novel_title=title,
            genre="Humorous Mystery / British Comedy",
            setting="1920s London & Country Estate (Blackwood Manor)",
            protagonist=CharacterSpec(
                name="Lord Reginald Finch",
                role="Protagonist (Eccentric wealthy amateur detective)",
                personality="Witty, dramatically over-confident, optimistic, slightly clueless aristocrat",
                speech_style="Upper-class British banter ('old chap', 'by Jove', 'frightfully intriguing')",
                aliases=["Reginald", "Reggie", "Lord Finch"],
            ),
            sidekick=CharacterSpec(
                name="Barnaby",
                role="Valet & Mastermind (Deadpan, brilliant butler)",
                personality="Calm, endlessly patient, razor-sharp intellect, subtly sarcastic",
                speech_style="Formal, understated, impeccably polite ('If I might suggest, my Lord')",
                aliases=["Barnaby"],
            ),
            antagonist=CharacterSpec(
                name="Inspector Higgins",
                role="Antagonist (Stubborn Scotland Yard Detective)",
                personality="Pompous, suspicious, loud-mouthed, quick to accuse the wrong person",
                speech_style="Gruff, authoritative police jargon ('Nonsense!', 'Under arrest!')",
                aliases=["Higgins", "Inspector Higgins"],
            ),
            supporting=[
                CharacterSpec(
                    name="Lady Beatrice",
                    role="Supporting (Formidable aristocratic aunt)",
                    personality="Domineering, sharp-tongued, obsessed with social propriety",
                    speech_style="Commanding, haughty ('Nonsense, Reginald!')",
                    aliases=["Aunt Beatrice", "Lady Beatrice"],
                ),
                CharacterSpec(
                    name="Professor Aris Thorne",
                    role="Supporting (Eccentric antique collector)",
                    personality="Absent-minded, superstitious, obsessed with rare artifacts",
                    speech_style="Fast-talking, academic, nervous",
                    aliases=["Thorne", "Professor Thorne"],
                ),
            ],
        )

    def to_prompt_context(self) -> str:
        """Formats the character bible into a strict system prompt constraint."""
        lines = [
            "==================================================",
            "STRICT ORIGINAL CHARACTER & WORLD BIBLE",
            "==================================================",
            f"• Novel Title: {self.novel_title}",
            f"• Genre: {self.genre}",
            f"• Setting: {self.setting}",
            "",
            "ALLOWED CAST MEMBERS (Do NOT invent or introduce any other characters):",
            f"1. {self.protagonist.name} ({self.protagonist.role}): {self.protagonist.personality}. Voice: {self.protagonist.speech_style}",
            f"2. {self.sidekick.name} ({self.sidekick.role}): {self.sidekick.personality}. Voice: {self.sidekick.speech_style}",
            f"3. {self.antagonist.name} ({self.antagonist.role}): {self.antagonist.personality}. Voice: {self.antagonist.speech_style}",
        ]

        for i, supp in enumerate(self.supporting, start=4):
            lines.append(f"{i}. {supp.name} ({supp.role}): {supp.personality}. Voice: {supp.speech_style}")

        lines.extend([
            "",
            "STRICT VOICE DIFFERENTIATION & DIALOGUE CONSTRAINTS:",
            "• Barnaby (Valet): MUST speak in deadpan, extremely short, polite sentences (under 15 words per turn, e.g. 'Very good, my Lord. If I might suggest...'). Never monologues.",
            "• Lord Reginald (Protagonist): Speaks in melodramatic, over-excited upper-class banter ('By Jove!', 'Old top!', 'Frightfully good!').",
            "• Mrs. Pett / Lady Beatrice: Speaks in blunt, domineering, sharp-tongued aristocratic commands.",
            "• DIALOGUE PACING: Enforce rapid back-and-forth dialogue exchanges. DO NOT allow characters to deliver long monologues.",
            "",
            "MANDATORY NARRATIVE CONSTRAINTS:",
            "• Use ONLY the characters listed above. NEVER introduce 'Father Brown', 'Flambeau', 'Jeeves', 'Bertie', 'Aria', or 'Stella Maris'.",
            "• STRICT OUTLINE ADHERENCE: Cover the exact scene goal step-by-step. Do not drift into unrelated conversations.",
            "==================================================",
        ])
        return "\n".join(lines)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "novel_title": self.novel_title,
            "genre": self.genre,
            "setting": self.setting,
            "protagonist": self.protagonist.to_dict(),
            "sidekick": self.sidekick.to_dict(),
            "antagonist": self.antagonist.to_dict(),
            "supporting": [s.to_dict() for s in self.supporting],
        }

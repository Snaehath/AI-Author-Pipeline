"""
Pre-Prose Chapter Blueprint Planner Module (AI Author Studio v2).

Generates a structured pre-prose blueprint before any chapter text is written:
- Goal
- Conflict
- Emotional Arc
- Secrets Revealed
- New Mystery
- Characters Present
- Objects Introduced
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any
import json


@dataclass
class ChapterBlueprint:
    """Represents a pre-prose structured blueprint for a single chapter."""
    chapter_num: int
    title: str
    goal: str
    conflict: str
    emotional_arc: str
    secrets_revealed: str
    new_mystery: str
    characters_present: List[str] = field(default_factory=list)
    objects_introduced: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_prompt_context(self) -> str:
        chars_str = ", ".join(self.characters_present)
        objs_str = ", ".join(self.objects_introduced)
        return (
            f"=== CHAPTER {self.chapter_num} PRE-PROSE BLUEPRINT ===\n"
            f"• Title: {self.title}\n"
            f"• Goal: {self.goal}\n"
            f"• Conflict: {self.conflict}\n"
            f"• Emotional Arc: {self.emotional_arc}\n"
            f"• Secrets Revealed: {self.secrets_revealed}\n"
            f"• New Mystery: {self.new_mystery}\n"
            f"• Characters Present: [{chars_str}]\n"
            f"• Objects Introduced: [{objs_str}]\n"
            f"=================================================="
        )


class BlueprintPlanner:
    """Orchestrates structured pre-prose blueprint planning for an entire novel."""

    def create_novel_blueprints(self, title: str, num_chapters: int = 5) -> List[ChapterBlueprint]:
        """Creates structured blueprints for all chapters."""
        base_blueprints = [
            ChapterBlueprint(
                chapter_num=1,
                title="The Urgent Invitation",
                goal="Lord Reginald must decide to attend Blackwood Manor despite Barnaby's warnings.",
                conflict="Barnaby warns of imminent social disaster, but Reginald insists on going.",
                emotional_arc="Optimistic & Over-confident -> Defiant -> Excited",
                secrets_revealed="Lady Beatrice is hosting a high-society weekend party.",
                new_mystery="Why did Mr. Peters leave sudden instructions about Blackwood Manor?",
                characters_present=["Lord Reginald Finch", "Barnaby", "Lady Beatrice"],
                objects_introduced=["Urgent Blue Envelope", "Silver Watch"],
            ),
            ChapterBlueprint(
                chapter_num=2,
                title="Afternoon Tea Chaos",
                goal="Lord Reginald attempts to impress Lady Beatrice and Professor Thorne during tea.",
                conflict="The prized silver teapot mysteriously disappears from the table.",
                emotional_arc="Charming -> Flustered -> Bewildered",
                secrets_revealed="Professor Thorne was arguing over a patent medicine earlier.",
                new_mystery="Where has the silver teapot gone?",
                characters_present=["Lord Reginald Finch", "Barnaby", "Lady Beatrice", "Professor Thorne"],
                objects_introduced=["Prized Silver Teapot", "Patent Medicine Vials"],
            ),
            ChapterBlueprint(
                chapter_num=3,
                title="Inspector Higgins Accuses",
                goal="Lord Reginald must defend his honor when Inspector Higgins arrives.",
                conflict="Higgins pompously accuses Lord Reginald of stealing the teapot.",
                emotional_arc="Indignant -> Outraged -> Determined",
                secrets_revealed="Higgins has no search warrant or actual evidence.",
                new_mystery="Who left footprints near the library window?",
                characters_present=["Lord Reginald Finch", "Barnaby", "Inspector Higgins", "Lady Beatrice"],
                objects_introduced=["Scotland Yard Badge", "Muddy Footprint Trace"],
            ),
            ChapterBlueprint(
                chapter_num=4,
                title="Barnaby's Quiet Investigation",
                goal="Barnaby investigates the study to uncover the real location of the teapot.",
                conflict="Professor Thorne refuses to admit he mislaid the teapot behind book stacks.",
                emotional_arc="Suspicious -> Analytic -> Triumphant",
                secrets_revealed="The teapot was never stolen; Thorne misplaced it while reading.",
                new_mystery="How to return the teapot without embarrassing Lady Beatrice?",
                characters_present=["Barnaby", "Professor Thorne", "Lord Reginald Finch"],
                objects_introduced=["Book Stack", "Silver Teapot"],
            ),
            ChapterBlueprint(
                chapter_num=5,
                title="Triumphant Resolution",
                goal="Barnaby discreetly returns the teapot before dinner concludes.",
                conflict="Higgins tries to save face while Reginald takes full credit.",
                emotional_arc="Tense -> Relieved -> Jubilant",
                secrets_revealed="Barnaby quietly solved the entire affair behind the scenes.",
                new_mystery="Which adventure will Lord Reginald embark on next?",
                characters_present=["Lord Reginald Finch", "Barnaby", "Lady Beatrice", "Inspector Higgins"],
                objects_introduced=["Dinner Bell", "Brandy Glasses"],
            ),
        ]

        if num_chapters <= len(base_blueprints):
            return base_blueprints[:num_chapters]

        # Dynamically extend for > 5 chapters
        extended = list(base_blueprints)
        for i in range(len(base_blueprints) + 1, num_chapters + 1):
            extended.append(
                ChapterBlueprint(
                    chapter_num=i,
                    title=f"The Misadventure Continues (Part {i})",
                    goal=f"Lord Reginald and Barnaby navigate escalating farce in Chapter {i}.",
                    conflict=f"A new comical misunderstanding arises between Reginald and Higgins.",
                    emotional_arc="Amused -> Flustered -> Triumphant",
                    secrets_revealed="Further revelations regarding Blackwood Manor emerge.",
                    new_mystery=f"Unresolved mystery for Chapter {i}",
                    characters_present=["Lord Reginald Finch", "Barnaby", "Lady Beatrice"],
                    objects_introduced=["Silver Watch", "Pocket Notebook"],
                )
            )
        return extended

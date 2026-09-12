"""
Enhanced Story Bible Database Module (AI Author Studio v2).

Queryable database tracking:
- Character attributes (age, role, speech style)
- Epistemic state (knows vs. doesn't know)
- Inventory tracker (active objects held)
- Dynamic trust affinity scores
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any


@dataclass
class CharacterProfileDB:
    """Detailed character record in Story Bible DB."""
    name: str
    age: int
    role: str
    speech_style: str
    knows: List[str] = field(default_factory=list)
    doesnt_know: List[str] = field(default_factory=list)
    inventory: List[str] = field(default_factory=list)
    trust_scores: Dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class StoryBibleDB:
    """Database managing persistent story facts, character states, and object continuity."""

    def __init__(self):
        self.characters: Dict[str, CharacterProfileDB] = {}
        self.object_locations: Dict[str, str] = {}

    def initialize_default_db(self):
        """Initializes default database for Blackwood Manor comedy cast."""
        self.characters = {
            "Lord Reginald Finch": CharacterProfileDB(
                name="Lord Reginald Finch",
                age=31,
                role="Protagonist (Aristocrat)",
                speech_style="Upper-class British banter ('By Jove!', 'Old top!')",
                knows=["Lady Beatrice invited him", "The teaset is missing"],
                doesnt_know=["Barnaby already knows where the teaset is"],
                inventory=["Silver Watch", "Urgent Blue Envelope"],
                trust_scores={"Barnaby": 9, "Inspector Higgins": 2, "Lady Beatrice": 8},
            ),
            "Barnaby": CharacterProfileDB(
                name="Barnaby",
                age=38,
                role="Valet & Mastermind",
                speech_style="Deadpan, ultra-concise, under 15 words per turn ('Very good, my Lord')",
                knows=["Teaset was misplaced by Thorne", "Higgins has no search warrant"],
                doesnt_know=["When Reginald will misplace his next watch"],
                inventory=["Pantry Keys", "Pocket Notebook"],
                trust_scores={"Lord Reginald Finch": 10, "Inspector Higgins": 1, "Lady Beatrice": 7},
            ),
            "Inspector Higgins": CharacterProfileDB(
                name="Inspector Higgins",
                age=50,
                role="Antagonist (Scotland Yard Detective)",
                speech_style="Pompous, gruff police jargon ('Under arrest!', 'Nonsense!')",
                knows=["A teaset is missing"],
                doesnt_know=["Reginald did not steal the teaset", "Thorne misplaced it"],
                inventory=["Scotland Yard Badge", "Magnifying Glass"],
                trust_scores={"Lord Reginald Finch": 2, "Barnaby": 1, "Lady Beatrice": 6},
            ),
        }
        self.object_locations = {
            "Silver Teapot": "In Blackwood Manor study, misplaced behind book stacks",
            "Urgent Blue Envelope": "In Lord Reginald's jacket pocket",
            "Scotland Yard Badge": "With Inspector Higgins",
        }

    def query_character_state(self, char_name: str) -> str:
        """Retrieves formatted state string for a character."""
        c = self.characters.get(char_name)
        if not c:
            return ""
        trust_str = ", ".join([f"{k}: {v}/10" for k, v in c.trust_scores.items()])
        return (
            f"• Character: {c.name} (Age: {c.age}, Role: {c.role})\n"
            f"  - Speech Style: {c.speech_style}\n"
            f"  - Knows: {'; '.join(c.knows)}\n"
            f"  - Doesn't Know: {'; '.join(c.doesnt_know)}\n"
            f"  - Inventory: {', '.join(c.inventory)}\n"
            f"  - Trust Affinity Scores: [{trust_str}]"
        )

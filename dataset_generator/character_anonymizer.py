"""
Character Anonymizer Module for Dataset Synthesis.

Replaces specific character names in raw book text with abstract role placeholders
([PROTAGONIST], [COMPANION], [ANTAGONIST]) so the fine-tuned model learns pure storytelling style
rather than memorizing specific character names.
"""

import re
from typing import Dict, List


class CharacterAnonymizer:
    """Anonymizes character names in text strings."""

    def __init__(self):
        # Known specific names across training books to map to abstract role tokens
        self.role_mapping: Dict[str, str] = {
            # Wodehouse Jeeves/Wooster
            "Jeeves": "[COMPANION]",
            "Bertie": "[PROTAGONIST]",
            "Wooster": "[PROTAGONIST]",
            "Lady Malvern": "[AUNT_FIGURE]",
            "Corky": "[FRIEND]",
            "Rockmetteller": "[FRIEND]",
            "Bickersteth": "[FRIEND]",

            # Chesterton Father Brown
            "Father Brown": "[PROTAGONIST]",
            "Brown": "[PROTAGONIST]",
            "Flambeau": "[COMPANION]",
            "Valentin": "[DETECTIVE]",
            "Armstrong": "[ANTAGONIST]",

            # Jerome Three Men in a Boat
            "Montmorency": "[DOG_COMPANION]",
            "Harris": "[COMPANION_A]",
            "George": "[COMPANION_B]",
            "Podger": "[UNCLE_FIGURE]",
        }

    def anonymize_text(self, text: str) -> str:
        """Replaces specific character names with abstract role tokens and cleans noise words."""
        if not text:
            return ""

        anonymized = text
        for name, placeholder in self.role_mapping.items():
            pattern = rf"\b{re.escape(name)}\b"
            anonymized = re.sub(pattern, placeholder, anonymized)

        # Sanitize single noise words in Speaker instruction fields
        noise_words = {
            "Speaker: Mrs": "Speaker: Character",
            "Speaker: Mrs.": "Speaker: Character",
            "Speaker: So": "Speaker: Character",
            "Speaker: Besides": "Speaker: Character",
            "Speaker: Well": "Speaker: Character",
            "Speaker: Standing": "Speaker: Character",
            "Speaker: Of": "Speaker: Character",
            "Speaker: At": "Speaker: Character",
            "Speaker: Where": "Speaker: Character",
            "Speaker: But": "Speaker: Character",
            "Speaker: Then": "Speaker: Character",
            "Speaker: Pill": "Speaker: Character",
            "Speaker: Unknown": "Speaker: Character",
            "Name: Then": "Name: Character",
        }
        for noise, clean in noise_words.items():
            anonymized = anonymized.replace(noise, clean)

        return anonymized

    def deanonymize_text(self, text: str, target_cast: Dict[str, str]) -> str:
        """Replaces abstract role tokens with target original character names for a specific novel."""
        if not text:
            return ""

        result = text
        default_cast = {
            "[PROTAGONIST]": "Lord Reginald",
            "[COMPANION]": "Barnaby",
            "[ANTAGONIST]": "Inspector Higgins",
            "[AUNT_FIGURE]": "Lady Beatrice",
            "[FRIEND]": "Professor Thorne",
            "[DETECTIVE]": "Inspector Higgins",
            "[COMPANION_A]": "Barnaby",
            "[COMPANION_B]": "Lord Reginald",
            "[DOG_COMPANION]": "Barnaby",
            "[UNCLE_FIGURE]": "Professor Thorne",
        }
        cast = {**default_cast, **target_cast}

        for token, original_name in cast.items():
            result = result.replace(token, original_name)

        return result

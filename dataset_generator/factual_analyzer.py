"""
Objective Factual Scene Analyzer.

Extracts ground-truth story facts directly present in the text:
- Characters involved and dialogue attribution
- Setting / Location
- Significant physical props / objects
- Dialogue ratio and turn metrics
- Explicit character goals / tensions
"""

import re
from typing import Dict, List, Set, Tuple
from dataset_generator.taxonomy import StoryFacts


class FactualSceneAnalyzer:
    """Analyzes prose to extract objective narrative facts without subjective interpretation."""

    # Common period locations in British comic fiction / social farce
    KNOWN_LOCATIONS = [
        "drawing-room", "drawing room", "study", "library", "pantry", "morning-room",
        "morning room", "hall", "vestibule", "dining-room", "dining room", "club",
        "drones club", "drones", "smoking-room", "terrace", "garden", "train", "station",
        "boudoir", "bedroom", "kitchen", "office", "court", "cab", "billiard-room"
    ]

    # Physical objects frequently driving comic farce / complications
    KNOWN_PROPS = [
        "letter", "telegram", "cheque", "check", "hat", "cap", "monocle", "umbrella",
        "stick", "manuscript", "book", "teapot", "tea-cup", "cup", "saucer", "tray",
        "whisky", "brandy", "cigarette", "cigar", "pipe", "key", "ring", "necklace",
        "cow-creamer", "statue", "vase", "portrait", "photograph", "card", "envelope",
        "watch", "coat", "boots", "trousers", "valise", "bag"
    ]

    # Speaking attribution verbs
    SPEAKING_VERBS = [
        "said", "replied", "answered", "observed", "murmured", "gasped", "inquired",
        "enquired", "cried", "shouted", "stammered", "exclaimed", "whispered", "growled",
        "demanded", "suggested", "remarked", "urged", "protested", "ventured"
    ]

    def __init__(self):
        # Compiled patterns for dialogue extraction
        # Matches double quotes and curly quotes
        self.dialogue_pattern = re.compile(r'["\u201c](.*?)["\u201d]', re.DOTALL)
        
        # Attribution regex: e.g. "said Bertie", "Bertie said", "observed Jeeves"
        verbs_union = "|".join(rf"[{v[0].lower()}{v[0].upper()}]{v[1:]}" for v in self.SPEAKING_VERBS)
        self.attr_pattern_post = re.compile(
            rf'(?:[.,!?;:"\'\u201c\u201d\s]+)(?:{verbs_union})\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)'
        )
        self.attr_pattern_pre = re.compile(
            rf'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+(?:{verbs_union})'
        )

    def analyze(self, text: str) -> StoryFacts:
        """Extract objective story facts from a passage of prose."""
        if not text or not text.strip():
            return StoryFacts()

        dialogue_ratio, turn_count = self._compute_dialogue_metrics(text)
        characters = self._extract_characters(text)
        location = self._extract_location(text)
        objects = self._extract_objects(text)
        character_goals = self._infer_character_goals(text, characters)

        return StoryFacts(
            characters=characters,
            location=location,
            objects=objects,
            character_goals=character_goals,
            dialogue_ratio=round(dialogue_ratio, 3),
            turn_count=turn_count
        )

    def _compute_dialogue_metrics(self, text: str) -> Tuple[float, int]:
        """Calculates spoken dialogue character ratio and number of speech turns."""
        matches = self.dialogue_pattern.findall(text)
        if not matches:
            # Fallback for alternative quotation conventions (e.g. single quotes used consistently)
            single_matches = re.findall(r"(?:^|\s)'([^'\n]+)'(?:\s|[.,;]|$)", text)
            if len(single_matches) >= 2:
                matches = single_matches

        total_len = len(text.strip())
        if total_len == 0:
            return 0.0, 0

        spoken_chars = sum(len(m.strip()) for m in matches)
        dialogue_ratio = min(1.0, spoken_chars / total_len)
        turn_count = len(matches)

        return dialogue_ratio, turn_count

    def _extract_characters(self, text: str) -> List[str]:
        """Extracts characters mentioned or speaking in the scene."""
        found: Set[str] = set()

        # 1. Look for speaking attributions
        for match in self.attr_pattern_post.finditer(text):
            candidate = match.group(1).strip()
            if self._is_valid_character_name(candidate):
                found.add(self._normalize_name(candidate))

        for match in self.attr_pattern_pre.finditer(text):
            candidate = match.group(1).strip()
            if self._is_valid_character_name(candidate):
                found.add(self._normalize_name(candidate))

        # 2. Look for well-known British comedic archetypes/honorifics
        honorific_pattern = re.compile(
            r'\b(Lord|Lady|Sir|Uncle|Aunt|Major|Colonel|Captain|Doctor|Dr|Professor|Mr|Mrs|Miss)\.?\s+([A-Z][a-z]+)',
            re.IGNORECASE
        )
        for match in honorific_pattern.finditer(text):
            name = f"{match.group(1).capitalize()} {match.group(2).capitalize()}"
            found.add(name)

        # 3. Direct address in dialogue: e.g., "my dear Bertie", "look here, Jeeves", ", Jeeves,"
        vocative_pattern = re.compile(
            r'(?:look here|my dear|tell me|confound it|dash it|listen),?\s+([A-Z][a-z]+)',
            re.IGNORECASE
        )
        for match in vocative_pattern.finditer(text):
            candidate = match.group(1).strip()
            if self._is_valid_character_name(candidate):
                found.add(self._normalize_name(candidate))

        dialogue_vocative = re.compile(r',\s*([A-Z][a-z]+)[,!?."]\s*')
        for match in dialogue_vocative.finditer(text):
            candidate = match.group(1).strip()
            if self._is_valid_character_name(candidate):
                found.add(self._normalize_name(candidate))

        # 4. Narrative subject before movement/action verbs
        action_pattern = re.compile(
            r'\b([A-Z][a-z]+)\s+(?:paced|strode|entered|looked|turned|stood|sat|waited|walked|glanced|cleared)\b'
        )
        for match in action_pattern.finditer(text):
            candidate = match.group(1).strip()
            if self._is_valid_character_name(candidate):
                found.add(self._normalize_name(candidate))

        # Sort for determinism
        sorted_chars = sorted(list(found))
        return sorted_chars if sorted_chars else ["Narrator"]

    def _extract_location(self, text: str) -> str:
        """Identifies scene setting if explicitly mentioned."""
        lower_text = text.lower()
        for loc in self.KNOWN_LOCATIONS:
            # Word boundary check
            pattern = rf'\b{re.escape(loc)}\b'
            if re.search(pattern, lower_text):
                return loc.replace("-", " ")
        return "unspecified_room"

    def _extract_objects(self, text: str) -> List[str]:
        """Extracts tangible props playing a role in the scene."""
        found: Set[str] = set()
        lower_text = text.lower()
        for prop in self.KNOWN_PROPS:
            pattern = rf'\b{re.escape(prop)}s?\b'
            if re.search(pattern, lower_text):
                found.add(prop.replace("-", " "))
        return sorted(list(found))

    def _infer_character_goals(self, text: str, characters: List[str]) -> Dict[str, str]:
        """Infers high-level immediate conversational tensions for present characters."""
        goals: Dict[str, str] = {}
        lower_text = text.lower()

        for char in characters:
            short_name = char.split()[-1].lower()
            if any(k in lower_text for k in ["apologize", "sorry", "forgive", "pardon"]):
                goals[char] = "offer apology or avert social fallout"
            elif any(k in lower_text for k in ["money", "cheque", "loan", "pound", "borrow"]):
                goals[char] = "secure financial assistance without admitting crisis"
            elif any(k in lower_text for k in ["hide", "conceal", "secret", "don't let", "never tell"]):
                goals[char] = "conceal embarrassing incident from discovery"
            elif any(k in lower_text for k in ["advice", "what shall", "help me", "how can i"]):
                goals[char] = "seek counsel or practical assistance"
            else:
                goals[char] = "maintain composure and social standing"

        return goals

    def _is_valid_character_name(self, name: str) -> bool:
        """Filters false positives from regex captures."""
        non_names = {
            "the", "a", "an", "it", "that", "this", "there", "here", "he", "she",
            "they", "we", "what", "how", "why", "when", "then", "now", "yes",
            "no", "good", "well", "great", "poor", "old", "dear", "sir", "lord",
            "before", "having", "after", "since", "while", "without", "meanwhile",
            "suddenly", "furthermore", "however", "someone", "anyone", "everyone",
            "something", "nothing", "anything", "mrs", "mr", "miss", "dr", "lady",
            "uncle", "aunt", "who", "whom", "whose", "which", "each", "both",
            "neither", "either", "another", "instead", "perhaps", "already"
        }
        words = name.lower().split()
        if not words or len(name) < 3:
            return False
        if any(w.endswith("ly") for w in words):
            return False
        if all(w in non_names for w in words):
            return False
        return True

    def _normalize_name(self, name: str) -> str:
        """Capitalizes name properly."""
        return " ".join(part.capitalize() for part in name.strip().split())

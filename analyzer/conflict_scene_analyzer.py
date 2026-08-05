"""
Conflict and Scene Purpose Analyzer Module.

Extracts narrative conflict categories (Person vs Nature, Person vs Person, etc.),
scene purpose taxonomy, and character introduction events.
"""

import re
from typing import Dict, Any, List, Optional
from AI_Author.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.ConflictScene")


class ConflictSceneAnalyzer:
    """Analyzes conflict types, scene purposes, and character introductions."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes ConflictSceneAnalyzer.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        default_conflicts = {
            "Person vs Nature": ["wind", "storm", "canyon", "mountain", "cold", "desert", "weather", "river", "beast", "wolves"],
            "Person vs Person": ["confront", "enemy", "sword", "fight", "argued", "shouted", "attacked", "rival", "villain"],
            "Internal Conflict": ["wondered", "feared", "doubted", "hesitated", "guilt", "thought to herself", "thought to himself"],
            "Person vs Society": ["law", "king", "guard", "rules", "rebellion", "outlaw", "crown", "empire"]
        }
        self.conflict_keywords = self.config.get("conflict_keywords", default_conflicts)

    def analyze_conflict(self, text: str) -> KnowledgeItem:
        """Categorizes narrative conflict in text block."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        scores: Dict[str, int] = {}
        category_evidences: Dict[str, str] = {}

        for category, kw_list in self.conflict_keywords.items():
            count = 0
            found_sentence = ""
            for kw in kw_list:
                for s in sentences:
                    if kw in s.lower():
                        count += 1
                        if not found_sentence:
                            found_sentence = s
            scores[category] = count
            category_evidences[category] = found_sentence

        best_category = max(scores, key=scores.get) if scores else "Person vs Nature"
        max_score = scores.get(best_category, 0)

        if max_score > 0:
            confidence = min(0.95, round(0.70 + (max_score * 0.06), 2))
            evidence = category_evidences[best_category] or text[:100]
            value = best_category
        else:
            confidence = 0.65
            evidence = sentences[0] if sentences else text[:80]
            value = "Person vs Environment / World"

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=evidence,
        )

    def analyze_scene_purpose(self, text: str, scene_index: int, total_scenes: int) -> KnowledgeItem:
        """Determines structural purpose of a scene within a chapter."""
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        first_sentence = sentences[0] if sentences else text[:80]

        if scene_index == 1 and total_scenes > 1:
            value = "Establish Setting & Goal"
            confidence = 0.90
            evidence = first_sentence
        elif scene_index == total_scenes:
            value = "Climax & Resolution"
            confidence = 0.88
            evidence = sentences[-1] if len(sentences) > 1 else text[-100:]
        else:
            value = "Escalate Tension & Plot"
            confidence = 0.82
            evidence = first_sentence

        return KnowledgeItem(
            value=value,
            confidence=confidence,
            evidence=evidence,
        )

    def extract_character_introductions(self, text: str) -> List[KnowledgeItem]:
        """Detects candidate character introductions based on proper nouns and dialogue tags."""
        # Find proper nouns (Capitalized words that aren't common sentence starters)
        common_words = {"The", "A", "An", "In", "On", "At", "It", "As", "We", "He", "She", "They", "Chapter", "Prologue", "Epilogue"}
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]

        found_names: Dict[str, str] = {}

        for sentence in sentences:
            words = re.findall(r"\b[A-Z][a-z]+\b", sentence)
            for w in words:
                if w not in common_words and len(w) > 2:
                    if w not in found_names:
                        found_names[w] = sentence

        introductions: List[KnowledgeItem] = []
        for name, sentence_evidence in found_names.items():
            introductions.append(KnowledgeItem(
                value=name,
                confidence=0.88,
                evidence=sentence_evidence,
            ))

        return introductions

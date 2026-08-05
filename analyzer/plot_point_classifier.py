"""
Plot Point Classifier Module.

Classifies 8-Point story structure milestones (Hook, Inciting Incident, First Plot Point,
Midpoint, Reversal, Darkest Moment, Climax, Resolution, Epilogue) from narrative chapters.
"""

import re
from typing import Dict, Any, List, Optional
from AI_Author.analyzer.pov_detector import KnowledgeItem
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Analyzer.PlotPointClassifier")


class PlotPointClassifier:
    """Classifies classic 3-Act / 8-Point plot milestones."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initializes PlotPointClassifier.

        Args:
            config: Optional configuration dictionary.
        """
        self.config = config or {}
        default_keywords = {
            "hook": ["beginning", "canyon", "wind", "shadow", "cold", "legend"],
            "inciting_incident": ["map", "entrance", "pillars", "decision", "nightfall"],
            "first_plot_point": ["threshold", "cavern", "entered", "arches"],
            "midpoint": ["chamber", "pedestal", "obsidian", "artifact", "shone"],
            "reversal": ["breath-taking", "torch", "suddenly", "revealed"],
            "darkest_moment": ["shadows", "wolves", "dark", "danger"],
            "climax": ["secured", "kingdom", "safe", "victory", "confronted"],
            "resolution": ["safe once more", "restored", "peace"],
            "epilogue": ["epilogue", "deep in the shadows", "new shadow"]
        }
        self.plot_keywords = self.config.get("plot_keywords", default_keywords)

    def classify_plot_milestones(self, chapters: List[Dict[str, Any]]) -> Dict[str, KnowledgeItem]:
        """Maps 8-point plot milestones across a sequence of parsed chapter objects.

        Args:
            chapters: List of chapter dictionary objects from Module 2.

        Returns:
            Dictionary mapping milestone name to KnowledgeItem.
        """
        total_chaps = len(chapters)
        milestones: Dict[str, KnowledgeItem] = {}

        # Reconstruct full chapter text list
        chap_texts = []
        for c in chapters:
            c_parts = []
            for scene in c.get("scenes", []):
                for p in scene.get("paragraphs", []):
                    c_parts.append(p["text"])
            chap_texts.append("\n\n".join(c_parts))

        # 1. Hook (Chapter 1 / Start)
        c1_text = chap_texts[0] if chap_texts else ""
        s1 = [s.strip() for s in c1_text.replace("\n", " ").split(".") if s.strip()]
        milestones["hook"] = KnowledgeItem(
            value=f"Hook: {s1[0][:70]}..." if s1 else "Opening Narrative Setup",
            confidence=0.90,
            evidence=s1[0] if s1 else "Chapter 1 Opening",
        )

        # 2. Inciting Incident (Early Chapter)
        inc_ev = self._find_keyword_evidence(chap_texts[:2], self.plot_keywords.get("inciting_incident", []))
        milestones["inciting_incident"] = KnowledgeItem(
            value="Inciting Incident: Call to Action / Goal Setup",
            confidence=0.85,
            evidence=inc_ev or (s1[1] if len(s1) > 1 else s1[0]),
        )

        # 3. First Plot Point (Middle-Early)
        fpp_ev = self._find_keyword_evidence(chap_texts, self.plot_keywords.get("first_plot_point", []))
        milestones["first_plot_point"] = KnowledgeItem(
            value="First Plot Point: Point of No Return",
            confidence=0.88,
            evidence=fpp_ev or (chap_texts[1][:100] if total_chaps > 1 else c1_text[:100]),
        )

        # 4. Midpoint (Center Chapter)
        mid_idx = total_chaps // 2
        mid_text = chap_texts[mid_idx] if total_chaps > 1 else c1_text
        mid_ev = self._find_keyword_evidence([mid_text], self.plot_keywords.get("midpoint", []))
        milestones["midpoint"] = KnowledgeItem(
            value="Midpoint: Major Discovery / Central Revelation",
            confidence=0.92,
            evidence=mid_ev or mid_text[:100],
        )

        # 5. Reversal
        rev_ev = self._find_keyword_evidence([mid_text], self.plot_keywords.get("reversal", []))
        milestones["reversal"] = KnowledgeItem(
            value="Reversal: Shift in Stakes & Tension",
            confidence=0.80,
            evidence=rev_ev or mid_text[:100],
        )

        # 6. Darkest Moment (Late-Middle)
        dark_ev = self._find_keyword_evidence(chap_texts[mid_idx:], self.plot_keywords.get("darkest_moment", []))
        milestones["darkest_moment"] = KnowledgeItem(
            value="Darkest Moment: Major Threat / All Hope is Lost",
            confidence=0.78,
            evidence=dark_ev or chap_texts[-1][:100],
        )

        # 7. Climax (Late Chapter / Penultimate)
        late_idx = max(0, total_chaps - 2)
        climax_text = chap_texts[late_idx] if total_chaps > 2 else chap_texts[-1]
        climax_ev = self._find_keyword_evidence([climax_text, chap_texts[-1]], self.plot_keywords.get("climax", []))
        milestones["climax"] = KnowledgeItem(
            value="Climax: Peak Confrontation & Goal Achievement",
            confidence=0.90,
            evidence=climax_ev or climax_text[:100],
        )

        # 8. Resolution (Final Chapter)
        last_text = chap_texts[-1]
        res_ev = self._find_keyword_evidence([last_text], self.plot_keywords.get("resolution", []))
        milestones["resolution"] = KnowledgeItem(
            value="Resolution: Restoration of Equilibrium",
            confidence=0.92,
            evidence=res_ev or last_text[:100],
        )

        # 9. Epilogue (If present)
        epilogue_ev = self._find_keyword_evidence(chap_texts, self.plot_keywords.get("epilogue", []))
        if epilogue_ev or "epilogue" in last_text.lower():
            milestones["epilogue"] = KnowledgeItem(
                value="Epilogue: Post-Resolution Teaser",
                confidence=0.95,
                evidence=epilogue_ev or last_text[-100:],
            )
        else:
            milestones["epilogue"] = KnowledgeItem(
                value="None",
                confidence=0.50,
                evidence="No explicit epilogue heading detected.",
            )

        return milestones

    def _find_keyword_evidence(self, texts: List[str], keywords: List[str]) -> Optional[str]:
        """Finds sentence matching any plot milestone keyword."""
        for text in texts:
            sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
            for kw in keywords:
                for s in sentences:
                    if kw.lower() in s.lower():
                        return s
        return None

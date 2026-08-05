"""
Workspace Manager Module for Local Editor.

Discovers book projects in outputs/, resolves chapters & metadata, saves author edits,
and exports complete novel manuscripts to .md or .txt.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Editor.WorkspaceManager")


class WorkspaceManager:
    """Manages book workspace projects, chapters, and manuscript exports."""

    def __init__(self, outputs_dir: Optional[Path] = None):
        """Initializes WorkspaceManager.

        Args:
            outputs_dir: Path to outputs directory containing processed books.
        """
        self.root_dir = Path(__file__).resolve().parent.parent
        self.outputs_dir = outputs_dir or (self.root_dir / "outputs")

    def list_books(self) -> List[Dict[str, Any]]:
        """Lists all processed book workspace directories in outputs/."""
        if not self.outputs_dir.exists():
            return []

        books = []
        for p in self.outputs_dir.iterdir():
            if p.is_dir() and not p.name.startswith("."):
                meta_file = p / "metadata.json"
                book_title = p.name.replace("_", " ").title()
                if meta_file.exists():
                    try:
                        with open(meta_file, "r", encoding="utf-8") as f:
                            meta = json.load(f)
                            book_title = meta.get("title", book_title)
                    except Exception:
                        pass

                chap_dir = p / "chapters"
                chap_count = len(list(chap_dir.glob("chapter_*.json"))) if chap_dir.exists() else 0

                books.append({
                    "slug": p.name,
                    "title": book_title,
                    "path": str(p),
                    "total_chapters": chap_count,
                    "has_story_analysis": (p / "story_analysis.json").exists(),
                    "has_character_analysis": (p / "character_analysis.json").exists(),
                    "has_emotion_analysis": (p / "emotion_analysis.json").exists(),
                    "has_plot_analysis": (p / "plot_analysis.json").exists(),
                })

        return sorted(books, key=lambda x: x["title"])

    def get_book_details(self, book_slug: str) -> Dict[str, Any]:
        """Loads complete analysis knowledge for a given book workspace slug."""
        book_path = self.outputs_dir / book_slug
        if not book_path.exists():
            raise FileNotFoundError(f"Book workspace slug '{book_slug}' not found.")

        details: Dict[str, Any] = {"slug": book_slug}

        for key, filename in [
            ("metadata", "metadata.json"),
            ("parsing_summary", "parsing_summary.json"),
            ("story_analysis", "story_analysis.json"),
            ("character_analysis", "character_analysis.json"),
            ("dialogue_analysis", "dialogue_analysis.json"),
            ("emotion_analysis", "emotion_analysis.json"),
            ("plot_analysis", "plot_analysis.json"),
        ]:
            fpath = book_path / filename
            if fpath.exists():
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        details[key] = json.load(f)
                except Exception:
                    pass

        # Chapter list summary
        chap_dir = book_path / "chapters"
        chapters = []
        if chap_dir.exists():
            for c_file in sorted(list(chap_dir.glob("chapter_*.json"))):
                try:
                    with open(c_file, "r", encoding="utf-8") as f:
                        chap_json = json.load(f)
                        chapters.append({
                            "index": chap_json.get("chapter_index"),
                            "title": chap_json.get("chapter_title"),
                            "word_count": chap_json.get("word_count"),
                            "filename": c_file.name,
                        })
                except Exception:
                    pass

        details["chapters"] = chapters
        return details

    def get_chapter(self, book_slug: str, chapter_index: int) -> Dict[str, Any]:
        """Loads single chapter content JSON."""
        chap_file = self.outputs_dir / book_slug / "chapters" / f"chapter_{chapter_index:02d}.json"
        if not chap_file.exists():
            raise FileNotFoundError(f"Chapter {chapter_index} not found for book '{book_slug}'.")

        with open(chap_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_chapter(self, book_slug: str, chapter_index: int, text_content: str) -> Dict[str, Any]:
        """Saves edited chapter text content back to chapter JSON."""
        chap_file = self.outputs_dir / book_slug / "chapters" / f"chapter_{chapter_index:02d}.json"
        if not chap_file.exists():
            raise FileNotFoundError(f"Chapter {chapter_index} not found for book '{book_slug}'.")

        with open(chap_file, "r", encoding="utf-8") as f:
            chap_data = json.load(f)

        words = text_content.split()
        chap_data["word_count"] = len(words)
        chap_data["scenes"] = [
            {
                "scene_index": 1,
                "word_count": len(words),
                "paragraphs": [
                    {
                        "paragraph_index": i + 1,
                        "text": p.strip(),
                        "type": "narration",
                        "word_count": len(p.split()),
                        "has_dialogue": False,
                        "dialogues": []
                    }
                    for i, p in enumerate(text_content.split("\n\n")) if p.strip()
                ]
            }
        ]

        with open(chap_file, "w", encoding="utf-8") as f:
            json.dump(chap_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved updated Chapter {chapter_index} for '{book_slug}'.")
        return chap_data

    def export_manuscript(self, book_slug: str, format_type: str = "markdown") -> Path:
        """Exports all chapters into a clean single manuscript (.md or .txt)."""
        book_path = self.outputs_dir / book_slug
        chap_dir = book_path / "chapters"

        if not chap_dir.exists():
            raise FileNotFoundError(f"No chapters directory found for '{book_slug}'.")

        chap_files = sorted(list(chap_dir.glob("chapter_*.json")))
        if not chap_files:
            raise FileNotFoundError(f"No chapter files found for '{book_slug}'.")

        title = book_slug.replace("_", " ").title()
        lines = [f"# {title}\n\n"]

        for c_file in chap_files:
            with open(c_file, "r", encoding="utf-8") as f:
                c_json = json.load(f)

            c_title = c_json.get("chapter_title", f"Chapter {c_json.get('chapter_index')}")
            lines.append(f"## {c_title}\n\n")

            for scene in c_json.get("scenes", []):
                for p in scene.get("paragraphs", []):
                    lines.append(f"{p['text']}\n\n")

        ext = ".md" if format_type == "markdown" else ".txt"
        export_file = book_path / f"{book_slug}_manuscript{ext}"

        with open(export_file, "w", encoding="utf-8") as f:
            f.writelines(lines)

        logger.info(f"Exported manuscript to: '{export_file}'")
        return export_file

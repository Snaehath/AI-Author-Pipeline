"""
Editor Server Module for Local Editor.

Provides a lightweight, zero-dependency HTTP server serving the AI Author Studio
Web Application UI and REST API.
"""

import json
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Dict, Any, Optional
from urllib.parse import urlparse, parse_qs

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.pipeline.editor.workspace_manager import WorkspaceManager
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Editor.Server")


class AuthorStudioHTTPHandler(BaseHTTPRequestHandler):
    """Custom HTTP Request Handler for AI Author Studio Web UI & REST API."""

    workspace = WorkspaceManager()
    generator = None  # Lazy-loaded StoryGenerator if invoked

    def do_GET(self):
        """Handles GET requests for static files and REST API."""
        parsed = urlparse(self.path)
        path = parsed.path

        # 1. API: List Books
        if path == "/api/books":
            books = self.workspace.list_books()
            self._send_json(books)
            return

        # 2. API: Book Details
        if path.startswith("/api/books/") and not "/chapters/" in path and not path.endswith("/export"):
            slug = path.split("/api/books/")[-1].strip("/")
            try:
                details = self.workspace.get_book_details(slug)
                self._send_json(details)
            except FileNotFoundError:
                self._send_error(404, "Book slug not found.")
            return

        # 3. API: Get Chapter
        if "/chapters/" in path:
            parts = path.strip("/").split("/")
            slug = parts[2]
            chap_idx = int(parts[4])
            try:
                chap = self.workspace.get_chapter(slug, chap_idx)
                self._send_json(chap)
            except Exception as e:
                self._send_error(404, str(e))
            return

        # 4. Static Files
        static_dir = Path(__file__).resolve().parent / "static"
        if path == "/" or path == "/index.html":
            file_path = static_dir / "index.html"
            content_type = "text/html"
        elif path == "/static/style.css":
            file_path = static_dir / "style.css"
            content_type = "text/css"
        elif path == "/static/app.js":
            file_path = static_dir / "app.js"
            content_type = "application/javascript"
        else:
            self._send_error(404, "File not found.")
            return

        if file_path.exists():
            with open(file_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self._send_error(404, "Static file missing.")

    def do_POST(self):
        """Handles POST requests for saving chapters, exports, and AI assistance."""
        parsed = urlparse(self.path)
        path = parsed.path

        content_len = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(content_len) if content_len > 0 else b""
        body_data = json.loads(body_bytes.decode("utf-8")) if body_bytes else {}

        # 1. API: Save Chapter
        if "/chapters/" in path:
            parts = path.strip("/").split("/")
            slug = parts[2]
            chap_idx = int(parts[4])
            text = body_data.get("text", "")
            try:
                res = self.workspace.save_chapter(slug, chap_idx, text)
                self._send_json({"status": "success", "data": res})
            except Exception as e:
                self._send_error(500, str(e))
            return

        # 2. API: Export Manuscript
        if path.endswith("/export"):
            parts = path.strip("/").split("/")
            slug = parts[2]
            try:
                exp_file = self.workspace.export_manuscript(slug)
                self._send_json({"status": "success", "export_path": str(exp_file)})
            except Exception as e:
                self._send_error(500, str(e))
            return

        # 3. API: AI Assist
        if path == "/api/ai_assist":
            task = body_data.get("task", "continue_story")
            instruction = body_data.get("instruction", "")
            text = body_data.get("text", "")

            # Lazy load generator
            if AuthorStudioHTTPHandler.generator is None:
                try:
                    from AI_Author.pipeline.inference.generator import StoryGenerator
                    AuthorStudioHTTPHandler.generator = StoryGenerator()
                except Exception as e:
                    self._send_json({"result": f"AI Engine Notice: {e}"})
                    return

            gen = AuthorStudioHTTPHandler.generator
            res = ""
            if task == "continue_story":
                res = gen.continue_story(text, instruction)
            elif task == "rewrite_scene":
                res = gen.rewrite_scene(text, instruction)
            elif task == "improve_dialogue":
                res = gen.improve_dialogue(text, instruction)
            elif task == "increase_suspense":
                res = gen.increase_suspense(text)
            elif task == "improve_pacing":
                res = gen.improve_pacing(text, instruction)
            elif task == "emotional_impact":
                res = gen.emotional_impact(text, instruction)

            self._send_json({"result": res})
            return

        self._send_error(404, "Endpoint not found.")

    def _send_json(self, data: Any, status: int = 200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_error(self, status: int, message: str):
        self._send_json({"error": message}, status=status)


def start_editor_server(host: str = "127.0.0.1", port: int = 8000) -> HTTPServer:
    """Starts local HTTP server for AI Author Studio."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, AuthorStudioHTTPHandler)
    logger.info(f"AI Author Studio Web Server running at: http://{host}:{port}")
    return httpd


if __name__ == "__main__":
    server = start_editor_server()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down AI Author Studio Server.")

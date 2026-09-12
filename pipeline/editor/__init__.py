"""
Local Editor Module for AI Author Studio.

Manages author workspaces, chapter editing, real-time AI assistance, and manuscript exports.
"""

from .workspace_manager import WorkspaceManager
from .editor_server import start_editor_server

__all__ = [
    "WorkspaceManager",
    "start_editor_server",
]

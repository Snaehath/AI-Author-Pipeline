# Module 11: Local Editor — Documentation

## Overview
**Module 11 (Local Editor)** provides a local **Web Application & Author Studio Workspace** for managing book projects, editing chapter drafts, inspecting extracted story/character/plot knowledge, executing AI author assistant commands in real-time, and exporting complete novel manuscripts.

The web application follows our modern design standards (dark mode, HSL tailored accents, glassmorphism, responsive layout, modern Inter & Outfit typography, rich micro-animations).

---

## Architecture & Components

```
AI_Author/editor/
├── workspace_manager.py # Manages book projects, chapter JSON edits, and manuscript exports
├── editor_server.py     # Zero-dependency Python HTTP server serving Web UI and REST API
└── static/
    ├── index.html       # AI Author Studio Web Application HTML template
    ├── style.css        # Glassmorphism & dark mode design system
    └── app.js           # Interactive frontend logic & API client
```

### Key Capabilities
1. 📚 **Book Project Dashboard**: Discovers books in `outputs/`.
2. ✍️ **Interactive Manuscript Editor**: Edit chapters with real-time word counting and saving.
3. 🤖 **AI Author Assistant Sidebar**: Triggers Module 10 commands directly from the UI:
   - *Continue Story*
   - *Rewrite Scene*
   - *Improve Dialogue*
   - *Increase Suspense*
   - *Improve Pacing*
   - *Emotional Impact*
4. 📊 **Story Knowledge Panel**: Inspect character traits, tone, and 8-point plot milestones.
5. 📄 **Manuscript Exporter**: One-click export to Markdown (`.md`) or text (`.txt`).

---

## How to Run & Test

### Running Unit Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_editor.py
```

### Launching Local Author Studio Web App
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python editor/editor_server.py
```

Open **`http://localhost:8000`** in your web browser to open the AI Author Studio!

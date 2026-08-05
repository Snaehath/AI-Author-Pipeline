# Module 1: Book Ingestion — Documentation

## Overview
**Module 1 (Book Ingestion)** is responsible for converting raw digital books in multiple formats (`.txt`, `.pdf`, `.epub`, `.docx`) into standardized, clean narrative text accompanied by structured metadata and chapter boundaries.

It runs completely locally, adhering to low-resource constraints (RTX 3050 4GB VRAM, 16GB RAM) without external APIs or cloud dependencies.

---

## Architecture & Components

```
AI_Author/ingestion/
├── __init__.py           # Package exports
├── extractors.py         # Format-specific extractors (TXT, PDF, EPUB, DOCX)
├── normalizer.py         # Unicode, smart quotes, whitespace, and OCR fixes
├── header_cleaner.py     # Strips page numbers & running headers/footers
├── chapter_splitter.py   # Multi-pattern regex chapter boundary detector
└── pipeline.py           # End-to-end pipeline orchestrator
```

### 1. Format Extractors (`extractors.py`)
- **TXT**: Multi-encoding reading with automatic fallback (`utf-8`, `utf-8-sig`, `latin-1`, `cp1252`).
- **PDF**: PyMuPDF (`fitz`) or `pypdf` page reader.
- **EPUB**: `ebooklib` + `BeautifulSoup4` HTML section extractor.
- **DOCX**: `python-docx` paragraph parser.
- Missing optional libraries fail gracefully with user guidance on how to install required packages (`pip install pymupdf ebooklib beautifulsoup4 python-docx`).

### 2. Text Normalizer (`normalizer.py`)
- **Unicode**: Normalizes text into standard `NFKC` form.
- **Punctuation & Quotes**: Converts curly smart quotes (`“”‘’`), backticks, accents, and em-dashes into clean standard narrative typography.
- **OCR Repair**: Fixes hyphenated line breaks split across lines (e.g. `develo-\npment` -> `development`).
- **Whitespace**: Strips line trailing whitespace, converts tabs, and limits consecutive blank lines to standard paragraph breaks (max 2).

### 3. Header & Footer Cleaner (`header_cleaner.py`)
- Filters out standalone page numbers (e.g., `- 45 -`, `Page 12`, centered numbers).
- Identifies running header/footer lines that repeat across pages and strips them from narrative flow.

### 4. Chapter Splitter (`chapter_splitter.py`)
- Detects chapter headers (`Chapter 1`, `CHAPTER IV`, `PROLOGUE`, `EPILOGUE`, `Book 1`, etc.).
- Returns structured `Chapter` objects containing:
  - `chapter_index`: 1-based index
  - `title`: Chapter title
  - `content`: Text body
  - `start_char` / `end_char`: Character byte offsets
  - `word_count`: Word count
- Provides fallback chunking (3,000 words default) if no explicit chapter headings exist.

### 5. Pipeline Orchestrator (`pipeline.py`)
Executes the full pipeline and writes output files under `AI_Author/outputs/<book_slug>/`:
- `cleaned.txt`: Unified cleaned book text.
- `metadata.json`: Comprehensive JSON summary.

---

## Output JSON Schema (`metadata.json`)
```json
{
  "title": "The Secret Passage",
  "author": "Author Name",
  "original_filename": "test_novel.txt",
  "format": "TXT",
  "character_count": 24500,
  "word_count": 4120,
  "line_count": 320,
  "chapter_count": 3,
  "chapters": [
    {
      "chapter_index": 1,
      "title": "PROLOGUE",
      "content": "...",
      "start_char": 0,
      "end_char": 1200,
      "word_count": 210
    }
  ],
  "ingestion_timestamp": "2026-08-03T14:25:00Z"
}
```

---

## How to Test and Run

### Running Unit & Integration Tests
Run unit tests from the workspace root (`d:\DevelopmentSide\ML`):
```bash
python -m unittest AI_Author/tests/test_ingestion.py
```

### Ingesting a Book via Command Line

**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python ingestion/pipeline.py path/to/book.epub --title "My Novel" --author "Jane Doe"
```

**From root `D:\DevelopmentSide\ML`:**
```powershell
python -m AI_Author.ingestion.pipeline path/to/book.epub --title "My Novel" --author "Jane Doe"
```

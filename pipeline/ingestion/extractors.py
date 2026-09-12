"""
Text Extractors for Multiple Book Formats (.txt, .pdf, .epub, .docx).

Provides robust file reading and text extraction with fallback encodings
and graceful dependency handling.
"""

from pathlib import Path
from typing import List
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Ingestion.Extractors")


class ExtractionError(Exception):
    """Exception raised for errors encountered during text extraction."""
    pass


def extract_from_txt(file_path: Path) -> str:
    """Extracts raw text from a plaintext file using UTF-8 or fallback encodings.

    Args:
        file_path: Path to the .txt file.

    Returns:
        Extracted text as a single string.

    Raises:
        ExtractionError: If file cannot be read using any supported encoding.
    """
    encodings = ["utf-8", "utf-8-sig", "latin-1", "cp1252", "utf-16"]
    for enc in encodings:
        try:
            with open(file_path, "r", encoding=enc) as f:
                content = f.read()
            logger.info(f"Successfully read TXT using '{enc}' encoding.")
            return content
        except (UnicodeDecodeError, Exception):
            continue

    raise ExtractionError(f"Failed to read file '{file_path}' with supported encodings.")


def extract_from_pdf(file_path: Path) -> str:
    """Extracts text from a PDF file using PyMuPDF (fitz) or pypdf.

    Args:
        file_path: Path to the .pdf file.

    Returns:
        Extracted text string.
    """
    # Attempt 1: fitz (PyMuPDF)
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(file_path)
        pages_text: List[str] = []
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text("text")
            if text.strip():
                pages_text.append(text)
        doc.close()
        logger.info(f"Extracted {len(pages_text)} pages from PDF using PyMuPDF.")
        return "\n\n".join(pages_text)
    except ImportError:
        logger.debug("PyMuPDF (fitz) not installed. Trying pypdf...")

    # Attempt 2: pypdf
    try:
        import pypdf
        reader = pypdf.PdfReader(str(file_path))
        pages_text = []
        for idx, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text and text.strip():
                pages_text.append(text)
        logger.info(f"Extracted {len(pages_text)} pages from PDF using pypdf.")
        return "\n\n".join(pages_text)
    except ImportError:
        raise ExtractionError(
            "PDF extraction requires 'pymupdf' or 'pypdf'. "
            "Please install via: pip install pymupdf (or pypdf)"
        )
    except Exception as e:
        raise ExtractionError(f"Failed to parse PDF file '{file_path}': {e}")


def extract_from_epub(file_path: Path) -> str:
    """Extracts text from an EPUB ebook using ebooklib and BeautifulSoup.

    Args:
        file_path: Path to the .epub file.

    Returns:
        Extracted text string.
    """
    try:
        import ebooklib
        from ebooklib import epub
        from bs4 import BeautifulSoup
    except ImportError:
        raise ExtractionError(
            "EPUB extraction requires 'ebooklib' and 'beautifulsoup4'. "
            "Please install via: pip install ebooklib beautifulsoup4"
        )

    try:
        book = epub.read_epub(str(file_path))
        chapters_text: List[str] = []

        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            html_content = item.get_content().decode("utf-8", errors="ignore")
            soup = BeautifulSoup(html_content, "html.parser")

            # Remove script and style tags
            for element in soup(["script", "style", "nav", "header", "footer"]):
                element.decompose()

            text = soup.get_text(separator="\n")
            if text.strip():
                chapters_text.append(text)

        logger.info(f"Extracted {len(chapters_text)} sections from EPUB.")
        return "\n\n".join(chapters_text)
    except Exception as e:
        raise ExtractionError(f"Failed to parse EPUB file '{file_path}': {e}")


def extract_from_docx(file_path: Path) -> str:
    """Extracts text from a Microsoft Word (.docx) document using python-docx.

    Args:
        file_path: Path to the .docx file.

    Returns:
        Extracted text string.
    """
    try:
        import docx
    except ImportError:
        raise ExtractionError(
            "DOCX extraction requires 'python-docx'. "
            "Please install via: pip install python-docx"
        )

    try:
        doc = docx.Document(str(file_path))
        paragraphs: List[str] = []
        for p in doc.paragraphs:
            if p.text.strip():
                paragraphs.append(p.text)

        logger.info(f"Extracted {len(paragraphs)} paragraphs from DOCX.")
        return "\n\n".join(paragraphs)
    except Exception as e:
        raise ExtractionError(f"Failed to parse DOCX file '{file_path}': {e}")


def extract_text_from_file(file_path: Path) -> str:
    """Main factory function to extract text based on file extension.

    Args:
        file_path: Absolute or relative Path to target file.

    Returns:
        Extracted raw text string.

    Raises:
        ExtractionError: If format is unsupported or file missing.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise ExtractionError(f"File not found: {file_path}")

    ext = file_path.suffix.lower()
    logger.info(f"Starting text extraction for '{file_path.name}' (format: {ext})")

    if ext == ".txt":
        return extract_from_txt(file_path)
    elif ext == ".pdf":
        return extract_from_pdf(file_path)
    elif ext == ".epub":
        return extract_from_epub(file_path)
    elif ext == ".docx":
        return extract_from_docx(file_path)
    else:
        raise ExtractionError(f"Unsupported file format '{ext}'. Supported formats: .txt, .pdf, .epub, .docx")

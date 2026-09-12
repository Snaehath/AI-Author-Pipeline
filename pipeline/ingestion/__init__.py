"""
Book Ingestion Module for AI Author Studio.

Handles text extraction from TXT, PDF, EPUB, and DOCX formats,
Unicode and whitespace normalization, header/footer stripping, OCR repair,
chapter segmentation, and output generation.
"""

from .extractors import extract_text_from_file
from .normalizer import TextNormalizer
from .header_cleaner import HeaderCleaner
from .chapter_splitter import ChapterSplitter
from .pipeline import IngestionPipeline, IngestionResult

__all__ = [
    "extract_text_from_file",
    "TextNormalizer",
    "HeaderCleaner",
    "ChapterSplitter",
    "IngestionPipeline",
    "IngestionResult",
]

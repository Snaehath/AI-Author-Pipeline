"""
Normalized Text Deduplication Engine for Narrative Corpora.

Detects exact and near-duplicate passages across disparate book sources, editions,
and chapters to prevent duplicated craft supervision in training data.
"""

import hashlib
import re
from typing import Dict, List, Optional, Set, Tuple


class NormalizedTextDeduplicator:
    """
    Detects cross-edition and cross-book duplicate passages using normalized
    cryptographic hashing (exact match) and character/word n-gram Jaccard overlap (near-match).
    """

    DEFAULT_SIMILARITY_THRESHOLD = 0.85

    def __init__(self, similarity_threshold: float = DEFAULT_SIMILARITY_THRESHOLD):
        self.similarity_threshold = similarity_threshold
        # exact hash -> canonical source_id
        self._exact_hashes: Dict[str, str] = {}
        # List of (canonical source_id, word_set, ngrams_set)
        self._registered_passages: List[Tuple[str, Set[str], Set[str]]] = []
        # Word-count length index: length -> list of indices in _registered_passages
        self._length_index: Dict[int, List[int]] = {}

    @staticmethod
    def normalize_text(text: str) -> str:
        """Normalizes prose: lowercase, standardized quotes/dashes, stripped punctuation, normalized whitespace."""
        # Standardize curly quotes and hyphens
        t = text.lower()
        t = re.sub(r'[\u2018\u2019\u201a\u201b\']', '', t)
        t = re.sub(r'[\u201c\u201d\u201e\u201f\"]', ' ', t)
        t = re.sub(r'[\u2013\u2014\-]', ' ', t)
        # Strip all punctuation except alphanumeric and space
        t = re.sub(r'[^\w\s]', ' ', t)
        # Collapse whitespace
        return re.sub(r'\s+', ' ', t).strip()

    @classmethod
    def exact_hash(cls, text: str) -> str:
        """Computes SHA-256 hash of normalized text."""
        norm = cls.normalize_text(text)
        return hashlib.sha256(norm.encode('utf-8')).hexdigest()

    @staticmethod
    def _compute_word_ngrams(words: List[str], n: int = 3) -> Set[str]:
        if len(words) < n:
            return set(words)
        return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}

    def is_duplicate(self, text: str, source_id: str) -> Tuple[bool, Optional[str]]:
        """
        Checks if text is an exact or near duplicate of any previously registered passage.
        Returns:
            (True, canonical_source_id) if duplicate
            (False, None) if original
        """
        norm = self.normalize_text(text)
        if not norm:
            return False, None

        # 1. Check exact hash
        h = hashlib.sha256(norm.encode('utf-8')).hexdigest()
        if h in self._exact_hashes:
            return True, self._exact_hashes[h]

        # 2. Check near-duplicate via Jaccard overlap on words and 3-grams
        words = norm.split()
        if len(words) < 15:
            # For very short passages, exact hash is the primary check
            return False, None

        word_set = set(words)
        wl = len(word_set)
        # Bounding prune: Jaccard(A, B) <= min(|A|, |B|) / max(|A|, |B|)
        # For Jaccard >= 0.82, length ratio must be >= 0.80 and <= 1.25
        min_len = int(wl * 0.80)
        max_len = int(wl * 1.25)

        candidate_indices: List[int] = []
        for l in range(min_len, max_len + 1):
            if l in self._length_index:
                candidate_indices.extend(self._length_index[l])

        ngrams: Optional[Set[str]] = None

        for c_idx in candidate_indices:
            canonical_id, prev_words, prev_ngrams = self._registered_passages[c_idx]
            # Fast filter: word vocabulary Jaccard
            word_intersection = len(word_set & prev_words)
            word_union = len(word_set | prev_words)
            if word_union > 0:
                word_sim = word_intersection / word_union
                if word_sim >= 0.82:
                    return True, canonical_id

                # Rigorous check: 3-gram Jaccard
                if ngrams is None:
                    ngrams = self._compute_word_ngrams(words, n=3)
                if len(ngrams) > 0 and len(prev_ngrams) > 0:
                    ngram_intersection = len(ngrams & prev_ngrams)
                    ngram_union = len(ngrams | prev_ngrams)
                    if ngram_union > 0 and (ngram_intersection / ngram_union) >= 0.65:
                        return True, canonical_id

        return False, None

    def register(self, text: str, source_id: str) -> None:
        """Registers a canonical passage into the deduplication index."""
        norm = self.normalize_text(text)
        if not norm:
            return

        h = hashlib.sha256(norm.encode('utf-8')).hexdigest()
        self._exact_hashes[h] = source_id

        words = norm.split()
        if len(words) >= 15:
            ngrams = self._compute_word_ngrams(words, n=3)
            word_set = set(words)
            idx = len(self._registered_passages)
            self._registered_passages.append((source_id, word_set, ngrams))
            wl = len(word_set)
            self._length_index.setdefault(wl, []).append(idx)

    def check_and_register(self, text: str, source_id: str) -> Tuple[bool, Optional[str]]:
        """Checks if duplicate; if not, automatically registers as canonical."""
        is_dup, canonical_id = self.is_duplicate(text, source_id)
        if not is_dup:
            self.register(text, source_id)
            return False, None
        return True, canonical_id

    def reset(self) -> None:
        """Clears index."""
        self._exact_hashes.clear()
        self._registered_passages.clear()

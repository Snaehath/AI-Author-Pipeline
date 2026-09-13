"""
tests/test_sft_dataset_formatter.py

Unit tests for Phase 4B SFT dataset formatter.
Validates:
  1. clean_craft_analysis removes boilerplate prefixes while keeping narrative substance.
  2. format_training_example constructs valid ChatML prompt and target schema.
  3. tokenize_sft_example properly masks prompt tokens with -100 in labels.
  4. load_and_format_train_records loads all 43 training records.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from dataset_generator.sft_dataset_formatter import (
    clean_craft_analysis,
    format_training_example,
    load_and_format_train_records,
    tokenize_sft_example,
)

TRAIN_PATH = Path("datasets/sft/comedy_sft_train.jsonl")


def test_clean_craft_analysis():
    raw_notes_1 = "Excellent escalation: the guinea-pigs consume the office, multiply into thousands."
    cleaned_1 = clean_craft_analysis(raw_notes_1)
    assert not cleaned_1.startswith("Excellent escalation:")
    assert "guinea-pigs consume the office" in cleaned_1

    raw_notes_2 = "Flagship escalation example: continual shipments, warehouse overflow, frantic packing."
    cleaned_2 = clean_craft_analysis(raw_notes_2)
    assert not cleaned_2.startswith("Flagship escalation example:")
    assert "continual shipments" in cleaned_2.lower()

    raw_notes_3 = "The comic turn is verbal: the narrator's distress over his wardrobe is answered."
    cleaned_3 = clean_craft_analysis(raw_notes_3)
    assert not cleaned_3.startswith("The comic turn is verbal:")
    assert "narrator's distress" in cleaned_3


def test_format_training_example():
    dummy_rec = {
        "audit_id": "audit_dummy",
        "source_text": "He tripped over the cat.",
        "human_audit": {
            "primary_mechanism": "PHYSICAL_COMPLICATION",
            "secondary_mechanisms": ["DEADPAN_REACTION"],
            "mechanism_horizon": "LOCAL",
            "notes": "Classic farce structure: physical mishap disrupts decorum.",
        },
    }

    messages, target_dict = format_training_example(dummy_rec)
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert "He tripped over the cat." in messages[1]["content"]

    assert target_dict["primary_mechanism"] == "PHYSICAL_COMPLICATION"
    assert target_dict["secondary_mechanisms"] == ["DEADPAN_REACTION"]
    assert target_dict["mechanism_horizon"] == "LOCAL"
    assert "Physical mishap disrupts decorum." in target_dict["craft_analysis"]


def test_load_and_format_train_records():
    records = load_and_format_train_records(TRAIN_PATH)
    assert len(records) == 43, f"Expected 43 training records, found {len(records)}"


class MockTokenizer:
    """Lightweight mock tokenizer to test prompt masking logic without GPU."""
    def __init__(self):
        self.eos_token_id = 999
        self.pad_token_id = 999

    def apply_chat_template(self, messages, tokenize=False, add_generation_prompt=False):
        text = ""
        for m in messages:
            text += f"<{m['role']}>{m['content']}</{m['role']}>"
        if add_generation_prompt:
            text += "<assistant>"
        return text

    def encode(self, text, add_special_tokens=False):
        return [hash(tok) % 1000 + 1 for tok in text.split()]

    def decode(self, token_ids, skip_special_tokens=True):
        return " ".join(str(tid) for tid in token_ids)


def test_tokenize_sft_example_masking():
    dummy_rec = {
        "audit_id": "audit_dummy",
        "source_text": "Simple test passage.",
        "human_audit": {
            "primary_mechanism": "VERBAL_WIT",
            "secondary_mechanisms": [],
            "mechanism_horizon": "LOCAL",
            "notes": "Sharp witty comeback.",
        },
    }

    mock_tok = MockTokenizer()
    tokenized = tokenize_sft_example(dummy_rec, mock_tok, max_seq_length=512)

    input_ids = tokenized["input_ids"]
    labels = tokenized["labels"]

    assert len(input_ids) == len(labels)
    # The initial prompt portion must be -100
    assert labels[0] == -100
    # At least one trailing token (the assistant target) must not be -100
    unmasked = [l for l in labels if l != -100]
    assert len(unmasked) > 0
    # Input IDs must be integers
    assert all(isinstance(x, int) for x in input_ids)


def test_tokenize_sft_example_long_passage_truncation():
    """Verify that very long source passages are truncated without losing target tokens."""
    long_rec = {
        "audit_id": "audit_long",
        "source_text": "word " * 2000,
        "human_audit": {
            "primary_mechanism": "ESCALATION",
            "secondary_mechanisms": ["MISUNDERSTANDING"],
            "mechanism_horizon": "LOCAL",
            "notes": "Escalating chaos.",
        },
    }

    mock_tok = MockTokenizer()
    max_len = 256
    tokenized = tokenize_sft_example(long_rec, mock_tok, max_seq_length=max_len)

    input_ids = tokenized["input_ids"]
    labels = tokenized["labels"]

    assert len(input_ids) <= max_len
    assert len(labels) == len(input_ids)
    unmasked = [l for l in labels if l != -100]
    assert len(unmasked) > 0, "Truncated example must preserve target tokens and have unmasked labels!"

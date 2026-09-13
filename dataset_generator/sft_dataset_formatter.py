"""
dataset_generator/sft_dataset_formatter.py

Phase 4B: SFT Dataset Formatter.
Formats comedy_sft_train.jsonl into causal LM ChatML training pairs with prompt token masking.

Key Features:
  1. Prompt Format Identity:
     Uses the exact same ChatML system and user prompt format as comedy_craft_evaluator.py.
  2. Label Masking:
     Sets label = -100 for all system and user prompt tokens so gradient updates
     apply strictly to the assistant's JSON response tokens.
  3. Grounded Craft Analysis:
     Cleans artificial meta-labels from human notes (e.g. "Excellent escalation: ",
     "Strong escalation: ", "Flagship escalation example: ") so the model learns
     descriptive dramatic analysis grounded in the passage rather than rote label-echoing.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from pipeline.evaluator.comedy_craft_evaluator import (
    CANONICAL_MECHANISMS,
    format_eval_prompt,
)


def clean_craft_analysis(notes: str) -> str:
    """
    Clean metadata prefixes from human notes to ensure craft_analysis is grounded
    in the narrative action rather than announcing the label.

    E.g. "Excellent escalation: the guinea-pigs consume..." -> "The guinea-pigs consume..."
    """
    if not notes:
        return "The passage develops comic tension through character interactions and narrative complications."

    cleaned = notes.strip()

    # Remove patterns like "Excellent escalation: ", "Strong escalation: ", "Flagship escalation example: "
    prefix_patterns = [
        r"^(?:Flagship|Excellent|Strong|Classic|Clear)\s+(?:farcical\s+)?(?:[a-z_]+)\s*(?:example)?\s*:\s*",
        r"^(?:Flagship|Excellent|Strong|Classic|Clear)\s+[a-z_]+\s+(?:structure|farce|example)\s*:\s*",
        r"^The\s+comic\s+turn\s+is\s+[a-z_]+\s*:\s*",
    ]

    for pat in prefix_patterns:
        cleaned = re.sub(pat, "", cleaned, flags=re.IGNORECASE)

    # Capitalize first letter
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]

    return cleaned


def format_training_example(
    record: dict[str, Any],
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    """
    Format an audit record into (messages, target_dict).
    Messages contains system and user prompt; target_dict is the assistant JSON response.
    """
    src_text = record.get("source_text", "")
    ha = record.get("human_audit", {})

    primary = ha.get("primary_mechanism", "UNKNOWN")
    secondary = ha.get("secondary_mechanisms", [])
    horizon = ha.get("mechanism_horizon", "LOCAL")
    raw_notes = ha.get("notes", "")

    craft_analysis = clean_craft_analysis(raw_notes)

    if "contrastive_analysis" in record:
        ca = record["contrastive_analysis"]
        target_dict = {
            "contrastive_analysis": {
                "causal_mechanism": ca["causal_mechanism"],
                "surface_cue": ca["surface_cue"],
                "tempting_alternative": ca["tempting_alternative"],
                "why_alternative_is_tempting": ca["why_alternative_is_tempting"],
                "counterfactual_test": ca["counterfactual_test"],
                "why_primary_wins": ca["why_primary_wins"],
            },
            "primary_mechanism": ca["primary_mechanism"],
            "secondary_mechanisms": record.get("secondary_mechanisms", []),
            "mechanism_horizon": record.get("setup_payoff_horizon", "LOCAL"),
            "craft_analysis": clean_craft_analysis(ca["causal_mechanism"]),
        }
    else:
        target_dict = {
            "primary_mechanism": primary,
            "secondary_mechanisms": secondary,
            "mechanism_horizon": horizon,
            "craft_analysis": craft_analysis,
        }

    messages = format_eval_prompt(src_text)
    return messages, target_dict


def tokenize_sft_example(
    record: dict[str, Any],
    tokenizer: Any,
    max_seq_length: int = 1024,
) -> dict[str, list[int]]:
    """
    Tokenizes a single training record with prompt token masking.
    Labels are set to -100 for all tokens prior to the assistant response.

    Invariants:
      1. Assistant target response is NEVER truncated; target tokens are 100% preserved.
      2. If prompt + target > max_seq_length, the source_text in the prompt is truncated.
      3. Guaranteed (labels != -100).sum() > 0 to prevent NaN cross-entropy loss.
    """
    messages, target_dict = format_training_example(record)
    target_json_str = json.dumps(target_dict, ensure_ascii=False, indent=2)

    full_messages = messages + [{"role": "assistant", "content": target_json_str}]
    full_text = tokenizer.apply_chat_template(
        full_messages,
        tokenize=False,
        add_generation_prompt=False,
    )
    prompt_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    prompt_ids = tokenizer.encode(prompt_text, add_special_tokens=False)
    full_ids = tokenizer.encode(full_text, add_special_tokens=False)
    target_len = len(full_ids) - len(prompt_ids)

    # If full sequence exceeds max_seq_length, truncate source_text so the target fits intact
    if len(full_ids) > max_seq_length:
        target_budget = target_len + 16
        prompt_budget = max_seq_length - target_budget

        empty_messages = format_eval_prompt("")
        empty_prompt_text = tokenizer.apply_chat_template(
            empty_messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        empty_prompt_len = len(tokenizer.encode(empty_prompt_text, add_special_tokens=False))

        allowed_src_tokens = max(100, prompt_budget - empty_prompt_len)
        src_tokens = tokenizer.encode(record.get("source_text", ""), add_special_tokens=False)[:allowed_src_tokens]
        truncated_src = tokenizer.decode(src_tokens, skip_special_tokens=True)

        record_copy = dict(record)
        record_copy["source_text"] = truncated_src
        messages, target_dict = format_training_example(record_copy)
        full_messages = messages + [{"role": "assistant", "content": target_json_str}]

        full_text = tokenizer.apply_chat_template(
            full_messages,
            tokenize=False,
            add_generation_prompt=False,
        )
        prompt_text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        prompt_ids = tokenizer.encode(prompt_text, add_special_tokens=False)
        full_ids = tokenizer.encode(full_text, add_special_tokens=False)

    # Ensure full_ids ends with eos_token_id if not present
    if tokenizer.eos_token_id and (not full_ids or full_ids[-1] != tokenizer.eos_token_id):
        full_ids.append(tokenizer.eos_token_id)

    # Final safety clamp on prompt prefix only
    if len(full_ids) > max_seq_length:
        overflow = len(full_ids) - max_seq_length
        full_ids = full_ids[overflow:]
        prompt_len = max(0, len(prompt_ids) - overflow)
    else:
        prompt_len = len(prompt_ids)

    labels = [-100] * prompt_len + full_ids[prompt_len:]
    attention_mask = [1] * len(full_ids)

    assert any(l != -100 for l in labels), (
        f"Record {record.get('audit_id')} has 0 unmasked target tokens!"
    )

    return {
        "input_ids": full_ids,
        "attention_mask": attention_mask,
        "labels": labels,
    }


def load_and_format_train_records(
    train_path: Path,
) -> list[dict[str, Any]]:
    """Load records from comedy_sft_train.jsonl."""
    if not train_path.exists():
        raise FileNotFoundError(f"Training dataset not found: {train_path}")

    records = []
    with open(train_path, encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if line_str:
                records.append(json.loads(line_str))

    return records

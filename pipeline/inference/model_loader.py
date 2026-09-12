"""
Model Loader Module for Inference.

Loads local base model (Qwen 2.5 1.5B Instruct) and attaches fine-tuned LoRA adapter.
"""

import sys
try:
    import pyarrow
except OSError:
    sys.modules["pyarrow"] = None

from pathlib import Path
from typing import Tuple, Optional, Any
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.ModelLoader")


def load_inference_model_and_tokenizer(
    base_model_path_or_id: str,
    lora_adapter_path: Optional[str] = None,
) -> Tuple[Any, Any]:
    """Loads base model and attaches fine-tuned PEFT LoRA adapter.

    Args:
        base_model_path_or_id: Path or model ID for base model.
        lora_adapter_path: Path to saved LoRA adapter folder.

    Returns:
        Tuple of (model, tokenizer).
    """
    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel
    except ImportError as e:
        raise RuntimeError(f"Missing inference dependencies ({e}). Run: pip install torch transformers peft")

    has_cuda = torch.cuda.is_available()
    device = "cuda" if has_cuda else "cpu"
    dtype = torch.bfloat16 if has_cuda else torch.float32

    b_path = Path(base_model_path_or_id).resolve()
    target_base = str(b_path) if b_path.exists() else base_model_path_or_id

    logger.info(f"Loading tokenizer from: '{target_base}'")
    tokenizer = AutoTokenizer.from_pretrained(target_base, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info(f"Loading base model weights on device ({device}) with dtype ({dtype})...")
    model = AutoModelForCausalLM.from_pretrained(
        target_base,
        dtype=dtype,
        device_map=device if has_cuda else None,
        trust_remote_code=True,
    )

    if lora_adapter_path:
        a_path = Path(lora_adapter_path).resolve()
        if a_path.exists():
            logger.info(f"Attaching fine-tuned LoRA adapter from: '{a_path}'")
            model = PeftModel.from_pretrained(model, str(a_path))
        else:
            logger.warning(f"LoRA adapter path not found at: '{a_path}'. Using base model.")

    model.eval()
    return model, tokenizer

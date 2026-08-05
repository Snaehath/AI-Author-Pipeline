"""
QLoRA Model & Tokenizer Builder Module.

Configures 4-bit NF4 quantization via bitsandbytes, loads model weights,
and attaches PEFT LoRA adapters optimized for low VRAM.
"""

import sys
try:
    import pyarrow
except OSError:
    sys.modules["pyarrow"] = None

from pathlib import Path
from typing import Dict, Any, Tuple, Optional
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Trainer.QLoRABuilder")


class TrainingDependencyError(Exception):
    """Raised when required training packages (torch, transformers, peft, bitsandbytes) are missing."""
    pass


def build_qlora_model_and_tokenizer(
    model_path_or_id: str,
    lora_settings: Optional[Dict[str, Any]] = None,
    use_4bit: bool = False,
) -> Tuple[Any, Any]:
    """Loads base model and attaches PEFT LoRA adapter.

    Args:
        model_path_or_id: Local folder path or Hugging Face repository ID.
        lora_settings: Dictionary containing LoRA hyperparameters (r, alpha, dropout, target_modules).
        use_4bit: Whether to use 4-bit quantization (BitsAndBytes). Defaults to False for native CUDA speed.

    Returns:
        Tuple of (peft_model, tokenizer).
    """
    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    except ImportError as e:
        raise TrainingDependencyError(
            f"Missing required training dependencies ({e}).\n"
            "Please install via: pip install torch transformers peft bitsandbytes accelerate trl"
        )

    resolved_path = Path(model_path_or_id).resolve()
    target_path = str(resolved_path) if resolved_path.exists() else model_path_or_id

    logger.info(f"Loading tokenizer from: '{target_path}'")
    tokenizer = AutoTokenizer.from_pretrained(target_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    has_cuda = torch.cuda.is_available()
    device_target = "cuda" if has_cuda else "cpu"

    if use_4bit and has_cuda:
        logger.info("Configuring 4-bit BitsAndBytes quantization (NF4, double quant)...")
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
        logger.info(f"Loading 4-bit quantized base model weights from: '{target_path}'")
        model = AutoModelForCausalLM.from_pretrained(
            target_path,
            quantization_config=bnb_config,
            torch_dtype=torch.bfloat16,
            device_map=device_target,
            trust_remote_code=True,
        )
        model = prepare_model_for_kbit_training(model)
    else:
        if not has_cuda:
            logger.warning("CUDA is not enabled in PyTorch. Install PyTorch with CUDA via:")
            logger.warning("pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124")
        logger.info(f"Loading BF16 model weights on device ({device_target}) from: '{target_path}'")
        model = AutoModelForCausalLM.from_pretrained(
            target_path,
            dtype=torch.bfloat16 if has_cuda else torch.float32,
            device_map=device_target if has_cuda else None,
            trust_remote_code=True,
        )

    model.config.use_cache = False

    # PEFT LoRA Configuration
    lora_cfg = lora_settings or {}
    r = lora_cfg.get("r", 16)
    alpha = lora_cfg.get("lora_alpha", 32)
    dropout = lora_cfg.get("lora_dropout", 0.05)
    target_modules = lora_cfg.get(
        "target_modules",
        ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
    )

    logger.info(f"Attaching LoRA adapter (r={r}, alpha={alpha}, dropout={dropout})...")
    peft_config = LoraConfig(
        r=r,
        lora_alpha=alpha,
        target_modules=target_modules,
        lora_dropout=dropout,
        bias="none",
        task_type="CAUSAL_LM",
    )

    peft_model = get_peft_model(model, peft_config)
    peft_model.print_trainable_parameters()

    return peft_model, tokenizer

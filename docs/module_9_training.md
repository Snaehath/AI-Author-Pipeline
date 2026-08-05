# Module 9: Training — Documentation

## Overview
**Module 9 (Training)** executes local QLoRA 4-bit fine-tuning of the base model (**Qwen 2.5 1.5B Instruct**) located at `models/Qwen2.5-1.5B-Instruct` using the synthesized SFT datasets (`datasets/train.jsonl` and `datasets/val.jsonl`).

The pipeline is optimized for low-VRAM GPUs (**RTX 3050 4GB VRAM**).

Outputs are written to `models/story_lora_adapter/`.

---

## Architecture & Components

```
AI_Author/trainer/
├── dataset_loader.py  # Formats train.jsonl into ChatML tokenized prompts
├── qlora_builder.py   # Quantizes base model in 4-bit NF4 and attaches PEFT LoRA adapter
└── train_pipeline.py  # Main pipeline orchestrator
```

### 1. Low-VRAM Hardware Optimization
- **4-Bit NF4 Quantization**: Loads base model weights in 4-bit NormalFloat4 (`nf4`) with double quantization enabled.
- **LoRA Adapter Hyperparameters**: $r=16$, $\alpha=32$, Dropout=0.05, Target Modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`.
- **Memory Management**: Batch size = 1, Gradient accumulation = 8, Max sequence length = 512, Gradient checkpointing = True, Optimizer = `paged_adamw_8bit`.
- **Peak VRAM Footprint**: **~2.8 GB - 3.4 GB VRAM**.

### 2. Dataset Loader (`dataset_loader.py`)
Formats SFT examples into ChatML template prompts:
```
<|im_start|>system
You are a professional AI novel author...<|im_end|>
<|im_start|>user
Write a scene...<|im_end|>
<|im_start|>assistant
Prose text...<|im_end|>
```

### 3. Training Orchestrator (`train_pipeline.py`)
Executes QLoRA fine-tuning and outputs:
- `models/story_lora_adapter/adapter_model.safetensors`
- `models/story_lora_adapter/adapter_config.json`
- `models/story_lora_adapter/training_metrics.json`

---

## How to Run & Test

### Running Unit & Format Verification Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_trainer.py
```

### Executing Local QLoRA Fine-Tuning
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python trainer/train_pipeline.py
```

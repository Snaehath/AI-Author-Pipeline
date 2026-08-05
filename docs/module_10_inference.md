# Module 10: Inference Engine — Documentation

## Overview
**Module 10 (Inference Engine)** loads the base model (**Qwen 2.5 1.5B Instruct**) located at `models/Qwen2.5-1.5B-Instruct` along with your fine-tuned **LoRA adapter** (`models/story_lora_adapter/`) to support 10 core professional author storytelling tasks.

---

## Architecture & Components

```
AI_Author/inference/
├── model_loader.py  # Loads base model and attaches fine-tuned PEFT LoRA adapter
├── generator.py     # Implements 10 specialized storytelling generation APIs
└── story_cli.py     # Interactive CLI tool for author novel generation
```

### The 10 Core Author Capabilities
1. 📖 **Create Novel**: Generates 3-Act story outlines and 8-point plot structure.
2. 📝 **Create Chapter**: Generates full chapter draft from scene summaries.
3. ⏩ **Continue Story**: Extends prose text seamlessly.
4. 🔄 **Rewrite Scene**: Revises scene according to custom artistic direction.
5. 💬 **Improve Dialogue**: Enhances subtext, character voice, and emotional expression.
6. ⚡ **Increase Suspense**: Heightens environmental threats, stakes, and tension.
7. 🏃 **Improve Pacing**: Tailors sentence lengths for fast action or slow immersion.
8. 💖 **Emotional Impact**: Enhances emotional resonance and valence.
9. 👤 **Character & World Generation**: Produces character profiles and world lore.
10. 🌅 **Ending Generation**: Crafts climactic resolutions and epilogue teasers.

---

## How to Run & Test

### Running Unit Tests
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python tests/test_inference.py
```

### Running Interactive Storytelling CLI
**From inside `D:\DevelopmentSide\ML\AI_Author`:**
```powershell
python inference/story_cli.py
```

### Running Non-Interactive Generation (CLI Commands)

#### 1. Create Novel Outline
```powershell
python inference/story_cli.py --task create_novel --title "The Lost Artifact" --genre "Fantasy" --premise "Two travelers seek a lost artifact."
```

#### 2. Create Chapter Scene
```powershell
python inference/story_cli.py --task create_chapter --title "The Lost Artifact" --summary "Aria and Kane find the entrance to the ancient cavern."
```

#### 3. Continue Story Snippet
```powershell
python inference/story_cli.py --task continue_story --text "Aria adjusted her leather cloak as the cold mountain wind howled."
```

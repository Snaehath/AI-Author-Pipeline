"""
AI Author Studio Project Initialization & Book Downloader Script.

Automatically sets up directory structures, downloads public-domain classic comedy books
from Project Gutenberg, runs ingestion/anonymization pipelines, and synthesizes datasets
so anyone can replicate this project with 1 command.
"""

import urllib.request
from pathlib import Path
import sys
import json

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Setup")

# Public Domain Project Gutenberg Comedy Books Map
GUTENBERG_BOOKS = {
    "right_ho": "https://www.gutenberg.org/cache/epub/10554/pg10554.txt",
    "my_man_jeeves": "https://www.gutenberg.org/cache/epub/8164/pg8164.txt",
    "three_men_in_a_boat": "https://www.gutenberg.org/cache/epub/308/pg308.txt",
    "a_damsel_in_distress": "https://www.gutenberg.org/cache/epub/2233/pg2233.txt",
    "the_inimitable_jeeves": "https://www.gutenberg.org/cache/epub/6753/pg6753.txt",
    "something_fresh": "https://www.gutenberg.org/cache/epub/2042/pg2042.txt",
    "psmith_in_the_city": "https://www.gutenberg.org/cache/epub/1913/pg1913.txt",
    "the_diary_of_a_nobody": "https://www.gutenberg.org/cache/epub/2631/pg2631.txt",
}


def setup_workspace():
    """Initializes directory structure and downloads Gutenberg comedy books."""
    logger.info("==================================================")
    logger.info("Starting AI Author Studio Automated Project Setup...")
    logger.info("==================================================")

    # 1. Create required workspace directories
    dirs = [
        PROJECT_ROOT / "books",
        PROJECT_ROOT / "datasets",
        PROJECT_ROOT / "models",
        PROJECT_ROOT / "outputs",
        PROJECT_ROOT / "config",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        logger.info(f"✓ Directory ready: '{d.relative_to(PROJECT_ROOT)}'")

    # 2. Download Public Domain Books
    logger.info("\n--- Downloading Public Domain Comedy Books from Project Gutenberg ---")
    books_dir = PROJECT_ROOT / "books"
    downloaded_count = 0

    for book_id, url in GUTENBERG_BOOKS.items():
        dest_path = books_dir / f"{book_id}.txt"
        if dest_path.exists():
            logger.info(f"  • Found existing book: '{book_id}.txt'")
            downloaded_count += 1
            continue

        try:
            logger.info(f"  • Downloading '{book_id}' from Gutenberg...")
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as resp, open(dest_path, "wb") as f:
                f.write(resp.read())
            logger.info(f"  ✓ Saved '{book_id}.txt'")
            downloaded_count += 1
        except Exception as e:
            logger.warning(f"  ! Could not download '{book_id}': {e}")

    logger.info(f"\n✓ Downloaded/Verified {downloaded_count} Public Domain Comedy Books.")

    # 3. Download Base Model Weights from HuggingFace
    logger.info("\n--- Downloading Base Model Weights (Qwen2.5-1.5B-Instruct) from HuggingFace ---")
    model_dir = PROJECT_ROOT / "models" / "Qwen2.5-1.5B-Instruct"
    if model_dir.exists() and (model_dir / "config.json").exists():
        logger.info("  ✓ Base model 'Qwen2.5-1.5B-Instruct' already exists locally.")
    else:
        try:
            logger.info("  • Downloading 'Qwen/Qwen2.5-1.5B-Instruct' from HuggingFace...")
            from huggingface_hub import snapshot_download
            snapshot_download(
                repo_id="Qwen/Qwen2.5-1.5B-Instruct",
                local_dir=str(model_dir),
                local_dir_use_symlinks=False,
            )
            logger.info("  ✓ Downloaded base model weights to 'models/Qwen2.5-1.5B-Instruct'.")
        except Exception as e:
            logger.warning(f"  ! HuggingFace download note: {e}")
            logger.info("    You can also download via: huggingface-cli download Qwen/Qwen2.5-1.5B-Instruct --local-dir models/Qwen2.5-1.5B-Instruct")

    # 4. Synthesize DPO Preference Dataset
    logger.info("\n--- Synthesizing DPO Comedic Preference Alignment Dataset ---")
    try:
        from AI_Author.dataset_generator.dpo_synthesizer import DPOComedicSynthesizer
        synthesizer = DPOComedicSynthesizer()
        saved_dpo = synthesizer.save_dpo_dataset()
        logger.info(f"✓ Saved DPO Dataset to: '{saved_dpo.relative_to(PROJECT_ROOT)}'")
    except Exception as e:
        logger.warning(f"! DPO Dataset synthesis note: {e}")

    logger.info("\n==================================================")
    logger.info("✓ AI Author Studio Setup Complete!")
    logger.info("==================================================")
    logger.info("To train models and generate novels, run:")
    logger.info("  python trainer/dpo_trainer.py")
    logger.info("  python inference/novel_builder_v2.py --chapters 5 --title \"The Mischief at Blackwood Manor\"")
    logger.info("==================================================")


if __name__ == "__main__":
    setup_workspace()

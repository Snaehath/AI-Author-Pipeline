"""
AI Author Studio — Master Automated Pipeline Orchestrator.

Runs the complete end-to-end AI Author workflow on any input e-book file (.txt, .pdf, .epub, .docx):
  1. Book Ingestion & Cleaning
  2. Chapter & Dialogue Parsing
  3. Story, POV, Tone & Pacing Analysis
  4. Character Trait & Relationship Mapping
  5. Dialogue Emotion & Sub-conflict Analysis
  6. Valence & Emotion Timeline Tracking
  7. 8-Point Plot Structure Mapping
  8. SFT Training Dataset Synthesis
  9. QLoRA Model Training (Optional flag --train)
  10. Automated Novel Generation & Manuscript Export (DOCX & PDF)
  11. Literary Evaluation Suite
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure project root and AI_Author directory are in sys.path
AI_AUTHOR_DIR = Path(__file__).resolve().parent
ML_DIR = AI_AUTHOR_DIR.parent

for p in (AI_AUTHOR_DIR, ML_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from AI_Author.ingestion.pipeline import IngestionPipeline
from AI_Author.parser.chapter_parser import ChapterParser
from AI_Author.analyzer.story_analyzer import StoryAnalyzer
from AI_Author.analyzer.character_analyzer import CharacterAnalyzer
from AI_Author.analyzer.dialogue_analyzer import DialogueAnalyzer
from AI_Author.analyzer.emotion_analyzer import EmotionAnalyzer
from AI_Author.analyzer.plot_analyzer import PlotAnalyzer
from AI_Author.dataset_generator.dataset_pipeline import DatasetPipeline
from AI_Author.inference.novel_builder import NovelBuilder
from AI_Author.evaluator.eval_pipeline import EvaluationPipeline
from AI_Author.utils.manuscript_exporter import export_book_workspace
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.MasterPipeline")


def run_master_pipeline(
    input_file_path: Path,
    title: str = "",
    author: str = "",
    train: bool = False,
    num_generated_chapters: int = 3,
    ingest_only: bool = False,
) -> Path:
    """Executes the master automated pipeline for a new input book.

    Args:
        input_file_path: Path to raw ebook file (.txt, .epub, .pdf, .docx).
        title: Optional book title override.
        author: Optional author override.
        train: Whether to run QLoRA fine-tuning after dataset generation.
        num_generated_chapters: Number of chapters for generated novel.
        ingest_only: If True, skips novel generation & evaluation steps.

    Returns:
        Path to output directory.
    """
    book_file = Path(input_file_path).resolve()
    if not book_file.exists():
        raise FileNotFoundError(f"Input ebook file not found at: '{book_file}'")

    print("\n" + "=" * 65)
    print("        🚀 AI AUTHOR STUDIO — MASTER AUTOMATED WORKFLOW        ")
    print("=" * 65)
    print(f"Processing File: {book_file.name}")

    # STEP 1: Ingestion
    print("\n[1/8] Running Book Ingestion & Chapter Segmentation...")
    ingestion = IngestionPipeline()
    ingest_res = ingestion.run(book_file, title=title, author=author)
    book_dir = ingest_res.cleaned_text_path.parent
    book_title = book_dir.name.replace("_", " ").title()
    print(f"✓ Ingestion complete. Output directory: '{book_dir.name}'")

    # STEP 2: Chapter Parsing
    print("\n[2/8] Parsing Scenes & Dialogue Turns...")
    ChapterParser().parse_book_directory(book_dir)
    print("✓ Chapter Parsing complete.")

    # STEP 3: Story Analysis
    print("\n[3/8] Analyzing Story POV, Tone, Pacing & Conflicts...")
    StoryAnalyzer().analyze_book_directory(book_dir)
    print("✓ Story Analysis complete.")

    # STEP 4: Character Analysis
    print("\n[4/8] Extracting Character Profiles & Relationship Maps...")
    CharacterAnalyzer().analyze_book_directory(book_dir)
    print("✓ Character Analysis complete.")

    # STEP 5: Dialogue Analysis
    print("\n[5/8] Analyzing Dialogue Emotions & Sub-conflicts...")
    DialogueAnalyzer().analyze_book_directory(book_dir)
    print("✓ Dialogue Analysis complete.")

    # STEP 6: Emotion Timeline Analysis
    print("\n[6/8] Tracking Valence & Emotion Timeline...")
    EmotionAnalyzer().analyze_book_directory(book_dir)
    print("✓ Emotion Timeline complete.")

    # STEP 7: Plot Analyzer
    print("\n[7/8] Mapping 8-Point Plot Structure Milestones...")
    PlotAnalyzer().analyze_book_directory(book_dir)
    print("✓ Plot Structure Mapping complete.")

    # STEP 8: Dataset Generator
    print("\n[8/8] Synthesizing SFT Instruction Datasets (train.jsonl & val.jsonl)...")
    ds_res = DatasetPipeline().run_pipeline([book_dir])
    print(f"✓ Dataset Synthesis complete ({ds_res.get('total_examples', 0)} total instruction pairs).")

    if ingest_only:
        print("\n" + "=" * 65)
        print(f"✓ INGESTION & ANALYSIS COMPLETE FOR: {book_title}")
        print("=" * 65 + "\n")
        return book_dir

    # STEP 9: Training (Optional)
    if train:
        print("\n[9/11] Executing Local QLoRA Fine-Tuning on GPU...")
        from AI_Author.trainer.train_pipeline import TrainingPipeline
        train_res = TrainingPipeline().run_training()
        print(f"✓ Training complete! Adapter saved to: '{train_res.adapter_output_dir.name}'")
    else:
        print("\n[9/11] Training step skipped (use --train flag to execute local fine-tuning).")

    # STEP 10: Novel Builder
    print("\n[10/11] Generating New Novel & Compiling Manuscript...")
    builder = NovelBuilder()
    gen_title = f"The Legacy of {book_title}"
    gen_premise = f"An epic detective adventure inspired by the storytelling structure of {book_title}."
    gen_res = builder.generate_complete_novel(
        title=gen_title,
        genre="Detective / Mystery",
        premise=gen_premise,
        num_chapters=num_generated_chapters
    )
    gen_dir = Path(gen_res["output_dir"])
    print(f"✓ Novel Generation complete. Output saved to: '{gen_dir.name}'")

    # STEP 11: Evaluation & Manuscript Export
    print("\n[11/11] Running Literary Evaluation Suite & Manuscript Exporter...")
    eval_res = EvaluationPipeline().evaluate_book_directory(gen_dir, reference_dir=book_dir)
    exp_res = export_book_workspace(gen_dir)

    print("\n" + "=" * 65)
    print("                     🎉 WORKFLOW COMPLETE!                     ")
    print("=" * 65)
    print(f"• Analyzed Reference Book : {book_title}")
    print(f"• Style Consistency Score  : {eval_res['author_style_consistency']['overall_style_consistency']}")
    print(f"• Generated Manuscript DOCX : {exp_res['docx_path']}")
    print(f"• Generated Manuscript PDF  : {exp_res['pdf_path']}")
    print("=" * 65 + "\n")

    return book_dir


def main():
    parser = argparse.ArgumentParser(description="AI Author Studio — Master Workflow Script")
    parser.add_argument("ebook", type=str, help="Path to raw ebook file (.txt, .epub, .pdf, .docx)")
    parser.add_argument("--title", type=str, default="", help="Optional book title override")
    parser.add_argument("--author", type=str, default="", help="Optional author override")
    parser.add_argument("--train", action="store_true", help="Run local QLoRA fine-tuning on GPU during workflow")
    parser.add_argument("--chapters", type=int, default=3, help="Number of chapters to generate for new novel")
    parser.add_argument("--ingest-only", action="store_true", help="Only run ingestion & analysis steps without generating story")

    args = parser.parse_args()
    run_master_pipeline(
        input_file_path=Path(args.ebook),
        title=args.title,
        author=args.author,
        train=args.train,
        num_generated_chapters=args.chapters,
        ingest_only=args.ingest_only,
    )


if __name__ == "__main__":
    main()

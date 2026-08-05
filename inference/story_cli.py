"""
AI Author Studio — Storytelling CLI Tool.

Interactive Command Line Interface allowing authors to execute 10 professional novel generation tasks
powered by Qwen 2.5 1.5B Instruct + fine-tuned LoRA adapter.
"""

import argparse
import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from AI_Author.inference.generator import StoryGenerator
from AI_Author.utils.logger import setup_logger

logger = setup_logger("AI_Author.Inference.CLI")


def run_interactive_menu(generator: StoryGenerator) -> None:
    """Runs interactive menu for prompt-driven novel creation."""
    print("\n" + "=" * 60)
    print("      AI AUTHOR STUDIO — INTERACTIVE STORYTELLING CLI      ")
    print("=" * 60)
    print("Select a task:")
    print(" 1. Create Novel Outline (3-Act / 8-Point Structure)")
    print(" 2. Create Chapter Scene")
    print(" 3. Continue Story")
    print(" 4. Rewrite Scene with Custom Direction")
    print(" 5. Improve Dialogue (Emotion & Subtext)")
    print(" 6. Increase Suspense & Tension")
    print(" 7. Improve Pacing (Fast vs Slow)")
    print(" 8. Emotional Impact & Valence")
    print(" 9. Character Profile & World Lore Generator")
    print("10. Ending & Resolution Generator")
    print(" 0. Exit")
    print("=" * 60)

    choice = input("Enter choice (0-10): ").strip()
    if choice == "0":
        print("Goodbye!")
        return

    output = ""
    if choice == "1":
        title = input("Novel Title: ") or "The Chronicles of Eldoria"
        genre = input("Genre: ") or "Fantasy / Adventure"
        premise = input("Premise: ") or "Two travelers seek a lost artifact in cold mountains."
        output = generator.create_novel(title, genre, premise)

    elif choice == "2":
        title = input("Book Title: ") or "Sample Novel"
        num = int(input("Chapter Number: ") or 1)
        summary = input("Scene Summary: ") or "Aria and Kane find the entrance to the ancient cavern."
        output = generator.create_chapter(title, num, summary)

    elif choice == "3":
        snippet = input("Enter snippet to continue:\n")
        goal = input("Continuation Goal (optional): ")
        output = generator.continue_story(snippet, goal)

    elif choice == "4":
        snippet = input("Enter original scene:\n")
        direction = input("Rewrite Direction: ") or "Make it suspenseful and dark."
        output = generator.rewrite_scene(snippet, direction)

    elif choice == "5":
        snippet = input("Enter dialogue scene:\n")
        emotion = input("Target Emotion (default: Urgent / Cautious): ") or "Urgent / Cautious"
        output = generator.improve_dialogue(snippet, emotion)

    elif choice == "6":
        snippet = input("Enter scene draft:\n")
        output = generator.increase_suspense(snippet)

    elif choice == "7":
        snippet = input("Enter scene draft:\n")
        pacing = input("Target Pacing (default: Fast-Paced Action): ") or "Fast-Paced Action"
        output = generator.improve_pacing(snippet, pacing)

    elif choice == "8":
        snippet = input("Enter scene draft:\n")
        emotion = input("Target Emotion (default: Wonder & Awe): ") or "Wonder & Awe"
        output = generator.emotional_impact(snippet, emotion)

    elif choice == "9":
        prompt = input("Character/World Requirements: ") or "Aria (Protagonist, brave warrior) and Frostclaw Mountains."
        output = generator.generate_character_world(prompt)

    elif choice == "10":
        context = input("Enter story context for ending:\n")
        output = generator.generate_ending(context)

    else:
        print("Invalid choice.")
        return

    print("\n" + "=" * 60)
    print("                     GENERATED OUTPUT                      ")
    print("=" * 60)
    print(output)
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="AI Author Studio — Inference CLI")
    parser.add_argument("--task", type=str, choices=[
        "create_novel", "create_chapter", "continue_story", "rewrite_scene",
        "improve_dialogue", "increase_suspense", "improve_pacing", "emotional_impact",
        "generate_character_world", "generate_ending"
    ], help="Task to execute non-interactively")

    parser.add_argument("--title", type=str, default="Sample Novel")
    parser.add_argument("--genre", type=str, default="Fantasy / Adventure")
    parser.add_argument("--premise", type=str, default="A quest for a lost artifact.")
    parser.add_argument("--summary", type=str, default="Opening scene in the mountains.")
    parser.add_argument("--text", type=str, default="Cold wind howled through the canyon.")
    parser.add_argument("--direction", type=str, default="Make it suspenseful.")
    parser.add_argument("--emotion", type=str, default="Urgent / Cautious")
    parser.add_argument("--pacing", type=str, default="Fast-Paced Action")
    parser.add_argument("--prompt", type=str, default="Aria, female warrior.")
    parser.add_argument("--output_file", type=str, help="Path to save generated output text file")

    args = parser.parse_args()

    generator = StoryGenerator()

    if not args.task:
        run_interactive_menu(generator)
        return

    output = ""
    if args.task == "create_novel":
        output = generator.create_novel(args.title, args.genre, args.premise)
    elif args.task == "create_chapter":
        output = generator.create_chapter(args.title, 1, args.summary)
    elif args.task == "continue_story":
        output = generator.continue_story(args.text)
    elif args.task == "rewrite_scene":
        output = generator.rewrite_scene(args.text, args.direction)
    elif args.task == "improve_dialogue":
        output = generator.improve_dialogue(args.text, args.emotion)
    elif args.task == "increase_suspense":
        output = generator.increase_suspense(args.text)
    elif args.task == "improve_pacing":
        output = generator.improve_pacing(args.text, args.pacing)
    elif args.task == "emotional_impact":
        output = generator.emotional_impact(args.text, args.emotion)
    elif args.task == "generate_character_world":
        output = generator.generate_character_world(args.prompt)
    elif args.task == "generate_ending":
        output = generator.generate_ending(args.text)

    print("\n" + "=" * 60)
    print(f"OUTPUT FOR TASK: {args.task}")
    print("=" * 60)
    print(output)
    print("=" * 60)

    if args.output_file:
        out_path = Path(args.output_file)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Saved output to: '{out_path}'")


if __name__ == "__main__":
    main()

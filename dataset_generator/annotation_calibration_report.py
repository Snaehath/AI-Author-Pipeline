"""
Annotation Calibration Audit & Review Sheet Generator.

Generates structured human audit review sheets (Markdown and JSON) for calibrating
automated AI craft annotations against human expert ground truth.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Ensure project and ML roots are on path
AI_AUTHOR_DIR = Path(__file__).resolve().parent.parent
ML_DIR = AI_AUTHOR_DIR.parent
for p in [str(AI_AUTHOR_DIR), str(ML_DIR)]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from .taxonomy import ComicMechanism
except ImportError:
    from dataset_generator.taxonomy import ComicMechanism


class AnnotationCalibrationReport:
    """Manages generation of human calibration review sheets and agreement score evaluation."""

    def __init__(self, sample_records: List[Dict[str, Any]]):
        self.records = sample_records

    def generate_review_sheet_md(self) -> str:
        """Generates a human-inspectable markdown review sheet with fillable audit forms."""
        lines = [
            "# Comedy Craft Annotation Calibration Sheet",
            "",
            "> **Audit Instructions**: Review each AI annotation against the unabridged source passage.",
            "> Check whether the primary mechanism, structural beats (setup/escalation/reversal/payoff),",
            "> and tone match your literary judgment. Record your human ground truth in the blanks provided.",
            "",
            "---",
            "",
        ]

        for i, rec in enumerate(self.records, 1):
            src = rec.get("source", {})
            facts = rec.get("facts", {})
            craft = rec.get("craft", {})

            source_id = src.get("source_id", f"passage_{i:03d}")
            book = src.get("source_book", "Unknown Book")
            chapter = src.get("chapter_index", "?")
            text = src.get("source_text", "").strip()

            ai_primary = craft.get("primary_mechanism", "UNKNOWN")
            ai_secondaries = ", ".join(craft.get("secondary_mechanisms", [])) or "None"
            detector_conf = craft.get("detector_confidence", craft.get("confidence", 0.0))
            craft_score = craft.get("linguistic_craft_score", craft.get("quality_score", 0.0))
            tone = craft.get("tone", "UNKNOWN")
            dialogue_ratio = facts.get("dialogue_ratio", 0.0)
            characters = ", ".join(facts.get("characters", [])) or "None"

            setup = craft.get("setup_summary", "")
            escalation = craft.get("escalation_summary", "")
            reversal = craft.get("reversal_summary", "")
            payoff = craft.get("payoff_summary", "")
            surface_slang = ", ".join(craft.get("surface_style_features", [])) or "None"

            lines.extend([
                f"## Example {i:02d} — `{source_id}`",
                "",
                f"**Source**: *{book}* (Chapter {chapter})  ",
                f"**Characters Identified**: {characters}  ",
                f"**Dialogue Ratio**: `{dialogue_ratio:.2f}` | **Surface Slang Isolated**: {surface_slang}  ",
                "",
                "### Passage",
                "```text",
                text,
                "```",
                "",
                "### AI Extraction",
                f"- **Primary Mechanism**: `{ai_primary}` (Detector Confidence: `{detector_conf:.2f}`)",
                f"- **Secondary Dynamics**: {ai_secondaries}",
                f"- **Linguistic Craft Score**: `{craft_score:.2f}`",
                f"- **Tone**: `{tone}`",
                f"- **Setup**: {setup}",
                f"- **Escalation**: {escalation}",
                f"- **Reversal**: {reversal}",
                f"- **Payoff**: {payoff}",
                "",
                "### Human Verification Form",
                "```text",
                "[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]",
                "[ ] HUMAN PRIMARY MECHANISM : _________________________",
                "[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]",
                "[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]",
                "[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]",
                "[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]",
                "[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]",
                "[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)",
                "[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)",
                "[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]",
                "[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]",
                "[ ] HUMAN AUDIT NOTES       : _________________________",
                "```",
                "",
                "---",
                "",
            ])

        return "\n".join(lines)

    def generate_review_sheet_json(self) -> List[Dict[str, Any]]:
        """Generates audit template in JSON format for automated evaluation."""
        audit_items = []
        for i, rec in enumerate(self.records, 1):
            src = rec.get("source", {})
            facts = rec.get("facts", {})
            craft = rec.get("craft", {})

            audit_items.append({
                "item_index": i,
                "source_id": src.get("source_id", ""),
                "source_book": src.get("source_book", ""),
                "chapter_index": src.get("chapter_index", 1),
                "source_text": src.get("source_text", ""),
                "ai_annotation": {
                    "primary_mechanism": craft.get("primary_mechanism", ""),
                    "secondary_mechanisms": craft.get("secondary_mechanisms", []),
                    "detector_confidence": craft.get("detector_confidence", craft.get("confidence", 0.0)),
                    "linguistic_craft_score": craft.get("linguistic_craft_score", craft.get("quality_score", 0.0)),
                    "tone": craft.get("tone", ""),
                    "setup": craft.get("setup_summary", ""),
                    "escalation": craft.get("escalation_summary", ""),
                    "reversal": craft.get("reversal_summary", ""),
                    "payoff": craft.get("payoff_summary", ""),
                },
                "human_audit": {
                    "verdict": None,  # "AGREE", "PARTIAL", "DISAGREE"
                    "human_primary_mechanism": None,
                    "human_secondary_mechanisms": [],
                    "setup_accurate": None,  # bool
                    "escalation_accurate": None,  # bool
                    "reversal_accurate": None,  # bool
                    "payoff_accurate": None,  # bool
                    "human_literary_quality": None,  # float [1-10]
                    "human_training_value": None,  # float [1-10] (Transferability to original scenes)
                    "human_mechanism_confidence": None,  # float [1-10]
                    "disagreement_category": None,  # e.g. "A_DETECTOR_FAILURE", "B_TAXONOMY_AMBIGUITY"
                    "notes": "",
                },
            })
        return audit_items

    @staticmethod
    def calculate_agreement_metrics(audited_records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculates inter-annotator agreement between AI extraction and human audits across 10 metrics."""
        total = len(audited_records)
        if total == 0:
            return {"total_audited": 0}

        mech_agreed = 0
        secondary_agreed = 0
        secondary_evaluated = 0
        setup_agreed = 0
        escalation_agreed = 0
        reversal_agreed = 0
        payoff_agreed = 0
        training_values = []
        quality_scores = []
        confidence_scores = []
        verdict_counts = {"AGREE": 0, "PARTIAL": 0, "DISAGREE": 0, "UNREVIEWED": 0}
        disagreement_counts: Dict[str, int] = {}

        reviewed_count = 0
        for rec in audited_records:
            human = rec.get("human_audit", {})
            ai = rec.get("ai_annotation", {})
            v = human.get("verdict") or "UNREVIEWED"
            verdict_counts[v] = verdict_counts.get(v, 0) + 1

            if v == "UNREVIEWED":
                continue

            reviewed_count += 1

            # 1. Primary mechanism agreement
            if human.get("human_primary_mechanism") == ai.get("primary_mechanism"):
                mech_agreed += 1

            # 2. Secondary mechanism agreement
            human_secs = set(human.get("human_secondary_mechanisms") or [])
            ai_secs = set(ai.get("secondary_mechanisms") or [])
            if human_secs or ai_secs:
                secondary_evaluated += 1
                if (human_secs & ai_secs) or (human_secs == ai_secs):
                    secondary_agreed += 1
            else:
                secondary_evaluated += 1
                secondary_agreed += 1

            # 3-6. Structural beat agreements
            if human.get("setup_accurate") is True:
                setup_agreed += 1
            if human.get("escalation_accurate") is True:
                escalation_agreed += 1
            if human.get("reversal_accurate") is True:
                reversal_agreed += 1
            if human.get("payoff_accurate") is True:
                payoff_agreed += 1

            # 7-9. Quantitative human scores
            if human.get("human_literary_quality") is not None:
                quality_scores.append(float(human["human_literary_quality"]))
            if human.get("human_training_value") is not None:
                training_values.append(float(human["human_training_value"]))
            if human.get("human_mechanism_confidence") is not None:
                confidence_scores.append(float(human["human_mechanism_confidence"]))

            # 10. Disagreement category breakdown
            cat = human.get("disagreement_category")
            if cat:
                disagreement_counts[cat] = disagreement_counts.get(cat, 0) + 1

        avg_training_val = round(sum(training_values) / len(training_values), 2) if training_values else None
        avg_quality = round(sum(quality_scores) / len(quality_scores), 2) if quality_scores else None
        avg_conf = round(sum(confidence_scores) / len(confidence_scores), 2) if confidence_scores else None

        if reviewed_count == 0:
            status = "UNREVIEWED"
            primary_pct = None
            sec_pct = None
            setup_pct = None
            escalation_pct = None
            reversal_pct = None
            payoff_pct = None
        elif reviewed_count < total:
            status = "IN_PROGRESS"
            primary_pct = round((mech_agreed / reviewed_count) * 100, 1)
            sec_pct = round((secondary_agreed / secondary_evaluated) * 100, 1) if secondary_evaluated else 0.0
            setup_pct = round((setup_agreed / reviewed_count) * 100, 1)
            escalation_pct = round((escalation_agreed / reviewed_count) * 100, 1)
            reversal_pct = round((reversal_agreed / reviewed_count) * 100, 1)
            payoff_pct = round((payoff_agreed / reviewed_count) * 100, 1)
        else:
            status = "COMPLETE"
            primary_pct = round((mech_agreed / total) * 100, 1)
            sec_pct = round((secondary_agreed / secondary_evaluated) * 100, 1) if secondary_evaluated else 0.0
            setup_pct = round((setup_agreed / total) * 100, 1)
            escalation_pct = round((escalation_agreed / total) * 100, 1)
            reversal_pct = round((reversal_agreed / total) * 100, 1)
            payoff_pct = round((payoff_agreed / total) * 100, 1)

        return {
            "total_records": total,
            "total_audited": reviewed_count,
            "calibration_status": status,
            "primary_mechanism_agreement_pct": primary_pct,
            "mechanism_agreement_pct": primary_pct,
            "secondary_mechanism_agreement_pct": sec_pct,
            "setup_agreement_pct": setup_pct,
            "escalation_agreement_pct": escalation_pct,
            "reversal_agreement_pct": reversal_pct,
            "payoff_agreement_pct": payoff_pct,
            "mean_literary_quality": avg_quality,
            "average_human_literary_quality": avg_quality,
            "mean_training_value": avg_training_val,
            "average_human_training_value": avg_training_val,
            "mean_mechanism_confidence": avg_conf,
            "disagreement_category_distribution": disagreement_counts,
            "verdict_distribution": verdict_counts,
            "disagreement_breakdown": disagreement_counts,
        }


def parse_args():
    parser = argparse.ArgumentParser(description="Generate Annotation Calibration Review Sheet or Evaluate Audit.")
    parser.add_argument(
        "--sample-path",
        type=str,
        default=str(AI_AUTHOR_DIR / "datasets" / "comedy_craft_sample_50.json"),
        help="Path to sample JSON file.",
    )
    parser.add_argument(
        "--output-md",
        type=str,
        default=str(AI_AUTHOR_DIR / "reports" / "comedy_craft_calibration_sheet.md"),
        help="Path to save markdown review sheet.",
    )
    parser.add_argument(
        "--output-json",
        type=str,
        default=str(AI_AUTHOR_DIR / "reports" / "comedy_craft_calibration_sheet.json"),
        help="Path to save JSON audit template.",
    )
    parser.add_argument(
        "--audit-file",
        type=str,
        default=None,
        help="Path to completed JSON audit file to calculate agreement metrics.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.audit_file:
        audit_path = Path(args.audit_file)
        if not audit_path.exists():
            print(f"Error: Audit file not found: {audit_path}")
            sys.exit(1)
        with open(audit_path, "r", encoding="utf-8") as f:
            audited_records = json.load(f)

        metrics = AnnotationCalibrationReport.calculate_agreement_metrics(audited_records)
        audited_count = metrics["total_audited"]
        total_records = metrics["total_records"]
        status = metrics["calibration_status"]

        print(f"\n=== Human Calibration Agreement ({total_records} records) ===\n")
        print(f"Audited: {audited_count} / {total_records}")

        if status == "UNREVIEWED":
            print("\nStatus: CALIBRATION INCOMPLETE")
            print("No human annotations are currently available.")
            print("Agreement percentages are therefore not meaningful (N/A).\n")
        elif status == "IN_PROGRESS":
            print(f"\nStatus: CALIBRATION IN PROGRESS ({audited_count}/{total_records} complete)\n")
        else:
            print("\nStatus: CALIBRATION COMPLETE\n")

        def _fmt_pct(val):
            return f"{val}%" if val is not None else "N/A"

        def _fmt_val(val):
            return str(val) if val is not None else "N/A"

        print(f"1. Primary Mechanism Agreement:   {_fmt_pct(metrics['primary_mechanism_agreement_pct'])}")
        print(f"2. Secondary Mechanism Agreement: {_fmt_pct(metrics['secondary_mechanism_agreement_pct'])}")
        print(f"3. Setup Agreement:               {_fmt_pct(metrics['setup_agreement_pct'])}")
        print(f"4. Escalation Agreement:          {_fmt_pct(metrics['escalation_agreement_pct'])}")
        print(f"5. Reversal Agreement:            {_fmt_pct(metrics['reversal_agreement_pct'])}")
        print(f"6. Payoff Agreement:              {_fmt_pct(metrics['payoff_agreement_pct'])}")
        print(f"7. Mean Literary Quality:         {_fmt_val(metrics['mean_literary_quality'])}")
        print(f"8. Mean Training Value:           {_fmt_val(metrics['mean_training_value'])}")
        print(f"9. Mean Mechanism Confidence:     {_fmt_val(metrics['mean_mechanism_confidence'])}")

        disagreement_str = (
            json.dumps(metrics["disagreement_category_distribution"], indent=2)
            if metrics["disagreement_category_distribution"]
            else "N/A"
        )
        print(f"10. Disagreement Distribution:    {disagreement_str}")
        print("\nFull metrics JSON:")
        print(json.dumps(metrics, indent=2))
        return

    sample_path = Path(args.sample_path)
    output_md_path = Path(args.output_md)
    output_json_path = Path(args.output_json)

    if not sample_path.exists():
        print(f"Error: Sample file not found: {sample_path}")
        sys.exit(1)

    with open(sample_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    print(f"=== Generating Annotation Calibration Sheet ({len(records)} examples) ===")
    calibrator = AnnotationCalibrationReport(records)

    md_content = calibrator.generate_review_sheet_md()
    json_content = calibrator.generate_review_sheet_json()

    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[OK] Markdown calibration review sheet saved to: {output_md_path}")

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(json_content, f, indent=2, ensure_ascii=False)
    print(f"[OK] JSON calibration audit template saved to: {output_json_path}")
    print("\nCalibration sheet is ready for human inspection.")


if __name__ == "__main__":
    main()

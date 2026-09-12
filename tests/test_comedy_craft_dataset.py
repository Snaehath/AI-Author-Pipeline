"""
Acceptance Test Suite for Phase 3A: Comedy Craft Dataset Builder.

Verifies:
1. Taxonomy schema serialization and round-trip integrity.
2. FactualSceneAnalyzer dialogue ratio and entity extraction.
3. ComedyCraftAnnotator confidence vs. quality independence and slang decoupling.
4. ContrastPurityValidator invariance checking and pair rejection.
5. CraftOperationBuilder Level 3 tasks and Level 4 DPO synthesis.
6. ComedyCraftPipeline stratified selection and report generation.
"""

import json
from pathlib import Path
import pytest

from dataset_generator.taxonomy import (
    ComicMechanism,
    SceneFunction,
    ComedicTone,
    AnnotationSource,
    ReviewStatus,
    ContrastDimension,
    TaskType,
    SourcePassage,
    StoryFacts,
    CraftAnnotation,
    CraftOperationTask,
    ControlledDPOPair,
    ContrastPurityReport,
    ComedyCraftRecord,
)
from dataset_generator.factual_analyzer import FactualSceneAnalyzer
from dataset_generator.craft_annotator import ComedyCraftAnnotator
from dataset_generator.contrast_purity import ContrastPurityValidator
from dataset_generator.operation_builder import CraftOperationBuilder
from dataset_generator.comedy_craft_builder import ComedyCraftPipeline


class TestTaxonomyAndSchema:
    def test_record_round_trip_serialization(self):
        source = SourcePassage(
            source_id="test_book_ch1_00001",
            source_book="My Man Jeeves",
            chapter_index=1,
            source_text='"I say, Jeeves," I said, "this is deuced awkward."',
        )
        facts = StoryFacts(
            characters=["Bertie", "Jeeves"],
            location="drawing room",
            objects=["tea-cup"],
            character_goals={"Bertie": "avert social fallout"},
            dialogue_ratio=0.75,
            turn_count=2,
        )
        craft = CraftAnnotation(
            primary_mechanism=ComicMechanism.STATUS_REVERSAL,
            secondary_mechanisms=[ComicMechanism.DEADPAN_REACTION],
            detector_confidence=0.92,
            linguistic_craft_score=0.85,
            scene_function=SceneFunction.SOCIAL_CONFLICT,
            tone=ComedicTone.DRY_WIT,
            setup_summary="Bertie faces crisis",
            escalation_summary="Bertie appeals to valet",
            reversal_summary="Valet takes charge",
            payoff_summary="Jeeves maintains deadpan order",
            surface_style_features=["deuced"],
            source=AnnotationSource.HEURISTIC,
            review_status=ReviewStatus.UNREVIEWED,
        )
        op = CraftOperationTask(
            task_type=TaskType.IDENTIFY_MECHANISM,
            prompt="Analyze the craft.",
            expected_output="Primary mechanism is STATUS_REVERSAL.",
            target_concept="STATUS_REVERSAL",
        )
        purity = ContrastPurityReport(
            prompt_identical=True,
            plot_events_same=True,
            characters_same=True,
            setting_same=True,
            target_dimension_changed=True,
            purity_score=0.95,
        )
        dpo = ControlledDPOPair(
            prompt="Write the scene",
            chosen="Good restrained prose",
            rejected="Bad joke-explaining prose",
            target_dimension=ContrastDimension.COMEDIC_RESTRAINT,
            purity_report=purity,
        )

        record = ComedyCraftRecord(
            source=source,
            facts=facts,
            craft=craft,
            operations=[op],
            dpo_pair=dpo,
        )

        # Test dictionary serialization and roundtrip
        data = record.to_dict()
        assert data["source"]["source_id"] == "test_book_ch1_00001"
        assert data["craft"]["primary_mechanism"] == "STATUS_REVERSAL"
        assert data["craft"]["confidence"] == 0.92
        assert data["craft"]["quality_score"] == 0.85
        assert data["dpo_pair"]["purity_report"]["purity_score"] == 0.95

        restored = ComedyCraftRecord.from_dict(data)
        assert restored.source.source_book == "My Man Jeeves"
        assert restored.craft.primary_mechanism == ComicMechanism.STATUS_REVERSAL
        assert restored.dpo_pair.target_dimension == ContrastDimension.COMEDIC_RESTRAINT


class TestFactualAnalyzer:
    def test_extract_facts_from_dialogue_scene(self):
        analyzer = FactualSceneAnalyzer()
        text = (
            'Bertie paced the drawing room in agitation. "Look here, Jeeves," said Bertie, '
            '"we are in a dreadful spot regarding Aunt Agatha\'s letter." '
            '"Indeed, sir?" observed Jeeves quietly, adjusting the teacup on the tray.'
        )

        facts = analyzer.analyze(text)
        assert "Bertie" in facts.characters
        assert "Jeeves" in facts.characters
        assert facts.dialogue_ratio > 0.30
        assert facts.turn_count >= 2
        assert facts.location == "drawing room"
        assert any(obj in facts.objects for obj in ["letter", "teacup", "tray"])


class TestComedyCraftAnnotator:
    def test_confidence_vs_quality_independence(self):
        annotator = ComedyCraftAnnotator()
        facts = StoryFacts(characters=["Bertie", "Jeeves"], dialogue_ratio=0.5, turn_count=2)

        # Short snippet with strong status reversal cues
        short_snippet = '"I submit, sir," said the valet respectfully.'
        ann_short = annotator.annotate(short_snippet, facts)
        
        # High confidence for status reversal, but lower quality because it is very short
        assert ann_short.confidence >= 0.30
        assert ann_short.quality_score <= 0.40  # Short snippets get modest quality scores

    def test_surface_slang_decoupled_from_mechanism(self):
        annotator = ComedyCraftAnnotator()
        facts = StoryFacts(characters=["Freddie"], dialogue_ratio=0.1, turn_count=1)
        text = "By Jove, old top! It was a ripping morning, right-o!"

        ann = annotator.annotate(text, facts)
        # Slang must be captured in surface features
        assert "by jove" in ann.surface_style_features
        assert "old top" in ann.surface_style_features
        assert "right-o" in ann.surface_style_features
        # But because there is no true structural tension, confidence should be low
        assert ann.confidence < 0.70
        assert ann.review_status == ReviewStatus.FLAGGED_LOW_CONFIDENCE


class TestContrastPurityValidator:
    def test_accepts_pure_contrast_pair(self):
        validator = ContrastPurityValidator()
        prompt = "Bertie faces crisis with Jeeves in the drawing room."
        chosen = (
            'Bertie paced the drawing room, clearing his throat with nervous delicacy. '
            '"It would appear, Jeeves, that disaster looms regarding the letter."\n\n'
            '"Indeed, sir?" observed Jeeves quietly, setting down the tea-tray. '
            '"The contingency offers ample scope for fortitude."'
        )
        rejected = (
            'Bertie paced the drawing room, waving his hands about frantically. '
            '"It is so hilarious because we are in complete disaster regarding the letter! '
            'How comical that the entire plan failed! What a ridiculous catastrophe!"\n\n'
            '"Indeed, sir," observed Jeeves, "it is laughable because you look absurd."'
        )

        report = validator.validate(
            prompt=prompt,
            chosen=chosen,
            rejected=rejected,
            target_dimension=ContrastDimension.COMEDIC_RESTRAINT,
        )
        assert report.purity_score >= 0.85
        assert report.target_dimension_changed is True

    def test_rejects_character_and_setting_drift(self):
        validator = ContrastPurityValidator()
        prompt = "Bertie faces crisis."
        chosen = 'Bertie sighed in the drawing room. "Alas, Jeeves."'
        rejected = 'Lord Emsworth wandered into the garden searching for Empress.'

        report = validator.validate(
            prompt=prompt,
            chosen=chosen,
            rejected=rejected,
            target_dimension=ContrastDimension.COMEDIC_RESTRAINT,
        )
        assert report.purity_score < 0.85
        assert report.characters_same is False
        assert report.rejection_reason is not None


class TestCraftOperationBuilder:
    def test_builds_all_five_operation_tasks(self):
        builder = CraftOperationBuilder()
        text = (
            'Bertie stared at the telegram. "Jeeves," he said, "disaster has arrived." '
            '"I am grieved to hear it, sir," said Jeeves impassively.'
        )
        facts = StoryFacts(characters=["Bertie", "Jeeves"], location="drawing room", dialogue_ratio=0.5, turn_count=2)
        craft = CraftAnnotation(
            primary_mechanism=ComicMechanism.STATUS_REVERSAL,
            secondary_mechanisms=[ComicMechanism.DEADPAN_REACTION],
            detector_confidence=0.88,
            linguistic_craft_score=0.82,
            tone=ComedicTone.DRY_WIT,
            setup_summary="Bertie reads telegram",
            escalation_summary="Bertie appeals to valet",
            reversal_summary="Jeeves maintains calm",
            payoff_summary="Deadpan acknowledgment",
        )

        tasks = builder.build_operations(text, facts, craft)
        assert len(tasks) == 5
        task_types = {t.task_type for t in tasks}
        assert TaskType.IDENTIFY_MECHANISM in task_types
        assert TaskType.EXTRACT_STRUCTURE in task_types
        assert TaskType.REWRITE_RESTRAINT in task_types
        assert TaskType.CONTINUE_TENSION in task_types
        assert TaskType.GENERATE_FROM_STRUCTURE in task_types


class TestAnnotationCalibrationReport:
    def test_generate_review_sheet_and_calculate_agreement(self):
        from dataset_generator.annotation_calibration_report import AnnotationCalibrationReport
        dummy_records = [
            {
                "source": {
                    "source_id": "jeeves_ch1_001",
                    "source_book": "My Man Jeeves",
                    "chapter_index": 1,
                    "source_text": '"Indeed, sir?" observed Jeeves.',
                },
                "facts": {"characters": ["Jeeves"], "dialogue_ratio": 0.8},
                "craft": {
                    "primary_mechanism": "STATUS_REVERSAL",
                    "secondary_mechanisms": ["DEADPAN_REACTION"],
                    "detector_confidence": 0.95,
                    "linguistic_craft_score": 0.85,
                    "tone": "DRY_WIT",
                    "setup_summary": "Initial setup",
                    "escalation_summary": "Tension rises",
                    "reversal_summary": "Reversal occurs",
                    "payoff_summary": "Payoff beat lands",
                },
            }
        ]

        calibrator = AnnotationCalibrationReport(dummy_records)
        md = calibrator.generate_review_sheet_md()
        assert "Comedy Craft Annotation Calibration Sheet" in md
        assert "jeeves_ch1_001" in md
        assert "HUMAN PRIMARY MECHANISM" in md

        json_sheet = calibrator.generate_review_sheet_json()
        assert len(json_sheet) == 1
        assert json_sheet[0]["source_id"] == "jeeves_ch1_001"
        assert json_sheet[0]["human_audit"]["verdict"] is None

        # Simulate human completed audit
        json_sheet[0]["human_audit"]["verdict"] = "AGREE"
        json_sheet[0]["human_audit"]["human_primary_mechanism"] = "STATUS_REVERSAL"
        json_sheet[0]["human_audit"]["setup_accurate"] = True
        json_sheet[0]["human_audit"]["escalation_accurate"] = True
        json_sheet[0]["human_audit"]["reversal_accurate"] = True
        json_sheet[0]["human_audit"]["payoff_accurate"] = True

        metrics = AnnotationCalibrationReport.calculate_agreement_metrics(json_sheet)
        assert metrics["total_audited"] == 1
        assert metrics["mechanism_agreement_pct"] == 100.0
        assert metrics["setup_agreement_pct"] == 100.0


class TestComedyCraftPipeline:
    def test_stratified_subset_selection(self, tmp_path):
        pipeline = ComedyCraftPipeline(random_seed=42)

        # Create dummy jsonl with varying mechanisms
        jsonl_file = tmp_path / "dummy_train.jsonl"
        items = []
        books = ["My Man Jeeves", "Three Men in a Boat", "The Diary of a Nobody"]
        for i in range(40):
            book = books[i % len(books)]
            text = (
                f'Chapter {i}. Bertie was pacing in agitation. "Look here, Jeeves, you thought I meant '
                f'something entirely different!" said Bertie. "On the contrary, sir," submitted Jeeves '
                f'respectfully, "I understood perfectly that the telegram was urgent."'
            )
            items.append({
                "output": text,
                "source_book": book,
                "chapter_index": (i % 5) + 1,
            })

        with open(jsonl_file, "w", encoding="utf-8") as f:
            for item in items:
                f.write(json.dumps(item) + "\n")

        records, stats = pipeline.build_from_jsonl(jsonl_file, max_records=10, stratified=True)
        assert len(records) == 10
        assert stats["total_selected"] == 10
        assert stats["source_examples_scanned"] == 40
        assert len(stats["source_book_distribution"]) > 1

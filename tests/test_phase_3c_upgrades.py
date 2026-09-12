"""
Phase 3C Regression Test Suite: Deduplication, Eligibility Gating, Refined Detectors, and Stratification.
"""

import json
from pathlib import Path
import pytest

from dataset_generator.taxonomy import (
    ComicMechanism,
    CraftPresence,
    CraftStratum,
    StoryFacts,
)
from dataset_generator.deduplicator import NormalizedTextDeduplicator
from dataset_generator.craft_filter import ComedyCraftEligibilityGate
from dataset_generator.craft_annotator import ComedyCraftAnnotator
from dataset_generator.comedy_craft_builder import ComedyCraftPipeline


FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "comedy_craft_calibration_v1.json"


class TestNormalizedTextDeduplicator:
    def test_exact_deduplication(self):
        dedup = NormalizedTextDeduplicator()
        text_a = 'Bertie gasped: "By Jove, Jeeves, you have saved the day!"'
        text_b = 'bertie gasped: "by jove, jeeves, you have saved the day!"'

        is_dup_a, canon_a = dedup.check_and_register(text_a, "scene_001")
        assert is_dup_a is False
        assert canon_a is None

        is_dup_b, canon_b = dedup.check_and_register(text_b, "scene_002")
        assert is_dup_b is True
        assert canon_b == "scene_001"

    def test_near_duplicate_detection(self):
        dedup = NormalizedTextDeduplicator(similarity_threshold=0.80)
        text_base = (
            "The market opened quietly, as financial papers put it when everything has gone to "
            "complete disaster and nobody wants to buy shares. We sat in the drawing room waiting "
            "for someone to make an offer, but the silence remained unbroken."
        )
        text_variant = (
            "The market opened quietly, as the financial papers put it when everything has gone to "
            "complete disaster and nobody wants to buy any shares. We sat in the drawing room, waiting "
            "for someone to make an offer, but the silence was unbroken."
        )
        is_dup1, _ = dedup.check_and_register(text_base, "base_001")
        assert is_dup1 is False

        is_dup2, canon2 = dedup.check_and_register(text_variant, "variant_002")
        assert is_dup2 is True
        assert canon2 == "base_001"

    def test_distinct_passages_not_deduplicated(self):
        dedup = NormalizedTextDeduplicator()
        text_1 = "Flannery counted sixty guinea pigs inside the express office cage."
        text_2 = "Jeeves shimmered into the room bearing a small silver salver with the morning mail."
        is_dup1, _ = dedup.check_and_register(text_1, "id_1")
        is_dup2, _ = dedup.check_and_register(text_2, "id_2")
        assert is_dup1 is False
        assert is_dup2 is False


class TestComedyCraftEligibilityGate:
    def setup_method(self):
        self.gate = ComedyCraftEligibilityGate()

    def test_rejects_genuine_drama_and_murder(self):
        murder_text = (
            "He screamed in agony as the dagger plunged into his chest. Blood poured across the floor "
            "and his pale, trembling hands reached out in blind despair before he collapsed as a lifeless corpse."
        )
        facts = StoryFacts(characters=["Victim", "Assassin"], dialogue_ratio=0.0, turn_count=0)
        presence, scores, reason = self.gate.evaluate(murder_text, facts)
        assert presence == CraftPresence.NO
        assert scores["serious_drama_signal"] > 0.40

    def test_rejects_academic_historical_citations(self):
        citation_text = (
            "In the parliamentary report of 1894 (vol. iv, pp. 24-29), archival evidence demonstrates "
            "that historians agree on the statute. The manuscript notes from the reign of Henry VII confirm this."
        )
        facts = StoryFacts(characters=[], dialogue_ratio=0.0, turn_count=0)
        presence, scores, reason = self.gate.evaluate(citation_text, facts)
        assert presence == CraftPresence.NO

    def test_passes_high_comedic_signal_scenes(self):
        comic_text = (
            '"Pigs is pigs," said Flannery doggedly, looking at the cage of guinea pigs. '
            '"The rule says eight cents a pig, and whether they be domestic or whether they be wild, '
            'pigs they remain in the eyes of the express company."'
        )
        facts = StoryFacts(characters=["Flannery", "Customer"], dialogue_ratio=0.60, turn_count=2)
        presence, scores, reason = self.gate.evaluate(comic_text, facts)
        assert presence == CraftPresence.YES
        assert scores["comedic_signal"] >= 0.50


class TestRefinedMechanismDetectors:
    def setup_method(self):
        self.annotator = ComedyCraftAnnotator()

    def test_escalation_detected_on_compounding_stakes_not_turn_count(self):
        # Guinea pig escalation
        escalation_text = (
            '"The trouble has compounded, sir," observed the clerk. "There were two guinea pigs yesterday, '
            'there are forty today, and by next week there will be hundreds! Furthermore, we have fresh complications '
            'regarding the food bill, which has multiplied until it exceeds the value of an elephant!"'
        )
        facts = StoryFacts(characters=["Clerk", "Agent"], dialogue_ratio=0.70, turn_count=3)
        ann = self.annotator.annotate(escalation_text, facts)
        assert ann.primary_mechanism == ComicMechanism.ESCALATION

    def test_deadpan_reaction_detected(self):
        deadpan_text = (
            '"The entire roof has collapsed and Aunt Agatha is demanding your head on a charger," I cried. '
            '"Indeed, sir?" observed Jeeves drily, without emotion. "I shall venture to prepare a soothing tisane."'
        )
        facts = StoryFacts(characters=["Bertie", "Jeeves"], dialogue_ratio=0.80, turn_count=2)
        ann = self.annotator.annotate(deadpan_text, facts)
        assert ann.primary_mechanism == ComicMechanism.DEADPAN_REACTION

    def test_dialogue_subtext_requires_polite_tension(self):
        subtext_text = (
            '"How delightful of you to drop in," she said sweetly with a strained polite smile, '
            'her eyes flashing coldly as she guarded her teacup like a fortress against an invader.'
        )
        facts = StoryFacts(characters=["Hostess", "Guest"], dialogue_ratio=0.45, turn_count=2)
        ann = self.annotator.annotate(subtext_text, facts)
        assert ann.primary_mechanism == ComicMechanism.DIALOGUE_SUBTEXT

    def test_status_reversal_requires_role_inversion(self):
        reversal_text = (
            '"Look here, Jeeves," I said, feeling utterly helpless at his mercy. "I leave the entire scheme '
            'in your hands." "I am gratified to hear it, sir," submitted the valet, taking complete charge.'
        )
        facts = StoryFacts(characters=["Bertie", "Jeeves"], dialogue_ratio=0.75, turn_count=2)
        ann = self.annotator.annotate(reversal_text, facts)
        assert ann.primary_mechanism == ComicMechanism.STATUS_REVERSAL


class TestCalibrationRegressionSuite:
    """Runs hard regression tests against the historical 50-example calibration fixture."""

    @pytest.fixture(autouse=True)
    def load_fixture(self):
        if not FIXTURE_PATH.exists():
            pytest.skip("Calibration fixture not found")
        with open(FIXTURE_PATH, "r", encoding="utf-8") as f:
            self.fixtures = json.load(f)

    def test_hard_rejection_of_non_comedy_examples(self):
        """Hard requirement: Known non-comedy items (Item 9, 21, 24, 26, 42, 45) must be rejected."""
        non_comic_items = [9, 21, 24, 26, 42, 45]
        pipeline = ComedyCraftPipeline(random_seed=42)

        for fix in self.fixtures:
            idx = fix["item_index"]
            if idx in non_comic_items:
                raw_item = {
                    "output": fix["source_text"],
                    "source_book": "Test Book",
                    "chapter_index": 1,
                }
                rec = pipeline.process_raw_example(raw_item, idx)
                assert rec is not None
                # Must be rejected by stratum or craft presence
                assert rec.craft.craft_stratum == CraftStratum.REJECT or rec.craft.craft_presence != CraftPresence.YES, (
                    f"Item {idx} should have been rejected from comedy craft training!"
                )

    def test_hard_detection_of_duplicate_pairs(self):
        """Hard requirement: Duplicate items (7, 13, 18, 32, 41, 47) must be flagged as duplicates."""
        pipeline = ComedyCraftPipeline(random_seed=42)

        # Process all 50 in sequential order
        processed = []
        for fix in self.fixtures:
            idx = fix["item_index"]
            raw_item = {
                "output": fix["source_text"],
                "source_book": f"Book_{idx}",
                "chapter_index": 1,
            }
            rec = pipeline.process_raw_example(raw_item, idx)
            processed.append((idx, rec))

        dup_indices = {7, 13, 18, 32, 41, 47}
        for idx, rec in processed:
            if idx in dup_indices:
                assert rec.craft.is_duplicate is True, f"Item {idx} was not detected as a duplicate!"
                assert rec.craft.craft_stratum == CraftStratum.REJECT

    def test_flagship_escalation_exemplar(self):
        """Soft/Hard requirement: Item 37 (guinea pig expansion) must be accepted with ESCALATION primary."""
        item_37 = next(fix for fix in self.fixtures if fix["item_index"] == 37)
        pipeline = ComedyCraftPipeline(random_seed=42)
        raw_item = {
            "output": item_37["source_text"],
            "source_book": "The Little Nugget",
            "chapter_index": 1,
        }
        rec = pipeline.process_raw_example(raw_item, 37)
        assert rec is not None
        assert rec.craft.craft_presence == CraftPresence.YES
        assert rec.craft.primary_mechanism == ComicMechanism.ESCALATION

    def test_phase_3c_regression_benchmark_runner(self):
        """Validates that Phase3CRegressionBenchmark computes the canonical benchmark report with 0 failure cases."""
        from dataset_generator.phase_3c_benchmark import Phase3CRegressionBenchmark

        benchmark = Phase3CRegressionBenchmark()
        metrics = benchmark.run()
        report = benchmark.generate_report(metrics)

        assert metrics["total_items"] == 50
        assert metrics["duplicate_detection"]["exact_duplicates"] == 6
        assert metrics["comedic_presence"]["yes_precision"] == 100.0
        assert metrics["comedic_presence"]["partial_routing_pct"] == 100.0
        assert metrics["foundation_purity"]["false_positives"] == 0
        assert metrics["known_failure_cases"]["drama_to_comedy"] == 0
        assert metrics["known_failure_cases"]["action_to_physical"] == 0
        assert metrics["known_failure_cases"]["progression_to_escalation"] == 0
        assert "=== Phase 3C Regression ===" in report

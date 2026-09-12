"""
Unit & Regression Tests for Phase 3D.1 Sampling, Scopes, Provenance, and Gold Evaluation.
"""

import json
from pathlib import Path
import pytest

from dataset_generator.taxonomy import (
    AnnotationSource,
    ComicMechanism,
    CraftPresence,
    CraftStratum,
    MechanismHorizon,
    ReviewStatus,
    get_mechanism_horizon,
    CraftAnnotation,
    ComedyCraftRecord,
    SourcePassage,
    StoryFacts,
    HumanCraftAudit,
)
from dataset_generator.audit_sampler import AuditSampler
from dataset_generator.gold_audit_evaluator import GoldAuditEvaluator


class TestPhase3DSamplingAndScopes:
    """Validates Phase 3D.1 sampling diversity, mechanism horizons, and gold evaluation."""

    def test_mechanism_horizon_classification(self):
        """Ensures CALLBACK and DRAMATIC_IRONY are classified as LONG_HORIZON while others are LOCAL."""
        assert get_mechanism_horizon(ComicMechanism.CALLBACK) == MechanismHorizon.LONG_HORIZON
        assert get_mechanism_horizon(ComicMechanism.DRAMATIC_IRONY) == MechanismHorizon.LONG_HORIZON
        assert get_mechanism_horizon(ComicMechanism.ESCALATION) == MechanismHorizon.LOCAL
        assert get_mechanism_horizon(ComicMechanism.MISUNDERSTANDING) == MechanismHorizon.LOCAL
        assert get_mechanism_horizon(ComicMechanism.STATUS_REVERSAL) == MechanismHorizon.LOCAL
        assert get_mechanism_horizon(ComicMechanism.DEADPAN_REACTION) == MechanismHorizon.LOCAL
        assert get_mechanism_horizon(ComicMechanism.SOCIAL_EMBARRASSMENT) == MechanismHorizon.LOCAL
        assert get_mechanism_horizon(ComicMechanism.VERBAL_WIT) == MechanismHorizon.LOCAL
        assert get_mechanism_horizon(ComicMechanism.PHYSICAL_COMPLICATION) == MechanismHorizon.LOCAL
        assert get_mechanism_horizon(ComicMechanism.DIALOGUE_SUBTEXT) == MechanismHorizon.LOCAL

    def test_annotation_provenance_tracking(self):
        """Ensures annotation_source is correctly preserved and serialized across craft and unified records."""
        craft = CraftAnnotation(
            primary_mechanism=ComicMechanism.ESCALATION,
            source=AnnotationSource.AUTOMATED,
        )
        assert craft.source == AnnotationSource.AUTOMATED
        assert craft.to_dict()["annotation_source"] == "AUTOMATED"

        # Round-trip deserialization
        restored = CraftAnnotation.from_dict(craft.to_dict())
        assert restored.source == AnnotationSource.AUTOMATED

        # Human reviewed provenance
        craft_human = CraftAnnotation(
            primary_mechanism=ComicMechanism.DEADPAN_REACTION,
            source=AnnotationSource.HUMAN_REVIEWED,
        )
        assert craft_human.source == AnnotationSource.HUMAN_REVIEWED
        assert craft_human.to_dict()["annotation_source"] == "HUMAN_REVIEWED"

    def test_human_craft_audit_dataclass(self):
        """Validates HumanCraftAudit independent schema serialization."""
        audit = HumanCraftAudit(
            craft_presence=CraftPresence.YES,
            craft_stratum=CraftStratum.PURE_MECHANISM,
            primary_mechanism=ComicMechanism.ESCALATION,
            secondary_mechanisms=[ComicMechanism.DEADPAN_REACTION],
            mechanism_horizon=MechanismHorizon.LOCAL,
            literary_quality=9,
            craft_clarity=8,
            training_value=10,
            keep_verdict="KEEP",
            detector_primary="MISUNDERSTANDING",
            detector_correct=False,
            notes="Detector defaulted to MISUNDERSTANDING, but actual craft is compounding escalation.",
        )
        d = audit.to_dict()
        assert d["craft_presence"] == "YES"
        assert d["primary_mechanism"] == "ESCALATION"
        assert d["craft_clarity"] == 8
        assert d["detector_correct"] is False

        restored = HumanCraftAudit.from_dict(d)
        assert restored.primary_mechanism == ComicMechanism.ESCALATION
        assert restored.craft_clarity == 8
        assert restored.training_value == 10

    def test_audit_batch_file_integrity(self):
        """Validates the generated 180-sample audit batch JSON structure."""
        batch_path = Path("reports/comedy_craft_audit_batch_180.json")
        assert batch_path.exists(), "Audit batch JSON file was not found!"

        with open(batch_path, "r", encoding="utf-8") as f:
            records = json.load(f)

        assert len(records) == 180

        # Pool counts
        pool_counts = {}
        for r in records:
            p = r["sample_pool"]
            pool_counts[p] = pool_counts.get(p, 0) + 1

        assert pool_counts["FOUNDATION"] == 15
        assert pool_counts["COMPOSITE"] == 60
        assert pool_counts["PARTIAL"] == 80
        assert pool_counts["NO_CONTROL"] == 25

        # Source work diversity (at least 15 distinct works)
        distinct_books = {r["source_book"] for r in records}
        assert len(distinct_books) >= 15

        # Check structure of first item
        item = records[0]
        assert "audit_id" in item
        assert "source_text" in item
        assert "detector_prediction" in item
        assert "human_audit" in item
        assert item["human_audit"]["craft_presence"] in ("YES", "NO", "PARTIAL", "UNREVIEWED")

    def test_gold_audit_evaluator_unreviewed(self, tmp_path):
        """Tests that unreviewed batch produces semantically correct N/A metrics without division errors."""
        unreviewed_file = tmp_path / "unreviewed_batch.json"
        unreviewed_records = [
            {
                "audit_id": f"audit_{i:03d}",
                "sample_pool": "FOUNDATION" if i < 15 else "COMPOSITE",
                "detector_prediction": {"primary_mechanism": "ESCALATION"},
                "human_audit": {"craft_presence": "UNREVIEWED"},
            }
            for i in range(1, 181)
        ]
        with open(unreviewed_file, "w", encoding="utf-8") as f:
            json.dump(unreviewed_records, f)

        evaluator = GoldAuditEvaluator(audit_file=unreviewed_file)
        metrics = evaluator.evaluate()
        assert metrics["total_records"] == 180
        assert metrics["audited_records"] == 0
        assert metrics["is_complete"] is False
        assert metrics["gate_evaluation"]["yes_precision_pct"] is None
        assert metrics["gate_evaluation"]["false_negative_rate_pct"] is None
        assert metrics["stratum_purity"]["foundation_purity_pct"] is None

    def test_gold_audit_evaluator_live_batch_runs(self):
        """Tests that live audit batch evaluates cleanly with current progress."""
        evaluator = GoldAuditEvaluator(audit_file=Path("reports/comedy_craft_audit_batch_180.json"))
        metrics = evaluator.evaluate()
        assert metrics["total_records"] == 180
        assert metrics["audited_records"] >= 0

    def test_gold_audit_evaluator_with_mock_judgments(self, tmp_path):
        """Tests evaluation calculations and dataset partitioning against simulated human audit data."""
        mock_records = [
            {
                "audit_id": "audit_001",
                "sample_pool": "FOUNDATION",
                "detector_prediction": {"primary_mechanism": "ESCALATION"},
                "human_audit": {
                    "craft_presence": "YES",
                    "craft_stratum": "PURE_MECHANISM",
                    "primary_mechanism": "ESCALATION",
                    "secondary_mechanisms": [],
                    "mechanism_horizon": "LOCAL",
                    "keep_verdict": "KEEP",
                    "detector_correct": True,
                },
            },
            {
                "audit_id": "audit_002",
                "sample_pool": "COMPOSITE",
                "detector_prediction": {"primary_mechanism": "MISUNDERSTANDING"},
                "human_audit": {
                    "craft_presence": "YES",
                    "craft_stratum": "COMPOSITE_CRAFT",
                    "primary_mechanism": "STATUS_REVERSAL",
                    "secondary_mechanisms": ["DEADPAN_REACTION"],
                    "mechanism_horizon": "LOCAL",
                    "keep_verdict": "KEEP",
                    "detector_correct": False,
                },
            },
            {
                "audit_id": "audit_003",
                "sample_pool": "PARTIAL",
                "detector_prediction": {"primary_mechanism": "MISUNDERSTANDING"},
                "human_audit": {
                    "craft_presence": "YES",
                    "craft_stratum": "COMPOSITE_CRAFT",
                    "primary_mechanism": "VERBAL_WIT",
                    "secondary_mechanisms": [],
                    "mechanism_horizon": "LOCAL",
                    "keep_verdict": "KEEP",
                    "detector_correct": False,
                },
            },
            {
                "audit_id": "audit_004",
                "sample_pool": "NO_CONTROL",
                "detector_prediction": {"primary_mechanism": "MISUNDERSTANDING"},
                "human_audit": {
                    "craft_presence": "NO",
                    "craft_stratum": "REJECT",
                    "primary_mechanism": None,
                    "secondary_mechanisms": [],
                    "mechanism_horizon": "LOCAL",
                    "keep_verdict": "REJECT",
                    "detector_correct": True,
                },
            },
        ]

        mock_file = tmp_path / "mock_audit.json"
        with open(mock_file, "w", encoding="utf-8") as f:
            json.dump(mock_records, f)

        evaluator = GoldAuditEvaluator(audit_file=mock_file)
        metrics = evaluator.evaluate()

        assert metrics["total_records"] == 4
        assert metrics["audited_records"] == 4
        assert metrics["is_complete"] is True
        assert metrics["gate_evaluation"]["yes_precision_pct"] == 100.0  # 2/2 in YES sample are true comedy
        assert metrics["gate_evaluation"]["false_negative_rate_pct"] == 0.0  # 0/1 false negatives in NO control
        assert metrics["gate_evaluation"]["rescue_rate_pct"] == 100.0  # 1/1 rescued in PARTIAL
        assert metrics["stratum_purity"]["foundation_purity_pct"] == 100.0  # 1/1 pure confirmed
        assert metrics["mechanism_performance"]["accuracy_pct"] == 33.3  # 1/3 correct on comedy

        # Test partitioning
        out_dir = tmp_path / "gold_out"
        partitions = evaluator.partition_gold_datasets(output_dir=out_dir)
        assert partitions["PURE"] == 1
        assert partitions["COMPOSITE"] == 2
        assert partitions["REJECT"] == 1
        assert (out_dir / "comedy_gold_pure.jsonl").exists()
        assert (out_dir / "comedy_gold_composite.jsonl").exists()
        assert (out_dir / "comedy_gold_reject.jsonl").exists()

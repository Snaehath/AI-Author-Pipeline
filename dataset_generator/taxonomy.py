"""
Comedy Craft Taxonomy and Data Schemas.

Defines the multi-tier taxonomy for analyzing, annotating, and operating upon
classic comic fiction / social farce mechanisms.
"""

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Dict, List, Optional


class ComicMechanism(str, Enum):
    """Core comedic machinery that drives comedic tension and resolution."""
    MISUNDERSTANDING = "MISUNDERSTANDING"
    STATUS_REVERSAL = "STATUS_REVERSAL"
    ESCALATION = "ESCALATION"
    DEADPAN_REACTION = "DEADPAN_REACTION"
    SOCIAL_EMBARRASSMENT = "SOCIAL_EMBARRASSMENT"
    VERBAL_WIT = "VERBAL_WIT"
    DRAMATIC_IRONY = "DRAMATIC_IRONY"
    DIALOGUE_SUBTEXT = "DIALOGUE_SUBTEXT"
    CALLBACK = "CALLBACK"
    PHYSICAL_COMPLICATION = "PHYSICAL_COMPLICATION"


class SceneFunction(str, Enum):
    """Narrative function of the comedic scene."""
    SOCIAL_CONFLICT = "SOCIAL_CONFLICT"
    SCHEME_EXECUTION = "SCHEME_EXECUTION"
    AWKWARD_ENCOUNTER = "AWKWARD_ENCOUNTER"
    CRISIS_RESOLUTION = "CRISIS_RESOLUTION"
    EXPOSITION_CONCEALED = "EXPOSITION_CONCEALED"
    AFTERMATH = "AFTERMATH"


class ComedicTone(str, Enum):
    """Prevailing tonal register of the passage."""
    DEADPAN = "DEADPAN"
    FARCE = "FARCE"
    LIGHT_SATIRICAL = "LIGHT_SATIRICAL"
    DRY_WIT = "DRY_WIT"
    DOMESTIC_ABSURDITY = "DOMESTIC_ABSURDITY"


class AnnotationSource(str, Enum):
    """Provenance of the annotation."""
    DETERMINISTIC = "DETERMINISTIC"
    HEURISTIC = "HEURISTIC"
    MODEL_ASSISTED = "MODEL_ASSISTED"
    HUMAN_VERIFIED = "HUMAN_VERIFIED"


class ReviewStatus(str, Enum):
    """Confidence and audit status for human review."""
    UNREVIEWED = "UNREVIEWED"
    VERIFIED = "VERIFIED"
    FLAGGED_LOW_CONFIDENCE = "FLAGGED_LOW_CONFIDENCE"
    REJECTED = "REJECTED"


class ContrastDimension(str, Enum):
    """The single craft dimension manipulated in controlled DPO pairs."""
    COMEDIC_RESTRAINT = "COMEDIC_RESTRAINT"
    DIALOGUE_SUBTEXT = "DIALOGUE_SUBTEXT"
    PACING_AND_TIMING = "PACING_AND_TIMING"
    STATUS_DYNAMIC = "STATUS_DYNAMIC"


class TaskType(str, Enum):
    """Types of craft operations the model learns to perform."""
    IDENTIFY_MECHANISM = "IDENTIFY_MECHANISM"
    EXTRACT_STRUCTURE = "EXTRACT_STRUCTURE"
    REWRITE_RESTRAINT = "REWRITE_RESTRAINT"
    CONTINUE_TENSION = "CONTINUE_TENSION"
    GENERATE_FROM_STRUCTURE = "GENERATE_FROM_STRUCTURE"


@dataclass
class SourcePassage:
    """Source reference anchoring the annotation directly to original text."""
    source_id: str
    source_book: str
    chapter_index: int
    source_text: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SourcePassage":
        return cls(**data)


@dataclass
class StoryFacts:
    """Level 1 Objective Factual Analysis: What is literally present in the text."""
    characters: List[str] = field(default_factory=list)
    location: str = "unknown"
    objects: List[str] = field(default_factory=list)
    character_goals: Dict[str, str] = field(default_factory=dict)
    dialogue_ratio: float = 0.0
    turn_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StoryFacts":
        return cls(**data)


class DisagreementCategory(str, Enum):
    """Categorization of audit disagreements to guide detector/taxonomy refinement."""
    A_DETECTOR_FAILURE = "A_DETECTOR_FAILURE"
    B_TAXONOMY_AMBIGUITY = "B_TAXONOMY_AMBIGUITY"
    C_HUMAN_DISAGREEMENT = "C_HUMAN_DISAGREEMENT"
    D_SOURCE_AMBIGUITY = "D_SOURCE_AMBIGUITY"
    E_COMPETING_MECHANISMS = "E_COMPETING_MECHANISMS"
    F_REJECT_EXAMPLE = "F_REJECT_EXAMPLE"


@dataclass
class CraftAnnotation:
    """Level 2 Craft Annotation: Why does the scene work structurally and comedically."""
    primary_mechanism: ComicMechanism
    secondary_mechanisms: List[ComicMechanism] = field(default_factory=list)
    confidence_scores: Dict[str, float] = field(default_factory=dict)
    detector_confidence: float = 0.0  # Heuristic / automated pattern match certainty [0.0, 1.0]
    human_confidence: Optional[float] = None  # Expert human confidence after review [0.0, 1.0]
    linguistic_craft_score: float = 0.0  # Automated syntactic, rhythm, and dialogue balance metric [0.0, 1.0]
    human_literary_quality: Optional[float] = None  # Literary execution quality [1 - 10]
    human_training_value: Optional[float] = None  # Transferable comedic training value [1 - 10]
    human_disagreement_category: Optional[DisagreementCategory] = None
    scene_function: SceneFunction = SceneFunction.SOCIAL_CONFLICT
    tone: ComedicTone = ComedicTone.DRY_WIT
    setup_summary: str = ""
    escalation_summary: str = ""
    reversal_summary: str = ""
    payoff_summary: str = ""
    surface_style_features: List[str] = field(default_factory=list)  # Period slang decoupled from craft
    source: AnnotationSource = AnnotationSource.HEURISTIC
    review_status: ReviewStatus = ReviewStatus.UNREVIEWED
    confidence: Optional[float] = None  # Alias kwarg support
    quality_score: Optional[float] = None  # Alias kwarg support

    def __post_init__(self):
        if self.confidence is not None and self.detector_confidence == 0.0:
            self.detector_confidence = self.confidence
        elif self.confidence is None:
            self.confidence = self.detector_confidence

        if self.quality_score is not None and self.linguistic_craft_score == 0.0:
            self.linguistic_craft_score = self.quality_score
        elif self.quality_score is None:
            self.quality_score = self.linguistic_craft_score

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["primary_mechanism"] = self.primary_mechanism.value
        d["secondary_mechanisms"] = [m.value for m in self.secondary_mechanisms]
        d["scene_function"] = self.scene_function.value
        d["tone"] = self.tone.value
        d["source"] = self.source.value
        d["review_status"] = self.review_status.value
        # Include aliases for backward-compatibility with existing code
        d["confidence"] = self.detector_confidence
        d["quality_score"] = self.linguistic_craft_score
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CraftAnnotation":
        data_copy = dict(data)
        data_copy["primary_mechanism"] = ComicMechanism(data_copy["primary_mechanism"])
        data_copy["secondary_mechanisms"] = [ComicMechanism(m) for m in data_copy.get("secondary_mechanisms", [])]
        data_copy["scene_function"] = SceneFunction(data_copy.get("scene_function", SceneFunction.SOCIAL_CONFLICT.value))
        data_copy["tone"] = ComedicTone(data_copy.get("tone", ComedicTone.DRY_WIT.value))
        data_copy["source"] = AnnotationSource(data_copy.get("source", AnnotationSource.HEURISTIC.value))
        data_copy["review_status"] = ReviewStatus(data_copy.get("review_status", ReviewStatus.UNREVIEWED.value))
        
        # Support both new and legacy field names
        if "detector_confidence" not in data_copy and "confidence" in data_copy:
            data_copy["detector_confidence"] = data_copy["confidence"]
        if "linguistic_craft_score" not in data_copy and "quality_score" in data_copy:
            data_copy["linguistic_craft_score"] = data_copy["quality_score"]
        
        # Clean temporary aliases before instantiation
        data_copy.pop("confidence", None)
        data_copy.pop("quality_score", None)
        return cls(**data_copy)


@dataclass
class CraftOperationTask:
    """Level 3 Writing Operation: Explicit prompt-response pair teaching manipulation of comedy."""
    task_type: TaskType
    prompt: str
    expected_output: str
    target_concept: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["task_type"] = self.task_type.value
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CraftOperationTask":
        data_copy = dict(data)
        data_copy["task_type"] = TaskType(data_copy["task_type"])
        return cls(**data_copy)


@dataclass
class ContrastPurityReport:
    """Validator report measuring single-dimension contrast purity for DPO pairs."""
    prompt_identical: bool
    plot_events_same: bool
    characters_same: bool
    setting_same: bool
    target_dimension_changed: bool
    purity_score: float  # [0.0, 1.0]
    rejection_reason: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ContrastPurityReport":
        return cls(**data)


@dataclass
class ControlledDPOPair:
    """Level 4 Controlled DPO Pair with audited contrast purity and preference strength."""
    prompt: str
    chosen: str
    rejected: str
    target_dimension: ContrastDimension
    purity_report: ContrastPurityReport
    preference_strength: float = 0.85  # Qualitative contrast magnitude [0.0, 1.0]
    human_verified: bool = False

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["target_dimension"] = self.target_dimension.value
        d["purity_report"] = self.purity_report.to_dict()
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ControlledDPOPair":
        data_copy = dict(data)
        data_copy["target_dimension"] = ContrastDimension(data_copy["target_dimension"])
        data_copy["purity_report"] = ContrastPurityReport.from_dict(data_copy["purity_report"])
        return cls(**data_copy)


@dataclass
class OriginalityMetrics:
    """Evaluation dimensions to ensure genre mastery without author mimicry."""
    genre_fit: float = 0.0
    craft_quality: float = 0.0
    character_originality: float = 0.0
    situation_originality: float = 0.0
    language_originality: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OriginalityMetrics":
        return cls(**data)


@dataclass
class ComedyCraftRecord:
    """
    Unified 4-tier schema preserving source, objective facts, craft analysis,
    and writing operations.
    """
    source: SourcePassage
    facts: StoryFacts
    craft: CraftAnnotation
    operations: List[CraftOperationTask] = field(default_factory=list)
    dpo_pair: Optional[ControlledDPOPair] = None
    originality: Optional[OriginalityMetrics] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source": self.source.to_dict(),
            "facts": self.facts.to_dict(),
            "craft": self.craft.to_dict(),
            "operations": [op.to_dict() for op in self.operations],
            "dpo_pair": self.dpo_pair.to_dict() if self.dpo_pair else None,
            "originality": self.originality.to_dict() if self.originality else None,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComedyCraftRecord":
        return cls(
            source=SourcePassage.from_dict(data["source"]),
            facts=StoryFacts.from_dict(data["facts"]),
            craft=CraftAnnotation.from_dict(data["craft"]),
            operations=[CraftOperationTask.from_dict(op) for op in data.get("operations", [])],
            dpo_pair=ControlledDPOPair.from_dict(data["dpo_pair"]) if data.get("dpo_pair") else None,
            originality=OriginalityMetrics.from_dict(data["originality"]) if data.get("originality") else None,
        )

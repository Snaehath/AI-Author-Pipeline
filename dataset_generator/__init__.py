"""
Dataset Generator Module for AI Author Studio.

Synthesizes extracted book knowledge into Supervised Fine-Tuning (SFT) datasets
covering core writing capabilities and multi-tier comedy craft mechanisms.
"""

import sys
from pathlib import Path

# Ensure ML root is on sys.path for AI_Author package resolution
_PKG_ROOT = Path(__file__).resolve().parent.parent
_ML_ROOT = _PKG_ROOT.parent
for _p in [str(_ML_ROOT), str(_PKG_ROOT)]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

from .prompt_templates import PromptTemplates
from .sft_synthesizer import SFTSynthesizer, SFTExample
from .dataset_pipeline import DatasetPipeline
from .taxonomy import (
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
from .factual_analyzer import FactualSceneAnalyzer
from .craft_annotator import ComedyCraftAnnotator
from .contrast_purity import ContrastPurityValidator
from .operation_builder import CraftOperationBuilder
from .comedy_craft_builder import ComedyCraftPipeline

__all__ = [
    "PromptTemplates",
    "SFTSynthesizer",
    "SFTExample",
    "DatasetPipeline",
    "ComicMechanism",
    "SceneFunction",
    "ComedicTone",
    "AnnotationSource",
    "ReviewStatus",
    "ContrastDimension",
    "TaskType",
    "SourcePassage",
    "StoryFacts",
    "CraftAnnotation",
    "CraftOperationTask",
    "ControlledDPOPair",
    "ContrastPurityReport",
    "ComedyCraftRecord",
    "FactualSceneAnalyzer",
    "ComedyCraftAnnotator",
    "ContrastPurityValidator",
    "CraftOperationBuilder",
    "ComedyCraftPipeline",
]


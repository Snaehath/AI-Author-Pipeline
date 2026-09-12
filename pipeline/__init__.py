"""
AI Author Pipeline Package.

Unified execution and processing modules:
- ingestion: Raw ebook loaders (.txt, .pdf, .epub, .docx)
- parser: Chapter, scene, paragraph, and dialogue parsers
- analyzer: Narrative, character, dialogue, emotion, and plot analysis
- editor: Manuscript editing, rules, and local server
- evaluator: Stylometric and literary metrics
- inference: Novel generation, blueprint planner, and critic engines
- trainer: QLoRA and DPO fine-tuning orchestrators
- experiments: Ablation benchmarks and runners
"""

__all__ = [
    "ingestion",
    "parser",
    "analyzer",
    "editor",
    "evaluator",
    "inference",
    "trainer",
    "experiments",
]

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ML_DIR = ROOT_DIR.parent
PIPELINE_DIR = ROOT_DIR / "pipeline"

for p in (ROOT_DIR, ML_DIR, PIPELINE_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import AI_Author  # Activates LegacyPipelineRedirectFinder

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ML_DIR = ROOT_DIR.parent

for p in (ROOT_DIR, ML_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

"""
AI Author Studio Root Package.

Narrative intelligence, continuity compilation, and comedy-craft synthesis.
"""

import sys
import importlib
import importlib.util
from importlib.abc import MetaPathFinder, Loader
from pathlib import Path

# Ensure ROOT and pipeline directory are in sys.path
ROOT_DIR = Path(__file__).resolve().parent
PIPELINE_DIR = ROOT_DIR / "pipeline"

for p in (ROOT_DIR, PIPELINE_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))


class _AliasingLoader(Loader):
    def __init__(self, real_loader, legacy_name: str, target_name: str):
        self.real_loader = real_loader
        self.legacy_name = legacy_name
        self.target_name = target_name

    def create_module(self, spec):
        if hasattr(self.real_loader, "create_module"):
            mod = self.real_loader.create_module(spec)
            if mod is not None:
                return mod
        return None

    def exec_module(self, module):
        # Register both the target name and the legacy name in sys.modules BEFORE execution
        sys.modules[self.legacy_name] = module
        sys.modules[self.target_name] = module
        
        # Also register bare legacy name if applicable (e.g., 'analyzer.pov_detector')
        parts = self.legacy_name.split(".", 1)
        if len(parts) > 1 and parts[0] == "AI_Author":
            sys.modules[parts[1]] = module

        self.real_loader.exec_module(module)


class LegacyPipelineRedirectFinder(MetaPathFinder):
    """Seamlessly redirects legacy `AI_Author.<module>` and `<module>` imports to `AI_Author.pipeline.<module>`."""

    _LEGACY = {
        "analyzer",
        "parser",
        "ingestion",
        "editor",
        "evaluator",
        "inference",
        "trainer",
        "experiments",
    }

    def find_spec(self, fullname: str, path, target=None):
        parts = fullname.split(".")
        target_name = None
        legacy_name = fullname

        if parts[0] == "AI_Author" and len(parts) > 1 and parts[1] in self._LEGACY:
            target_name = "AI_Author.pipeline." + ".".join(parts[1:])
        elif parts[0] in self._LEGACY:
            target_name = "AI_Author.pipeline." + fullname

        if target_name:
            try:
                real_spec = importlib.util.find_spec(target_name)
                if real_spec and real_spec.loader:
                    real_spec.loader = _AliasingLoader(real_spec.loader, legacy_name, target_name)
                    return real_spec
            except (ModuleNotFoundError, ValueError, AttributeError):
                return None
        return None


# Install finder at highest priority
sys.meta_path = [f for f in sys.meta_path if not isinstance(f, LegacyPipelineRedirectFinder)]
sys.meta_path.insert(0, LegacyPipelineRedirectFinder())

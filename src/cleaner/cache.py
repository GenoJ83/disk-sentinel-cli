import os
import shutil
from typing import List, Tuple

DEFAULT_PATTERNS = [".DS_Store", "__pycache__", ".pytest_cache", ".tmp", ".cache"]

class CacheCleaner:
    def __init__(self, patterns: List[str] = None):
        self.patterns = patterns or DEFAULT_PATTERNS
        
    def identify_targets(self, root_dir: str) -> List[Tuple[str, bool, int]]:
        """Returns list of (path, is_dir, size_bytes)."""
        targets = []
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for d in list(dirnames):
                if any(pat in d for pat in self.patterns):
                    full_d = os.path.join(dirpath, d)
                    targets.append((full_d, True, 0))
            for f in filenames:
                if any(pat in f for pat in self.patterns):
                    full_f = os.path.join(dirpath, f)
                    sz = os.path.getsize(full_f) if os.path.exists(full_f) else 0
                    targets.append((full_f, False, sz))
        return targets
        
    def purge(self, targets: List[Tuple[str, bool, int]], dry_run: bool = True) -> int:
        freed = 0
        for path, is_dir, sz in targets:
            freed += sz
            if not dry_run:
                try:
                    if is_dir and os.path.isdir(path):
                        shutil.rmtree(path)
                    elif os.path.isfile(path):
                        os.remove(path)
                except OSError:
                    pass
        return freed

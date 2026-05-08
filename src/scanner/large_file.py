import os
from typing import List, Tuple

def find_largest_files(root_dir: str, limit: int = 10) -> List[Tuple[str, int]]:
    files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                files.append((fp, os.path.getsize(fp)))
            except OSError:
                pass
    return sorted(files, key=lambda x: x[1], reverse=True)[:limit]

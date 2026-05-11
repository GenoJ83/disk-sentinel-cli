import os
from typing import List

def remove_empty_directories(root_dir: str, dry_run: bool = True) -> List[str]:
    empty_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if not dirnames and not filenames and dirpath != root_dir:
            empty_dirs.append(dirpath)
            if not dry_run:
                try: os.rmdir(dirpath)
                except OSError: pass
    return empty_dirs

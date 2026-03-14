from dataclasses import dataclass, field
from typing import Optional, List
import time

@dataclass
class FileNode:
    path: str
    size: int
    is_dir: bool
    modified_at: float = field(default_factory=time.time)
    children: List["FileNode"] = field(default_factory=list)
    
@dataclass
class DuplicateGroup:
    hash_digest: str
    total_size: int
    file_paths: List[str]
    wasted_bytes: int

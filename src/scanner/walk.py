import os
from typing import List, Optional
from src.core.models import FileNode

class DirectoryScanner:
    def __init__(self, max_depth: int = 10, skip_hidden: bool = True):
        self.max_depth = max_depth
        self.skip_hidden = skip_hidden
        
    def scan(self, root_dir: str, current_depth: int = 0) -> FileNode:
        if not os.path.exists(root_dir):
            raise FileNotFoundError(f"Path does not exist: {root_dir}")
            
        is_dir = os.path.isdir(root_dir)
        if not is_dir:
            stat = os.stat(root_dir)
            return FileNode(path=root_dir, size=stat.st_size, is_dir=False, modified_at=stat.st_mtime)
            
        node = FileNode(path=root_dir, size=0, is_dir=True)
        if current_depth > self.max_depth:
            return node
            
        total_size = 0
        try:
            entries = os.listdir(root_dir)
        except PermissionError:
            return node
            
        for entry in entries:
            if self.skip_hidden and entry.startswith("."):
                continue
            child_path = os.path.join(root_dir, entry)
            try:
                child_node = self.scan(child_path, current_depth + 1)
                node.children.append(child_node)
                total_size += child_node.size
            except OSError:
                pass
                
        node.size = total_size
        return node

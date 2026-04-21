from typing import List
from src.core.models import FileNode

class NodeFilter:
    def __init__(self, min_size: int = 0, extension: str = None):
        self.min_size = min_size
        self.extension = extension.lower() if extension else None
        
    def filter_nodes(self, nodes: List[FileNode]) -> List[FileNode]:
        res = []
        for n in nodes:
            if n.size < self.min_size:
                continue
            if self.extension and not n.path.lower().endswith(self.extension):
                continue
            res.append(n)
        return res

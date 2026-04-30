from typing import Dict, Any, List

class DirectoryTrie:
    def __init__(self):
        self.root: Dict[str, Any] = {}
        
    def insert(self, path: str, size: int) -> None:
        parts = [p for p in path.strip("/").split("/") if p]
        curr = self.root
        for p in parts:
            curr = curr.setdefault(p, {"_size": 0, "_children": {}})["_children"]

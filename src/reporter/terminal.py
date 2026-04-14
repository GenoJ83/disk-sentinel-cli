import os
from typing import List
from src.core.models import FileNode, DuplicateGroup
from src.utils.formatter import format_bytes

class TerminalReporter:
    @staticmethod
    def format_tree(node: FileNode, max_items: int = 5) -> str:
        lines = [f"{node.path} [{format_bytes(node.size)}]"]
        sorted_children = sorted(node.children, key=lambda x: x.size, reverse=True)[:max_items]
        for c in sorted_children:
            kind = "DIR" if c.is_dir else "FILE"
            lines.append(f"  └── [{kind}] {os.path.basename(c.path)}: {format_bytes(c.size)}")
        return "\n".join(lines)
        
    @staticmethod
    def format_duplicates(dupes: List[DuplicateGroup]) -> str:
        if not dupes:
            return "No duplicate files found."
        lines = [f"Found {len(dupes)} duplicate sets:"]
        for g in dupes[:5]:
            lines.append(f"- Hash {g.hash_digest[:8]}: {len(g.file_paths)} copies, wasted {format_bytes(g.wasted_bytes)}")
            for p in g.file_paths:
                lines.append(f"    • {p}")
        return "\n".join(lines)

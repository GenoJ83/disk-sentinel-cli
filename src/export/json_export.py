import json
from typing import Dict, Any, List
from src.core.models import FileNode, DuplicateGroup

class JsonExporter:
    @staticmethod
    def export_summary(root_node: FileNode, dupes: List[DuplicateGroup]) -> str:
        payload = {
            "root": root_node.path,
            "total_size": root_node.size,
            "duplicate_groups": len(dupes),
            "total_wasted_bytes": sum(d.wasted_bytes for d in dupes)
        }
        return json.dumps(payload, indent=2)

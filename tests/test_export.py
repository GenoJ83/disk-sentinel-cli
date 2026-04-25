import json
from src.export.json_export import JsonExporter
from src.core.models import FileNode, DuplicateGroup

def test_json_export():
    root = FileNode("/tmp", 10000, True)
    dg = DuplicateGroup("hash1", 500, ["/a", "/b"], 500)
    res = json.loads(JsonExporter.export_summary(root, [dg]))
    assert res["root"] == "/tmp"
    assert res["total_wasted_bytes"] == 500

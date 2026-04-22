from src.core.models import FileNode
from src.filter.criteria import NodeFilter

def test_node_filter():
    n1 = FileNode("/a.log", 500, False)
    n2 = FileNode("/b.txt", 5000, False)
    f = NodeFilter(min_size=1000, extension=".txt")
    matched = f.filter_nodes([n1, n2])
    assert len(matched) == 1 and matched[0].path == "/b.txt"

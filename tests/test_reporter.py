from src.core.models import FileNode, DuplicateGroup
from src.reporter.terminal import TerminalReporter

def test_reporter_formatting():
    node = FileNode(path="/root", size=2048, is_dir=True)
    c = FileNode(path="/root/test.txt", size=2048, is_dir=False)
    node.children.append(c)
    txt = TerminalReporter.format_tree(node)
    assert "/root" in txt
    assert "test.txt" in txt

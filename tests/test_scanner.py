import os
import tempfile
from src.scanner.walk import DirectoryScanner

def test_scanner_traversal():
    with tempfile.TemporaryDirectory() as tmp:
        f1 = os.path.join(tmp, "a.txt")
        with open(f1, "w") as f:
            f.write("hello world")
        sub = os.path.join(tmp, "sub")
        os.makedirs(sub)
        f2 = os.path.join(sub, "b.txt")
        with open(f2, "w") as f:
            f.write("1234567890")
            
        scanner = DirectoryScanner()
        node = scanner.scan(tmp)
        assert node.is_dir is True
        assert node.size == len("hello world") + len("1234567890")
        assert len(node.children) == 2

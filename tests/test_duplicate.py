import tempfile, os
from src.analyzer.duplicate import DuplicateFinder

def test_find_duplicates():
    with tempfile.TemporaryDirectory() as tmp:
        p1 = os.path.join(tmp, "file1.txt")
        p2 = os.path.join(tmp, "file2.txt")
        p3 = os.path.join(tmp, "unique.txt")
        with open(p1, "w") as f: f.write("duplicate content")
        with open(p2, "w") as f: f.write("duplicate content")
        with open(p3, "w") as f: f.write("different content")
        
        finder = DuplicateFinder()
        dupes = finder.find_duplicates([p1, p2, p3])
        assert len(dupes) == 1
        assert len(dupes[0].file_paths) == 2
        assert dupes[0].wasted_bytes == len("duplicate content")

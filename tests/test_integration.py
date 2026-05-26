import tempfile, os
from src.scanner.walk import DirectoryScanner
from src.analyzer.duplicate import DuplicateFinder
from src.reporter.terminal import TerminalReporter

def test_full_disk_sentinel_workflow():
    with tempfile.TemporaryDirectory() as tmp:
        p1 = os.path.join(tmp, "copy1.txt")
        p2 = os.path.join(tmp, "copy2.txt")
        with open(p1, "w") as f: f.write("same payload")
        with open(p2, "w") as f: f.write("same payload")
        scanner = DirectoryScanner()
        tree = scanner.scan(tmp)
        finder = DuplicateFinder()
        dupes = finder.find_duplicates([p1, p2])
        assert tree.size == len("same payload") * 2
        assert len(dupes) == 1
        summary = TerminalReporter.format_duplicates(dupes)
        assert "Found 1 duplicate sets" in summary

import tempfile, os
from src.scanner.large_file import find_largest_files

def test_large_files():
    with tempfile.TemporaryDirectory() as tmp:
        f1 = os.path.join(tmp, "small.txt")
        f2 = os.path.join(tmp, "big.txt")
        with open(f1, "w") as f: f.write("a" * 10)
        with open(f2, "w") as f: f.write("b" * 100)
        res = find_largest_files(tmp, limit=1)
        assert len(res) == 1 and res[0][0] == f2 and res[0][1] == 100

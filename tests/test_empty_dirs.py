import tempfile, os
from src.cleaner.empty_dirs import remove_empty_directories

def test_empty_dirs():
    with tempfile.TemporaryDirectory() as tmp:
        sub = os.path.join(tmp, "empty_sub")
        os.makedirs(sub)
        assert remove_empty_directories(tmp, dry_run=True) == [sub]
        assert os.path.exists(sub)
        remove_empty_directories(tmp, dry_run=False)
        assert not os.path.exists(sub)

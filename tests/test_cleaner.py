import tempfile, os
from src.cleaner.cache import CacheCleaner

def test_cache_cleaner_dry_run():
    with tempfile.TemporaryDirectory() as tmp:
        ds = os.path.join(tmp, ".DS_Store")
        with open(ds, "w") as f: f.write("ds-data")
        cleaner = CacheCleaner()
        targets = cleaner.identify_targets(tmp)
        assert len(targets) == 1
        freed = cleaner.purge(targets, dry_run=True)
        assert freed == len("ds-data")
        assert os.path.exists(ds)
        
        cleaner.purge(targets, dry_run=False)
        assert not os.path.exists(ds)

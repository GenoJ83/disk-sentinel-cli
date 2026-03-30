import tempfile
from src.hasher.hasher import compute_partial_hash, compute_full_hash

def test_hasher():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write("deterministic-hash-payload-123456")
        f.flush()
        h1 = compute_partial_hash(f.name)
        h2 = compute_full_hash(f.name)
        assert isinstance(h1, str) and len(h1) == 64
        assert isinstance(h2, str) and len(h2) == 64

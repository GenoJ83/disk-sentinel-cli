import hashlib

def compute_partial_hash(file_path: str, block_size: int = 4096) -> str:
    """Computes SHA-256 over first block for quick pre-filtering."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        chunk = f.read(block_size)
        hasher.update(chunk)
    return hasher.hexdigest()

def compute_full_hash(file_path: str, chunk_size: int = 65536) -> str:
    """Computes full SHA-256 digest of file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

import os
from typing import Dict, List
from src.core.models import DuplicateGroup
from src.hasher.hasher import compute_partial_hash, compute_full_hash

class DuplicateFinder:
    def __init__(self, min_size_bytes: int = 1):
        self.min_size_bytes = min_size_bytes
        
    def find_duplicates(self, file_paths: List[str]) -> List[DuplicateGroup]:
        # 1. Group by file size
        size_map: Dict[int, List[str]] = {}
        for p in file_paths:
            try:
                s = os.path.getsize(p)
                if s >= self.min_size_bytes and os.path.isfile(p):
                    size_map.setdefault(s, []).append(p)
            except OSError:
                continue
                
        candidates = [paths for size, paths in size_map.items() if len(paths) > 1]
        duplicates = []
        
        # 2. Hash check
        for group in candidates:
            hash_map: Dict[str, List[str]] = {}
            for p in group:
                try:
                    h = compute_full_hash(p)
                    hash_map.setdefault(h, []).append(p)
                except OSError:
                    continue
                    
            for digest, matched_paths in hash_map.items():
                if len(matched_paths) > 1:
                    file_sz = os.path.getsize(matched_paths[0])
                    wasted = file_sz * (len(matched_paths) - 1)
                    duplicates.append(DuplicateGroup(hash_digest=digest, total_size=file_sz, file_paths=matched_paths, wasted_bytes=wasted))
                    
        return sorted(duplicates, key=lambda x: x.wasted_bytes, reverse=True)

from typing import Dict

class SnapshotComparator:
    @staticmethod
    def compare(snap_prev: Dict[str, int], snap_curr: Dict[str, int]) -> Dict[str, int]:
        diff = {}
        all_keys = set(snap_prev.keys()) | set(snap_curr.keys())
        for k in all_keys:
            p = snap_prev.get(k, 0)
            c = snap_curr.get(k, 0)
            if p != c:
                diff[k] = c - p
        return diff

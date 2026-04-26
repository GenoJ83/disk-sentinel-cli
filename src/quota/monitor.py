import shutil
from typing import Dict, Any

class DiskSpaceMonitor:
    @staticmethod
    def get_usage(path: str = "/") -> Dict[str, Any]:
        total, used, free = shutil.disk_usage(path)
        percent = (used / total) * 100.0 if total > 0 else 0.0
        return {
            "total_bytes": total,
            "used_bytes": used,
            "free_bytes": free,
            "used_percent": round(percent, 2)
        }

from src.quota.monitor import DiskSpaceMonitor

def test_disk_usage_monitor():
    usage = DiskSpaceMonitor.get_usage(".")
    assert usage["total_bytes"] > 0
    assert 0.0 <= usage["used_percent"] <= 100.0

class DiskSentinelError(Exception):
    """Base exception for disk-sentinel."""

class ScanPermissionError(DiskSentinelError):
    """Raised when scan target lacks read permissions."""

class CleanOperationError(DiskSentinelError):
    """Raised when deletion operations fail."""

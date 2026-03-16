def format_bytes(byte_count: int) -> str:
    """Convert byte integer to human-readable binary prefix string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(byte_count) < 1024.0:
            return f"{byte_count:3.1f} {unit}" if unit != "B" else f"{byte_count} B"
        byte_count /= 1024.0
    return f"{byte_count:.1f} PB"

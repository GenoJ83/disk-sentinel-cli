from src.utils.formatter import format_bytes

def test_format_bytes():
    assert format_bytes(500) == "500 B"
    assert format_bytes(1024) == "1.0 KB"
    assert format_bytes(1048576) == "1.0 MB"
    assert format_bytes(1073741824) == "1.0 GB"

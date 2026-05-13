import csv, io
from typing import List, Tuple

def export_files_csv(files: List[Tuple[str, int]]) -> str:
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(["path", "size_bytes"])
    for path, sz in files:
        writer.writerow([path, sz])
    return out.getvalue()

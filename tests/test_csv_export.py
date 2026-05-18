from src.reporter.csv_export import export_files_csv

def test_csv_export():
    csv_txt = export_files_csv([("/a.txt", 100), ("/b.txt", 200)])
    assert "path,size_bytes" in csv_txt
    assert "/a.txt,100" in csv_txt

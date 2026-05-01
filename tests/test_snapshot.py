from src.history.snapshot import SnapshotComparator

def test_snapshot_comparison():
    s1 = {"/var/log": 100, "/tmp": 50}
    s2 = {"/var/log": 150, "/home": 200}
    delta = SnapshotComparator.compare(s1, s2)
    assert delta["/var/log"] == 50
    assert delta["/tmp"] == -50
    assert delta["/home"] == 200

from src.tree.trie import DirectoryTrie

def test_trie_insert():
    t = DirectoryTrie()
    t.insert("/var/log/syslog", 1024)
    assert "var" in t.root
    assert "log" in t.root["var"]["_children"]

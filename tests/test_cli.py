from src.cli.main import build_parser, main

def test_cli_parser():
    p = build_parser()
    opts = p.parse_args(["/var/log", "--top", "5"])
    assert opts.path == "/var/log"
    assert opts.top == 5
    assert main(["--version"]) == 0

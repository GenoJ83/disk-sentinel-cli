import argparse
import sys

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="disksentinel", description="Disk space analyzer and duplicate finder")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("path", nargs="?", default=".", help="Root directory to analyze")
    p.add_argument("--dry-run", action="store_true", default=True, help="Simulate cleaner actions")
    p.add_argument("--top", type=int, default=10, help="Number of largest items to list")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("disksentinel v0.1.0")
        return 0
    return 0

# disk-sentinel-cli

Interactive disk space analyzer, duplicate file detector with rolling cryptographic hashes, stale cache purger, and storage health reporter.

[![CI](https://github.com/GenoJ83/disk-sentinel-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/disk-sentinel-cli/actions)

## Features
- **Fast Recursive Scan**: Aggregates directory sizes with depth limits and permission tolerance
- **Two-Pass Duplicate Finder**: File-size clustering followed by SHA-256 hash comparison
- **Orphan & Cache Purge**: Cleans `.DS_Store`, `__pycache__`, and temporary build artifacts with dry-run protection
- **Disk Quota Metrics**: Monitors system disk usage percentages and free space headroom

## CLI Quickstart
```bash
# Analyze folder hierarchy
disksentinel /path/to/folder

# Purge temporary build caches safely
disksentinel clean /path/to/folder --dry-run
```

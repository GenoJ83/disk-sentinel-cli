# DiskSentinel CLI Usage

Run against any filesystem path to detect disk bloat, duplicates, and prune orphaned cache.

```bash
# Scan root directory and print top 10 files
disksentinel /var/log --top 10

# Purge stale caches (dry run)
disksentinel clean /tmp --dry-run
```

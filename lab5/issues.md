# Issues found and fixed — museum_catalog.py

| Issue | Type | Line(s) (original) | Description | Fix Approach |
|-------|------|--------------------|-------------|--------------|
| SQL injection (Bandit B608, Medium) | Security | 11 | `addArtifact` built the INSERT by concatenating `title` and `era` into the SQL string, so a title like `x'); DROP TABLE artifacts;--` is executed as SQL | Parameterized query with `?` placeholders and a tuple of values |
| Hardcoded password (B105, Low) | Security | 7 | `CURATOR_PASSWORD = "m4seum!"` stored a secret in source control | Read from the `CURATOR_PASSWORD` environment variable |
| `shell=True` / partial path / subprocess import (B602, B607, B404) | Security | 3, 37 | `subprocess.call("echo ...", shell=True)` spawned a shell just to print a line | Removed `subprocess`; `backup_note` now uses `print()` |
| Unused import `datetime` (F401 / W0611) | Quality | 2 | Import never used | Removed |
| Unused argument `curator` (W0613) | Bug risk | 15 | `displayStatus` accepted a `curator` argument it never used | Removed the parameter and updated the call in `main` |
| Non-snake_case function names (C0103) | Style | 10, 15, 24, 31, 36 | `addArtifact`, `displayStatus`, `totalValue`, `moveToDisplay`, `backupNote` | Renamed to `add_artifact`, `display_status`, `total_value`, `move_to_display`, `backup_note` |
| Missing docstrings (C0114, C0116) | Documentation | 1, 10, 15, 24, 31, 36, 40 | Module and every function lacked docstrings | Added concise docstrings |
| Unnecessary `else` after `return` (R1705) | Quality | 17-20 | `else` after a `return` adds nesting | Removed the `else` and de-indented |
| Module code runs on import | Design | 50 | `main()` was called at import time | Added `if __name__ == "__main__":` guard |
| Long lines (E501 / C0301) | Style | 6, 11, 16, 26, 32 | Lines up to 158 characters | Wrapped long SQL strings and calls |
| Too many blank lines (E303) | Style | 24 | Three blank lines before `totalValue` | Reduced to two |
| Missing operator whitespace (E225) | Style | 25 | `total=0` | `total = 0` |

## Scores

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.85/10 | 10.00/10 |
| Bandit | 5 issues (1 Medium, 4 Low) | 0 issues |
| Flake8 | 8 issues | 0 issues |

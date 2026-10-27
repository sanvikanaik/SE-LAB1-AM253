# Lab 5 Report: Static Code Analysis — Museum Artifact Catalog

## Overview
Target file: `museum_catalog.py` (SETAPESU26/L5_15_museum_catalog). Tools: Pylint, Bandit and Flake8, run in a Python 3.13 virtual environment. The program was run before and after the changes and prints the same output both times (`on display`, `135000`, `catalog backup complete`).

## Commits

- `d070831` Fix Bandit findings: parameterize SQL, remove hardcoded password and shell call
- `5824c3d` Fix Pylint findings: docstrings, snake_case names, unused import/argument, no-else-return, main guard
- `4326b7f` Fix Flake8 findings: wrap long lines, fix blank lines and operator spacing

## Issues found and fixed

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

### Scores

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.85/10 | 10.00/10 |
| Bandit | 5 issues (1 Medium, 4 Low) | 0 issues |
| Flake8 | 8 issues | 0 issues |

## Reflection

**1. Which issues were the easiest to fix, and which the hardest?**
Style and naming issues (Flake8 E501/E303/E225, Pylint snake_case, unused import) were mechanical and quick. The hardest were the security ones, because they needed a design decision rather than a rewrite: the SQL injection required switching to parameterized queries, and the hardcoded password required deciding where a secret should live (an environment variable) instead of just deleting it.

**2. Did the tools report any false positives, or issues you chose not to fix?**
Bandit's B602/B607 on `subprocess.call("echo ...", shell=True)` is low risk in practice because the command is a constant string, so it is arguably a false positive. I still removed it, since the call did nothing a `print()` can't do and shell=True is a pattern that becomes dangerous the moment the string gains user input. B105 on the password was a true positive.

**3. How could static analysis be integrated into a real development workflow?**
Run all three tools as a pre-commit hook and again in CI (for example a GitHub Actions job) so that a pull request fails on Bandit findings or a Pylint score below a threshold. Keeping configuration in `setup.cfg` / `.pylintrc` lets the team agree on rules once instead of arguing per-PR.

**4. What tangible improvements did you see in the code after the fixes?**
Pylint went from 4.85 to 10.00, Bandit from 5 findings to 0 and Flake8 from 8 to 0. Beyond the numbers, the code is no longer injectable through `title` or `era`, no longer ships a secret, can be imported without side effects, and every function is documented and consistently named, which makes it easier to read, test and maintain.

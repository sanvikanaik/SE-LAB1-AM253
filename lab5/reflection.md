# Reflection

**1. Which issues were the easiest to fix, and which the hardest?**
Style and naming issues (Flake8 E501/E303/E225, Pylint snake_case, unused import) were mechanical and quick. The hardest were the security ones, because they needed a design decision rather than a rewrite: the SQL injection required switching to parameterized queries, and the hardcoded password required deciding where a secret should live (an environment variable) instead of just deleting it.

**2. Did the tools report any false positives, or issues you chose not to fix?**
Bandit's B602/B607 on `subprocess.call("echo ...", shell=True)` is low risk in practice because the command is a constant string, so it is arguably a false positive. I still removed it, since the call did nothing a `print()` can't do and shell=True is a pattern that becomes dangerous the moment the string gains user input. B105 on the password was a true positive.

**3. How could static analysis be integrated into a real development workflow?**
Run all three tools as a pre-commit hook and again in CI (for example a GitHub Actions job) so that a pull request fails on Bandit findings or a Pylint score below a threshold. Keeping configuration in `setup.cfg` / `.pylintrc` lets the team agree on rules once instead of arguing per-PR.

**4. What tangible improvements did you see in the code after the fixes?**
Pylint went from 4.85 to 10.00, Bandit from 5 findings to 0 and Flake8 from 8 to 0. Beyond the numbers, the code is no longer injectable through `title` or `era`, no longer ships a secret, can be imported without side effects, and every function is documented and consistently named, which makes it easier to read, test and maintain.

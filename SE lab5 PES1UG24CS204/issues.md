# Lab 5 - Static Code Analysis
## Identified Issues and Fixes

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Hardcoded password | Security | 5 | Password stored directly in source code | Removed hardcoded credential |
| SQL injection | Security | 9 | SQL query constructed using f-strings | Used parameterized SQL queries |
| Unsafe eval() | Security | 21 | eval() permits arbitrary code execution | Replaced with restricted AST arithmetic evaluator |
| Mutable default argument | Bug | 8 | history=[] shares state across calls | Changed default to None and initialize inside function |
| Broad exception | Code quality | 22 | Catches all exceptions indiscriminately | Caught specific exceptions |
| Missing docstrings | Code quality | Multiple | Functions and module lacked documentation | Added module and function docstrings |
| Naming convention | Code quality | 8 | addDue did not follow snake_case | Renamed to add_due |
| Inconsistent return | Code quality | 12 | Function return paths were inconsistent | Added explicit return value |
| None comparison | Code quality | 29 | Compared rows using != None | Used truth-value check |
| Long lines | Style | 4, 13, 15 | Lines exceeded recommended length | Reformatted long statements |
| Missing blank lines | Style | 12 | Incorrect spacing between definitions | Applied PEP 8 spacing |
| E711 comparison | Style | 29 | Compared directly against None | Removed unnecessary comparison |

## Before and After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.81/10 | 10.00/10 |
| Bandit | 3 findings | 0 findings |
| Flake8 | 5 violations | 0 violations |

## Conclusion

Static analysis helped identify security vulnerabilities,
programming errors, and style violations. After correcting
the identified issues, all three tools reported clean results.

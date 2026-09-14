## 2024-05-24 - Timing attack vulnerability in API key verification
**Vulnerability:** API key verification in `artifacts/pipeline-api/main.py` used standard string comparison (`!=`) which returns early on the first mismatched character. This is vulnerable to timing attacks where an attacker can iteratively guess the API key by measuring the time taken for the server to respond.
**Learning:** Using standard string comparison operators (`==` or `!=`) for comparing sensitive secrets (like API keys, passwords, or tokens) leaks timing information.
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest(a, b)` for comparing secrets in Python. Additionally, ensure both operands are strings before passing them to `compare_digest` to prevent `TypeError` crashes.

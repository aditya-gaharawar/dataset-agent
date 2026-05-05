## 2026-05-05 - [API Key Timing Attack]
**Vulnerability:** The API key validation in `main.py` was using a simple string equality check (`!=`), which is vulnerable to timing attacks. An attacker could potentially guess the API key character by character by measuring the response time.
**Learning:** Security-critical string comparisons (like API keys, tokens, or passwords) must use constant-time comparison functions to prevent timing attacks.
**Prevention:** Always use `secrets.compare_digest()` for comparing security tokens or keys in Python.

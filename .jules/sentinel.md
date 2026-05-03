## 2024-05-03 - Timing Attack Vulnerability in API Key Verification

**Vulnerability:** The API key verification in `artifacts/pipeline-api/main.py` used a simple string comparison (`token != _API_KEY`) to validate the `Authorization` header. This is susceptible to timing attacks, where an attacker can determine the correct API key by observing the time it takes for the server to reject incorrect guesses character by character.

**Learning:** String comparison operations (`==` and `!=`) exit as soon as a mismatch is found. This variable execution time leaks information about the expected string. In security contexts (like token/password verification), constant-time comparisons must be used to prevent this information leakage.

**Prevention:** Always use `secrets.compare_digest(a, b)` for comparing security-sensitive strings, such as passwords, tokens, or API keys, to ensure constant-time comparison regardless of matches or mismatches.
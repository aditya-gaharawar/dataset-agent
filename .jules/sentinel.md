## 2024-04-11 - [Timing Attack in Token Verification]
**Vulnerability:** The API key middleware in `artifacts/pipeline-api/main.py` uses `if token != _API_KEY:` for token verification. This simple string comparison stops evaluating at the first non-matching character, making the system vulnerable to timing attacks where an attacker can determine the correct API key character by character based on the response time.
**Learning:** Even simple string comparisons for sensitive tokens like API keys must use constant-time comparison functions to prevent timing attacks.
**Prevention:** Use `secrets.compare_digest(token, _API_KEY)` instead of `==` or `!=` when verifying sensitive tokens.

## 2025-02-14 - Fix Timing Attack Vulnerability in Authentication Middleware
**Vulnerability:** The API key verification in `artifacts/pipeline-api/main.py` used standard string equality (`token != _API_KEY`) which stops checking at the first mismatched character. This allows attackers to perform a timing attack by measuring response times to guess the correct API key character by character.
**Learning:** Python's built-in string equality comparison is optimized for performance (fail-fast), not security. This makes it unsuitable for comparing sensitive values like API keys, tokens, or passwords.
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest` from the built-in `secrets` module when verifying secure tokens, passwords, or API keys.

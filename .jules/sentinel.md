## 2024-05-28 - Timing Attack Vulnerability in API Key Authentication
**Vulnerability:** The API Key authentication middleware in `main.py` was using the `!=` operator to compare the provided token with the expected API key. This string comparison operator returns early upon encountering a mismatch, leaking information about the expected string character by character through the time taken to process the comparison.
**Learning:** String comparison with `!=` or `==` is not suitable for cryptographic secrets or authentication tokens.
**Prevention:** Always use `secrets.compare_digest(a, b)` for comparing secret values. Additionally, validate inputs to `compare_digest` to ensure they are both strings (e.g. using `isinstance`), as passing incorrect types may result in `TypeError` crashes.

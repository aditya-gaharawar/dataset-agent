## 2024-05-24 - Timing Attack on API Key Verification
**Vulnerability:** The API key verification logic used a simple string comparison (`token != _API_KEY`) to check the validity of incoming bearer tokens. This approach is vulnerable to timing attacks.
**Learning:** Simple string comparison stops at the first mismatched character. An attacker can use the response time to guess the API key character by character by measuring how long the comparison takes.
**Prevention:** Always use a constant-time comparison function, such as `secrets.compare_digest` in Python, when verifying sensitive tokens, passwords, or hashes.

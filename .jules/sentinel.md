## 2025-03-05 - [Timing Attack Vulnerability in API Key Verification]
**Vulnerability:** API key token validation used a basic equality check (`token != _API_KEY`) which exposes the application to timing attacks, allowing an attacker to guess the API key character by character based on response time.
**Learning:** Security tokens and API keys require constant-time comparison methods, as standard string equality checks return early upon the first mismatched character.
**Prevention:** Always use `secrets.compare_digest` in Python (or equivalent constant-time functions in other languages) when validating sensitive tokens, passwords, or hashes.

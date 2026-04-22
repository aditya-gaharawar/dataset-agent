## 2024-04-22 - [API Key Verification Timing Attack]
**Vulnerability:** API key verification was using standard string equality (`token != _API_KEY`).
**Learning:** Standard string comparisons can exit early, leaking information about the matching string length to an attacker based on timing. This allows attackers to brute-force auth tokens.
**Prevention:** Use `secrets.compare_digest(a, b)` for constant-time comparisons when validating API keys, secrets, tokens, or passwords to prevent timing attacks.
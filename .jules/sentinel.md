## 2026-05-21 - [API Key Timing Attack Vulnerability]
**Vulnerability:** The API key validation used normal string inequality (`!=`), which terminates early at the first mismatched character, opening the system to timing attacks to brute-force the API Key character-by-character.
**Learning:** Normal string comparisons should never be used for securely verifying tokens, API keys, or passwords.
**Prevention:** Use constant-time comparison methods, like `secrets.compare_digest()`, to compare tokens and secrets without leaking timing information.

## 2024-05-24 - API Key Timing Attack Vulnerability
**Vulnerability:** The `API_KEY` authentication middleware in `artifacts/pipeline-api/main.py` used direct string comparison (`!=`) to verify tokens. This exposes the application to timing attacks, allowing an attacker to progressively guess the API key by measuring response times.
**Learning:** Python's built-in string comparison operator short-circuits on the first mismatch, creating a detectable timing difference proportional to the number of correctly guessed characters.
**Prevention:** Always use `secrets.compare_digest` for sensitive string comparisons, such as API keys, passwords, and cryptographic hashes, to ensure constant-time evaluation regardless of correct characters.

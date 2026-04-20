## 2024-04-20 - API Key Verification Timing Attack
**Vulnerability:** Standard string inequality (`!=`) was used to verify the API key token in `artifacts/pipeline-api/main.py`. This allowed for potential timing attacks because the standard comparison function exits early as soon as a mismatch is found, leaking information about the valid token's characters.
**Learning:** I learned that even in internal or API proxy environments, all authentication tokens must be compared in constant time to prevent side-channel timing attacks.
**Prevention:** Always use `secrets.compare_digest()` (in Python) or an equivalent constant-time comparison function for any secure tokens, passwords, or API keys.

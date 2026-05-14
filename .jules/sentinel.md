## 2024-05-14 - Fix Timing Attack Vulnerability in API Key Verification

**Vulnerability:** The API key verification in `main.py` used simple string equality (`token != _API_KEY`) to validate authentication headers. This allows a timing attack where an attacker can determine the correct API key one character at a time by observing the response time.
**Learning:** String comparisons in Python terminate early on the first mismatched character. This is standard behavior for string comparisons but is insecure for comparing secrets.
**Prevention:** Always use `secrets.compare_digest(a, b)` for comparing secrets, tokens, or passwords to ensure constant-time comparison, which prevents timing side-channel attacks.

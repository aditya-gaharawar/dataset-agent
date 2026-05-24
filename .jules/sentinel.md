## 2024-05-24 - [API Key Verification Timing Attack]
**Vulnerability:** The API key middleware in `artifacts/pipeline-api/main.py` used a simple string comparison (`token != _API_KEY`) to verify the authentication token. This is vulnerable to timing attacks where an attacker can determine the secret API key character by character based on the time it takes the server to reject the request.
**Learning:** Standard string comparison operators in Python (and most languages) return early upon finding the first mismatched character. When comparing secrets, this early return leaks information about the length of the matching prefix.
**Prevention:** Always use constant-time comparison functions, such as `secrets.compare_digest()`, when verifying cryptographic secrets, API keys, or passwords.

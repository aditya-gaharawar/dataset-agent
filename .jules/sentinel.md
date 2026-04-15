## 2024-05-18 - API Key Timing Attack Vulnerability
**Vulnerability:** The API key middleware in `artifacts/pipeline-api/main.py` used standard string comparison (`token != _API_KEY`) to verify the `API_KEY` provided in the Authorization header.
**Learning:** Standard string comparison in Python compares characters one by one and returns `False` as soon as a mismatch is found. This allows an attacker to measure the time taken to respond and guess the API key character by character (a timing attack).
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest(a, b)` (or `hmac.compare_digest`) when checking sensitive strings such as API keys, passwords, or tokens.

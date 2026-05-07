## 2024-05-18 - Prevent Timing Attack in Authentication Middleware
**Vulnerability:** The API key verification in the FastAPI middleware used a simple string comparison (`token != _API_KEY`). This could allow an attacker to guess the API key character by character by measuring the response time (a timing attack), because standard string comparison stops as soon as a mismatch is found.
**Learning:** Security-sensitive string comparisons, such as verifying passwords or tokens, must always use constant-time operations to prevent information leakage through execution time variations.
**Prevention:** Always use `secrets.compare_digest(a, b)` for comparing secret strings or tokens in Python.

## 2024-05-24 - [Fix API Key Timing Attack]
**Vulnerability:** The API key validation used a standard string comparison (`token != _API_KEY`), which short-circuits and leaks the length of the matching prefix.
**Learning:** This exposes the application to a timing side-channel attack where an attacker can guess the API key character by character by measuring response times.
**Prevention:** Use `secrets.compare_digest` for cryptographic strings like API keys, tokens, and passwords to ensure a constant-time comparison.

## 2024-05-18 - [API Key Timing Attack]
**Vulnerability:** The API key verification in `api_key_middleware` (`main.py`) used standard string equality (`token != _API_KEY`). This direct comparison leaks timing information because it returns False as soon as a character mismatch is found.
**Learning:** An attacker could theoretically guess the API key character by character by measuring the response time of requests with different test keys. This is a classic timing attack against string comparison.
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest(a, b)` (in Python) when comparing sensitive secrets such as API keys, tokens, or passwords.

## 2025-02-28 - Timing Attack Vulnerability in API Key Validation
**Vulnerability:** The API key validation in `main.py` used standard string comparison (`token != _API_KEY`). This is vulnerable to timing attacks, as attackers can determine the valid API key character by character by measuring the response time.
**Learning:** Standard string equality checks short-circuit on the first mismatched character, creating a measurable difference in execution time depending on how many leading characters are correct.
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest()` for security-sensitive string comparisons, such as passwords, tokens, or API keys.

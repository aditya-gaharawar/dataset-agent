
## 2025-04-27 - Timing Attack Vulnerability in API Key Comparison
**Vulnerability:** The API key verification middleware (`api_key_middleware`) in `artifacts/pipeline-api/main.py` used a simple string comparison (`token != _API_KEY`) to validate the API key.
**Learning:** Standard string comparisons terminate early when a character mismatch is found, meaning the time taken to compare two strings is proportional to the number of matching prefix characters. This can allow an attacker to guess the API key character by character by measuring the response time (a timing attack).
**Prevention:** Always use constant-time string comparison functions like `secrets.compare_digest` from the built-in `secrets` module when comparing sensitive information such as passwords, tokens, or API keys.

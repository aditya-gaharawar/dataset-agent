## 2024-05-24 - Timing attack on API Key Validation
**Vulnerability:** The API key verification in `api_key_middleware` compares the token and API key using `token != _API_KEY`, which is susceptible to timing attacks. An attacker can determine the API key by analyzing the time it takes for the server to reject an invalid key character by character.
**Learning:** String comparison operations (`==` and `!=`) exit early upon encountering the first mismatch, leading to variable execution times.
**Prevention:** Use a constant-time string comparison function, such as `secrets.compare_digest`, when verifying sensitive values like passwords or API keys to ensure the operation takes the same amount of time regardless of the input.

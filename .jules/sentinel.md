## $(date +%Y-%m-%d) - [Timing Attack in API Key Verification]
**Vulnerability:** API key verification used a simple string equality check (`token != _API_KEY`), which is susceptible to timing attacks. An attacker could measure the time taken to verify the token, revealing the key character by character.
**Learning:** This existed because standard string equality checks are not constant-time.
**Prevention:** Use `secrets.compare_digest()` for comparing secrets like API keys, as it ensures constant-time comparison, mitigating timing attacks.

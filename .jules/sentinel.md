## 2024-04-24 - Timing Attack Vulnerability in API Key Verification
**Vulnerability:** The API key middleware in `main.py` used a standard string comparison (`!=`) to verify the authorization token against the secret `API_KEY`. This is susceptible to timing attacks, where an attacker can deduce the valid key by measuring the time it takes for the comparison to fail.
**Learning:** This occurred because simple string equality checks in Python short-circuit when they find the first mismatched character, causing the execution time to depend on how much of the string matched.
**Prevention:** Always use `secrets.compare_digest()` for comparing cryptographic secrets, passwords, or API keys, as it compares the strings in constant time, mitigating timing attacks.

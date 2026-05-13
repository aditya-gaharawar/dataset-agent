## 2024-05-15 - [Timing Attack Vulnerability in API Key Verification]
**Vulnerability:** API key verification was performed using a standard string comparison (`!=`) instead of a constant-time comparison algorithm.
**Learning:** Using simple string comparison for secrets like API keys introduces a timing attack vulnerability. An attacker can iteratively guess the API key by measuring the response time, as string comparison stops evaluating at the first incorrect character.
**Prevention:** Always use constant-time comparison algorithms like `secrets.compare_digest` for validating authentication tokens, passwords, or any other secrets to prevent timing side channels.

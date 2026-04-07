## 2025-02-28 - Fix Timing Attack Vulnerability in API Key Verification
**Vulnerability:** A simple string comparison (`!=`) was used to compare the provided bearer token with the expected API key.
**Learning:** Using `==` or `!=` for sensitive token comparison introduces a timing attack vulnerability, allowing attackers to incrementally deduce the API key by observing response latency.
**Prevention:** Always use `secrets.compare_digest` in Python for cryptographic token, password, or key comparisons to ensure constant-time execution and prevent side-channel timing attacks.

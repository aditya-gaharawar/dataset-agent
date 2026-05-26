## 2025-05-26 - [API Key Timing Attack Vulnerability]
**Vulnerability:** The API key verification in the FastAPI middleware used standard string equality (`!=`), which is vulnerable to timing attacks. An attacker could potentially infer the API key by measuring response times.
**Learning:** Python's standard equality operator short-circuits, making it insecure for secrets.
**Prevention:** Always use `secrets.compare_digest` for comparing tokens, passwords, API keys, or hashes to ensure constant-time comparison.

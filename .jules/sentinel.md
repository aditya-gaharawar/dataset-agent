## 2025-04-12 - Timing Attack in API Key Verification
**Vulnerability:** API key verification in the FastAPI backend used a standard string comparison (`token != _API_KEY`). This allowed for a timing attack where an attacker could theoretically guess the key by measuring how long the comparison took, since `!=` fails fast on the first mismatched character.
**Learning:** String comparison for security tokens like API keys should always be constant-time to prevent timing attacks.
**Prevention:** Use `secrets.compare_digest` instead of `==` or `!=` for comparing security credentials or tokens.

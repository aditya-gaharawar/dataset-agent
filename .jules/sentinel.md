## 2026-05-10 - Constant-Time API Key Comparison
**Vulnerability:** The FastAPI backend uses a standard string equality operator (`==` or `!=`) to verify the API key in the authentication middleware. This exposes the endpoint to timing attacks, where an attacker could deduce the API key by measuring the response time for different characters.
**Learning:** Standard string comparison operators in Python short-circuit when a character mismatch is found. This makes the execution time proportional to the length of the matching prefix of the strings being compared.
**Prevention:** Always use `secrets.compare_digest()` for comparing security-sensitive strings like API keys, tokens, or passwords to ensure constant-time comparison and prevent timing side-channel attacks.

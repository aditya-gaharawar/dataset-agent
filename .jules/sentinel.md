## 2024-05-22 - Prevent Timing Attacks on API Key Validation
**Vulnerability:** API key verification in the FastAPI middleware was using standard string comparison (`token != _API_KEY`), making it vulnerable to timing attacks where an attacker could guess the key character by character based on response times.
**Learning:** Standard string equality operators (`==`, `!=`) return immediately upon finding the first mismatching character, leaking information about the length of the matching prefix.
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest()` for validating sensitive tokens, passwords, or API keys to prevent timing-based side-channel attacks.

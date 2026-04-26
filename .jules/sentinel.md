## 2026-04-26 - Timing Attack Vulnerability in Token Verification
**Vulnerability:** API key verification was performed using simple string equality (`token != _API_KEY`), which is vulnerable to timing attacks. An attacker could measure the time taken to reject a token to guess the API key character by character.
**Learning:** Standard string comparison operators in Python (and many other languages) fail fast—they return `False` as soon as a character mismatch is found. This makes the execution time depend on the number of matching prefix characters.
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest(a, b)` for verifying secrets, passwords, or tokens.

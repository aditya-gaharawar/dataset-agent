## 2024-05-14 - Fix API Key Timing Attack Vulnerability
**Vulnerability:** The API key verification used standard string equality `token != _API_KEY` to authenticate API requests. This comparison approach is vulnerable to timing attacks, where the string comparison time differs based on the number of character matches, allowing an attacker to theoretically guess the key character by character.
**Learning:** Even internal or simple APIs need proper cryptographic comparisons for authentication tokens and passwords. Python's default string equality checks short-circuit on the first mismatched character.
**Prevention:** Always use constant-time comparison functions like `secrets.compare_digest(a, b)` for comparing secrets, tokens, or passwords to mitigate timing attacks.

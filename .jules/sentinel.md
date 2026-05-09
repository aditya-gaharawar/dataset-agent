## 2023-10-27 - [Timing Attack Vulnerability in API Key Validation]
**Vulnerability:** API key verification was performed using standard string equality checking (`token != _API_KEY`).
**Learning:** Standard string equality operators compare strings character by character and return as soon as a mismatch is found. This means the time it takes to process the request can reveal how many characters of the provided key match the actual key, allowing an attacker to guess the key via a timing attack.
**Prevention:** Always use constant-time comparison functions, such as `secrets.compare_digest()`, when verifying secrets like API keys, passwords, and tokens.

## 2024-05-17 - Authentication Token Timing Attack Vulnerability
**Vulnerability:** The API key token validation in `api_key_middleware` of `main.py` was using standard equality string comparison (`token != _API_KEY`).
**Learning:** Standard string comparison operators (`==` or `!=`) often short-circuit when they find a mismatch. This allows attackers to perform a timing attack by measuring the validation time, potentially deducing the correct secret character-by-character.
**Prevention:** Use a constant-time comparison function, such as `secrets.compare_digest` in Python, whenever validating sensitive secrets like tokens, passwords, or hashes.

## 2024-05-18 - API Key Verification Timing Attack
**Vulnerability:** API key verification in main.py used a non-constant time string equality check (`!=`), which could allow a timing side-channel attack where an attacker guesses the API key character-by-character based on the response time.
**Learning:** Basic string equality operators exit early on the first mismatch, leading to varied response times that leak information about the correct API key.
**Prevention:** Use `secrets.compare_digest` for secure string comparison of secrets like API keys or passwords, which takes constant time regardless of mismatches, thus mitigating timing attacks.

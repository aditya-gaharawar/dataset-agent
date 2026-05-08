## 2024-05-08 - [Timing Attack in API Key Auth]

**Vulnerability:** The API key verification middleware used a standard string comparison (`token != _API_KEY`). This allows attackers to perform a timing attack by observing the response time, which can reveal the characters of the API key one by one, as standard string comparison returns early on the first mismatch.
**Learning:** API key or password verification should never use standard string equality operators, as it leaks information about the secret via timing side channels.
**Prevention:** Always use a constant-time comparison function, such as `secrets.compare_digest()` in Python, or equivalent functions in other languages when comparing security-sensitive tokens, passwords, or hashes.

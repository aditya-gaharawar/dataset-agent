## 2024-05-01 - [Timing Attack in Authentication]
**Vulnerability:** API key verification was done using standard string comparison `!=`, which makes it vulnerable to timing attacks. An attacker could potentially infer the key one character at a time by observing the response times.
**Learning:** String comparisons in authentication routes fail early, leaking information about the matching prefix of the token compared to the expected secret.
**Prevention:** Use `secrets.compare_digest(a, b)` for constant-time comparisons when validating API keys, passwords, or hashes.

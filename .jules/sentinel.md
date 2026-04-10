## 2025-04-10 - Timing Attack Vulnerability in API Key Verification
**Vulnerability:** The `api_key_middleware` in `artifacts/pipeline-api/main.py` verified the authentication token using standard string equality (`token != _API_KEY`).
**Learning:** Standard string equality checks return `False` immediately upon the first character mismatch, allowing an attacker to deduce the length and contents of the correct API key by measuring response times.
**Prevention:** Always use a constant-time comparison algorithm, such as Python's `secrets.compare_digest()`, when verifying secrets or API keys.

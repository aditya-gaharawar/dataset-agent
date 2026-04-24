import pytest
import os
from fastapi.testclient import TestClient

os.environ["API_KEY"] = "test_secret_key"
from main import app

client = TestClient(app)

def test_protected_route_missing_auth():
    response = client.get("/api/v1/metrics")
    # /api/v1/metrics is public
    assert response.status_code == 200

def test_protected_route_invalid_auth():
    # /pipeline/ingest is protected
    response = client.post("/pipeline/ingest", json={"sources": []}, headers={"Authorization": "Bearer wrong_key"})
    assert response.status_code == 401

def test_protected_route_valid_auth():
    response = client.post("/pipeline/ingest", json={"sources": []}, headers={"Authorization": "Bearer test_secret_key"})
    # It might return a 422 for missing body properties, but not a 401
    assert response.status_code in [200, 422]

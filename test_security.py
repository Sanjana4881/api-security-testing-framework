import pytest
from app import app

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_owner_can_read_own_document(client):
    response = client.get(
        "/documents/doc-101",
        headers={"Authorization": "Bearer demo-token-alice"},
    )
    assert response.status_code == 200
    assert response.json["id"] == "doc-101"

def test_other_user_cannot_read_document(client):
    response = client.get(
        "/documents/doc-101",
        headers={"Authorization": "Bearer demo-token-bob"},
    )
    assert response.status_code == 404

def test_missing_authentication_is_rejected(client):
    response = client.get("/documents/doc-101")
    assert response.status_code == 401

def test_invalid_token_is_rejected(client):
    response = client.get(
        "/documents/doc-101",
        headers={"Authorization": "Bearer invalid-token"},
    )
    assert response.status_code == 401

def test_unknown_document_is_not_found(client):
    response = client.get(
        "/documents/no-such-doc",
        headers={"Authorization": "Bearer demo-token-alice"},
    )
    assert response.status_code == 404

def test_security_headers_are_present(client):
    response = client.get("/health")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["Cache-Control"] == "no-store"
    assert "frame-ancestors 'none'" in response.headers["Content-Security-Policy"]

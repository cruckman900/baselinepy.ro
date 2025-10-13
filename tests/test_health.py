from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import Session
from app.db import engine

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "fanTABulous is alive and riffing 🤘"}

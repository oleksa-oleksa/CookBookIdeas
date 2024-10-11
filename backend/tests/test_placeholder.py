# backend/tests/test_placeholder.py

from fastapi.testclient import TestClient
from backend.main import app 
client = TestClient(app)

def test_placeholder():
    response = client.get("/") 
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my receipt collection FastAPI app"}  
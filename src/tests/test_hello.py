from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_hello():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, World!"}

from fastapi.testclient import TestClient
from src.api import main

client = TestClient(main.app)


def setup_function():
    # reset counter before each test
    main._counter = 0


def test_counter_increment():
    r1 = client.post("/counter")
    assert r1.status_code == 200
    assert r1.json()["counter"] == 1

    r2 = client.post("/counter")
    assert r2.json()["counter"] == 2

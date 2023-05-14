from random import randint

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_healthchecker():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Api is running"}

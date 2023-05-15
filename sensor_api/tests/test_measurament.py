from random import randint
from datetime import datetime

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

now = datetime.now()

register_payload = {
    "sensor_id": randint(100, 999),
    "variable": "temp",
    "value": 1.0,
    "unit": "celsius",
    "created_at": now.isoformat(),
}


def test_register_measurement():
    response = client.post("/api/v1/measurement", json=register_payload)
    assert response.status_code == 201


def test_bad_register_measurement():
    response_erro = client.post("/api/v1/measurement", json=register_payload)
    assert response_erro.status_code == 400


def test_get_all_measurement_by_sensor_id():
    response = client.get(f"/api/v1/measurement/{register_payload['sensor_id']}")
    response_json = response.json()
    assert response.status_code == 200
    assert isinstance(response_json, list)


from fastapi.testclient import TestClient

from api.database import get_db, tests_db
from main import app
from measurement.routes import create_mensurement
from measurement.model import Measurement

Measurement.metadata.create_all(bind=tests_db())

app.dependency_overrides[get_db] = tests_db

client = TestClient(app)


def test_register_measurement():
    response = client.post("/measurement", json={"sensor_id": "sensor_id", "variable": "variable", "value": "value", "unit": "unit"})
    assert response.status_code == 200
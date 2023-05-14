import os
from random import randint

from locust import HttpUser, between, task

API_PORT = os.getenv("API_PORT")


class LoadTestAPI(HttpUser):
    @task
    def measurament(self):
        id = randint(100, 999)
        payload = {
            "sensor_id": str(id),
            "variable": "temp",
            "value": 10.0,
            "unit": "celsius",
        }
        self.client.post("/api/v1/measurement", json=payload)

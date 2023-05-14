from random import randint

from locust import HttpUser, task


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

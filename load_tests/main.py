from random import randint

from locust import HttpUser, between, task


def get_random_sensor_id():
    return randint(100, 999)


class LoadTestAPI(HttpUser):
    @task
    def measurement(self):
        try:
            payload = {
                "sensor_id": str(get_random_sensor_id()),
                "variable": "temp",
                "value": 10.0,
                "unit": "celsius",
            }
            self.client.post("/api/v1/measurement", json=payload)
        except Exception as e:
            print(e)

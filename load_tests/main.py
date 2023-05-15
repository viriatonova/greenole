from datetime import datetime
from random import randint

from locust import HttpUser, task

def set_random_sensor_id():
    return randint(100, 999)

def set_datetime():
    now = datetime.now()
    return now.isoformat()

class LoadTestAPI(HttpUser):
    @task
    def measurement(self):
        try:
            payload = {
                "sensor_id": str(set_random_sensor_id()),
                "variable": "temp",
                "value": 10.0,
                "unit": "celsius",
                "created_at": set_datetime(),
            }
            self.client.post("/api/v1/measurement", json=payload)
        except Exception as e:
            print(e)

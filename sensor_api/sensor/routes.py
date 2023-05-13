
from fastapi import APIRouter, status

sensor_routes = APIRouter()

@sensor_routes.post("/sensor", status_code=status.HTTP_200_OK)
def create_sensor(sensor):
    return sensor


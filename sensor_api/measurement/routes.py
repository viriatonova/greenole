from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from measurement.schema import MeasurementBase, MeasurementRead
from .helpers import get_measurement_by_sensor_id, register_measurement


measurement_routes = APIRouter()

@measurement_routes.post("/measurement", status_code=status.HTTP_201_CREATED, response_model=MeasurementBase)
async def create_mensurement(measurement: MeasurementBase, db: Session = Depends(get_db)):
    return register_measurement(measurement, db)

@measurement_routes.post("/measurement/{sensor_id}", status_code=status.HTTP_200_OK, response_model=list[MeasurementRead])
async def get_measurement_by_sensor_id(sensor_id: int,  db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    db_measurement_list = get_measurement_by_sensor_id(sensor_id, db, skip, limit)
    return db_measurement_list
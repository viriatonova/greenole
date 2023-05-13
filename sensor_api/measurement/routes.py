import datetime
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from measurement.schema import MeasurementBase
from .helpers import register_measurement, get_last_measurement_by_sensor_id


measurement_routes = APIRouter()

@measurement_routes.post("/measurement", status_code=status.HTTP_201_CREATED, response_model=MeasurementBase)
async def create_mensurement(measurement: MeasurementBase, db: Session = Depends(get_db)):
        now = datetime.datetime.now()
        last_sensor_measurement = get_last_measurement_by_sensor_id(measurement.sensor_id, db)
        if not last_sensor_measurement:
              return register_measurement(measurement, db)
        # Checking if the last measurement is older than 1 minute
        if now - last_sensor_measurement.timestamp < datetime.timedelta(minutes=1):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Last measurement not is older than 1 minute")  
        return register_measurement(measurement, db)

import datetime

from api.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from measurement.schema import MeasurementBase, MeasurementRead
from sqlalchemy.orm import Session

from .helpers import (
    get_all_measurement_by_sensor_id,
    get_last_measurement_by_sensor_id,
    register_measurement,
)

measurement_routes = APIRouter()


@measurement_routes.post(
    "/measurement", status_code=status.HTTP_201_CREATED, response_model=MeasurementBase
)
async def create_mensurement(
    measurement: MeasurementBase, db: Session = Depends(get_db)
):
    now = datetime.datetime.now()
    last_sensor_measurement = get_last_measurement_by_sensor_id(
        measurement.sensor_id, db
    )
    if not last_sensor_measurement:
        return register_measurement(measurement, db)

    # Checking if the last measurement is older than 5 seconds
    if (
        measurement.sensor_id == last_sensor_measurement.sensor_id
        and now - last_sensor_measurement.created_at < datetime.timedelta(seconds=5)
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Last measurement not is older than 1 minute",
        )
    return register_measurement(measurement, db)


@measurement_routes.get(
    "/measurement/{sensor_id}", response_model=list[MeasurementRead]
)
async def get_all_measurements(sensor_id: str, db: Session = Depends(get_db)):
    db_measurements = get_all_measurement_by_sensor_id(sensor_id=sensor_id, db=db)
    return db_measurements

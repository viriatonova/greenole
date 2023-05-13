from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .model import Measurement
from .schema import MeasurementBase


def get_last_measurement_by_sensor_id(sensor_id: str, db: Session):
    return db.query(Measurement).filter(Measurement.sensor_id == sensor_id).order_by(Measurement.timestamp.desc()).first()

def register_measurement(measurement: MeasurementBase, db: Session):
    try:
        db_measurement = Measurement(
            sensor_id=measurement.sensor_id, 
            variable=measurement.variable, 
            value=measurement.value, 
            unit=measurement.unit)
        db.add(db_measurement)
        db.commit()
        db.refresh(db_measurement)
        return db_measurement
    except (IntegrityError) as error:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'A database error occurred: {error.orig}')
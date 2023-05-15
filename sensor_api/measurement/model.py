from api.database import BASE
from sqlalchemy import Column, DateTime, Float, Integer, String, func


class Measurement(BASE):
    __tablename__ = "measurements"
    __table_args__ = ({"schema": "sensor_measurement"},)

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, index=True)
    created_at = Column(DateTime(timezone=True))
    variable = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False)

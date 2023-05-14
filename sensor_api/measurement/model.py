from api.database import BASE
from sqlalchemy import Column, DateTime, Integer, String, func


class Measurement(BASE):
    __tablename__ = "measurements"
    __table_args__ = ({"schema": "sensor_measurement"},)

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), default=func.now())
    variable = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    unit = Column(String, nullable=False)

from datetime import datetime

from pydantic import BaseModel, validator

class MeasurementBase(BaseModel):
    sensor_id: str
    timestamp: datetime | None = None
    variable: str
    value: int
    unit: str

    class Config:
        orm_mode = True
    

class MeasurementRead(MeasurementBase):
    class Config:
        orm_mode = True
        fields = {}
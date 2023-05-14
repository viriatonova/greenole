from datetime import datetime

from pydantic import BaseModel, validator
from pydantic.schema import Optional

class MeasurementBase(BaseModel):
    sensor_id: Optional[str]
    timestamp: Optional[datetime]
    variable: Optional[str]
    value: Optional[int]
    unit: Optional[str]

    class Config:
        orm_mode = True
        fields = {}

class MeasurementRead(MeasurementBase):
    class Config:
        orm_mode = True
        fields = {}
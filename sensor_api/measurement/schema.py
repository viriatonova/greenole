from datetime import datetime

from pydantic import BaseModel
from pydantic.schema import Optional


class MeasurementBase(BaseModel):
    sensor_id: Optional[int]
    created_at: Optional[datetime]
    variable: Optional[str]
    value: Optional[float]
    unit: Optional[str]

    class Config:
        orm_mode = True
        fields = {}


class MeasurementRead(MeasurementBase):
    class Config:
        orm_mode = True
        fields = {}

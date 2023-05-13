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
        fields = { "variable": {"exclude": True}, "value": {"exclude": True}, "unit": {"exclude": True}}
    
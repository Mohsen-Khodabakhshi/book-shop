from pydantic import BaseModel as PydanticBaseModel

from datetime import datetime


class BaseModel(PydanticBaseModel):
    deleted: bool | None = False
    deleted_time: datetime | None = None
    modified_time: datetime
    created_time: datetime

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S')
        }

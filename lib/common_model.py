from pydantic import BaseModel as PydanticBaseModel

from datetime import datetime


class SoftDeleteBaseModel(PydanticBaseModel):
    deleted: bool | None = False
    deleted_time: datetime | None = None


class DateTimeBaseModel(PydanticBaseModel):
    modified_time: datetime
    created_time: datetime

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S')
        }


class ReadBaseModel(SoftDeleteBaseModel, DateTimeBaseModel):
    ...


class UpdateBaseModel(SoftDeleteBaseModel):
    ...


class CreateBaseModel(SoftDeleteBaseModel, DateTimeBaseModel):
    ...

from pydantic import Field

from beanie import Document, Replace, Insert, Delete, before_event, after_event

from datetime import datetime


class BaseModel(Document):
    created_at: str = Field(default_factory=datetime.now)
    updated_at: str | None = None
    deleted_at: str | None = None
    deleted: bool = Field(default=False)

    class Settings:
        validate_on_save = True

    @staticmethod
    async def datetime_formatter(dt: datetime):
        return dt.strftime("%m-%d-%Y %H:%M:%S")

    @before_event(Insert)
    async def set_datetime_formats(self):
        fields = self.__fields__

        for field in fields.keys():

            if fields.get(field).type_ is datetime:
                took_value = self.__dict__[field]

                if took_value:
                    setattr(self, field, await self.datetime_formatter(took_value))

    @after_event(Replace)
    async def set_updated_at(self):
        self.updated_at = await self.datetime_formatter(datetime.now())

    @before_event(Delete)
    async def set_deleted_at(self):
        # TODO: soft delete should handle here
        self.deleted_at = await self.datetime_formatter(datetime.now())
        self.deleted = True

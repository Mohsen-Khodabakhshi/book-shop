from beanie import Document

from lib import exceptions


class BaseCRUD:
    def __init__(self, model):
        self.model: Document = model

    async def get(self, **kwargs):
        document = await self.model.find_one(kwargs)
        if not document:
            raise exceptions.NotFound
        return document

    async def create(self, **kwargs):
        document = await self.model(**kwargs).insert()  # noqa
        return document

    async def get_and_update(self, filter_: dict, update_fields: dict):
        document = await self.get(**filter_)

        for key, value in update_fields.items():
            setattr(document, key, value)

        return await document.save()

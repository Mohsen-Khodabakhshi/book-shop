from beanie import Document


class BaseCRUD:
    def __init__(self, model):
        self.model: Document = model

    async def get(self, **kwargs):
        document = await self.model.find_one(kwargs)
        return document

    async def create(self, **kwargs):
        document = await self.model(**kwargs).insert() # noqa
        return document

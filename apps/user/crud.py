from services.db.mongo.crud import BaseCRUD as MongoBaseCRUD

from apps.user.models import User
from apps.user.schema import ClientRegisterSchema


class UserCRUD(MongoBaseCRUD):
    async def create_new_user(self, user: ClientRegisterSchema):
        document = await self.model(**user.dict()).insert()  # noqa
        return document


user_crud = UserCRUD(User)

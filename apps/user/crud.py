from services.db.mongo.crud import BaseCRUD as MongoBaseCRUD

from apps.user.models import User
from apps.user.schema import UserRegisterSchema

from beanie.exceptions import UniqueFieldExists

from fastapi import status, HTTPException


class UserCRUD(MongoBaseCRUD):
    async def create_new_user(self, user: UserRegisterSchema):
        try:
            document = await self.model(**user.dict()).insert()  # noqa
        except UniqueFieldExists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        return document


user_crud = UserCRUD(User)

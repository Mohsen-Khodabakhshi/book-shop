from services.db.mongo.crud import BaseCRUD as MongoBaseCRUD

from .models import UserModel


class UserCRUD(MongoBaseCRUD):
    ...


user_crud = UserCRUD(UserModel)

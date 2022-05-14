from services.db.mongo.crud import BaseCRUD as MongoBaseCRUD

from .models import User


class UserCRUD(MongoBaseCRUD):
    ...


user_crud = UserCRUD(User)

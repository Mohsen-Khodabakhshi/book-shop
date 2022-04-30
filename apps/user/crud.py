from services.db.mongo.crud import BaseCRUD as MongoBaseCRUD

from main.config import db_settings

from .models import User


class UserCRUD(MongoBaseCRUD):
    ...


user_create = UserCRUD(
    create_model=User,
    update_model=User,
    read_model=User,
)

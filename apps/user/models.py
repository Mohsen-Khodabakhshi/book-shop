from services import global_services

from umongo import Document, fields
from umongo.frameworks import MotorAsyncIOInstance


db = global_services.DB
instance = MotorAsyncIOInstance(db)


@instance.register
class UserModel(Document):
    name = fields.StringField()

    class Meta:
        collection = db.user

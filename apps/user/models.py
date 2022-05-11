from services import global_services

from lib.common_model import BaseModel

from umongo import fields


db = global_services.DB
instance = global_services.instance


@instance.register
class UserModel(BaseModel):
    first_name = fields.StringField(allow_none=True)
    last_name = fields.StringField(allow_none=True)
    email = fields.EmailField(allow_none=False, unique=True)
    password = fields.StringField(allow_none=False)

    class Meta:
        collection = db.user

from services import global_services

from lib.common_model import BaseDocumentModel, BaseEmbeddedDocumentModel
from lib.regex import iran_phone_number, only_letters

from umongo import fields, validate


db = global_services.DB
instance = global_services.instance


@instance.register
class AddressModel(BaseEmbeddedDocumentModel):
    title = fields.StringField(allow_none=False)
    line_1 = fields.StringField(allow_none=False)
    line_2 = fields.StringField(allow_none=True)
    post_code = fields.StringField(allow_none=False)
    phone = fields.StringField(allow_none=True)
    additions = fields.StringField(allow_none=True)


@instance.register
class UserModel(BaseDocumentModel):
    first_name = fields.StringField(
        allow_none=True,
        validate=[
            validate.Regexp(only_letters),
        ],
    )
    last_name = fields.StringField(
        allow_none=True,
        validate=[
            validate.Regexp(only_letters),
        ],
    )
    email = fields.EmailField(allow_none=False, unique=True)
    password = fields.StringField(allow_none=False)
    addresses = fields.EmbeddedField(allow_none=True, embedded_document=AddressModel)
    avatar = fields.UrlField(allow_none=True)
    phone_number = fields.StringField(
        allow_none=True,
        validate=[
            validate.Regexp(iran_phone_number),
        ],
    )
    national_code = fields.StringField(unique=True, allow_none=True)

    class Meta:
        collection = db.user

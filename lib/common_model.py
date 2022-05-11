from umongo import Document, fields

from services import global_services

db = global_services.DB
instance = global_services.instance


@instance.register
class BaseModel(Document):
    created_at = fields.DateTimeField(allow_none=True)
    updated_at = fields.DateTimeField(allow_none=True)
    deleted_at = fields.DateTimeField(allow_none=True)
    deleted = fields.BooleanField(default=False)

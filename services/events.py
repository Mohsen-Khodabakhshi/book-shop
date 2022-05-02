from services.db.mongo.connection import Connection

from main.config import db_settings

mongo_connection = Connection(
    host=db_settings.host,
    port=db_settings.port,
    auth=db_settings.auth,
    user=db_settings.user,
    pwd=db_settings.pwd,
    name=db_settings.name,
)


async def initialize_db():
    return mongo_connection.db


def sync_initialize_db():
    return mongo_connection.db

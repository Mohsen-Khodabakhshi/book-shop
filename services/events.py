from services.db.mongo.connection import Connection

from main.config import db_settings


async def initialize_db():
    return Connection(
        host=db_settings.host,
        port=db_settings.port,
        auth=db_settings.auth,
        user=db_settings.user,
        pwd=db_settings.pwd,
        name=db_settings.name,
    ).db

from umongo.frameworks.motor_asyncio import MotorAsyncIOInstance

from typing import Any
from .events import sync_initialize_db, initialize_db


async def umongo_instance():
    db = await initialize_db()
    return MotorAsyncIOInstance(db)


def sync_umongo_instance():
    db = sync_initialize_db()
    return MotorAsyncIOInstance(db)


class Services(object):
    DB: Any = sync_initialize_db()
    LOGGER: Any | None = None
    instance: Any = sync_umongo_instance()


global_services = Services()

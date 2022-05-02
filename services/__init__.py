from typing import Any
from .events import sync_initialize_db


class Services(object):
    DB: Any = sync_initialize_db()
    LOGGER: Any | None = None


global_services = Services()

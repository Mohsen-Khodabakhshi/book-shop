from typing import Any
from .events import sync_initialize_db


class Services(object):
    DB: Any | None = sync_initialize_db()


global_services = Services()

from typing import Any
from .events import initialize_db


class Services(object):
    DB: Any = None


global_services = Services()

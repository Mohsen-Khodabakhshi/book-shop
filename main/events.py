import services

from typing import Callable

from services import events


def create_start_app_handler() -> Callable:
    async def start_app() -> None:
        services.global_services.DB = await events.initialize_db()

    return start_app

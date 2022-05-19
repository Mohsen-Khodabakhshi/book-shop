import services

from beanie import init_beanie

from typing import Callable

from services import events

from apps import application_models


def create_start_app_handler() -> Callable:
    async def start_app() -> None:
        services.global_services.LOGGER = await events.initialize_logger()
        services.global_services.LOGGER.info("logger ok :)")

        services.global_services.DB = await events.initialize_db()
        services.global_services.LOGGER.info("database connected :)")

        await initialize_models_and_indexes(services.global_services.DB)
        services.global_services.LOGGER.info("database models and indexes ok :)")

    return start_app


async def initialize_models_and_indexes(db):
    await init_beanie(database=db, document_models=application_models)

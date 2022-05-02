import services

from fastapi import Request
from fastapi.responses import JSONResponse

from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from typing import Callable

from services import events

from .config import JWTSettings

from apps import application_models


async def ensure_db_indexes(models):
    for model in models:
        await model.ensure_indexes()


def create_start_app_handler() -> Callable:
    async def start_app() -> None:
        services.global_services.DB = await events.initialize_db()
        await ensure_db_indexes(application_models)

    return start_app


def config_jwt_auth(app):
    @AuthJWT.load_config
    def get_config():
        return JWTSettings()

    @app.exception_handler(AuthJWTException)
    def authjwt_exception_handler(request: Request, exc: AuthJWTException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message}
        )

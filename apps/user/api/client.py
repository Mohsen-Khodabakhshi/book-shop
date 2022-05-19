from fastapi import APIRouter, status, Depends

from apps.user.controller import UserController
from apps.user.schema import (
    ClientRegisterSchema,
    ClientShortDetailSchema,
    ClientLoginSchema,
    ClientAuthTokenSchema,
)

from main.config import JWTSettings

from lib.jwt import JWTHandler

client_router = APIRouter()
user_controller = UserController()
jwt = JWTHandler(JWTSettings().secret_key)


@client_router.post(
    "/register",
    response_model=ClientShortDetailSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register(user: ClientRegisterSchema):
    return await user_controller.register(user=user)


@client_router.post(
    "/login",
    response_model=ClientAuthTokenSchema,
    status_code=status.HTTP_200_OK,
)
async def login(user: ClientLoginSchema):
    return await user_controller.login(user=user)


@client_router.get(
    "",
    response_model=ClientShortDetailSchema,
    status_code=status.HTTP_200_OK,
)
async def profile(user=Depends(jwt.auth_wrapper)):
    return await user_controller.profile(user=user)

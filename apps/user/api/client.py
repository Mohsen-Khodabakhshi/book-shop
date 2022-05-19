from fastapi import APIRouter, Depends, status

from fastapi_jwt_auth import AuthJWT

from apps.user.controller import UserController
from apps.user.schema import (
    ClientRegisterSchema,
    ClientShortDetailSchema,
    ClientLoginSchema,
    ClientAuthTokenSchema,
)

client_router = APIRouter()
user_controller = UserController()


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
async def login(user: ClientLoginSchema, authorize: AuthJWT = Depends()):
    return await user_controller.login(user=user, authorize=authorize)

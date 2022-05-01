from fastapi import APIRouter, Depends

from fastapi_jwt_auth import AuthJWT

from apps.user.controller import UserController
from apps.user.schema import TestSchema

client_router = APIRouter()
user_controller = UserController()


@client_router.post("/login")
async def login(user: TestSchema, authorize: AuthJWT = Depends()):
    return await user_controller.login(user=user, authorize=authorize)

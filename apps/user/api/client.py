from fastapi import APIRouter, Depends

from fastapi_jwt_auth import AuthJWT

from apps.user.controller import UserController
from apps.user.schema import TestSchema
from apps.user.crud import user_crud

client_router = APIRouter()
user_controller = UserController()


@client_router.post("/login")
async def login(user: TestSchema, authorize: AuthJWT = Depends()):
    return await user_controller.login(user=user, authorize=authorize)


@client_router.get('')
async def home():
    print(await user_crud.get(name="mohsen"))
    return {"name": "name"}

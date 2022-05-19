from fastapi import APIRouter, Depends, status

from fastapi_jwt_auth import AuthJWT

from apps.user.controller import UserController
from apps.user.schema import UserRegisterSchema, UserShortDetailSchema
from apps.user.crud import user_crud

client_router = APIRouter()
user_controller = UserController()


@client_router.post("/register", response_model=UserShortDetailSchema, status_code=status.HTTP_201_CREATED)
async def register(user: UserRegisterSchema):
    return await user_controller.register(user=user)


@client_router.get('')
async def home():
    # print(await user_crud.create(name="mohsen"))
    # doc = await user_crud.get(name="mohsen")
    # doc = await user_crud.get_and_update(filter_={"name": "Hasan"}, update_fields={"name": "Hasan"})
    # print(doc.json())
    return {"name": "name"}

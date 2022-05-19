from fastapi import HTTPException, Depends

from fastapi_jwt_auth import AuthJWT

from main.config import app_settings

from apps.user.schema import UserRegisterSchema
from apps.user.crud import user_crud

from lib.encoder import Password

password_encoder = Password()


class UserController:
    @staticmethod
    async def register(user: UserRegisterSchema):
        user.password = await password_encoder.encrypt(user.password, app_settings.password_hashing_key)
        user = await user_crud.create_new_user(user)
        return user
# class UserController:
#     @staticmethod
#     async def login(user: UserRegisterSchema, authorize: AuthJWT = Depends()):
#         if user.username != "test":
#             raise HTTPException(status_code=401, detail="Bad username or password")
#
#         access_token = authorize.create_access_token(subject=user.username)
#         return {"access_token": access_token}

from fastapi import HTTPException, status


from main.config import app_settings, JWTSettings

from apps.user.schema import (
    ClientRegisterSchema,
    ClientLoginSchema,
    ClientAuthTokenSchema,
)
from apps.user.crud import user_crud

from lib.jwt import JWTHandler
from lib.encoder import Password
from lib import exceptions

from beanie.exceptions import UniqueFieldExists

password_encoder = Password()
jwt = JWTHandler(secret_key=JWTSettings().secret_key)


class UserController:
    @staticmethod
    async def register(user: ClientRegisterSchema):
        user.password = await password_encoder.encrypt(
            user.password, app_settings.password_hashing_key
        )
        try:
            user = await user_crud.create_new_user(user)
        except UniqueFieldExists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        return user

    @staticmethod
    async def login(user: ClientLoginSchema):
        try:
            user_in = await user_crud.get(email=user.email)
        except exceptions.NotFound:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        else:
            if (
                not await password_encoder.decrypt(
                    user_in.password, app_settings.password_hashing_key
                )
                == user.password
            ):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            return ClientAuthTokenSchema(
                access_token=jwt.create_access_token(subject=user_in.username),
                verified=user_in.verified,
            )

    @staticmethod
    async def profile(user):
        try:
            user_in = await user_crud.get(username=user)
        except exceptions.NotFound:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return user_in

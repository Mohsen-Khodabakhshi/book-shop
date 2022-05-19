from fastapi import HTTPException, Depends, status

from fastapi_jwt_auth import AuthJWT

from main.config import app_settings

from apps.user.schema import (
    ClientRegisterSchema,
    ClientLoginSchema,
    ClientAuthTokenSchema,
)
from apps.user.crud import user_crud

from lib.encoder import Password
from lib import exceptions

from beanie.exceptions import UniqueFieldExists

password_encoder = Password()


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
    async def login(user: ClientLoginSchema, authorize: AuthJWT = Depends()):
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
                access_token=authorize.create_access_token(subject=user_in.username),
                refresh_token=authorize.create_refresh_token(subject=user_in.username),
                verified=user_in.verified,
            )

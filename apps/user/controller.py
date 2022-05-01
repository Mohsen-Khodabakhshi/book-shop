from fastapi import HTTPException, Depends

from fastapi_jwt_auth import AuthJWT

from .schema import TestSchema


class UserController:
    @staticmethod
    async def login(user: TestSchema, authorize: AuthJWT = Depends()):
        if user.username != "test":
            raise HTTPException(status_code=401, detail="Bad username or password")

        access_token = authorize.create_access_token(subject=user.username)
        return {"access_token": access_token}

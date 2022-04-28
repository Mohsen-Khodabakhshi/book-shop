from pydantic import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class JWTSettings(BaseSettings):
    token: str = "MyToken"

    class Config:
        env_prefix = "JWT_"


jwt_settings = JWTSettings()

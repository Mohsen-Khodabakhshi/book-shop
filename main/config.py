from pydantic import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class AppSettings(BaseSettings):
    password_hashing_key: bytes

    class Config:
        env_prefix = "APP_"


app_settings = AppSettings()


class JWTSettings(BaseSettings):
    secret_key: str = "MyToken"

    class Config:
        env_prefix = "JWT_"


jwt_settings = JWTSettings()


class DBSettings(BaseSettings):
    host: str = "localhost"
    port: int = 27017
    auth: bool = False
    user: str
    pwd: str
    name: str = "shop"

    class Config:
        env_prefix = "DB_"


db_settings = DBSettings()

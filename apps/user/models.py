from lib.common_model import BaseModel


class User(BaseModel):
    name: str
    description: str | None = None

    class Settings:
        name = "users"

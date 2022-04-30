from lib.common_model import BaseModel


class User(BaseModel):
    name: str | None = "mohsen"

    class Config:
        table = "user"

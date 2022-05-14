from beanie import Document


class User(Document):
    name: str
    description: str | None = None

    class Settings:
        name = "users"

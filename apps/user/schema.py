from pydantic import BaseModel


class TestSchema(BaseModel):
    username: str

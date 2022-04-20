from pydantic import BaseModel


class TestSchemaOut(BaseModel):
    hello: str

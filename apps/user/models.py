from lib.common_model import BaseModel
from lib.regex import *

from typing import List

from pydantic import Field, HttpUrl

from beanie import Link


class Address(BaseModel):
    title: str = Field(min_length=1)
    post_code: str | None = None
    line_1: str = Field(min_length=1)
    line_2: str | None = None
    phone: str | None = None

    class Settings:
        name = "addresses"


class User(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    username: str = Field(regex=only_letters)
    phone_number: str | None = Field(regex=iran_phone_number)
    email: str = Field(regex=email)
    password: str = Field(min_length=1)
    avatar: HttpUrl | None = None
    verified: bool = False
    addresses: List[Link[Address]] | None = None

    class Settings:
        name = "users"

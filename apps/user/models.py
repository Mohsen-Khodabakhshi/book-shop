from lib.common_model import BaseModel
from lib import regex

from typing import List

from pydantic import Field, HttpUrl, EmailStr

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
    first_name: str | None = Field(None, max_length=25)
    last_name: str | None = Field(None, max_length=35)
    username: str = Field(regex=regex.only_letters)
    phone_number: str | None = Field(regex=regex.iran_phone_number)
    email: EmailStr
    password: str = Field(min_length=1)
    avatar: HttpUrl | None = None
    verified: bool = False
    addresses: List[Link[Address]] | None = []

    class Settings:
        name = "users"
        unique_fields = ['username', 'email']

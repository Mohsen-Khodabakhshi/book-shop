from pydantic import BaseModel, HttpUrl, Field, EmailStr

from lib import regex


class BaseUserSchema(BaseModel):
    username: str = Field(regex=regex.only_letters)
    email: EmailStr
    first_name: str | None = Field(None, max_length=25)
    last_name: str | None = Field(None, max_length=35)
    phone_number: str | None = Field(None, regex=regex.iran_phone_number)


class UserRegisterSchema(BaseUserSchema):
    password: str


class UserShortDetailSchema(BaseUserSchema):
    avatar: HttpUrl | None = None
    verified: bool

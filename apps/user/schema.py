from pydantic import BaseModel, HttpUrl, Field, EmailStr

from lib import regex


class BaseClientSchema(BaseModel):
    username: str = Field(regex=regex.only_letters)
    email: EmailStr
    first_name: str | None = Field(None, max_length=25)
    last_name: str | None = Field(None, max_length=35)
    phone_number: str | None = Field(None, regex=regex.iran_phone_number)


class ClientShortDetailSchema(BaseClientSchema):
    avatar: HttpUrl | None = None
    verified: bool


class ClientRegisterSchema(BaseClientSchema):
    password: str = Field(min_length=8)


class ClientLoginSchema(BaseModel):
    email: EmailStr
    password: str


class ClientAuthTokenSchema(BaseModel):
    access_token: str
    verified: bool

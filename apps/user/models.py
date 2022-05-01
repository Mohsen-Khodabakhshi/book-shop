from lib.common_model import ReadBaseModel, UpdateBaseModel, CreateBaseModel
from lib import regex

from pydantic import Field, BaseModel

from typing import List


class AddressBaseModel(BaseModel):
    title: str
    line_1: str
    line_2: str | None = None
    city: str
    state: str
    post_code: str
    country: str | None = "iran"

    class Config:
        table = "address"


class AddressReadModel(AddressBaseModel, ReadBaseModel):
    ...


class AddressCreateModel(AddressBaseModel, CreateBaseModel):
    ...


class AddressUpdateModel(AddressBaseModel, UpdateBaseModel):
    title: str | None = None
    line_1: str | None = None
    city: str | None = None
    state: str | None = None
    post_code: str | None = None


class UserBaseSettings(BaseModel):
    notification_by_email: bool | None = True
    two_step_auth: bool | None = False


class UserReadSettings(BaseModel, ReadBaseModel):
    ...


class UserCreateSettings(BaseModel, CreateBaseModel):
    ...


class UserUpdateSettings(BaseModel, UpdateBaseModel):
    ...


class UserBaseModel(BaseModel):
    username: str = Field(min_length=1, max_length=20)
    first_name: str | None = Field(max_length=20, regex=regex.only_letters)
    last_name: str | None = Field(max_length=25, regex=regex.only_letters)
    email: str | None = Field(max_length=55, regex=regex.email)
    is_active: bool | None = True
    is_verified: bool | None = False
    password: str = Field(min_length=1)
    addresses: List[AddressBaseModel] | None = []
    settings: UserBaseSettings | None = {}

    class Config:
        table = "user"


class UserReadModel(UserBaseModel, ReadBaseModel):
    password: str | None = None
    addresses: List[AddressReadModel] | None = []
    settings: UserReadSettings | None = {}


class UserCreateModel(UserBaseModel, CreateBaseModel):
    addresses: List[AddressCreateModel] | None = []
    settings: UserCreateSettings | None = {}


class UserUpdateModel(UserBaseModel, UpdateBaseModel):
    username: str | None = Field(max_length=20)
    password: str | None = None
    addresses: List[AddressUpdateModel] | None = []
    settings: UserUpdateSettings | None = {}

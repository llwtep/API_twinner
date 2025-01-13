from typing import Union

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str = Field(min_length=8)
    model_config = ConfigDict(extra='forbid')


class UserOutputSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    model_config = ConfigDict(extra='forbid')


class UserInLogin(BaseModel):
    email: str
    password: str


class UserWithToken(BaseModel):
    token: str


class UserInUpdate(BaseModel):
    id: int
    first_name: Union[str, None]
    last_name: Union[str, None]
    email: Union[EmailStr, None]
    password: Union[str, None]

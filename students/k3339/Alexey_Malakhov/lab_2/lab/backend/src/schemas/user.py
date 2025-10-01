from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    last_name: str
    first_name: str
    patronymic: str
    passport_number: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id_user: int

    class Config:
        orm_mode = True

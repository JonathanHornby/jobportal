from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import date, datetime
from typing import Optional

class UserBase(BaseModel):
    email: str | None = None
    name: str | None = None
    status: str | None = None
    
    class Config:
        orm_mode = True
    
class UserDetail(UserBase):
    username: str
    email: str | None = None
    name: str | None = None
    disabled: bool | None = None
    
    class Config:
        orm_mode = True

class UserCreate(UserBase):

    class Config:
        orm_mode = True
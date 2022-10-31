from ssl import create_default_context
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import date, datetime
from typing import Optional

class SeekerLogin(BaseModel):
    email: EmailStr
    password: str

class RecruiterLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import date, datetime
from typing import Optional

class User(BaseModel):
    username: str
    email: str | None = None
    first_name: str | None = None
    disabled: bool | None = None
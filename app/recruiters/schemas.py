from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import date, datetime
from typing import Optional

class RecruiterBase(BaseModel):
    email: str | None = None
    company_name: str | None = None
    status: str | None = None
    
    class Config:
        orm_mode = True
    
class RecruiterDetail(RecruiterBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class RecruiterCreate(RecruiterBase):
    password: str

    class Config:
        orm_mode = True
        
class RecruiterCreated(RecruiterBase):
    id: int
    password: str

    class Config:
        orm_mode = True
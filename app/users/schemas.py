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
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True
        

class UserCreated(UserBase):
    password: str
    id: int

    class Config:
        orm_mode = True
        
     
class CreateCoverLetter(BaseModel):
    user_id: int
    name: str
    
    class Config:
        orm_mode = True     
        
        
class CoverLetter(CreateCoverLetter):
    id: int
    created_at: datetime

    
class CVCreate(BaseModel):
    user_id: int
    name: str
    
    class Config:
        orm_mode = True
    
class CV(CVCreate):
    id: int
    created_at: datetime

from pydantic import BaseModel
from datetime import datetime


class JobBase(BaseModel):
    title: str
    industry: str
    category: str
    summary: str
    salary_min: int
    salary_max: int

    class Config:
        orm_mode = True


class JobBasic(JobBase):
    id: int
    poster_id: int
    created_at: datetime
    status: str
    published: bool


class JobCreate(JobBase):
    product_type: int
    valid_duration: int
    company: str
    country: str
    state: str
    city: str
    employment_type: str
    remote_status: str
    salary_currency: str
    content: str
    contact_name: str
    contact_number: str
    perk_car: bool
    perk_visa: bool
    perk_relocation: bool
    perk_days_week: int
    perk_phone: bool
    perk_laptop: bool
    perk_bonus: bool

    class Config:
        orm_mode = True


class JobDetail(JobCreate, JobBasic):

    class Config:
        orm_mode = True
        

class CreateJobApplication(BaseModel):
    recruiter_status: str
    job_id: int
    cv_id: int
    cover_letter_id: int
    
    class Config:
        orm_mode = True


class CreateSavedJob(BaseModel):
    job_id: int
    cv_id: int
    cover_letter_id: int
    
    class Config:
        orm_mode = True        


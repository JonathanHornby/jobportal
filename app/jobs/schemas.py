from pydantic import BaseModel
from app.jobs.models import Job
from datetime import date, datetime

class JobBase(BaseModel):
    id: int
    poster_id: int
    created_at: datetime
    status: str
    published: bool
    title: str
    industry: str
    category: str
    summary: str
    salary_min: int
    salary_max: int

    class Config:
        orm_mode = True

class JobDetail(JobBase):
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
    perk_days_week: bool
    perk_phone: bool
    perk_laptop: bool
    perk_bonus: bool

    class Config:
        orm_mode = True

class JobCreate(JobBase):
    pass
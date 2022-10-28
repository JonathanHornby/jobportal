from pydantic import BaseModel
from app.jobs.models import Job
from datetime import date, datetime


class JobOut(BaseModel):
    id: int
    poster_id: int
    #poster = relationship("Recruiter")
    created_at: datetime
    status: str
    published: bool
    product_type: int
    valid_duration: int
    title: str
    company: str
    country: str
    state: str
    city: str
    industry: str
    category: str
    employment_type: str
    remote_status: str
    salary_min: int
    salary_max: int
    salary_currency: str
    summary: str
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
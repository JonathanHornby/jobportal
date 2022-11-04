from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, column, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..database.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, nullable=False)
    poster_id = Column(Integer, ForeignKey("recruiters.id", ondelete="CASCADE"), nullable=False)
    poster = relationship("Recruiter")
    # applications = relationship("JobApplication")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    status = Column(String, nullable=False, server_default='active')
    published = Column(Boolean, server_default='FALSE', nullable=False)
    product_type = Column(Integer, nullable=False, server_default=text('1'))
    valid_duration = Column(Integer, nullable=False, server_default=text('30'))
    title = Column(Text)
    company = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    industry = Column(String)
    category = Column(String)
    employment_type = Column(String)
    remote_status = Column(String)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    salary_currency = Column(String)
    summary = Column(Text)
    content = Column(Text)
    contact_name = Column(String)
    contact_number = Column(String)
    perk_car = Column(Boolean, nullable=False, server_default=text('False'))
    perk_visa = Column(Boolean, nullable=False, server_default=text('False'))
    perk_relocation = Column(Boolean, nullable=False, server_default=text('False'))
    perk_days_week = Column(Integer, nullable=False, server_default=text('5'))
    perk_phone = Column(Boolean, nullable=False, server_default=text('False'))
    perk_laptop = Column(Boolean, nullable=False, server_default=text('False'))
    perk_bonus = Column(Boolean, nullable=False, server_default=text('False'))
    
class JobApplication(Base):
    __tablename__ = 'job_applications'
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    recruiter_status = Column(String, nullable=False, server_default='new')
    cv_path = Column(String)
    cover_letter_path = Column(String)
    
    
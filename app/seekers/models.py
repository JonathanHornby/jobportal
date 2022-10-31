from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..database.database import Base

class Seeker(Base):
    __tablename__ = "seekers"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    status = Column(String, nullable=False, server_default='active')
    name = Column(String)

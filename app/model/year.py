from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from .base import Base

class Year_Section(Base):
    __tablename__ = "year_section"
    id = Column(Integer, primary_key= True)
    name = Column(Integer, nullable=False)
    year_section= Column(String,nullable=False)
    staff = relationship("year_section", cascade = "all, delete-orphan")
    created_at= Column(Integer)
    created_by= Column(String)
    updated_by= Column(String)
    updated_at= Column(Integer)
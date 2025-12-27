from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    role = relationship("role", cascade = "all, delete-orphan")
    created_at= Column(Integer)
    created_by= Column(String)
    updated_by= Column(String)
    updated_at= Column(Integer)
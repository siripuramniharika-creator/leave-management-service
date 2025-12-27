from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Student(Base):
    __tablename__ = "student"
    roll_no = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey("year_section.id", ondelete="CASCADE"), nullable=False)
    department = Column(String, nullable=False)
    leave_days = Column(Integer)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id", ondelete="CASCADE"), nullable= False)
    security_question = Column(String)
    answer = Column(String)
    student = relationship("student", cascade = "all, delete-orphan")
    created_at= Column(Integer)
    created_by= Column(String)
    updated_by= Column(String)
    updated_at= Column(Integer)

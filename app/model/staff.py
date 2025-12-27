from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Staff(Base):
    __tablename__ = "staff"
    staff_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    department=Column(String, nullable=False)
    designation=Column(String, nullable=False)
    password = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey("year_section.id", ondelete="CASCADE"), nullable=False)
    role_id = Column(Integer, ForeignKey("role.id", ondelete="CASCADE"), nullable= False)
    leave_days = Column(Integer)
    security_question = Column(String)
    answer = Column(String)
    staff = relationship("staff", cascade = "all, delete-orphan")
    created_at= Column(Integer)
    created_by= Column(String)
    updated_by= Column(String)
    updated_at= Column(Integer)
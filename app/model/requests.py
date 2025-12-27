from sqlalchemy import Integer, Column, String, ForeignKey
from .base import Base


class LeaveRequests(Base):
    __tablename__ = "requests"
    id= Column(Integer, auto_increment=True, primary_key=True, nullable= False)
    staff_id = Column(String, ForeignKey("staff.staff_id", ondelete="CASCADE"), nullable= False)
    student_id = Column(String, ForeignKey("student.roll_no", ondelete="CASCADE"), nullable= False)
    from_date = Column(Integer)
    to_date = Column(Integer)
    reason = Column(String)
    status = Column(String)
    created_at= Column(Integer)
    created_by= Column(String)
    updated_by= Column(String)
    updated_at= Column(Integer)
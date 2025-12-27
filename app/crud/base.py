from sqlalchemy.orm import Session
from . import model, schema

def create_student(db: Session,student : schema.StudentCreate):
    db_student =model.Student(roll_no=student.roll_no,name=student.name,class_id=student.class_id,department=student.department,leave_days=student.leave_days,password=student.password,role_id=student.role_id,security_question=student.security_question,answer=student.answer,created_at=student.created_at,created_by=student.created_by,updated_by=student.updated_by,updated_at=student.updated_at)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db:Session):
    return db.query(model.Student).all()

def update_student(db:Session,roll_no:str,student:schema.UpdateStudent):
    db_student = db.query(model.Student).filter(model.Student.roll_no == roll_no).first()
    if student.name is not None:
        db_student.name=student.name
    if student.email is not None:
        db_student.email=student.email
    if student.department is not None:
        db_student.department=student.department
    if student.contact_number is not None:
        db_student.contact_number=student.contact_number
    if student.date_of_birth is not None:
        db_student.date_of_birth=student.date_of_birth
    if student.age is not None:
        db_student.age=student.age
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, roll_no:str):
    student=db.query(model.Student).filter(model.Student.roll_no == roll_no).first()
    db.delete(student)
    db.commit()

def create_staff(db: Session,staff : schema.StaffCreate):
    db_staff =model.Staff(staff_id=staff.staff_id,name=staff.name,department=staff.department,designation=staff.designation,password=staff.password,class_id=staff.class_id,role_id=staff.role_id,leave_days=staff.leave_days,security_question=staff.security_question,answer=staff.answer,created_at=staff.created_at,created_by=staff.created_by,updated_by=staff.updated_by,updated_at=staff.updated_at)
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def get_staff(db:Session):
    return db.query(model.Staff).all()

def update_staff(db:Session,staff_id:str,staff:schema.UpdateStaff):
    db_staff = db.query(model.Staff).filter(model.Staff.staff_id == staff_id).first()
    if staff.name is not None:
        db_staff.name=staff.name
    if staff.email is not None:
        db_staff.email=staff.email
    if staff.username is not None:
        db_staff.username=staff.username
    if staff.department is not None:
        db_staff.department=staff.department
    if staff.designation is not None:
        db_staff.designation=staff.designation
    if staff.contact_no is not None:
        db_staff.contact_no=staff.contact_no
    if staff.date_of_birth is not None:
        db_staff.date_of_birth=staff.date_of_birth
    if staff.age is not None:
        db_staff.age=staff.age
    db.commit()
    db.refresh(db_staff)
    return db_staff

def delete_staff(db: Session, staff_id:str):
    staff=db.query(model.Staff).filter(model.Staff.staff_id == staff_id).first()
    db.delete(staff)
    db.commit()


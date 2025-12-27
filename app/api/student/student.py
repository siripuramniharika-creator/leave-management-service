from fastapi import Request,APIRouter
from schema.student import AddStudent,UpdateStudent

router= APIRouter()

@router.post("/student",
    tags= ["Student Management"],
    name = "Add Student"

)
def add_student(request:Request,payload:AddStudent):
    return {"status": "OK"}

@router.put("/student",
    tags= ["Student Management"],
    name = "Update Student"

)
def update_student(request: Request, payload: UpdateStudent,roll_number:int ):
    return {"status": "OK"}

@router.get("/student",
    tags= ["Student Management"],
    name = "Get Student"

)
def get_student(request: Request, roll_number: str= None, name: str = None):
    return {"status":"OK"}

@router.delete("/student",
    tags= ["Student Management"],
    name = "Delete Student"

)
def delete_student(request: Request, roll_number: str= None):
    return {"status":"OK"}
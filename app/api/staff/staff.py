from fastapi import Request, APIRouter
from schema.staff import AddStaff, UpdateStaff

router = APIRouter()
@router.post("/staff",
    tags= ["Staff Management"],
    name = "Add Staff"

)
def add_staff(request: Request, payload: AddStaff):
    return {"status": "OK"}

@router.put("/staff",
    tags= ["Staff Management"],
    name = "Update Staff"

)
def update_staff(request: Request, payload: UpdateStaff,staff_id:int):
    return {"status": "OK"}

@router.get("/staff",
    tags= ["Staff Management"],
    name = "Get Staff"

)
def get_staff(request: Request, staff_id: int= None, name: str = None):
    return {"status":"OK"}

@router.delete("/staff",
    tags= ["Staff Management"],
    name = "Delete Staff"

)
def delete_staff(request: Request, staff_id: int= None):
    return {"status":"OK"}
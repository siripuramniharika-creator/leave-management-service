from fastapi import Request,APIRouter

router= APIRouter()

@router.get("/leave-history",
    tags= ["Leave History"],
    name = "Get Student/Staff leave_history"

)
def get_student(request: Request, roll_number: str= None, staff_id:str=None,):
    return {"status":"OK"}
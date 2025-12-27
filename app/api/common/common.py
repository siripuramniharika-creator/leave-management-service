from fastapi import Request, APIRouter
from schema.common import UpdatePassword

router = APIRouter()
@router.put("/common",
    tags= ["Forgot-Password Management"],
    name = "Update password"

)
def update_password(request: Request, payload: UpdatePassword,username:str):
    return {"status": "OK"}

# @router.get("/common",
#     tags= ["Forgot-Password Management"],
#     name = "Get password"

# )
# def get_password(request: Request, username: str):
#     return {"status":"OK"}
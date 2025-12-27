from fastapi import Request, APIRouter

router = APIRouter()
@router.get("/utils",
    tags= ["Authentication Management"],
    name = "Authentication-role"

)
def authentication_role(request: Request, role: str,username:str, password: str):
    return {"status":"OK"}
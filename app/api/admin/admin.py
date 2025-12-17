from fastapi import Request, APIRouter

router = APIRouter()

@router.get("/health",
            tags= ["Admin Management"]
)
def health_check(request: Request):
    return {"status": "OKs"}
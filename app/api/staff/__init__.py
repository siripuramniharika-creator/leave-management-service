from fastapi import APIRouter
from . import staff

router = APIRouter()

router.include_router(staff.router)

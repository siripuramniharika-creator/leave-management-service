from fastapi import APIRouter
from . import leave_history

router = APIRouter()

router.include_router(leave_history.router)
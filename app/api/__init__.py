from fastapi import APIRouter
from . import staff
from . import student
from . import common
from . import utils
from . import leave_history

api_router = APIRouter()

def get_routes():
    api_router.include_router(staff.router)
    api_router.include_router(student.router)
    api_router.include_router(common.router)
    api_router.include_router(utils.router)
    api_router.include_router(leave_history.router)
    return api_router


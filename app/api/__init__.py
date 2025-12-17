from fastapi import APIRouter
from . import admin

api_router = APIRouter()

def get_routes():
    api_router.include_router(admin.router)
    return api_router


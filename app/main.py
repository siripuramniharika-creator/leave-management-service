from fastapi import FastAPI,Depends
from api import get_routes

def init_app():
    app = FastAPI(
        title="FastAPI",
        description="Basic FastAPI template",
        version="1.0.0"
    )
    return app


app = init_app()
app.include_router(get_routes())
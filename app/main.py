from fastapi import FastAPI
from api import get_routes
import uvicorn

def init_app():
    app = FastAPI(
        title="FastAPI Starter",
        description="Basic FastAPI template",
        version="1.0.0"
    )
    return app


app = init_app()
app.include_router(get_routes())
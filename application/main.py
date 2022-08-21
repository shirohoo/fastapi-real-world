from fastapi import FastAPI

from application.routes import index


def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(index.router)
    return _app


app = create_app()

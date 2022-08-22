from fastapi import FastAPI

from application.routes import index

app = FastAPI()
app.include_router(index.router, tags=["index"])

"""Main API entry point for the vinyl collection tool."""

from http import HTTPStatus
from fastapi import FastAPI

from api.controllers import routers

app = FastAPI()

for router in routers:
    app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/favicon.ico")
def read_favicon():
    return HTTPStatus.NO_CONTENT

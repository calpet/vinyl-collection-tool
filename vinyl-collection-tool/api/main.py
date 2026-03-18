"""Main API entry point for the vinyl collection tool."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
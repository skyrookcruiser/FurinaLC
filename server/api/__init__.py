from fastapi import FastAPI
from . import CheckSeasonLog


def add_api_handler(app: FastAPI):
    app.post("/api/CheckSeasonLog")(CheckSeasonLog.handle)

from fastapi import FastAPI
from . import CheckSeasonLog, FetchLatestSynchronousData, LoadUserDataAll


def add_api_handler(app: FastAPI):
    app.post("/api/FetchLatestSynchronousData")(FetchLatestSynchronousData.handle)
    app.post("/api/LoadUserDataAll")(LoadUserDataAll.handle)
    app.post("/api/CheckSeasonLog")(CheckSeasonLog.handle)

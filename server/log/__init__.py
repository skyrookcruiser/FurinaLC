from fastapi import FastAPI
from . import GetMailLogAll


def add_log_handler(app: FastAPI):
    app.post("/log/GetMailLogAll")(GetMailLogAll.handle)

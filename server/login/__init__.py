from fastapi import FastAPI
from . import CheckClientVersion


def add_login_handler(app: FastAPI):
    app.post("/login/CheckClientVersion")(CheckClientVersion.handle)

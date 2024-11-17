from fastapi import FastAPI
from . import Schnajang


def add_middleware(app: FastAPI):
    app.middleware("http")(Schnajang.handle)

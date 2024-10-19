from fastapi import FastAPI
from uvicorn import run
from server.adder import (
    add_middleware,
    add_iap_routes,
    add_login_routes,
    add_api_routes,
)
from server.config import C


def start_server(app: FastAPI, config: tuple):
    add_middleware(app)
    add_login_routes(app)
    add_api_routes(app)
    add_iap_routes(app)
    run(app, host=config[0], port=config[1])


if __name__ == "__main__":
    start_server(FastAPI(), C)

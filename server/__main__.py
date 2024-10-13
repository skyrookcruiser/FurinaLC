from fastapi import FastAPI
from uvicorn import run
from server.adder import (
    add_middleware,
    add_iap_routes,
    add_login_routes,
    add_api_routes,
)

S = (FastAPI(), "127.0.0.1", 21000)


def decorate(app: FastAPI):
    add_middleware(app)
    add_login_routes(app)
    add_api_routes(app)
    add_iap_routes(app)


def start_server(config: tuple = S):
    decorate(config[0])
    run(config[0], host=config[1], port=config[2])


if __name__ == "__main__":
    start_server()

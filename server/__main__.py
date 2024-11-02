from fastapi import FastAPI
from server.middleware import add_middleware
from server.api import add_api_handler
from server.iap import add_iap_handler
from server.login import add_login_handler
from server.config import HOST, PORT
import uvicorn


def start_server():
    app = FastAPI()
    add_middleware(app)
    add_api_handler(app)
    add_iap_handler(app)
    add_login_handler(app)

    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    start_server()

from fastapi import FastAPI
from . import UpdateSteamPendingPurchase


def add_iap_handler(app: FastAPI):
    app.post("/iap/UpdateSteamPendingPurchase")(UpdateSteamPendingPurchase.handle)

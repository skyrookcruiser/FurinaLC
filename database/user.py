from pymongo import DESCENDING
from pydantic import BaseModel
from typing import Optional
from database.client import db
from utils import get_date_time


class FurinaUser(BaseModel):
    uid: int
    token: str
    register_date: str


user_collection = db["users"]


def create_user(uid: int, token: str) -> int:
    try:
        user = FurinaUser(uid=uid, token=token, register_date=get_date_time()).dict()

        user_collection.insert_one(user)
        return uid
    except Exception as e:
        print("WARN:     " + str(e))
        return -1


def check_user(token: str) -> Optional[int]:
    try:
        existing_user = user_collection.find_one({"token": token})
        if existing_user:
            return existing_user["uid"]

        max_user = user_collection.find_one(sort=[("uid", DESCENDING)])
        new_uid = max_user["uid"] + 1 if max_user else 1

        return create_user(new_uid, token)

    except Exception as e:
        print("WARN:     " + str(e))
        return None

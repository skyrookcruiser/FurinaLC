from pymongo import DESCENDING
from pydantic import BaseModel
from typing import Optional
from database.client import db
from utils import get_date_time
from database.ego import insert_ego_formats
from database.personality import insert_personality_formats


class FurinaUser(BaseModel):
    uid: int
    token: str
    register_date: str
    account_type: str


user_collection = db["users"]


def create_user(uid: int, token: str, account_type: str) -> int:
    try:
        user = FurinaUser(
            uid=uid,
            token=token,
            register_date=get_date_time(),
            account_type=account_type,
        ).dict()
        user_collection.insert_one(user)
        insert_ego_formats(uid)
        insert_personality_formats(uid)

        return uid
    except Exception as e:
        print("WARN:     " + str(e))

        return -1


def check_user(token: str, account_type: str = "unk") -> Optional[int]:
    try:
        existing_user = user_collection.find_one({"token": token})
        if existing_user:
            return existing_user["uid"]

        max_user = user_collection.find_one(sort=[("uid", DESCENDING)])
        new_uid = max_user["uid"] + 1 if max_user else 1

        return create_user(new_uid, token, account_type)
    except Exception as e:
        print("WARN:     " + str(e))

        return None

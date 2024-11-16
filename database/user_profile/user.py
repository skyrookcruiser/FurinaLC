from pymongo import DESCENDING
from pydantic import BaseModel
from typing import Optional
from database.client import db
from utils import get_date_time
from limbus.formats import UserInfo
from database.user_stuff.ego import insert_ego_formats
from database.user_stuff.personality import insert_personality_formats
from database.user_stuff.item import insert_item_formats
from database.user_stuff.announcer import insert_announcer_format
from database.user_stuff.formation import insert_formation_formats
from database.user_profile.banner import insert_user_banner_data_formats
from database.user_profile.ticket import insert_profile_ticket_data
from database.user_profile.profile import (
    insert_user_public_profile_with_supporters_format,
)
# from database.lobbycg import insert_lobby_cg_format

user_collection = db["users"]


class FurinaUserInfo(BaseModel):
    uid: int
    level: int
    exp: int
    stamina: int
    last_stamina_recover: str
    current_storybattle_nodeid: int
    first_login_today: str
    token: str
    register_date: str
    account_type: str


def create_user(uid: int, token: str, account_type: str) -> int:
    try:
        curr_date = get_date_time()
        user = FurinaUserInfo(
            uid=uid,
            token=token,
            register_date=curr_date,
            account_type=account_type,
            level=302,
            exp=0,
            stamina=183,
            last_stamina_recover=curr_date,
            current_storybattle_nodeid=-1,
            first_login_today=curr_date,
        ).dict()

        user_collection.insert_one(user)

        insert_ego_formats(uid)
        insert_personality_formats(uid)
        insert_item_formats(uid)
        insert_announcer_format(uid)
        insert_formation_formats(uid)
        insert_user_banner_data_formats(uid)
        insert_profile_ticket_data(uid)
        insert_user_public_profile_with_supporters_format(uid)
        # insert_lobby_cg_format(uid)

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


def get_user_info_by_uid(uid: int) -> Optional[UserInfo]:
    try:
        doc = user_collection.find_one({"uid": uid})

        if doc:
            return UserInfo(
                uid=doc["uid"],
                level=doc["level"],
                exp=doc["exp"],
                stamina=doc["stamina"],
                last_stamina_recover=doc["last_stamina_recover"],
                current_storybattle_nodeid=doc["current_storybattle_nodeid"],
                first_login_today=doc["first_login_today"],
            )

        return None

    except Exception as e:
        print("WARN:     " + str(e))

        return None


def update_user_info(
    uid: int,
    level: Optional[int] = None,
    exp: Optional[int] = None,
    stamina: Optional[int] = None,
    last_stamina_recover: Optional[str] = None,
    current_storybattle_nodeid: Optional[int] = None,
    first_login_today: Optional[str] = None,
) -> bool:
    try:
        update_fields = {}
        if level is not None:
            update_fields["level"] = level
        if exp is not None:
            update_fields["exp"] = exp
        if stamina is not None:
            update_fields["stamina"] = stamina
        if last_stamina_recover is not None:
            update_fields["last_stamina_recover"] = last_stamina_recover
        if current_storybattle_nodeid is not None:
            update_fields["current_storybattle_nodeid"] = current_storybattle_nodeid
        if first_login_today is not None:
            update_fields["first_login_today"] = first_login_today

        if update_fields:
            user_collection.update_one({"uid": uid}, {"$set": update_fields})

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False

from pydantic import BaseModel
from database.client import db
from resources.announcer import create_announcer_format
from limbus.formats import AnnouncerFormat
from typing import List, Optional

announcer_collection = db["announcers"]


class AnnouncerFormatWithUID(BaseModel):
    uid: int
    announcer_ids: List[int]
    cur_announcer_ids: List[int]


def insert_announcer_format(uid: int) -> None:
    try:
        announcer_format = create_announcer_format()

        announcer_format_with_uid = AnnouncerFormatWithUID(
            uid=uid,
            announcer_ids=announcer_format.announcer_ids,
            cur_announcer_ids=announcer_format.cur_announcer_ids,
        )

        announcer_collection.insert_one(announcer_format_with_uid.dict())
    except Exception as e:
        print("WARN:     " + str(e))


def get_announcer_format_by_uid(uid: int) -> Optional[AnnouncerFormat]:
    try:
        doc = announcer_collection.find_one({"uid": uid})

        if doc:
            return AnnouncerFormat(
                announcer_ids=doc["announcer_ids"],
                cur_announcer_ids=doc["cur_announcer_ids"],
            )

        return None

    except Exception as e:
        print("WARN:     " + str(e))

        return None


def update_announcer_format(
    uid: int, new_cur_announcer_ids: Optional[List[int]] = None
) -> bool:
    try:
        if new_cur_announcer_ids is not None:
            result = announcer_collection.update_one(
                {"uid": uid}, {"$set": {"cur_announcer_ids": new_cur_announcer_ids}}
            )

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False

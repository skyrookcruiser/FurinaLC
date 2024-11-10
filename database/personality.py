from pydantic import BaseModel
from database.client import db
from limbus.formats import PersonalityFormat
from resources.personality import create_personality_format_list
from typing import List, Optional

personality_collection = db["personalities"]


class PersonalityFormatWithUID(BaseModel):
    uid: int
    personality_id: int
    level: int = 0
    exp: int = 0
    gacksung: int = 0
    order_id: int = 0
    gacksung_illust_type: int = 0
    acquire_time: str = ""


def insert_personality_formats(uid: int) -> None:
    try:
        personality_format_list = create_personality_format_list()

        personality_format_with_uid_list = [
            PersonalityFormatWithUID(
                uid=uid,
                personality_id=personality_format.personality_id,
                level=personality_format.level,
                exp=personality_format.exp,
                gacksung=personality_format.gacksung,
                order_id=personality_format.order_id,
                gacksung_illust_type=personality_format.gacksung_illust_type,
                acquire_time=personality_format.acquire_time,
            )
            for personality_format in personality_format_list
        ]
        if personality_format_with_uid_list:
            personality_collection.insert_many(
                [pf.dict() for pf in personality_format_with_uid_list]
            )

    except Exception as e:
        print("WARN:     " + str(e))


def get_personality_formats_by_uid(uid: int) -> List[PersonalityFormat]:
    try:
        personality_docs = personality_collection.find({"uid": uid})

        return [
            PersonalityFormat(
                personality_id=doc["personality_id"],
                level=doc["level"],
                exp=doc["exp"],
                gacksung=doc["gacksung"],
                order_id=doc["order_id"],
                gacksung_illust_type=doc["gacksung_illust_type"],
                acquire_time=doc["acquire_time"],
            )
            for doc in personality_docs
        ]

    except Exception as e:
        print("WARN:     " + str(e))

        return []


def update_personality_format(
    uid: int,
    personality_id: int,
    level: Optional[int] = None,
    gacksung: Optional[int] = None,
) -> bool:
    try:
        update_fields = {}
        if level is not None:
            update_fields["level"] = level
        if gacksung is not None:
            update_fields["gacksung"] = gacksung

        if update_fields:
            result = personality_collection.update_one(
                {"uid": uid, "personality_id": personality_id}, {"$set": update_fields}
            )

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False

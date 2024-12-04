from pydantic import BaseModel
from database.client import db
from limbus.formats import PersonalityFormat
from resources.parser.user_stuff.personality import create_personality_format_list
from typing import List, Optional

personality_collection = db["personalities"]


class PersonalityFormatWithUID(BaseModel):
    uid: int
    personality_id: int
    level: int
    exp: int
    gacksung: int
    order_id: int
    gacksung_illust_type: int
    acquire_time: str


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


def get_one_personality_format(
    uid: int, personality_id: int
) -> Optional[PersonalityFormat]:
    try:
        doc = personality_collection.find_one(
            {"uid": uid, "personality_id": personality_id}
        )

        if doc:
            return PersonalityFormat(
                personality_id=doc["personality_id"],
                level=doc["level"],
                exp=doc["exp"],
                gacksung=doc["gacksung"],
                order_id=doc["order_id"],
                gacksung_illust_type=doc["gacksung_illust_type"],
                acquire_time=doc["acquire_time"],
            )

        return None

    except Exception as e:
        print("WARN:     " + str(e))

        return None


def update_personality_format(
    uid: int,
    personality_id: int,
    level: Optional[int] = None,
    gacksung: Optional[int] = None,
    gacksung_illust_type: Optional[int] = None,
) -> bool:
    try:
        update_fields = {}
        if level is not None:
            update_fields["level"] = level
        if gacksung is not None:
            update_fields["gacksung"] = gacksung
        if gacksung_illust_type is not None:
            update_fields["gacksung_illust_type"] = gacksung_illust_type

        if update_fields:
            personality_collection.update_one(
                {"uid": uid, "personality_id": personality_id}, {"$set": update_fields}
            )

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False


def sync_personality_formats(uid: int) -> Optional[List[PersonalityFormat]]:
    try:
        existing_personality_docs = personality_collection.find({"uid": uid})
        existing_personality_ids = {
            doc["personality_id"] for doc in existing_personality_docs
        }

        new_personality_formats = create_personality_format_list()

        new_personalities_to_add = [
            personality
            for personality in new_personality_formats
            if personality.personality_id not in existing_personality_ids
        ]

        if new_personalities_to_add:
            personality_format_with_uid_list = [
                PersonalityFormatWithUID(
                    uid=uid,
                    personality_id=personality.personality_id,
                    level=personality.level,
                    exp=personality.exp,
                    gacksung=personality.gacksung,
                    order_id=personality.order_id,
                    gacksung_illust_type=personality.gacksung_illust_type,
                    acquire_time=personality.acquire_time,
                )
                for personality in new_personalities_to_add
            ]

            personality_collection.insert_many(
                [pf.dict() for pf in personality_format_with_uid_list]
            )

            print(
                "INFO:     "
                + f"{len(new_personalities_to_add)} new personality(ies) inserted for UID {uid}."
            )

            return [
                PersonalityFormat(
                    personality_id=personality.personality_id,
                    level=personality.level,
                    exp=personality.exp,
                    gacksung=personality.gacksung,
                    order_id=personality.order_id,
                    gacksung_illust_type=personality.gacksung_illust_type,
                    acquire_time=personality.acquire_time,
                )
                for personality in new_personalities_to_add
            ]
        else:
            print("INFO:     " + f"No new personality data to insert for UID {uid}.")
            return None

    except Exception as e:
        print("WARN:     " + str(e))
        return None

from pydantic import BaseModel
from database.client import db
from resources.ego import create_ego_format_list
from limbus.formats import EgoFormat
from typing import List, Optional

ego_collection = db["egos"]


class EgoFormatWithUID(BaseModel):
    uid: int
    ego_id: int
    gacksung: int
    acquire_time: str


def insert_ego_formats(uid: int) -> None:
    try:
        ego_format_list = create_ego_format_list()
        ego_format_with_uid_list = [
            EgoFormatWithUID(
                uid=uid,
                ego_id=ego_format.ego_id,
                gacksung=ego_format.gacksung,
                acquire_time=ego_format.acquire_time,
            )
            for ego_format in ego_format_list
        ]

        if ego_format_with_uid_list:
            ego_collection.insert_many([ego.dict() for ego in ego_format_with_uid_list])
    except Exception as e:
        print("WARN:     " + str(e))


def get_ego_formats_by_uid(uid: int) -> List[EgoFormat]:
    try:
        ego_docs = ego_collection.find({"uid": uid})

        return [
            EgoFormat(
                ego_id=doc["ego_id"],
                gacksung=doc["gacksung"],
                acquire_time=doc["acquire_time"],
            )
            for doc in ego_docs
        ]

    except Exception as e:
        print("WARN:     " + str(e))

        return []


def update_ego_format(uid: int, ego_id: int, gacksung: Optional[int] = None) -> bool:
    try:
        update_fields = {}
        if gacksung is not None:
            update_fields["gacksung"] = gacksung

        if update_fields:
            result = ego_collection.update_one(
                {"uid": uid, "ego_id": ego_id}, {"$set": update_fields}
            )

            return result.modified_count > 0

        return False

    except Exception as e:
        print("WARN:     " + str(e))

        return False

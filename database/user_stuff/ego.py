from pydantic import BaseModel
from database.client import db
from resources.user_stuff.ego import create_ego_format_list
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
            ego_collection.update_one(
                {"uid": uid, "ego_id": ego_id}, {"$set": update_fields}
            )

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False


def sync_ego_formats(uid: int) -> Optional[List[EgoFormat]]:
    try:
        existing_ego_docs = ego_collection.find({"uid": uid})
        existing_ego_ids = {doc["ego_id"] for doc in existing_ego_docs}

        new_ego_formats = create_ego_format_list()

        new_ego_formats_to_add = [
            ego_format
            for ego_format in new_ego_formats
            if ego_format.ego_id not in existing_ego_ids
        ]

        if new_ego_formats_to_add:
            ego_format_with_uid_list = [
                EgoFormatWithUID(
                    uid=uid,
                    ego_id=ego_format.ego_id,
                    gacksung=ego_format.gacksung,
                    acquire_time=ego_format.acquire_time,
                )
                for ego_format in new_ego_formats_to_add
            ]

            ego_collection.insert_many([ego.dict() for ego in ego_format_with_uid_list])

            print(
                "INFO:     "
                + f"{len(new_ego_formats_to_add)} new EGO(s) inserted for UID {uid}."
            )

            return [
                EgoFormat(
                    ego_id=ego_format.ego_id,
                    gacksung=ego_format.gacksung,
                    acquire_time=ego_format.acquire_time,
                )
                for ego_format in new_ego_formats_to_add
            ]
        else:
            print("INFO:     " + f"No new EGO data to insert for UID {uid}.")
            return None

    except Exception as e:
        print("WARN:     " + str(e))
        return None

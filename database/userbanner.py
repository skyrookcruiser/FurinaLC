from pydantic import BaseModel
from database.client import db
from resources.userbanner import create_user_banner_data_format_list
from limbus.formats import UserBannerDataFormat
from typing import List, Optional

banner_collection = db["userbanners"]


class UserBannerDataFormatWithUID(BaseModel):
    uid: int
    id: int
    acquiretime: str
    value: int
    value2: int


def insert_user_banner_data_formats(uid: int) -> None:
    try:
        banner_data_list = create_user_banner_data_format_list()

        banner_data_with_uid_list = [
            UserBannerDataFormatWithUID(
                uid=uid,
                id=banner_data.id,
                acquiretime=banner_data.acquiretime,
                value=banner_data.value,
                value2=banner_data.value2,
            )
            for banner_data in banner_data_list
        ]

        if banner_data_with_uid_list:
            banner_collection.insert_many(
                [banner.dict() for banner in banner_data_with_uid_list]
            )

    except Exception as e:
        print("WARN:     " + str(e))


def get_user_banner_data_by_uid(uid: int) -> List[UserBannerDataFormat]:
    try:
        banner_docs = banner_collection.find({"uid": uid})

        return [
            UserBannerDataFormat(
                id=doc["id"],
                acquiretime=doc["acquiretime"],
                value=doc["value"],
                value2=doc["value2"],
            )
            for doc in banner_docs
        ]

    except Exception as e:
        print("WARN:     " + str(e))

        return []


def update_user_banner_data(
    uid: int, banner_id: int, value: Optional[int] = None, value2: Optional[int] = None
) -> bool:
    try:
        update_fields = {}
        if value is not None:
            update_fields["value"] = value
        if value2 is not None:
            update_fields["value2"] = value2

        if update_fields:
            banner_collection.update_one(
                {"uid": uid, "id": banner_id}, {"$set": update_fields}
            )

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False

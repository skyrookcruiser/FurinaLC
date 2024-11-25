from pydantic import BaseModel
from database.client import db
from resources.parser.user_profile.profile import (
    create_user_public_profile_with_supporters_format,
)
from limbus.formats import (
    UserPublicProfileWithSupportersFormat,
    UserPublicBannerFormat,
    SupportPersonalitySlotFormat,
)
from typing import Optional, List
from utils import get_date_time

user_profile_collection = db["userprofiles"]


class UserPublicProfileWithSupportersFormatWithUID(BaseModel):
    uid: int
    public_uid: Optional[str] = None
    illust_id: Optional[int] = None
    illust_gacksung_level: Optional[int] = None
    leftborder_id: Optional[int] = None
    rightborder_id: Optional[int] = None
    egobackground_id: Optional[int] = None
    sentence_id: Optional[int] = None
    word_id: Optional[int] = None
    banners: Optional[List[UserPublicBannerFormat]] = None
    level: Optional[int] = None
    date: Optional[str] = None
    support_personalities: Optional[List[SupportPersonalitySlotFormat]] = None


def insert_user_public_profile_with_supporters_format(uid: int) -> None:
    try:
        profile = create_user_public_profile_with_supporters_format(uid)
        profile_with_uid = UserPublicProfileWithSupportersFormatWithUID(
            uid=uid,
            public_uid=profile.public_uid,
            illust_id=profile.illust_id,
            illust_gacksung_level=profile.illust_gacksung_level,
            leftborder_id=profile.leftborder_id,
            rightborder_id=profile.rightborder_id,
            egobackground_id=profile.egobackground_id,
            sentence_id=profile.sentence_id,
            word_id=profile.word_id,
            banners=profile.banners,
            level=profile.level,
            date=profile.date,
            support_personalities=profile.support_personalities,
        )

        user_profile_collection.insert_one(profile_with_uid.dict())

    except Exception as e:
        print("WARN:     " + str(e))


def get_user_profile_data_by_uid(
    uid: int,
) -> Optional[UserPublicProfileWithSupportersFormat]:
    try:
        profile_doc = user_profile_collection.find_one({"uid": uid})

        if profile_doc:
            return UserPublicProfileWithSupportersFormat(
                public_uid=profile_doc["public_uid"],
                illust_id=profile_doc["illust_id"],
                illust_gacksung_level=profile_doc["illust_gacksung_level"],
                leftborder_id=profile_doc["leftborder_id"],
                rightborder_id=profile_doc["rightborder_id"],
                egobackground_id=profile_doc["egobackground_id"],
                sentence_id=profile_doc["sentence_id"],
                word_id=profile_doc["word_id"],
                banners=profile_doc["banners"],
                level=profile_doc["level"],
                date=get_date_time(),
                support_personalities=profile_doc["support_personalities"],
            )

        return None

    except Exception as e:
        print("WARN:     " + str(e))

        return None


def update_user_profile_data(
    uid: int,
    public_uid: Optional[str] = None,
    illust_id: Optional[int] = None,
    illust_gacksung_level: Optional[int] = None,
    leftborder_id: Optional[int] = None,
    rightborder_id: Optional[int] = None,
    egobackground_id: Optional[int] = None,
    sentence_id: Optional[int] = None,
    word_id: Optional[int] = None,
    banners: Optional[List[UserPublicBannerFormat]] = None,
    level: Optional[int] = None,
    date: Optional[str] = get_date_time(),
    support_personalities: Optional[List[SupportPersonalitySlotFormat]] = None,
) -> bool:
    try:
        update_fields = {}

        if public_uid is not None:
            update_fields["public_uid"] = public_uid
        if illust_id is not None:
            update_fields["illust_id"] = illust_id
        if illust_gacksung_level is not None:
            update_fields["illust_gacksung_level"] = illust_gacksung_level
        if leftborder_id is not None:
            update_fields["leftborder_id"] = leftborder_id
        if rightborder_id is not None:
            update_fields["rightborder_id"] = rightborder_id
        if egobackground_id is not None:
            update_fields["egobackground_id"] = egobackground_id
        if sentence_id is not None:
            update_fields["sentence_id"] = sentence_id
        if word_id is not None:
            update_fields["word_id"] = word_id
        if banners is not None:
            update_fields["banners"] = [banner.dict() for banner in banners]

        if level is not None:
            update_fields["level"] = level
        if date is not None:
            update_fields["date"] = date
        if support_personalities is not None:
            update_fields["support_personalities"] = [
                supporter.dict() for supporter in support_personalities
            ]

        if update_fields:
            user_profile_collection.update_one({"uid": uid}, {"$set": update_fields})

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False

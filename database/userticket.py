from pydantic import BaseModel
from database.client import db
from resources.userticket import (
    create_border_left_format_list,
    create_border_right_format_list,
    create_egobg_format_list,
)
from limbus.formats import UserProfileBorderFormat, UserProfileEgobackgroundFormat
from limbus.responses import RspGetProfileTicketDecoDatas
from typing import List, Optional

user_tickets_collection = db["usertickets"]


class ProfileTicketDataWithUID(BaseModel):
    uid: int
    leftBorders: List[UserProfileBorderFormat]
    rightBorders: List[UserProfileBorderFormat]
    egoBackgrounds: List[UserProfileEgobackgroundFormat]


def insert_profile_ticket_data(uid: int) -> None:
    try:
        left_borders = create_border_left_format_list()
        right_borders = create_border_right_format_list()
        ego_backgrounds = create_egobg_format_list()

        profile_ticket_data = ProfileTicketDataWithUID(
            uid=uid,
            leftBorders=left_borders,
            rightBorders=right_borders,
            egoBackgrounds=ego_backgrounds,
        )

        user_tickets_collection.insert_one(profile_ticket_data.dict())

    except Exception as e:
        print("WARN:     " + str(e))


def get_profile_ticket_data_by_uid(uid: int) -> Optional[RspGetProfileTicketDecoDatas]:
    try:
        ticket_doc = user_tickets_collection.find_one({"uid": uid})

        if ticket_doc:
            return RspGetProfileTicketDecoDatas(
                leftBorders=ticket_doc["leftBorders"],
                rightBorders=ticket_doc["rightBorders"],
                egoBackgrounds=ticket_doc["egoBackgrounds"],
            )

        return None

    except Exception as e:
        print("WARN:     " + str(e))

        return None

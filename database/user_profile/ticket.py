from pydantic import BaseModel
from database.client import db
from resources.user_profile.ticket import (
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


# We immediately return this as the Rsp
# Because I'm too lazy to bother to change it
# into returning a tuple
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


# We don't need to return a ticket format here
# Because when you open the ticket deco menu,
# It always reloads them from db
def sync_profile_ticket_data(uid: int) -> None:
    try:
        existing_ticket_doc = user_tickets_collection.find_one({"uid": uid})

        new_left_borders = create_border_left_format_list()
        new_right_borders = create_border_right_format_list()
        new_ego_backgrounds = create_egobg_format_list()

        updated_fields = {}
        left_borders_to_add = []
        right_borders_to_add = []
        ego_backgrounds_to_add = []

        if existing_ticket_doc:
            existing_left_ids = {
                border["id"] for border in existing_ticket_doc["leftBorders"]
            }
            left_borders_to_add = [
                border
                for border in new_left_borders
                if border.id not in existing_left_ids
            ]
        else:
            left_borders_to_add = new_left_borders

        if left_borders_to_add:
            updated_fields["leftBorders"] = (
                existing_ticket_doc["leftBorders"]
                + [border.dict() for border in left_borders_to_add]
                if existing_ticket_doc
                else [border.dict() for border in left_borders_to_add]
            )

        if existing_ticket_doc:
            existing_right_ids = {
                border["id"] for border in existing_ticket_doc["rightBorders"]
            }
            right_borders_to_add = [
                border
                for border in new_right_borders
                if border.id not in existing_right_ids
            ]
        else:
            right_borders_to_add = new_right_borders

        if right_borders_to_add:
            updated_fields["rightBorders"] = (
                existing_ticket_doc["rightBorders"]
                + [border.dict() for border in right_borders_to_add]
                if existing_ticket_doc
                else [border.dict() for border in right_borders_to_add]
            )

        if existing_ticket_doc:
            existing_ego_bg_ids = {
                bg["id"] for bg in existing_ticket_doc["egoBackgrounds"]
            }
            ego_backgrounds_to_add = [
                bg for bg in new_ego_backgrounds if bg.id not in existing_ego_bg_ids
            ]
        else:
            ego_backgrounds_to_add = new_ego_backgrounds

        if ego_backgrounds_to_add:
            updated_fields["egoBackgrounds"] = (
                existing_ticket_doc["egoBackgrounds"]
                + [bg.dict() for bg in ego_backgrounds_to_add]
                if existing_ticket_doc
                else [bg.dict() for bg in ego_backgrounds_to_add]
            )

        if updated_fields:
            user_tickets_collection.update_one(
                {"uid": uid}, {"$set": updated_fields}, upsert=True
            )

            total_new_entries = (
                len(left_borders_to_add)
                + len(right_borders_to_add)
                + len(ego_backgrounds_to_add)
            )
            print(
                "INFO:     "
                + f"{total_new_entries} new ticket item(s) inserted for UID {uid}."
            )
        else:
            print("INFO:     " + "No new ticket data to insert for UID {uid}.")

    except Exception as e:
        print("WARN:     " + str(e))

import re
from server.config import ALLOW_SYNC_COMMAND
from limbus.requests import Cs, ReqUseCoupon
from limbus.responses import Sc, RspUseCoupon
from limbus.formats import (
    UpdatedFormat,
    PersonalityFormat,
    Element,
    ELEMENT_TYPE,
    STR_ELEMENT_TYPE,
    EgoFormat,
    ItemFormat,
)
from database.user_stuff.personality import (
    update_personality_format,
    sync_personality_formats,
)
from database.user_stuff.ego import update_ego_format, sync_ego_formats
from database.user_stuff.item import update_item_format, sync_item_formats
from database.user_stuff.announcer import sync_announcer_format
from database.user_profile.banner import sync_profile_banner_data
from database.user_profile.ticket import sync_profile_ticket_data
from database.user_profile.user import update_user_info, get_user_info_by_uid


def extract_ints(input_str: str, expected_count: int) -> tuple:
    numbers = re.findall(r"\d+", input_str)
    numbers = [int(num) for num in numbers]

    if len(numbers) < expected_count:
        print("WARN:     " + "Coupon command has incorrect argument count.")

        return tuple([0] * expected_count)

    return tuple(numbers[:expected_count])


async def handle(req: Cs[ReqUseCoupon]):
    uid = req.userAuth.uid
    code = req.parameters.code
    match code[:1]:
        case "S":
            if code[:4] != "SYNC" and ALLOW_SYNC_COMMAND is not True:
                return Sc[RspUseCoupon](result=RspUseCoupon(state=2))
            else:
                # We can do multiple flags!
                # ...I think.
                sync_flags = code[4:]

                if "ITEM" in sync_flags:
                    sync_item_format = sync_item_formats(uid)

                if "EGO" in sync_flags:
                    new_ego_format = sync_ego_formats(uid)

                if "ANNOUNCER" in sync_flags:
                    new_announcer_format = sync_announcer_format(uid)

                if "PERSONALITY" in sync_flags:
                    new_personality_format = sync_personality_formats(uid)

                if "TICKET" in sync_flags:
                    sync_profile_ticket_data(uid)

                banner_update = "BANNER" in sync_flags
                if banner_update is not False:
                    sync_profile_banner_data(uid)

                # If not specified, just sync everything.
                if not sync_flags:
                    sync_profile_banner_data(uid)
                    sync_profile_ticket_data(uid)
                    new_ego_format = sync_ego_formats(uid)
                    new_announcer_format = sync_announcer_format(uid)
                    new_personality_format = sync_personality_formats(uid)
                    sync_item_format = sync_item_formats(uid)

                return Sc[RspUseCoupon](
                    updated=UpdatedFormat(
                        personalityList=new_personality_format
                        if "personality" in sync_flags or not sync_flags
                        else None,
                        egoList=new_ego_format
                        if "ego" in sync_flags or not sync_flags
                        else None,
                        itemList=sync_item_format
                        if "item" in sync_flags or not sync_flags
                        else None,
                        announcer=new_announcer_format
                        if "announcer" in sync_flags or not sync_flags
                        else None,
                        isUpdateUserBanner=banner_update,
                        # Ticket decos are loaded everytime you open the menu
                        # We don't need to add anything in here.
                        # well, there's no field for ticket deco anyways lol.
                    ),
                    result=RspUseCoupon(
                        state=1,
                        rewards=[
                            Element(
                                type=STR_ELEMENT_TYPE.ITEM,
                                _type=ELEMENT_TYPE.ITEM,
                                id=2,
                                num=1,
                            )
                        ],
                    ),
                )
        # PERSONALITY, EXAMPLE USAGE:
        # P10101L50G4
        # Personality ID 10101, set level 50, set gacksung to 4
        case "P":
            pid, pl, pg = extract_ints(code, 3)
            if pid == 0:
                return Sc[RspUseCoupon](result=RspUseCoupon(state=2))
            else:
                update_personality_format(
                    uid=uid, personality_id=pid, level=pl, gacksung=pg
                )

                return Sc[RspUseCoupon](
                    updated=UpdatedFormat(
                        personalityList=[
                            PersonalityFormat(
                                personality_id=pid,
                                level=pl,
                                gacksung=pg,
                            )
                        ]
                    ),
                    result=RspUseCoupon(
                        state=1,
                        rewards=[
                            Element(
                                type=STR_ELEMENT_TYPE.PERSONALITY,
                                _type=ELEMENT_TYPE.PERSONALITY,
                                id=pid,
                                num=1,
                            )
                        ],
                    ),
                )
        # EGO, EXAMPLE USAGE:
        # E20101G4
        # Ego id 20101, set gacksung to 4
        case "E":
            eid, eg = extract_ints(code, 2)
            if eid == 0:
                return Sc[RspUseCoupon](result=RspUseCoupon(state=2))
            else:
                update_ego_format(
                    uid=uid,
                    ego_id=eid,
                    gacksung=eg,
                )

                return Sc[RspUseCoupon](
                    updated=UpdatedFormat(
                        egoList=[
                            EgoFormat(
                                ego_id=eid,
                                gacksung=eg,
                            )
                        ]
                    ),
                    result=RspUseCoupon(
                        state=1,
                        rewards=[
                            Element(
                                type=STR_ELEMENT_TYPE.EGO,
                                _type=ELEMENT_TYPE.EGO,
                                id=eid,
                                num=1,
                            )
                        ],
                    ),
                )
        # ITEM, EXAMPLE USAGE:
        # I11C100
        # Item ID 11, Set count to 100
        case "I":
            iid, ic = extract_ints(code, 2)
            if iid == 0:
                return Sc[RspUseCoupon](result=RspUseCoupon(state=2))
            else:
                update_item_format(
                    uid=uid,
                    item_id=iid,
                    num=ic,
                )

                return Sc[RspUseCoupon](
                    updated=UpdatedFormat(
                        itemList=[
                            ItemFormat(
                                item_id=iid,
                                num=ic,
                            )
                        ]
                    ),
                    result=RspUseCoupon(
                        state=1,
                        rewards=[
                            Element(
                                type=STR_ELEMENT_TYPE.ITEM,
                                _type=ELEMENT_TYPE.ITEM,
                                id=iid,
                                num=ic,
                            )
                        ],
                    ),
                )
        # USER, EXAMPLE USAGE:
        # U1L100S100
        # User ID 1, Set Level 100, Set Stamina 100
        # In truth, User ID can be anything
        # Because we use the req packet's uid instead
        case "U":
            uid, ul, us = extract_ints(code, 3)
            if uid == 0:
                return Sc[RspUseCoupon](result=RspUseCoupon(state=2))
            else:
                update_user_info(uid=uid, level=ul, stamina=us)
                user = get_user_info_by_uid(uid)

                return Sc[RspUseCoupon](
                    updated=UpdatedFormat(userInfo=user),
                    result=RspUseCoupon(
                        state=1,
                        rewards=[
                            Element(
                                type=STR_ELEMENT_TYPE.ITEM,
                                _type=ELEMENT_TYPE.ITEM,
                                id=2,
                                num=1,
                            )
                        ],
                    ),
                )
        # UNKNOWN
        case _:
            return Sc[RspUseCoupon](result=RspUseCoupon(state=2))

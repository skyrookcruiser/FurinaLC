from models.packets import ResPacekt_UseCoupon
from models.types import (
    Element,
    UpdatedFormat,
    EgoFormat,
    PersonalityFormat,
    ItemFormat,
)
from util.time import get_curr_time
from util.id import get_order_id
from util.user import get_user
from solemn.insert_util import insert_ego, insert_personality, insert_item


def parse_ego(req_input: str) -> tuple[UpdatedFormat, ResPacekt_UseCoupon]:
    numbers = tuple(
        [
            int(num)
            for num in "".join(
                char if char.isdigit() else " " for char in req_input
            ).split()
        ]
    )
    ego_id, gacksung = numbers

    res_packet = ResPacekt_UseCoupon(
        state=1,
        rewards=[
            Element(
                type_="EGO",
                id=ego_id,
                num=1,
            ),
        ],
    )

    ego_give = EgoFormat(
        ego_id=ego_id,
        gacksung=gacksung,
        acquire_time=get_curr_time(),
    )

    res_update = UpdatedFormat(
        userInfo=get_user(),
        egoList=[ego_give],
    )

    insert_ego(ego_give)

    return res_update, res_packet


def parse_personality(req_input: str) -> tuple[UpdatedFormat, ResPacekt_UseCoupon]:
    numbers = tuple(
        [
            int(num)
            for num in "".join(
                char if char.isdigit() else " " for char in req_input
            ).split()
        ]
    )
    personality_id, gacksung, level = numbers

    res_packet = ResPacekt_UseCoupon(
        state=1,
        rewards=[
            Element(
                type_="PERSONALITY",
                id=personality_id,
                num=1,
                level=level,
            ),
        ],
    )

    personality_give = PersonalityFormat(
        personality_id=personality_id,
        level=level,
        gacksung=gacksung,
        order_id=get_order_id(personality_id),
        gacksung_illust_type=1,
        acquire_time=get_curr_time(),
    )

    res_update = UpdatedFormat(
        userInfo=get_user(),
        personalityList=[personality_give],
    )

    insert_personality(personality_give)

    return res_update, res_packet


def parse_item(req_input: str) -> tuple[UpdatedFormat, ResPacekt_UseCoupon]:
    numbers = tuple(
        [
            int(num)
            for num in "".join(
                char if char.isdigit() else " " for char in req_input
            ).split()
        ]
    )
    item_id, count = numbers

    res_packet = ResPacekt_UseCoupon(
        state=1,
        rewards=[
            Element(
                type_="ITEM",
                id=item_id,
                num=count,
            ),
        ],
    )

    item_give = ItemFormat(
        item_id=item_id,
        num=count,
    )

    res_update = UpdatedFormat(
        userInfo=get_user(),
        itemList=[item_give],
    )

    insert_item(item_give)

    return res_update, res_packet
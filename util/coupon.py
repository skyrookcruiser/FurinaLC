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
from util.data import get_user
from solemn.insert_util import (
    insert_ego,
    insert_personality,
    insert_item,
    insert_ego_many,
    insert_personality_many,
)


def give_all() -> (
    tuple[UpdatedFormat, ResPacekt_UseCoupon]
):
    sinners = []
    # Yi Sang
    sinners.extend(
        range(10102, 10111)
    )  # 10102 to 10110
    # Faust
    sinners.extend(
        range(10202, 10211)
    )  # 10202 to 10210
    # Don Quixote
    sinners.extend(
        range(10302, 10310)
    )  # 10302 to 10309
    # Ryoshu
    sinners.extend(
        range(10402, 10411)
    )  # 10402 to 10410
    # Meursault
    sinners.extend(
        range(10502, 10512)
    )  # 10502 to 10511
    # Honglu
    sinners.extend(
        range(10602, 10611)
    )  # 10602 to 10610
    # Heathcliff
    sinners.extend(
        range(10702, 10711)
    )  # 10702 to 10710
    # Ishmael
    sinners.extend(
        range(10802, 10811)
    )  # 10802 to 10810
    # Rodion
    sinners.extend(
        range(10902, 10911)
    )  # 10902 to 10910
    # Sinclair
    sinners.extend(
        range(11002, 11011)
    )  # 11002 to 11010
    # Outis
    sinners.extend(
        range(11102, 11112)
    )  # 11102 to 11111
    # Gregor
    sinners.extend(
        range(11202, 11210)
    )  # 11202 to 11209

    egos = []
    # Yi Sang
    egos.extend(range(20102, 20107))  # 20102 1to 20106
    # Faust
    egos.extend(range(20202, 20208))  # 20202 to 20207
    # Don Quixote
    egos.extend(range(20302, 20307))  # 20302 to 20306
    # Ryoshu
    egos.extend(range(20402, 20408))  # 20402 to 20407
    # Meursault
    egos.extend(range(20502, 20507))  # 20502 to 20506
    # Honglu
    egos.extend(range(20602, 20608))  # 20602 to 20607
    # Heathcliff
    egos.extend(range(20702, 20708))  # 20702 to 20707
    # Ishmael
    egos.extend(range(20802, 20808))  # 20802 to 20807
    # Rodion
    egos.extend(range(20902, 20907))  # 20902 to 20906
    # Sinclair
    egos.extend(range(21002, 21007))  # 21002 to 21006
    # Outis
    egos.extend(range(21102, 21108))  # 21102 to 21107
    # Gregor
    egos.extend(range(21202, 21208))  # 21202 to 21207

    personality_elements = [
        Element(
            type_="PERSONALITY",
            id=p,
            num=1,
        )
        for p in sinners
    ]

    ego_elements = [
        Element(
            type_="EGO",
            id=e,
            num=1,
        )
        for e in egos
    ]

    give_reward = []
    give_reward.extend(personality_elements)
    give_reward.extend(ego_elements)

    res_packet = ResPacekt_UseCoupon(
        state=1,
        rewards=give_reward,
    )

    ego_formats = [
        EgoFormat(
            ego_id=e,
            gacksung=4,
            acquire_time=get_curr_time(),
        )
        for e in egos
    ]

    personality_formats = [
        PersonalityFormat(
            personality_id=p,
            level=50,
            gacksung=4,
            order_id=get_order_id(p),
            gacksung_illust_type=1,
            acquire_time=get_curr_time(),
        )
        for p in sinners
    ]

    insert_ego_many(ego_formats)
    insert_personality_many(personality_formats)

    res_update = UpdatedFormat(
        userInfo=get_user(),
        egoList=ego_formats,
        personalityList=personality_formats,
    )

    return res_update, res_packet


def parse_ego(
    req_input: str,
) -> tuple[UpdatedFormat, ResPacekt_UseCoupon]:
    numbers = tuple(
        [
            int(num)
            for num in "".join(
                char if char.isdigit() else " "
                for char in req_input
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


def parse_personality(
    req_input: str,
) -> tuple[UpdatedFormat, ResPacekt_UseCoupon]:
    numbers = tuple(
        [
            int(num)
            for num in "".join(
                char if char.isdigit() else " "
                for char in req_input
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


def parse_item(
    req_input: str,
) -> tuple[UpdatedFormat, ResPacekt_UseCoupon]:
    numbers = tuple(
        [
            int(num)
            for num in "".join(
                char if char.isdigit() else " "
                for char in req_input
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

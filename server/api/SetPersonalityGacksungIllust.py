from limbus.requests import Cs, ReqSetPersonalityGacksungIllust
from limbus.responses import Sc, RspNull
from limbus.formats import UpdatedFormat
from database.user_stuff.personality import (
    get_one_personality_format,
    update_personality_format,
)
from fastapi import HTTPException


async def handle(req: Cs[ReqSetPersonalityGacksungIllust]):
    uid = req.userAuth.uid
    personality_id = req.parameters.personalityId
    illust_type = req.parameters.type

    if (
        update_personality_format(
            uid=uid,
            personality_id=personality_id,
            gacksung_illust_type=illust_type,
        )
        is not True
    ):
        raise HTTPException(
            status_code=500,
            detail="Personality not found or update failed.",
        )

    updated_personality = get_one_personality_format(uid, personality_id)

    return Sc[RspNull](
        updated=UpdatedFormat(personalityList=[updated_personality]),
        result=RspNull(),
    )

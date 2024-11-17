from limbus.requests import Cs, ReqChangeCurrentAnnouncer
from limbus.responses import Sc, RspNull
from limbus.formats import UpdatedFormat
from database.user_stuff.announcer import (
    get_announcer_format_by_uid,
    update_announcer_format,
)
from fastapi import HTTPException


async def handle(req: Cs[ReqChangeCurrentAnnouncer]):
    uid = req.userAuth.uid
    req_announcers = req.parameters.announcerIds

    if (
        update_announcer_format(
            uid=uid,
            new_cur_announcer_ids=req_announcers,
        )
        is not True
    ):
        raise HTTPException(
            status_code=500,
            detail="Announcer not found or update failed.",
        )

    updated_announcer = get_announcer_format_by_uid(uid)

    return Sc[RspNull](
        updated=UpdatedFormat(announcer=updated_announcer),
        result=RspNull(),
    )

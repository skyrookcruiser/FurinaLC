from limbus.requests import Cs, ReqUpdateProfileTicketDeco
from limbus.responses import Sc, RspUpdateProfileTicketDeco
from database.user_profile.profile import update_user_profile_data
from fastapi import HTTPException


async def handle(req: Cs[ReqUpdateProfileTicketDeco]):
    uid = req.userAuth.uid
    param = req.parameters
    new_left_border = param.leftBorderId
    new_right_border = param.rightBorderId
    new_ego_bg = param.egoBackgroundId

    if (
        update_user_profile_data(
            uid=uid,
            leftborder_id=new_left_border,
            rightborder_id=new_right_border,
            egobackground_id=new_ego_bg,
        )
        is not True
    ):
        raise HTTPException(
            status_code=500, detail="User profile not found or update failed."
        )

    return Sc[RspUpdateProfileTicketDeco](
        result=RspUpdateProfileTicketDeco(
            leftBorderId=new_left_border,
            rightBorderId=new_right_border,
            egoBackgroundId=new_ego_bg,
        )
    )

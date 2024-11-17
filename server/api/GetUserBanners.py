from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetUserBanners
from database.user_profile.banner import get_user_banner_data_by_uid


async def handle(req: Cs[ReqNull]):
    uid = req.userAuth.uid

    return Sc[RspGetUserBanners](
        result=RspGetUserBanners(banners=get_user_banner_data_by_uid(uid))
    )

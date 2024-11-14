from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetUserBanners
from resources.userbanner import create_user_banner_data_format_list


# TODO: Use DB for this
def handle(req: Cs[ReqNull]):
    return Sc[RspGetUserBanners](
        result=RspGetUserBanners(banners=create_user_banner_data_format_list())
    )

from limbus.requests import Cs, ReqSignInAsSteam
from limbus.responses import Sc, RspSignInAsSteam
from limbus.formats import UserAuthFormat, AccountInfoFormat
from utils import get_date_time


async def handle(req: Cs[ReqSignInAsSteam]):
    # TODO: do something with steamToken
    # maybe to create a user, then assign uid,
    # and only access db with that uid yeah?
    # token = req.parameters.steamToken
    user_id = 1
    auth = UserAuthFormat(
        last_update_date=get_date_time(),
        last_login_date=get_date_time(),
        uid=user_id,
        public_id=user_id,
        data_version=16,
        db_id=0,
        auth_code="yulian",
    )
    rsp = RspSignInAsSteam(
        userAuth=auth,
        accountInfo=AccountInfoFormat(uid=user_id),
        walletCurrency="IDR",
    )

    return Sc[RspSignInAsSteam](result=rsp)

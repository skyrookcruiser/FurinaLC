from limbus.requests import Cs, ReqSignInAsGoogle
from limbus.responses import Sc, RspSignInAsGoogle
from limbus.formats import UserAuthFormat, AccountInfoFormat
from database.user import check_user
from utils import get_date_time


async def handle(req: Cs[ReqSignInAsGoogle]):
    # hardcoding this because i don't want to use a mod
    # just to modify the token field given by client
    token = "furinatoken"  # req.parameters.googleToken
    user_id = check_user(token, "steam")
    auth = UserAuthFormat(
        last_update_date=get_date_time(),
        last_login_date=get_date_time(),
        uid=user_id,
        public_id=user_id,
        data_version=16,
        db_id=0,
        auth_code="furinalc",
    )
    rsp = RspSignInAsGoogle(
        userAuth=auth,
        accountInfo=AccountInfoFormat(uid=user_id),
        walletCurrency="IDR",
    )

    return Sc[RspSignInAsGoogle](result=rsp)

from fastapi import Request
from models.packets import ReqPacket_SignInAsSteam, ResPacket_SignInAsSteam
from models.types import UserAuthFormat, AccountInfoFormat
from models.server import ResponsePacket, RequestPacket
from util.time import get_curr_time


async def handle(request: Request):
    req_body = await request.json()
    req_packet = RequestPacket[ReqPacket_SignInAsSteam].parse_obj(req_body)

    user_auth = UserAuthFormat(
        last_update_date=get_curr_time(),
        last_login_date=get_curr_time(),
        uid=404,
        public_id=404,
        data_version=16,
        db_id=0,
        auth_code=req_packet.parameters.steamToken,
    )
    res_packet = ResPacket_SignInAsSteam(
        userAuth=user_auth,
        accountInfo=AccountInfoFormat(uid=404),
        walletCurrency="USD",
    )
    response = ResponsePacket[ResPacket_SignInAsSteam](result=res_packet)

    return response.dict()

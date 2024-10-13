from fastapi import Request
from models.packets import ResPacekt_GetUserCouponState
from models.server import ResponsePacket


async def handle(request: Request):
    res_packet = ResPacekt_GetUserCouponState(ispossiblestate=True)
    response = ResponsePacket[ResPacekt_GetUserCouponState](result=res_packet)

    return response.dict()

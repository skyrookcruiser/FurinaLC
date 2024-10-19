from fastapi import Request
from models.packets import (
    ResPacket_ClaimClosedGachaRewards,
)
from models.server import ResponsePacket


async def handle(request: Request):
    res_packet = ResPacket_ClaimClosedGachaRewards()
    response = ResponsePacket[
        ResPacket_ClaimClosedGachaRewards
    ](result=res_packet)

    return response.dict()

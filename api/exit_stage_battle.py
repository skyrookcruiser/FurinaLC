from fastapi import Request
from models.packets import (
    ReqPacket_ExitStageBattleCommand,
    ResPacket_ExitStageBattleCommand,
)
from models.server import RequestPacket, ResponsePacket


async def handle(request: Request):
    req_body = await request.json()
    req_packet = RequestPacket[ReqPacket_ExitStageBattleCommand].parse_obj(req_body)

    res_packet = ResPacket_ExitStageBattleCommand(
        stageid=req_packet.parameters.stageid,
        iswin=req_packet.parameters.iswin,
        cleartype=2,
    )
    response = ResponsePacket[ResPacket_ExitStageBattleCommand](result=res_packet)

    return response.dict()

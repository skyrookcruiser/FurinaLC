from fastapi import Request
from models.packets import (
    ReqPacket_EnterStageBattleCommand,
    ResPacket_EnterStageBattleCommand,
)
from models.server import RequestPacket, ResponsePacket
from models.types import (
    AbnormalityUnlockInformationFormat,
)


async def handle(request: Request):
    req_body = await request.json()
    req_packet = RequestPacket[
        ReqPacket_EnterStageBattleCommand
    ].parse_obj(req_body)
    res_packet = ResPacket_EnterStageBattleCommand()
    response = ResponsePacket[
        ResPacket_EnterStageBattleCommand
    ](result=res_packet)

    return response.dict()

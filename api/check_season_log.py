from fastapi import Request
from models.packets import ResPacket_CheckSeasonLog
from models.server import ResponsePacket


async def handle(request: Request):
    res_packet = ResPacket_CheckSeasonLog()
    response = ResponsePacket[ResPacket_CheckSeasonLog](result=res_packet)

    return response.dict()

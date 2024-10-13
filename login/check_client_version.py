from fastapi import Request
from models.packets import ResPacket_CheckClientVersion
from models.server import ResponsePacket


async def handle(request: Request):
    res_packet = ResPacket_CheckClientVersion(timeoffset=0)
    response = ResponsePacket[ResPacket_CheckClientVersion](result=res_packet)

    return response.dict()

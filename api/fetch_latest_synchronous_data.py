from fastapi import Request
from models.packets import ResPacket_NULL
from models.server import ResponsePacket


async def handle(request: Request):
    res_packet = ResPacket_NULL()
    response = ResponsePacket[ResPacket_NULL](result=res_packet)

    return response.dict()

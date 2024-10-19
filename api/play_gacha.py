from fastapi import Request
from models.packets import (
    ResPacket_PlayGacha,
)
from models.server import ResponsePacket
from models.types import GachaLogDetail


# TODO:
# make it insert to database & implement banners
# from resource instead of hardcoding.
async def handle(request: Request):
    # req_body = await request.json()
    # req_packet = RequestPacket[ReqPacket_PlayGacha].parse_obj(req_body)
    yisang = [
        GachaLogDetail(type_="PERSONALITY", id=10101)
        for _ in range(10)
    ]

    res_packet = ResPacket_PlayGacha(
        gachaLogDetails=yisang
    )
    response = ResponsePacket[ResPacket_PlayGacha](
        result=res_packet
    )

    return response.dict()

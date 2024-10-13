from fastapi import Request
from models.packets import ReqPacket_UseCoupon, ResPacekt_UseCoupon
from models.server import RequestPacket, ResponsePacket
from util.coupon import parse_ego, parse_item, parse_personality


async def handle(request: Request):
    req_body = await request.json()
    req_packet = RequestPacket[ReqPacket_UseCoupon].parse_obj(req_body)
    req_input = req_packet.parameters.code

    if req_input.startswith("EGO"):
        res_update, res_packet = parse_ego(req_input)
    elif req_input.startswith("PER"):
        res_update, res_packet = parse_personality(req_input)
    elif req_input.startswith("ITEM"):
        res_update, res_packet = parse_item(req_input)
    else:
        res_update = None
        res_packet = ResPacekt_UseCoupon(state=0, rewards=[])

    response = ResponsePacket[ResPacekt_UseCoupon](
        updated=res_update,
        result=res_packet,
    )

    return response.dict()

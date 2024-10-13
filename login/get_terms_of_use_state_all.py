from fastapi import Request
from models.packets import ResPacket_GetTermsOfUseStateAll
from models.types import TermsOfUseState
from models.server import ResponsePacket


async def handle(request: Request):
    terms = [TermsOfUseState(version=1, state=1, uid=404)]
    res_packet = ResPacket_GetTermsOfUseStateAll(termsOfUseStateList=terms)
    response = ResponsePacket[ResPacket_GetTermsOfUseStateAll](result=res_packet)

    return response.dict()

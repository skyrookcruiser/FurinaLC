from fastapi import Request
from models.packets import ResPacket_RefreshMailbox
from models.server import ResponsePacket
from models.types import MailFormat


async def handle(request: Request):
    res_packet = ResPacket_RefreshMailbox(
        initializedMailList=[
            MailFormat(
                mail_id=1,
                sent_date="2023-09-27T01:00:00.000Z",
                expiry_date="2025-09-27T01:00:00.000Z",
                parameters=["Hello there."],
            )
        ],
    )
    response = ResponsePacket[ResPacket_RefreshMailbox](result=res_packet)

    return response.dict()

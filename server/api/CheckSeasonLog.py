from fastapi import Request
from limbus.responses import Sc, RspCheckSeasonLog


async def handle(req: Request):
    return Sc[RspCheckSeasonLog](result=RspCheckSeasonLog()).dict()

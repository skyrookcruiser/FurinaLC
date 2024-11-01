from fastapi import Request
from limbus.responses import Sc, RspCheckClientVersion


async def handle(req: Request):
    return Sc[RspCheckClientVersion](result=RspCheckClientVersion()).dict()

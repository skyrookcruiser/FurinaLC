from fastapi import Request
from limbus.responses import Sc, RspNULL


async def handle(req: Request):
    return Sc[RspNULL](result=RspNULL()).dict()

from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspCheckClientVersion


async def handle(req: Cs[ReqNull]):
    return Sc[RspCheckClientVersion](result=RspCheckClientVersion())

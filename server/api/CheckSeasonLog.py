from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspCheckSeasonLog


async def handle(req: Cs[ReqNull]):
    return Sc[RspCheckSeasonLog](result=RspCheckSeasonLog()).dict()

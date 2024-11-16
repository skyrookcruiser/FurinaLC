from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetMailLogAll


async def handle(req: Cs[ReqNull]):
    return Sc[RspGetMailLogAll](result=RspGetMailLogAll())

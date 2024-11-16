from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspClaimClosedGachaRewards


async def handle(req: Cs[ReqNull]):
    return Sc[RspClaimClosedGachaRewards](result=RspClaimClosedGachaRewards())

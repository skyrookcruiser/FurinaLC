from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspUpdateSteamPendingPurchase


async def handle(req: Cs[ReqNull]):
    return Sc[RspUpdateSteamPendingPurchase](result=RspUpdateSteamPendingPurchase())

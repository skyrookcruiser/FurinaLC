from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetDailyDungeonInfo


async def handle(req: Cs[ReqNull]):
    return Sc[RspGetDailyDungeonInfo](result=RspGetDailyDungeonInfo())

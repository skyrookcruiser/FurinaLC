from limbus.requests import Cs, ReqEnterRailwayDungeon
from limbus.responses import Sc, RspEnterRailwayDungeon


async def handle(req: Cs[ReqEnterRailwayDungeon]):
    return Sc[RspEnterRailwayDungeon](result=RspEnterRailwayDungeon())

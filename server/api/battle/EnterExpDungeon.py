from limbus.requests import Cs, ReqEnterExpDungeon
from limbus.responses import Sc, RspEnterExpDungeon


async def handle(req: Cs[ReqEnterExpDungeon]):
    return Sc[RspEnterExpDungeon](result=RspEnterExpDungeon())

from limbus.requests import Cs, ReqEnterStageBattleCommand
from limbus.responses import Sc, RspEnterStageBattleCommand


async def handle(req: Cs[ReqEnterStageBattleCommand]):
    return Sc[RspEnterStageBattleCommand](result=RspEnterStageBattleCommand())

from limbus.requests import Cs, ReqGetRailwayDungeonNodeAndLogAllCommand
from limbus.responses import Sc, RspGetRailwayDungeonNodeAndLogAllCommand


async def handle(req: Cs[ReqGetRailwayDungeonNodeAndLogAllCommand]):
    return Sc[RspGetRailwayDungeonNodeAndLogAllCommand](
        result=RspGetRailwayDungeonNodeAndLogAllCommand()
    )

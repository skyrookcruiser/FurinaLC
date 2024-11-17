from limbus.requests import Cs, ReqLobbyCgCommand
from limbus.responses import Sc, RspNull
from limbus.formats import UpdatedFormat


async def handle(req: Cs[ReqLobbyCgCommand]):
    cg = req.parameters.lobbyCg

    return Sc[RspNull](updated=UpdatedFormat(lobbyCG=cg), result=RspNull())

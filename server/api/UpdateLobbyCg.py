from limbus.requests import Cs, ReqLobbyCgCommand
from limbus.responses import Sc, RspNull
from limbus.formats import UpdatedFormat


async def handle(req: Cs[ReqLobbyCgCommand]):
    uid = req.userAuth.uid
    new_lobby_cg = req.parameters.lobbyCg
    # TODO: make db for this
    return Sc[RspNull](updated=UpdatedFormat(lobbyCG=new_lobby_cg), result=RspNull())

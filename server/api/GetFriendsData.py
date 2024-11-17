from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetFriendsData


async def handle(req: Cs[ReqNull]):
    return Sc[RspGetFriendsData](result=RspGetFriendsData())

from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetUserCouponState


async def handle(req: Cs[ReqNull]):
    return Sc[RspGetUserCouponState](result=RspGetUserCouponState(ispossiblestate=True))

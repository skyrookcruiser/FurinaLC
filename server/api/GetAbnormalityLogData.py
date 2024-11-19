from limbus.requests import Cs, ReqGetAbnormalityLogData
from limbus.responses import Sc, RspGetAbnormalityLogData


async def handle(req: Cs[ReqGetAbnormalityLogData]):
    return Sc[RspGetAbnormalityLogData](result=RspGetAbnormalityLogData())
from limbus.requests import Cs, ReqExitStoryCommand
from limbus.responses import Sc, RspExitStoryCommand


async def handle(req: Cs[ReqExitStoryCommand]):
    return Sc[RspExitStoryCommand](result=RspExitStoryCommand())

from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetDanteNoteState


async def handle(req: Cs[ReqNull]):
    # TODO: GET FROM RESOURCE
    return Sc[RspGetDanteNoteState](
        result=RspGetDanteNoteState(
            page=49,
            todayPage=65,
        )
    )
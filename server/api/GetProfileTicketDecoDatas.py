from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetProfileTicketDecoDatas
from database.userticket import get_profile_ticket_data_by_uid


async def handle(req: Cs[ReqNull]):
    uid = req.userAuth.uid

    return Sc[RspGetProfileTicketDecoDatas](result=get_profile_ticket_data_by_uid(uid))

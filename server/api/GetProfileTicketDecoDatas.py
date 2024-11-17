from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetProfileTicketDecoDatas
from database.user_profile.ticket import get_profile_ticket_data_by_uid


async def handle(req: Cs[ReqNull]):
    uid = req.userAuth.uid
    ticket_rsp = get_profile_ticket_data_by_uid(uid)

    return Sc[RspGetProfileTicketDecoDatas](result=ticket_rsp)

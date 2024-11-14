from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetProfileTicketDecoDatas
from resources.userticket import (
    create_border_left_format_list,
    create_border_right_format_list,
    create_egobg_format_list,
)


# TODO: Use DB for this
def handle(req: Cs[ReqNull]):
    return Sc[RspGetProfileTicketDecoDatas](
        result=RspGetProfileTicketDecoDatas(
            leftBorders=create_border_left_format_list(),
            rightBorders=create_border_right_format_list(),
            egoBackgrounds=create_egobg_format_list(),
        )
    )

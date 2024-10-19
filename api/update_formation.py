from fastapi import Request, HTTPException
from models.packets import (
    ReqPacket_UpdateFormationCommand,
    ResPacket_NULL,
)
from models.server import RequestPacket, ResponsePacket
from models.types import (
    FormationFormat,
    FormationDetailFormat,
    UpdatedFormat,
)
from solemn.modify_util import modify_formation_by_id
from util.data import get_user


async def handle(request: Request):
    req_body = await request.json()
    req_packet = RequestPacket[
        ReqPacket_UpdateFormationCommand
    ].parse_obj(req_body)

    formation_id = req_packet.parameters.formation.id
    formation_details = (
        req_packet.parameters.formation.formationDetails
    )

    success = False
    for detail in formation_details:
        success = (
            modify_formation_by_id(
                formation_id=formation_id,
                personality_id=detail.personalityId,
                egos=detail.egos,
                is_participated=detail.isParticipated,
                participation_order=detail.participationOrder,
            )
            or success
        )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Formation not found or update failed.",
        )

    updated_formation = FormationFormat(
        id=formation_id,
        formationDetails=[
            FormationDetailFormat(
                personalityId=detail.personalityId,
                egos=detail.egos,
                isParticipated=detail.isParticipated,
                participationOrder=detail.participationOrder,
            )
            for detail in formation_details
        ],
    )

    res_update = UpdatedFormat(
        formationList=[updated_formation],
        userInfo=get_user(),
    )

    res_packet = ResPacket_NULL()
    response = ResponsePacket[ResPacket_NULL](
        updated=res_update, result=res_packet
    )

    return response

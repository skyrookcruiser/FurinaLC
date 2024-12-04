from limbus.requests import Cs, ReqUpdateFormationCommand
from limbus.responses import Sc, RspNull
from limbus.formats import UpdatedFormat
from database.user_stuff.formation import update_formation_format
from fastapi import HTTPException


async def handle(req: Cs[ReqUpdateFormationCommand]):
    uid = req.userAuth.uid
    req_formation = req.parameters.formation
    formation_id = req_formation.id
    formation_details = req_formation.formationDetails
    formation_names = req_formation.formationNameFormat

    if (
        update_formation_format(
            uid=uid,
            formation_id=formation_id,
            formationDetails=formation_details,
            formationNameFormat=formation_names,
        )
        is not True
    ):
        raise HTTPException(
            status_code=500,
            detail="Formation not found or update failed.",
        )

    return Sc[RspNull](
        updated=UpdatedFormat(formationList=[req_formation]),
        result=RspNull(),
    )

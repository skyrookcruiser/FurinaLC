from limbus.requests import Cs, ReqExitStageBattleCommand
from limbus.responses import Sc, RspExitStageBattleCommand
from limbus.formats import StagePersonalityInfoFormat
from database.user_stuff.formation import get_one_formation_format


async def handle(req: Cs[ReqExitStageBattleCommand]):
    uid = req.userAuth.uid
    param = req.parameters

    formation = get_one_formation_format(uid, param.formationid)

    if formation:
        personalityinfos = [
            StagePersonalityInfoFormat(
                personalityid=detail.personalityId,
                prevlevel=50,
            )
            for detail in formation.formationDetails
        ]
    else:
        personalityinfos = []

    return Sc[RspExitStageBattleCommand](
        result=RspExitStageBattleCommand(
            stageid=param.stageid,
            iswin=param.iswin,
            cleartype=2,
            personalityinfos=personalityinfos,
        )
    )

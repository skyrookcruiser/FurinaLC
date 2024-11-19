from limbus.requests import Cs, ReqExitExpDungeon
from limbus.responses import Sc, RspExitExpDungeon
from limbus.formats import ExpDungeonClearInfoFormat, StagePersonalityInfoFormat
from database.user_stuff.formation import get_one_formation_format


async def handle(req: Cs[ReqExitExpDungeon]):
    uid = req.userAuth.uid
    param = req.parameters

    formation = get_one_formation_format(uid, param.formationId)

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

    return Sc[RspExitExpDungeon](
        result=RspExitExpDungeon(
            clearInfo=ExpDungeonClearInfoFormat(clearnumber=param.isWin),
            personalityinfos=personalityinfos,
        )
    )

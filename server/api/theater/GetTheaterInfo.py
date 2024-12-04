from limbus.requests import Cs, ReqNull
from limbus.responses import Sc, RspGetTheaterInfo
from limbus.formats import UserTheaterInfoFormat
from database.user_stuff.personality import get_personality_formats_by_uid


async def handle(req: Cs[ReqNull]):
    personalities = get_personality_formats_by_uid(req.userAuth.uid)

    return Sc[RspGetTheaterInfo](
        result=RspGetTheaterInfo(
            theaterInfo=UserTheaterInfoFormat(
                # I think there should actually be a P in front of the id
                # I don't gaf it doesnt crash so wtv
                rewardedIDList=[str(doc.personality_id) for doc in personalities]
            )
        )
    )

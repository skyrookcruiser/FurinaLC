from limbus.requests import Cs, ReqCompleteTheaterStory
from limbus.responses import Sc, RspCompleteTheaterStory
from limbus.formats import UserTheaterInfoFormat


async def handle(req: Cs[ReqCompleteTheaterStory]):
    story_id = req.parameters.storyId
    # I think there should actually be a P instead?
    # I don't gaf it doesnt crash so wtv
    reward_id = story_id.replace("P", "")

    return Sc[RspCompleteTheaterStory](
        result=RspCompleteTheaterStory(
            isRewarded=True,
            theaterInfo=UserTheaterInfoFormat(rewardedIDList=[reward_id]),
        )
    )

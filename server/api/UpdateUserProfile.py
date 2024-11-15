from limbus.requests import Cs, ReqUpdateUserProfile
from limbus.responses import Sc, RspNull
from database.userprofile import update_user_profile_data
from fastapi import HTTPException


async def handle(req: Cs[ReqUpdateUserProfile]):
    uid = req.userAuth.uid
    param = req.parameters
    new_illust_id = param.illustId
    new_illust_g = param.illustGacksungLevel
    new_sentence_id = param.sentenceId
    new_word_id = param.wordId
    new_banners = param.banners
    new_supports = param.supportPersonalities

    if (
        update_user_profile_data(
            uid=uid,
            illust_id=new_illust_id,
            illust_gacksung_level=new_illust_g,
            sentence_id=new_sentence_id,
            word_id=new_word_id,
            banners=new_banners,
            support_personalities=new_supports,
        )
        is not True
    ):
        raise HTTPException(
            status_code=500, detail="User profile not found or update failed."
        )

    return Sc[RspNull](result=RspNull())

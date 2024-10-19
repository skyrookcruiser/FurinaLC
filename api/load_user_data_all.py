from fastapi import Request
from models.packets import ResPacket_LoadUserDataAll
from models.types import (
    UpdatedFormat,
    UserPublicProfileWithSupportersFormat,
    DanteAbilityFormat,
    BattlePassFormat,
    AnnouncerFormat,
    LobbyCgFormat,
    UserPublicBannerFormat,
    MailFormat,
)
from models.server import ResponsePacket
from solemn.get_util import (
    get_personality,
    get_formation,
    get_ego,
    get_item,
)
from util.data import (
    get_formatted_user_codes,
    load_main_chapter_state,
    get_user,
)
from util.time import get_curr_time


async def handle(request: Request):
    res_update = UpdatedFormat(
        isInitialized=True,
        userInfo=get_user(),
        personalityList=get_personality(),
        egoList=get_ego(),
        formationList=get_formation(),
        lobbyCG=LobbyCgFormat(
            characterId=1,
            lobbycgdetails=[],
            isShowProfile=True,
        ),
        itemList=get_item(),
        chanceList=[],
        battlePass=BattlePassFormat(
            today_rand_value=12,
            limbus_apply_level=4,
            is_limbus=True,
        ),
        mainChapterStateList=load_main_chapter_state(),
        mailList=[
            MailFormat(
                mail_id=1,
                sent_date="2023-10-27T01:00:00.000Z",
                expiry_date="2025-09-27T01:00:00.000Z",
                parameters=[
                    "Private Server Made By Yulian. Thx <L.O.9> for encryption."
                ],
            )
        ],
        announcer=AnnouncerFormat(
            announcer_ids=list(range(100)),
            cur_announcer_ids=[9],
        ),
        membershipList=[],
        gachaList=[],
        userUnlockCodeList=get_formatted_user_codes(),
        eventRewardStateList=[],
        isUpdateUserBanner=False,
        isResetMirrorDungeon=False,
        missionList=[],
        missionConditionList=[],
        danteAbilityList=[
            DanteAbilityFormat(
                remaincount=1,
                abilityids=[90101],
                category=0,
            ),
            DanteAbilityFormat(
                remaincount=1,
                abilityids=[90101],
                category=1,
            ),
        ],
    )
    res_packet = ResPacket_LoadUserDataAll(
        showedWeekByMinistory=-1,
        profile=UserPublicProfileWithSupportersFormat(
            public_uid="Private Account",
            illust_id=10209,
            illust_gacksung_level=3,
            leftborder_id=29,
            rightborder_id=29,
            egobackground_id=32,
            sentence_id=36,
            word_id=3,
            level=404,
            date=get_curr_time(),
            banners=[
                UserPublicBannerFormat(
                    id=35,
                    value=-1,
                    value2=-1,
                    idx=0,
                ),
                UserPublicBannerFormat(
                    id=42,
                    value=-1,
                    value2=-1,
                    idx=1,
                ),
                UserPublicBannerFormat(
                    id=7,
                    value=-1,
                    value2=-1,
                    idx=2,
                ),
                UserPublicBannerFormat(
                    id=19,
                    value=-1,
                    value2=-1,
                    idx=3,
                ),
                UserPublicBannerFormat(
                    id=24,
                    value=-1,
                    value2=-1,
                    idx=4,
                ),
            ],
        ),
        isExistReceiveFriendRequest=False,
        danteNoteTodayPage=49,
        dailyLoginWeekId=-1,
    )
    response = ResponsePacket[
        ResPacket_LoadUserDataAll
    ](updated=res_update, result=res_packet)

    return response.dict()

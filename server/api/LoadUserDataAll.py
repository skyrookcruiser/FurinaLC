from limbus.requests import Cs, ReqLoadUserDataAll
from limbus.responses import Sc, RspLoadUserDataAll
from limbus.formats import (
    UserPublicProfileWithSupportersFormat,
    DailyLoginRewardStateFormat,
    SupportPersonalitySlotFormat,
    ProfileEgoContainIndexFormat,
    UpdatedFormat,
    SynchronizedFormat,
    UserInfo,
    FormationFormat,
    LobbyCgFormat,
    ItemFormat,
    ChanceFormat,
    BattlePassFormat,
    MailFormat,
    AnnouncerFormat,
    MembershipFormat,
    GachaRecordFormat,
    UnlockCodeFormat,
    EventRewardStateFormat,
    MissionFormat,
    DanteAbilityFormat,
    FormationDetailFormat,
    FormationNameElement,
    LobbyCgDetailFormat,
    BattlePassMissionState,
    MISSION_STATE,
    Element,
    STR_ELEMENT_TYPE,
    ELEMENT_TYPE,
    MISSION_CATEGORY,
    DANTE_ABILITY_CATEGORY,
    UserPublicBannerFormat,
    NoticeFormat,
    MailContentFormat,
)
from utils import get_date_time
from database.ego import get_ego_formats_by_uid
from database.personality import get_personality_formats_by_uid
from database.item import get_item_formats_by_uid
from resources.stage_node_reward import create_main_chapter_state_list
from resources.unlockcode_subchapter import create_unlock_code_format_list


async def handle(req: Cs[ReqLoadUserDataAll]):
    user_auth = req.userAuth
    update = UpdatedFormat(
        isInitialized=True,
        userInfo=UserInfo(
            uid=user_auth.uid, level=297, last_stamina_recover=get_date_time()
        ),
        personalityList=get_personality_formats_by_uid(user_auth.uid),
        egoList=get_ego_formats_by_uid(user_auth.uid),
        formationList=[
            FormationFormat(
                id=1,
                formationDetails=[
                    FormationDetailFormat(
                        personalityId=10101,
                        egos=[20101],
                        isParticipated=True,
                        participationOrder=1,
                    )
                ],
                formationNameElement=[
                    FormationNameElement(
                        k=1,
                        v=1,
                    )
                ],
            )
        ],
        lobbyCG=LobbyCgFormat(
            characterId=1,
            lobbycgdetails=[
                # LobbyCgDetailFormat(
                #     id=10101,
                #     g=1,
                # )
            ],
            isShowProfile=True,
        ),
        itemList=get_item_formats_by_uid(user_auth.uid),
        chanceList=[
            # ChanceFormat(
            #     id=1,
            #     value=1,
            # )
        ],
        battlePass=BattlePassFormat(
            is_limbus=True,
            # level=5000,
            # exp=0,
            today_rand_value=12,
            # ex_reward_level=5000,
            limbus_apply_level=4,
            # rewards_state=[1],
            # missions_state=[
            #     BattlePassMissionState(id=100, count=100, state=MISSION_STATE.REWARDED)
            # ],
            # special_product_state=0,
            # ex_reward_limbus_level=5000,
        ),
        mainChapterStateList=create_main_chapter_state_list(),
        mailList=[
            # MailFormat(
            #     mail_id=1,
            #     sent_date="",
            #     expiry_date="",
            #     content_id=0,
            #     attachments=[
            #         Element(
            #             type=STR_ELEMENT_TYPE.ITEM,
            #             _type=ELEMENT_TYPE.ITEM,
            #             id=1,
            #             num=1,
            #             tags=[""],
            #         )
            #     ],
            #     parameters=[""],
            # )
        ],
        # TODO: Parse announcer static data and make DB for it
        announcer=AnnouncerFormat(
            announcer_ids=list(range(100)),
            cur_announcer_ids=[9],
        ),
        membershipList=[
            # MembershipFormat(iap_id=0, expiry_date="datetime")
        ],
        gachaList=[
            # GachaRecordFormat(
            #     gachaId=197,
            #     pityPoint=199,
            # )
        ],
        userUnlockCodeList=create_unlock_code_format_list(),
        eventRewardStateList=[
            # EventRewardStateFormat(
            #     eventID=1,
            #     rewardID=1,
            #     count=1,
            # )
        ],
        isUpdateUserBanner=False,
        isResetMirrorDungeon=False,
        missionList=[
            # MissionFormat(
            #     category=MISSION_CATEGORY.UNRECOGNIZED,
            #     id=0,
            #     state=MISSION_STATE.UNRECOGNIZED,
            #     initconditionvalue=-1,
            #     conditionvalue=-1,
            #     expiredate="datetime",
            # )
        ],
        # TODO: get dante ability from resources
        danteAbilityList=[
            DanteAbilityFormat(
                category=DANTE_ABILITY_CATEGORY.DEFAULT,
                abilityids=[90101],
                remaincount=1,
            ),
            DanteAbilityFormat(
                category=DANTE_ABILITY_CATEGORY.RAILWAY_DUNGEON,
                abilityids=[90101],
                remaincount=1,
            ),
        ],
    )

    user = UserPublicProfileWithSupportersFormat(
        public_uid=str(user_auth.uid),
        illust_id=10209,
        illust_gacksung_level=3,
        leftborder_id=29,
        rightborder_id=29,
        egobackground_id=32,
        sentence_id=36,
        word_id=3,
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
        level=297,
        date=get_date_time(),
        support_personalities=[
            SupportPersonalitySlotFormat(
                idx=10101,
                pid=1,
                l=50,
                egos=[
                    # ProfileEgoContainIndexFormat(
                    #     idx=20101,
                    #     id=20101,
                    #     g=4,
                    # )
                ],
                gl=4,
                gi=1,
            )
        ],
    )

    daily = DailyLoginRewardStateFormat(weekid=0, id=0)

    rsp = RspLoadUserDataAll(
        profile=user,
        danteNoteTodayPage=49,
        dailyLoginRewardStates=[daily],
        dailyLoginWeekId=-1,
        showedWeekByMinistory=-1,
        date=get_date_time(),
    )

    return Sc[RspLoadUserDataAll](
        updated=update,
        # synchronized=SynchronizedFormat(
        #     version=user_auth.synchronousDataVersion,
        #     noticelist=[
        #         # NoticeFormat()
        #     ],
        #     mailContentList=[
        #         # MailContentFormat()
        #     ],
        # ),
        result=rsp,
    )

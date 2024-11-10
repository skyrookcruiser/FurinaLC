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
    MailContentFormat,
)
from utils import get_date_time
from database.ego import get_ego_formats_by_uid
from database.personality import get_personality_formats_by_uid
from database.item import get_item_formats_by_uid
from database.announcer import get_announcer_format_by_uid
from resources.stage_node_reward import create_main_chapter_state_list
from resources.unlockcode_subchapter import create_unlock_code_format_list
from resources.chance import create_chance_format_list
from resources.battlepass import create_battlepass_format
from resources.iap_membership import create_membership_formats


async def handle(req: Cs[ReqLoadUserDataAll]):
    user_auth = req.userAuth
    update = UpdatedFormat(
        isInitialized=True,
        # TODO: implement coupon, then use it to edit all levels
        # personality, ego, user, etc.
        userInfo=UserInfo(
            uid=user_auth.uid, level=302, last_stamina_recover=get_date_time()
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
                # NOTE: ADDING THESE BREAK THE FUCKING
                # LOADING INTO MENU!!! maybe needs to be the same
                # as line 167??
                # LobbyCgDetailFormat(
                #     id=10101,
                #     g=1,
                # )
            ],
            isShowProfile=True,
        ),
        itemList=get_item_formats_by_uid(user_auth.uid),
        chanceList=create_chance_format_list(),
        # TODO: FIX CLAIMED REWARDS
        battlePass=create_battlepass_format(),
        mainChapterStateList=create_main_chapter_state_list(),
        mailList=[],
        announcer=get_announcer_format_by_uid(user_auth.uid),
        membershipList=create_membership_formats(),
        # TODO: edge the player with 199 pity point
        # oh and, implement actual gacha?
        gachaList=[
            # GachaRecordFormat(
            #     gachaId=197,
            #     pityPoint=199,
            # )
        ],
        userUnlockCodeList=create_unlock_code_format_list(),
        # NOTE: this should just be empty, theres no event anyways
        eventRewardStateList=[
            # EventRewardStateFormat(
            #     eventID=1,
            #     rewardID=1,
            #     count=1,
            # )
        ],
        isUpdateUserBanner=False,
        isResetMirrorDungeon=False,
        # TODO: parse from static data and give
        # misisonstate finish to all of them
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
                id=35,  # LoR banner
                value=-1,
                value2=-1,
                idx=0,
            ),
            UserPublicBannerFormat(
                id=7,  # maxed out rail line 1
                value=52,  # turn count
                value2=-1,  # cycle count
                idx=1,
            ),
            UserPublicBannerFormat(
                id=19,  # maxed out rail line 2
                value=70,
                value2=5,
                idx=2,
            ),
            UserPublicBannerFormat(
                id=27,  # maxed out rail line 3
                value=31,
                value2=-1,
                idx=3,
            ),
            UserPublicBannerFormat(
                id=40,  # maxed out rail line 4
                value=29,
                value2=-1,
                idx=4,
            ),
        ],
        level=302,
        date=get_date_time(),
        # TODO: fill support character list
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

    rsp = RspLoadUserDataAll(
        profile=user,
        danteNoteTodayPage=49,
        dailyLoginRewardStates=[],
        dailyLoginWeekId=-1,
        showedWeekByMinistory=-1,
        date=get_date_time(),
    )

    return Sc[RspLoadUserDataAll](
        updated=update,
        result=rsp,
    )

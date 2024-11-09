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
    NoticeFormat,
    MailContentFormat,
)
from database.ego import get_ego_formats_by_uid
from database.personality import get_personality_formats_by_uid
from resources.stage_node_reward import create_main_chapter_state_list


async def handle(req: Cs[ReqLoadUserDataAll]):
    user_auth = req.userAuth
    update = UpdatedFormat(
        isInitialized=True,
        userInfo=UserInfo(
            uid=user_auth.uid, level=404, last_stamina_recover=user_auth.last_login_date
        ),
        personalityList=get_personality_formats_by_uid(user_auth.uid),
        egoList=get_ego_formats_by_uid(user_auth.uid),
        formationList=[
            FormationFormat(
                id=0,
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
                LobbyCgDetailFormat(
                    id=10101,
                    g=1,
                )
            ],
            isShowProfile=True,
        ),
        itemList=[
            ItemFormat(
                item_id=1,
                num=9999,
            )
        ],
        chanceList=[
            ChanceFormat(
                id=1,
                value=1,
            )
        ],
        battlePass=BattlePassFormat(
            is_limbus=True,
            level=5000,
            exp=0,
            today_rand_value=1,
            ex_reward_level=5000,
            limbus_apply_level=0,
            rewards_state=[1],
            missions_state=[
                BattlePassMissionState(id=100, count=100, state=MISSION_STATE.REWARDED)
            ],
            special_product_state=0,
            ex_reward_limbus_level=5000,
        ),
        mainChapterStateList=create_main_chapter_state_list(),
        mailList=[
            MailFormat(
                mail_id=1,
                sent_date="",
                expiry_date="",
                content_id=0,
                attachments=[
                    Element(
                        type=STR_ELEMENT_TYPE.ITEM,
                        _type=ELEMENT_TYPE.ITEM,
                        id=1,
                        num=1,
                        tags=[""],
                    )
                ],
                parameters=[""],
            )
        ],
        announcer=AnnouncerFormat(
            announcer_ids=[9],
            cur_announcer_ids=[9],
        ),
        membershipList=[MembershipFormat(iap_id=0, expiry_date="datetime")],
        gachaList=[
            GachaRecordFormat(
                gachaId=197,
                pityPoint=199,
            )
        ],
        userUnlockCodeList=[
            UnlockCodeFormat(
                unlockcode=100,
                expireDate="datetime",
            )
        ],
        eventRewardStateList=[
            EventRewardStateFormat(
                eventID=1,
                rewardID=1,
                count=1,
            )
        ],
        isUpdateUserBanner=False,
        isResetMirrorDungeon=False,
        missionList=[
            MissionFormat(
                category=MISSION_CATEGORY.UNRECOGNIZED,
                id=0,
                state=MISSION_STATE.UNRECOGNIZED,
                initconditionvalue=-1,
                conditionvalue=-1,
                expiredate="datetime",
            )
        ],
        danteAbilityList=[
            DanteAbilityFormat(
                category=DANTE_ABILITY_CATEGORY.DEFAULT,
                abilityids=[1],
                remaincount=100,
            )
        ],
    )

    user = UserPublicProfileWithSupportersFormat(
        support_personalities=[
            SupportPersonalitySlotFormat(
                idx=1,
                pid=1,
                l=1,
                egos=[
                    ProfileEgoContainIndexFormat(
                        idx=1,
                        id=1,
                        g=1,
                    )
                ],
                gl=1,
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
        date=user_auth.last_login_date,
    )

    return Sc[RspLoadUserDataAll](
        updated=update,
        synchronized=SynchronizedFormat(
            version=user_auth.data_version,
            noticelist=[NoticeFormat()],
            mailContentList=[MailContentFormat()],
        ),
        result=rsp,
    )

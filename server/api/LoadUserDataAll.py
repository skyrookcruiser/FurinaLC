from limbus.requests import Cs, ReqLoadUserDataAll
from limbus.responses import Sc, RspLoadUserDataAll
from limbus.formats import (
    UpdatedFormat,
    LobbyCgFormat,
    DanteAbilityFormat,
    DANTE_ABILITY_CATEGORY,
)
from utils import get_date_time
from database.ego import get_ego_formats_by_uid
from database.user import get_user_info_by_uid
from database.personality import get_personality_formats_by_uid
from database.item import get_item_formats_by_uid
from database.announcer import get_announcer_format_by_uid
from database.formation import get_formation_formats_by_uid
from database.userprofile import get_user_profile_data_by_uid
from resources.stage_node_reward import create_main_chapter_state_list
from resources.unlockcode_subchapter import create_unlock_code_format_list
from resources.chance import create_chance_format_list
from resources.battlepass import create_battlepass_format
from resources.iap_membership import create_membership_formats
# from database.lobbycg import get_one_lobby_cg_format


async def handle(req: Cs[ReqLoadUserDataAll]):
    curr_date = get_date_time()
    user_auth = req.userAuth
    uid = user_auth.uid

    update = UpdatedFormat(
        # isInitialize pretty much sets the base updatedformat
        # for future update shenanigans
        isInitialized=True,
        userInfo=get_user_info_by_uid(uid),
        personalityList=get_personality_formats_by_uid(uid),
        egoList=get_ego_formats_by_uid(uid),
        formationList=get_formation_formats_by_uid(uid),
        lobbyCG=LobbyCgFormat(
            characterId=1,
            lobbycgdetails=[],
            isShowProfile=True,
        ),  # get_one_lobby_cg_format(uid),
        itemList=get_item_formats_by_uid(uid),
        chanceList=create_chance_format_list(),
        battlePass=create_battlepass_format(),
        mainChapterStateList=create_main_chapter_state_list(),
        mailList=[],
        announcer=get_announcer_format_by_uid(uid),
        membershipList=create_membership_formats(),
        gachaList=[],
        userUnlockCodeList=create_unlock_code_format_list(),
        eventRewardStateList=[],
        isUpdateUserBanner=False,
        isResetMirrorDungeon=False,
        missionList=[],
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

    rsp = RspLoadUserDataAll(
        profile=get_user_profile_data_by_uid(uid),
        danteNoteTodayPage=49,
        dailyLoginRewardStates=[],
        dailyLoginWeekId=-1,
        showedWeekByMinistory=-1,
        date=curr_date,
    )

    return Sc[RspLoadUserDataAll](
        updated=update,
        result=rsp,
    )

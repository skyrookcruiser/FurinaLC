from limbus.requests import Cs, ReqLoadUserDataAll
from limbus.responses import Sc, RspLoadUserDataAll
from limbus.formats import (
    UserPublicProfileWithSupportersFormat,
    DailyLoginRewardStateFormat,
    SupportPersonalitySlotFormat,
    ProfileEgoContainIndexFormat,
    UpdatedFormat,
    UserInfo,
    PersonalityFormat,
    EgoFormat,
    FormationFormat,
    LobbyCgFormat,
    ItemFormat,
    ChanceFormat,
    BattlePassFormat,
    MainChapterStateFormat,
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
    SubChapterStateFormat,
    NodeStateFormat,
    Element,
    MISSION_CATEGORY,
    DANTE_ABILITY_CATEGORY,
)


async def handle(req: Cs[ReqLoadUserDataAll]):
    update = UpdatedFormat()
    user = UserPublicProfileFormat()
    daily = DailyLoginRewardStateFormat()
    rsp = RspLoadUserDataAll()

    return Sc[RspLoadUserDataAll](result=rsp)

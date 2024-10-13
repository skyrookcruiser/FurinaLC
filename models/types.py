from pydantic import BaseModel, Field
from typing import List, Optional


class Element(BaseModel):
    type: str = Field(default="", alias="type_")
    id: int = 0
    num: int = 0


class BattlePassParameterFormat(BaseModel):
    enemyKillCount: int = 0
    abnormalityKillCount: int = 0
    isUsedDailyChar: bool = False
    isUsedSeasonEgo: bool = False
    isUsedSeasonAnnouncer: bool = False


class StagePersonalityInfoFormat(BaseModel):
    personalityid: int = 0
    prevlevel: int = 0
    totaladdexp: int = 0


class ExpDungeonClearInfoFormat(BaseModel):
    dungeonid: int = 0
    clearnumber: int = 0


class PartResistFormat(BaseModel):
    id: int = 0
    attr: List[int] = []
    atkr: List[int] = []


class AbnormalityUnlockInformationFormat(BaseModel):
    id: int = 0
    k: int = 0
    s: List[int] = []
    p: List[int] = []
    ps: List[PartResistFormat] = []


class ThreadDungeonClearInfoFormat(BaseModel):
    dungeonid: int = 0
    clearnumber: int = 0
    dungeonlevel: int = 0


class DailyLoginRewardStateFormat(BaseModel):
    weekid: int = 0
    id: int = 0


class MissionConditionContextFormat(BaseModel):
    type: str = Field(default="", alias="type_")
    target1: int = 0
    target2: int = 0
    target3: int = 0
    value: int = 0


class DungeonEgoFormat(BaseModel):
    id: int = 0
    g: int = 0
    idx: int = 0


class StoryDungeonSaveUnitInfoFormat(BaseModel):
    sp: int = 0
    gi: int = 0
    pid: int = 0
    ch: int = 0
    cm: int = 0
    mhos: int = 0
    g: int = 0
    l: int = 0
    es: List[DungeonEgoFormat] = []
    isp: int = 0


class DungeonMapNodeFormat(BaseModel):
    f: int = 0
    s: int = 0
    nid: int = 0


class DungeonMapEgoGiftFormat(BaseModel):
    id: int = 0
    pids: List[int] = []
    un: int = 0
    ul: int = 0


class DungeonChoiceEventSaveDataFormat(BaseModel):
    sl: List[int] = []
    cs: int = 0
    ri: int = 0
    nei: Optional[int] = None


class DungeonEgoSkillStockFormat(BaseModel):
    t: str = ""
    n: int = 0


class StoryDungeonCurrentInfoFormat(BaseModel):
    dul: List[StoryDungeonSaveUnitInfoFormat] = []
    scpn: DungeonMapNodeFormat = DungeonMapNodeFormat()
    scpegl: List[DungeonMapEgoGiftFormat] = []
    opn: List[int] = []
    cn: DungeonMapNodeFormat = DungeonMapNodeFormat()
    egs: List[DungeonMapEgoGiftFormat] = []
    pnids: List[int] = []
    nr: int = 0
    pce: List[DungeonChoiceEventSaveDataFormat] = []
    ess: List[DungeonEgoSkillStockFormat] = []
    dn: int = 0


class StoryDungeonSaveInfoFormat(BaseModel):
    dungeonid: int = 0
    currentinfo: StoryDungeonCurrentInfoFormat = StoryDungeonCurrentInfoFormat()


class MirrorDungeonSaveUnitInfoFormat(BaseModel):
    upidx: List[int] = []
    mlos: int = 0
    pid: int = 0
    ch: int = 0
    cm: int = 0
    mhos: int = 0
    g: int = 0
    l: int = 0
    es: List[DungeonEgoFormat] = []
    isp: int = 0


class MirrorDungeonEgoGiftPoolSetFormat(BaseModel):
    setId: int = 0
    keyword: str = ""
    pool: List[int] = []


class RandomDungeonMapThemeFormat(BaseModel):
    f: int = 0
    tid: int = 0
    tfid: int = 0
    egs: List[int] = []


class ThemeFloorPool(BaseModel):
    tfid: int = 0
    egs: List[int] = []
    upegs: List[int] = []


class RandomDungeonEncounterRewardEventInfoFormat(BaseModel):
    rt: str = ""
    se: int = 0
    sh: int = 0
    pool: List[int] = []
    pool_v2: List[int] = []
    pool_v3: List[int] = []


class UserMirrorDungeonShopDataFormat(BaseModel):
    ph: int = 0
    pup: int = 0
    upid: int = 0
    peg: List[int] = []
    pcf: int = 0
    pabu: int = 0
    pueg: int = 0
    egpool: List[int] = []
    pseg: int = 0
    rc: int = 0
    fre: int = 0


class MirrorDungeonPrevUnitInfoFormat(BaseModel):
    pid: int = 0
    upidx: List[int] = []


class MirrorDungeonCurrentInfoFormat(BaseModel):
    eid: int = 0
    dul: List[MirrorDungeonSaveUnitInfoFormat] = []
    sepsId: int = 0
    seps: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    sepsCreated: int = 0
    tfs: List[RandomDungeonMapThemeFormat] = []
    tfps: List[ThemeFloorPool] = []
    tfpsCreated: int = 0
    rre: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    ri: int = 0
    cost: int = 0
    shop: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    prevdul: List[MirrorDungeonPrevUnitInfoFormat] = []
    preves: List[int] = []
    leveladders: List[int] = []
    bonusChipReward: int = 0
    consumedChipIn: int = 0
    consumedChipOut: int = 0
    fundedChip: int = 0
    startKeyword: str = ""
    cn: DungeonMapNodeFormat = DungeonMapNodeFormat()
    egs: List[DungeonMapEgoGiftFormat] = []
    pnids: List[int] = []
    nr: int = 0
    pce: List[DungeonChoiceEventSaveDataFormat] = []
    ess: List[DungeonEgoSkillStockFormat] = []
    dn: int = 0


class RandomDungeonMapNodeFormatForMapFormat(BaseModel):
    f: int = 0
    s: int = 0
    nid: int = 0
    e: int = 0
    eid: int = 0
    nnids: List[int] = []


class RandomDungeonMapFormat(BaseModel):
    ns: List[RandomDungeonMapNodeFormatForMapFormat] = []


class DungeonStatisticsDataFormat(BaseModel):
    id: int = 0
    gd: int = 0
    rd: int = 0


class MirrorDungeonSaveInfoFormat(BaseModel):
    dungeonId: int = 0
    idx: int = 0
    currentInfo: MirrorDungeonCurrentInfoFormat = MirrorDungeonCurrentInfoFormat()
    dungeonMap: RandomDungeonMapFormat = RandomDungeonMapFormat()
    choiceEventList: List[int] = []
    addUserExp: int = 0
    statistics: List[DungeonStatisticsDataFormat] = []
    encounterstatistics: List[int] = []
    isEndDungeon: int = 0
    isReset: int = 0
    version: int = 0


class RailwayUnitInfoFormat(BaseModel):
    pid: int = 0
    g: int = 0
    l: int = 0
    es: List[DungeonEgoFormat] = []
    sp: int = 0
    gi: int = 0


class RailwayExtraRewardStateFormat(BaseModel):
    id: int = 0
    isRewarded: bool = False


class RailwayBuffFormat(BaseModel):
    id: int = 0
    count: int = 0
    targetids: List[int] = []


class RailwayBuffSetFormat(BaseModel):
    setid: int = 0
    buffs: List[RailwayBuffFormat] = []
    recentbuffid: int = 0
    currentbuffids: List[int] = []


class SaveDataForBS(BaseModel):
    section: int = 0
    isActive: bool = False


class SaveDataForPart(BaseModel):
    partHp: int = 0
    bs: List[SaveDataForBS] = []
    originBs: List[SaveDataForBS] = []


class SaveDataForEach(BaseModel):
    abnormalityHp: int = 0
    abnormalityMaxHp: int = 0
    abnormalityMp: int = 0
    partsData: List[SaveDataForPart] = []
    lastPhase: int = 0
    checkList: List[bool] = []


class SaveDataForRailwayDungeon(BaseModel):
    lastWave: int = 0
    lastTurn: int = 0
    abnoSaveDataList: List[SaveDataForEach] = []


class RailwayDungeonSaveInfoFormat(BaseModel):
    id: int = 0
    prevclearnode: int = 0
    currentnode: int = 0
    lastclearnode: int = 0
    personalities: List[RailwayUnitInfoFormat] = []
    payreward: int = 0
    rewardstate: int = 0
    extrarewardstate: List[RailwayExtraRewardStateFormat] = []
    firstcleardate: str = ""
    currentclearrotation: int = 0
    lastenternodeid: int = 0
    lastclearrotation: int = 0
    buffsets: List[RailwayBuffSetFormat] = []
    initseed: int = 0
    currentseed: int = 0
    enemySaveData: SaveDataForRailwayDungeon = SaveDataForRailwayDungeon()


class StoryMirrorDungeonSaveUnitInfoFormat(BaseModel):
    sp: int = 0
    upidx: List[int] = []
    mlos: int = 0
    pid: int = 0
    ch: int = 0
    cm: int = 0
    mhos: int = 0
    g: int = 0
    l: int = 0
    es: List[DungeonEgoFormat] = []
    isp: int = 0


class StoryMirrorDungeonCurrentInfoFormat(BaseModel):
    cn: DungeonMapNodeFormat = DungeonMapNodeFormat()
    egs: List[DungeonMapEgoGiftFormat] = []
    pnids: List[int] = []
    nr: int = 0
    pce: List[DungeonChoiceEventSaveDataFormat] = []
    ess: List[DungeonEgoSkillStockFormat] = []
    eid: int = 0
    dul: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    rre: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    shop: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    cost: int = 0
    prevdul: List[MirrorDungeonPrevUnitInfoFormat] = []
    preves: List[int] = []
    seps: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    sepsCreated: int = 0


class StoryMirrorDungeonSaveInfoFormat(BaseModel):
    dungeonid: int = 0
    currentinfo: StoryMirrorDungeonCurrentInfoFormat = (
        StoryMirrorDungeonCurrentInfoFormat()
    )
    map: RandomDungeonMapFormat = RandomDungeonMapFormat()
    choiceeventlist: List[int] = []
    statistics: List[DungeonStatisticsDataFormat] = []


class MirrorDungeonClearInfoFormat(BaseModel):
    dungeonid: int = 0
    idx: int = 0
    clearnumber: int = 0
    defeatnumber: int = 0


class MirrorDungeonPersonalityRestStatusFormat(BaseModel):
    pid: int = 0
    cnt: int = 0


class MirrorDungeonPrevPlayRecordFormat(BaseModel):
    pids: List[int] = []
    epsId: int = 0
    prevtfids: List[int] = []
    tfids: List[int] = []


class MirrorDungeonHistoryFormat(BaseModel):
    dungeonid: int = 0
    restStatuses: List[MirrorDungeonPersonalityRestStatusFormat] = []
    prevPlayRecord: MirrorDungeonPrevPlayRecordFormat = (
        MirrorDungeonPrevPlayRecordFormat()
    )


class GachaLogDetail(BaseModel):
    type: str = Field(default="", alias="type_")
    id: int = 0
    ex: Element = Element()


class ItemFormat(BaseModel):
    item_id: int = 0
    num: int = 0


class GachaLog(BaseModel):
    gachaId: int = 0
    gachaDate: str = ""
    paymentId: int = 0
    payments: List[ItemFormat] = []
    gachaLogDetails: List[GachaLogDetail] = []


class PityExpirationUIPopup_PityPoint(BaseModel):
    gachaID: int = 0
    pityNumber: int = 0


class PersonalityFormat(BaseModel):
    personality_id: int = 0
    level: int = 0
    exp: int = 0
    gacksung: int = 0
    order_id: int = 0
    gacksung_illust_type: int = 0
    acquire_time: str = ""


class ProfileEgoContainIndexFormat(BaseModel):
    idx: int = 0
    id: int = 0
    g: int = 0


class SupportPersonalitySlotFormat(BaseModel):
    idx: int = 0
    pid: int = 0
    l: int = 0
    egos: List[ProfileEgoContainIndexFormat] = []
    gl: int = 0
    gi: int = 0


class UserPublicBannerFormat(BaseModel):
    id: int = 0
    value: int = 0
    value2: int = 0
    idx: int = 0


class UserPublicProfileWithSupportersFormat(BaseModel):
    support_personalities: List[SupportPersonalitySlotFormat] = []
    public_uid: str = ""
    illust_id: int = 0
    illust_gacksung_level: int = 0
    leftborder_id: int = 0
    rightborder_id: int = 0
    egobackground_id: int = 0
    sentence_id: int = 0
    word_id: int = 0
    banners: List[UserPublicBannerFormat] = []
    level: int = 0
    date: str = ""


class SeasonLogFormat(BaseModel):
    seasonTo: int = 0
    seasonFrom: int = 0
    unreceivedBattlePassRewards: List[Element] = []
    lostPieces: List[ItemFormat] = []
    acquiredFromLostPieces: List[ItemFormat] = []
    lostPackages: List[ItemFormat] = []
    acquiredFromLostPackages: List[ItemFormat] = []
    date: str = ""


class LobbyCgDetailFormat(BaseModel):
    id: int = 0
    g: int = 0


class LobbyCgFormat(BaseModel):
    characterId: int = 0
    lobbycgdetails: List[LobbyCgDetailFormat] = []
    isShowProfile: bool = False


class UserAuthFormat(BaseModel):
    uid: int = 0
    public_id: int = 0
    db_id: int = 0
    auth_code: str = ""
    last_login_date: str = ""
    last_update_date: str = ""
    data_version: int = 0


class AccountInfoFormat(BaseModel):
    uid: int = 0
    google_account: str = ""
    apple_account: str = ""
    steam_account: str = ""
    unlink_date: str = ""


class LinkAuthFormat(BaseModel):
    public_id: int = 0
    password: str = ""
    expiry_date: str = ""
    details: str = ""


class MailFormat(BaseModel):
    mail_id: int = 0
    sent_date: str = ""
    expiry_date: str = ""
    content_id: int = 0
    attachments: List[Element] = []
    parameters: List[str] = []


class MailLog(BaseModel):
    maillog_id: int = 0
    sent_date: str = ""
    content_id: int = 0
    attachments: List[Element] = []
    unsealed_date: str = ""
    parameters: List[str] = []


class MirrorDungeonGetCharacterInfoFormat(BaseModel):
    pid: int = 0
    egos: List[DungeonEgoFormat] = []


class MirrorDungeonFormationEgoFormat(BaseModel):
    prevEgoId: int = 0
    nextEgoId: int = 0


class MirrorDungeonFormationFormat(BaseModel):
    pervPersonalityId: int = 0
    nextPersonalityId: int = 0
    egos: List[MirrorDungeonFormationEgoFormat] = []


class MirrorDungeonAcquiredChipFormat(BaseModel):
    clearFloorChip: int = 0
    clearNodeChip: int = 0
    battleWinCount: int = 0
    battleWinChip: int = 0
    acquiredEgoGiftChip: int = 0
    difficultyProb: float = 0.0
    startEgoGiftPoolSetBonusChip: int = 0
    personalityRestBonusChip: int = 0
    bonusChipReward: int = 0
    themeBonusChip: int = 0
    consumedChip: int = 0
    totalChip: int = 0


class MirrorDungeonStartBuffInfoFormat(BaseModel):
    dungeonid: int = 0
    bufstate: List[int] = []
    specialbufstate: List[int] = []
    disabled: List[int] = []
    chip: int = 0


class RandomDungeonLevelUpPersonalityInfoFormat(BaseModel):
    pid: int = 0
    ego: DungeonEgoFormat = DungeonEgoFormat()


class MirrorDungeonAcquiredRewardFormat(BaseModel):
    useWeeklyRewardChance: bool = False
    useWeeklyHardRewardChance: bool = False
    acquiredUserExp: int = 0
    rewardList: List[Element] = []


class MirrorDungeonExitRewardFormat(BaseModel):
    chanceConsumption: int = 0
    rewardList: List[Element] = []
    moduleConsumption: int = 0


class TermsOfUseState(BaseModel):
    version: int = 0
    state: int = 0


class UserTheaterInfoFormat(BaseModel):
    rewardedIDList: List[str] = []


class FormationDetailFormat(BaseModel):
    personalityId: int = 0
    egos: List[int] = []
    isParticipated: bool = False
    participationOrder: int = 0


class FormationNameElement(BaseModel):
    k: int = 0
    v: int = 0


class FormationFormat(BaseModel):
    id: int = 0
    formationDetails: List[FormationDetailFormat] = []
    formationNameFormat: List[FormationNameElement] = []


class UserBannerDataFormat(BaseModel):
    id: int = 0
    acquiretime: str = ""
    value: int = 0
    value2: int = 0


class UserPublicProfileFormat(BaseModel):
    public_uid: str = ""
    illust_id: int = 0
    illust_gacksung_level: int = 0
    leftborder_id: int = 0
    rightborder_id: int = 0
    egobackground_id: int = 0
    sentence_id: int = 0
    word_id: int = 0
    banners: List[UserPublicBannerFormat] = []
    level: int = 0
    date: str = ""


class SupportPersonalityFormat(BaseModel):
    pid: int = 0
    l: int = 0
    egos: List[ProfileEgoContainIndexFormat] = []
    gl: int = 0
    gi: int = 0


class UserProfileBorderFormat(BaseModel):
    id: int = 0
    date: str = ""


class UserProfileEgobackgroundFormat(BaseModel):
    id: int = 0
    date: str = ""


class StoryMirrorDungeonGetCharacterInfoFormat(BaseModel):
    pid: int = 0
    egos: List[DungeonEgoFormat] = []
    sp: int = 0


class StoryMirrorDungeonLevelUpPersonalityInfoFormat(BaseModel):
    pid: int = 0
    egos: List[DungeonEgoFormat] = []


class RailwayEGOStockFormat(BaseModel):
    t: str = ""
    n: int = 0


class RailwayUnitSinFormat(BaseModel):
    sp: List[int] = []
    cs: List[int] = []
    rs: int = 0


class RailwayUnitStatusFormat(BaseModel):
    pid: int = 0
    hp: int = 0
    mp: int = 0
    isp: int = 0
    sin: RailwayUnitSinFormat = RailwayUnitSinFormat()
    egos: List[DungeonEgoFormat] = []
    sp: int = 0
    lv: int = 0
    g: int = 0
    gi: int = 0


class RailwayStatisticsDataFormat(BaseModel):
    id: int = 0
    gd: int = 0
    rd: int = 0


class RailwayNodeDataFormat(BaseModel):
    nodeid: int = 0
    egostocks: List[RailwayEGOStockFormat] = []
    status: List[RailwayUnitStatusFormat] = []
    clearturn: int = 0
    playturn: int = 0
    statistics: List[RailwayStatisticsDataFormat] = []
    enemy: SaveDataForRailwayDungeon = SaveDataForRailwayDungeon()
    nodestate: int = 0


class RailwayDetailStatisticsDataFormat(BaseModel):
    collectionId: int = 0
    personalities: List[RailwayUnitInfoFormat] = []
    statistics: List[RailwayStatisticsDataFormat] = []


class RailwayTurnsPerNode(BaseModel):
    nid: int = 0
    turn: int = 0


class RailwayLogDataFormat(BaseModel):
    idx: int = 0
    personalities: List[RailwayUnitInfoFormat] = []
    statistics: List[RailwayStatisticsDataFormat] = []
    detailstatistics: List[RailwayDetailStatisticsDataFormat] = []
    clearturn: int = 0
    turnspernode: List[RailwayTurnsPerNode] = []
    clearrotation: int = 0
    buffsets: List[RailwayBuffSetFormat] = []
    date: str = ""
    deadunitnumber: int = 0


class RailwayBuffSetRequestFormat(BaseModel):
    setId: int = 0
    buffId: int = 0
    targetId: int = 0


class UserInfo(BaseModel):
    uid: int = 0
    level: int = 0
    exp: int = 0
    stamina: int = 0
    last_stamina_recover: str = ""


class EgoFormat(BaseModel):
    ego_id: int = 0
    gacksung: int = 0
    acquire_time: str = ""


class ChanceFormat(BaseModel):
    id: int = 0
    value: int = 0


class BattlePassMissionState(BaseModel):
    id: int = 0
    count: int = 0
    state: int = 0


class BattlePassFormat(BaseModel):
    is_limbus: bool = False
    level: int = 0
    exp: int = 0
    today_rand_value: int = 0
    ex_reward_level: int = 0
    limbus_apply_level: int = 0
    rewards_state: List[int] = []
    missions_state: List[BattlePassMissionState] = []
    special_product_state: int = 0
    ex_reward_limbus_level: int = 0


class NodeStateFormat(BaseModel):
    id: int = 0
    ct: int = 0
    cn: int = 0
    dn: int = 0


class SubChapterStateFormat(BaseModel):
    id: int = 0
    nss: List[NodeStateFormat] = []
    rss: List[int] = []


class MainChapterStateFormat(BaseModel):
    id: int = 0
    subcss: List[SubChapterStateFormat] = []


class AnnouncerFormat(BaseModel):
    announcer_ids: List[int] = []
    cur_announcer_ids: List[int] = []


class MembershipFormat(BaseModel):
    iap_id: int = 0
    expiry_date: str = ""


class GachaRecordFormat(BaseModel):
    gachaId: int = 0
    pityPoint: int = 0


class UnlockCodeFormat(BaseModel):
    unlockcode: int = 0


class EventRewardStateFormat(BaseModel):
    eventID: int = 0
    rewardID: int = 0
    count: int = 0


class MissionFormat(BaseModel):
    category: int = 0
    id: int = 0
    state: int = 0


class MissionConditionFormat(BaseModel):
    id: int = 0
    value: int = 0


class DanteAbilityFormat(BaseModel):
    category: int = 0
    abilityids: List[int] = []
    remaincount: int = 0


class UpdatedFormat(BaseModel):
    isInitialized: bool = False
    userInfo: UserInfo = UserInfo()
    personalityList: List[PersonalityFormat] = []
    egoList: List[EgoFormat] = []
    formationList: List[FormationFormat] = []
    lobbyCG: LobbyCgFormat = LobbyCgFormat()
    itemList: List[ItemFormat] = []
    chanceList: List[ChanceFormat] = []
    battlePass: BattlePassFormat = BattlePassFormat()
    mainChapterStateList: List[MainChapterStateFormat] = []
    mailList: List[MailFormat] = []
    announcer: AnnouncerFormat = AnnouncerFormat()
    membershipList: List[MembershipFormat] = []
    gachaList: List[GachaRecordFormat] = []
    userUnlockCodeList: List[UnlockCodeFormat] = []
    eventRewardStateList: List[EventRewardStateFormat] = []
    isUpdateUserBanner: bool = False
    isResetMirrorDungeon: bool = False
    missionList: List[MissionFormat] = []
    missionConditionList: List[MissionConditionFormat] = []
    danteAbilityList: List[DanteAbilityFormat] = []

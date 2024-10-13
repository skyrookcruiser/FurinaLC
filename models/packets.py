from pydantic import BaseModel, Field
from typing import List
from models.types import *


class ResPacket_GetHellsChickenState(BaseModel):
    dollsNum: int = 0
    rewardState: List[int] = []


class ReqPacket_AcquireHellsChickenReward(BaseModel):
    rewardId: int = 0


class ResPacket_AcquireHellsChickenReward(BaseModel):
    rewardState: List[int] = []
    rewards: List[Element] = []


class ReqPacket_ChangeCurrentAnnouncer(BaseModel):
    announcerIds: List[int] = []


class ResPacket_GetAttendanceState(BaseModel):
    rewardState: List[int] = []
    consumption: int = 0


class ReqPacket_AcquireAttendanceReward(BaseModel):
    partid: int = 0
    id: int = 0


class ResPacket_AcquireAttendanceReward(BaseModel):
    rewardState: List[int] = []
    rewards: List[Element] = []


class ReqPacket_BattlePassMissionReward(BaseModel):
    missionType: int = 0
    missionId: int = 0


class ReqPacket_BattlePassReward(BaseModel):
    level: int = 0


class ResPacket_BattlePassExLevelReward(BaseModel):
    resultElements: List[Element] = []


class ResPacket_BattlePassReward(BaseModel):
    resultElements: List[Element] = []


class ReqPacket_PurchaseBattlePassLevel(BaseModel):
    level: int = 0


class ReqPacket_UseCoupon(BaseModel):
    code: str = ""


class ResPacekt_UseCoupon(BaseModel):
    state: int = 0
    rewards: List[Element] = []
    backoffdate: str = ""
    backoffduration: int = 0


class ResPacekt_GetUserCouponState(BaseModel):
    ispossiblestate: bool = False
    backoffdate: str = ""
    backoffduration: int = 0


class ReqPacket_EnterExpDungeon(BaseModel):
    dungeonid: int = 0


class ResPacket_EnterExpDungeon(BaseModel):
    isclear: int = 0


class ReqPacket_ExitExpDungeon(BaseModel):
    formationId: int = 0
    isWin: int = 0
    supportCharacterId: int = 0
    supportParticipate: bool = False
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    usedDanteAbilityCount: int = 0


class ResPacket_ExitExpDungeon(BaseModel):
    userExp: int = 0
    personalityinfos: List[StagePersonalityInfoFormat] = []
    acquiredtickets: List[Element] = []
    rewards: List[Element] = []
    clearInfo: ExpDungeonClearInfoFormat = ExpDungeonClearInfoFormat()


class ReqPacket_SkipExpDungeon(BaseModel):
    dungeonid: int = 0


class ResPacket_SkipExpDungeon(BaseModel):
    userExp: int = 0
    rewards: List[Element] = []


class ReqPacket_EnterThreadDungeon(BaseModel):
    dungeonid: int = 0
    level: int = 0
    abnormalityids: List[int] = []


class ResPacket_EnterThreadDungeon(BaseModel):
    isClear: int = 0
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_ExitThreadDungeon(BaseModel):
    isWin: int = 0
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    usedDanteAbilityCount: int = 0


class ResPacket_ExitThreadDungeon(BaseModel):
    userExp: int = 0
    rewards: List[Element] = []
    clearInfo: ThreadDungeonClearInfoFormat = ThreadDungeonClearInfoFormat()


class ResPacket_GetDailyDungeonClearInfo(BaseModel):
    expDungeonClearInfo: List[ExpDungeonClearInfoFormat] = []
    threadDungeonClearInfo: List[ThreadDungeonClearInfoFormat] = []


class ReqPacket_SkipThreadDungeon(BaseModel):
    dungeonid: int = 0
    dungeonlevel: int = 0


class ResPacket_SkipThreadDungeon(BaseModel):
    userExp: int = 0
    rewards: List[Element] = []


class ResPacket_GetDailyLoginState(BaseModel):
    weekid: int = 0
    id: int = 0
    rewardstates: List[DailyLoginRewardStateFormat] = []


class ReqPacket_AcquireDailyLoginReward(BaseModel):
    weekid: int = 0
    id: int = 0


class ResPacket_AcquireDailyLoginReward(BaseModel):
    rewards: List[Element] = []


class ResPacket_GetDanteNoteState(BaseModel):
    page: int = 0
    todayPage: int = 0


class ReqPacket_GetStageProgressRateRewardCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    rewardType: int = 0


class ResPacket_GetStageProgressRateRewardCommand(BaseModel):
    rewardList: List[Element] = []


class ReqPacket_EnterStageBattleCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0
    abnormalityids: List[int] = []


class ResPacket_EnterStageBattleCommand(BaseModel):
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_ExitStageBattleCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0
    iswin: bool = False
    turn: int = 0
    formationid: int = 0
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    supportCharacterId: int = 0
    supportPersonalityId: int = 0
    supportEgoIds: List[int] = []
    supportParticipate: bool = False
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    missionConditionContexts: List[MissionConditionContextFormat] = []
    usedDanteAbilityCount: int = 0


class ResPacket_ExitStageBattleCommand(BaseModel):
    stageid: int = 0
    iswin: bool = False
    cleartype: int = 0
    addexptouser: int = 0
    personalityinfos: List[StagePersonalityInfoFormat] = []
    expticket: List[Element] = []
    rewarditem: List[Element] = []
    exrewarditem: List[Element] = []
    firstrewarditem: List[Element] = []
    givebackstaminabyDefeat: Element = Element()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_GetDungeonSaveInfoAll(BaseModel):
    railwayDungeonId: int = 0


class ResPacket_GetDungeonSaveInfoAll(BaseModel):
    storySaveInfo: StoryDungeonSaveInfoFormat = StoryDungeonSaveInfoFormat()
    mirrorOriginSaveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()
    railwaySaveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    storyMirrorSaveInfo: StoryMirrorDungeonSaveInfoFormat = (
        StoryMirrorDungeonSaveInfoFormat()
    )
    mirrorDungeonClearInfos: List[MirrorDungeonClearInfoFormat] = []
    mirrorDungeonHistories: List[MirrorDungeonHistoryFormat] = []


class ResPacket_GetStoryDungeonSaveInfo(BaseModel):
    saveInfo: StoryDungeonSaveInfoFormat = StoryDungeonSaveInfoFormat()


class ReqPacket_EnterStoryDungeon(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0
    personalities: List[StoryDungeonSaveUnitInfoFormat] = []


class ResPacket_EnterStoryDungeon(BaseModel):
    saveInfo: StoryDungeonSaveInfoFormat = StoryDungeonSaveInfoFormat()
    nodesRecord: List[int] = []


class ReqPacket_ReEnterStoryDungeonCommand(BaseModel):
    stageid: int = 0


class ResPacket_ReEnterStoryDungeon(BaseModel):
    saveInfo: StoryDungeonSaveInfoFormat = StoryDungeonSaveInfoFormat()
    nodesRecord: List[int] = []
    statistics: List[DungeonStatisticsDataFormat] = []


class ReqPacket_ExitStoryDungeonCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0


class ResPacket_ExitStoryDungeonCommand(BaseModel):
    saveInfo: StoryDungeonSaveInfoFormat = StoryDungeonSaveInfoFormat()
    iswin: bool = False
    cleartype: int = 0
    addexptouser: int = 0
    personalityinfos: List[StagePersonalityInfoFormat] = []
    expticket: List[Element] = []
    rewarditem: List[Element] = []
    exrewarditem: List[Element] = []
    firstrewarditem: List[Element] = []
    givebackstaminabyDefeat: Element = Element()
    statistics: List[DungeonStatisticsDataFormat] = []
    isGacksung: bool = False


class ReqPacket_EnterStoryDungeonMapNodeCommand(BaseModel):
    floornumber: int = 0
    sectornumber: int = 0
    nodeid: int = 0
    abnormalityids: List[int] = []
    participatedPIds: List[int] = []


class ResPacket_EnterStoryDungeonMapNodeCommand(BaseModel):
    node: DungeonMapNodeFormat = DungeonMapNodeFormat()
    nr: int = 0
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_UpdateStoryDungeonMapNodeCommand(BaseModel):
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    dungeonUnitList: List[StoryDungeonSaveUnitInfoFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []


class ResPacket_UpdateStoryDungeonMapNodeCommand(BaseModel):
    prevChoiceEvent: List[DungeonChoiceEventSaveDataFormat] = []
    currentEgoGifts: List[DungeonMapEgoGiftFormat] = []
    isAllDie: int = 0


class ReqPacket_EnterStoryDungeonMapNodeBattleAfterChoice(BaseModel):
    dungeonUnitList: List[StoryDungeonSaveUnitInfoFormat] = []
    participatedPids: List[int] = []
    abnormalityids: List[int] = []


class ResPacket_EnterStoryDungeonMapNodeBattleAfterChoice(BaseModel):
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    isAllDie: int = 0


class ReqPacket_ExitStoryDungeonMapNodeCommand(BaseModel):
    noderesult: int = 0
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    dungeonunitlist: List[StoryDungeonSaveUnitInfoFormat] = []
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    openedNode: int = 0
    isupdatedEgoSkillStock: int = 0
    egoSkillStockList: List[DungeonEgoSkillStockFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []
    statistics: List[DungeonStatisticsDataFormat] = []
    usedDanteAbilityCount: int = 0


class ResPacket_ExitStoryDungeonMapNodeCommand(BaseModel):
    saveInfo: StoryDungeonSaveInfoFormat = StoryDungeonSaveInfoFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    acquiredEgogifts: List[DungeonMapEgoGiftFormat] = []
    isAllDie: int = 0


class ReqPacket_UpdateStoryDungeonUnits(BaseModel):
    dungeonunitlist: List[StoryDungeonSaveUnitInfoFormat] = []


class ResPacket_ReturnSavePointStoryDungeonMap(BaseModel):
    currentInfo: StoryDungeonCurrentInfoFormat = StoryDungeonCurrentInfoFormat()


class ResPacket_ExitStoryDungeonMapNodeByForcely(BaseModel):
    currentInfo: StoryDungeonCurrentInfoFormat = StoryDungeonCurrentInfoFormat()
    isAllDie: int = 0


class ReqPacket_ExitStoryCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0


class ResPacket_ExitStoryCommand(BaseModel):
    rewarditem: List[Element] = []
    exrewarditem: List[Element] = []


class ReqPacket_GetAbnormalityLogData(BaseModel):
    abnormalityIds: List[int] = []


class ResPacket_GetAbnormalityLogData(BaseModel):
    logdatas: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_UpdateAbnormalityLogData(BaseModel):
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ResPacket_UpdateAbnormalityLogData(BaseModel):
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_GetStoryDungeonNodeRecord(BaseModel):
    dungeonid: int = 0


class ResPacket_GetStoryDungeonNodeRecord(BaseModel):
    nodes: List[int] = []


class ReqPacket_ClaimEventRewardCommand(BaseModel):
    eventId: int = 0
    eventRewardId: int = 0
    count: int = 0


class ResPacket_ClaimEventRewardCommand(BaseModel):
    acquiredElements: List[Element] = []


class ReqPacket_ClaimEventReward_ALLCommand(BaseModel):
    eventId: int = 0
    count: int = 0


class ResPacket_ClaimEventReward_ALLCommand(BaseModel):
    acquiredElements: List[Element] = []


class ReqPacket_PlayGacha(BaseModel):
    gachaId: int = 0
    paymentId: int = 0


class ResPacket_PlayGacha(BaseModel):
    gachaLogDetails: List[GachaLogDetail] = []


class ResPacket_GetGachaLogAll(BaseModel):
    gachaLogs: List[GachaLog] = []


class ReqPacket_UseGachaPityPoint(BaseModel):
    gachaId: int = 0
    targetIdx: int = 0


class ResPacket_UseGachaPityPoint(BaseModel):
    gachaLogDetails: List[GachaLogDetail] = []


class ResPacket_ClaimClosedGachaRewards(BaseModel):
    pityPointDataList: List[PityExpirationUIPopup_PityPoint] = []


class ReqPacket_Purchase(BaseModel):
    productId: str = ""
    receipt: str = ""
    platform: int = 0


class ReqPacket_PurchaseAsGoogle(BaseModel):
    productId: str = ""
    receipt: str = ""


class ReqPacket_PurchaseAsApple(BaseModel):
    productId: str = ""
    receipt: str = ""


class ReqPacket_InitPurchaseAsSteam(BaseModel):
    productId: str = ""
    steamId: str = ""
    language: str = ""
    productDesc: str = ""


class ReqPacket_FinalizePurchaseAsSteam(BaseModel):
    orderId: str = ""


class ReqPacket_InitPurchase(BaseModel):
    productId: str = ""


class ResPacket_InitPurchase(BaseModel):
    resultState: str = ""


class ReqPacket_PurchaseIngameProduct(BaseModel):
    igProductId: int = 0


class ReqPacket_UseItem(BaseModel):
    itemId: int = 0
    usage: int = 0
    targetIdx: int = 0
    target: Element = Element()


class ResPacket_UseItem(BaseModel):
    pickedUpElementList: List[Element] = []
    resultElementList: List[Element] = []


class ReqPacket_PurchaseEnkephalinModule(BaseModel):
    num: int = 0


class ReqPacket_PurchaseEnkephalin(BaseModel):
    num: int = 0


class ReqPacket_PersonalityGacksung(BaseModel):
    personalityId: int = 0


class ReqPacket_SetPersonalityGacksungIllust(BaseModel):
    personalityId: int = 0
    type: int = Field(default=0, alias="type_")


class ReqPacket_EgoGacksung(BaseModel):
    egoId: int = 0


class ReqPacket_UsePersonalityExpItem(BaseModel):
    targetPersonalityId: int = 0
    items: List[ItemFormat] = []


class ResPacket_UsePersonalityExpItem(BaseModel):
    resultPersonality: PersonalityFormat = PersonalityFormat()


class ReqPacket_UseEgoGacksungItem(BaseModel):
    targetEgoId: int = 0
    usingItem: ItemFormat = ItemFormat()


class ReqPacket_LoadUserDataAll(BaseModel):
    pass


class ResPacket_LoadUserDataAll(BaseModel):
    secession_Date: str = ""
    profile: UserPublicProfileWithSupportersFormat = (
        UserPublicProfileWithSupportersFormat()
    )
    isExistReceiveFriendRequest: bool = False
    danteNoteTodayPage: int = 0
    dailyLoginRewardStates: List[DailyLoginRewardStateFormat] = []
    dailyLoginWeekId: int = 0
    dailyLoginId: int = 0
    showedWeekByMinistory: int = 0
    date: str = ""


class ResPacket_CheckSeasonLog(BaseModel):
    seasonLog: SeasonLogFormat = SeasonLogFormat()


class ReqPacket_LobbyCgCommand(BaseModel):
    lobbyCg: LobbyCgFormat = LobbyCgFormat()


class ReqPacket_SignInAsGuest(BaseModel):
    guestId: int = 0
    authToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ResPacket_SignInAsGuest(BaseModel):
    userAuth: UserAuthFormat = UserAuthFormat()


class ReqPacket_SignInAsNewGuest(BaseModel):
    deviceModel: str = ""


class ResPacket_SignInAsNewGuest(BaseModel):
    userAuth: UserAuthFormat = UserAuthFormat()
    authToken: str = ""


class ReqPacket_SignInAsGoogle(BaseModel):
    googleToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ResPacket_SignInAsGoogle(BaseModel):
    userAuth: UserAuthFormat = UserAuthFormat()
    accountInfo: AccountInfoFormat = AccountInfoFormat()


class ReqPacket_LinkWithGoogle(BaseModel):
    googleToken: str = ""
    version: str = ""


class ResPacket_LinkWithGoogle(BaseModel):
    userAuth: UserAuthFormat = UserAuthFormat()
    accountInfo: AccountInfoFormat = AccountInfoFormat()


class ReqPacket_SignInAsApple(BaseModel):
    appleToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ResPacket_SignInAsApple(BaseModel):
    userAuth: UserAuthFormat = UserAuthFormat()
    accountInfo: AccountInfoFormat = AccountInfoFormat()


class ReqPacket_LinkWithApple(BaseModel):
    appleToken: str = ""
    version: str = ""


class ResPacket_LinkWithApple(BaseModel):
    userAuth: UserAuthFormat = UserAuthFormat()
    accountInfo: AccountInfoFormat = AccountInfoFormat()


class ReqPacket_SignInAsSteam(BaseModel):
    steamToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ResPacket_SignInAsSteam(BaseModel):
    userAuth: UserAuthFormat = UserAuthFormat()
    accountInfo: AccountInfoFormat = AccountInfoFormat()
    walletCurrency: str = ""


class ReqPacket_RefreshLinkAuth(BaseModel):
    details: str = ""


class ResPacket_RefreshLinkAuth(BaseModel):
    linkAuth: LinkAuthFormat = LinkAuthFormat()
    state: str = ""


class ReqPacket_GetInfoOfLinkWith(BaseModel):
    targetPublicId: str = ""
    password: str = ""


class ResPacket_GetInfoOfLinkWith(BaseModel):
    details: str = ""
    state: str = ""


class ReqPacket_LinkWithAnother(BaseModel):
    targetPublicId: str = ""
    password: str = ""
    mainIsTarget: bool = False


class ResPacket_LinkWithAnother(BaseModel):
    state: str = ""


class ResPacket_TryToSecede(BaseModel):
    secessionDate: str = ""


class ResPacket_CheckClientVersion(BaseModel):
    timeoffset: int = 0


class ResPacket_GetBanDetails(BaseModel):
    startDate: str = ""
    endDate: str = ""
    reason: str = ""


class ReqPacket_UnLinkWithAnother(BaseModel):
    accountInfo: AccountInfoFormat = AccountInfoFormat()
    isUnlinkGoogle: bool = False
    isUnlinkApple: bool = False
    isUnlinkSteam: bool = False
    accountType: str = ""


class ResPacket_UnLinkWithAnother(BaseModel):
    accountInfo: AccountInfoFormat = AccountInfoFormat()


class ResPacket_RefreshMailbox(BaseModel):
    initializedMailList: List[MailFormat] = []


class ReqPacket_UnsealMails(BaseModel):
    mailIds: List[int] = []


class ResPacket_UnsealMails(BaseModel):
    attachedElements: List[Element] = []


class ResPacket_GetMailLogAll(BaseModel):
    mailLogs: List[MailLog] = []


class ReqPacket_ReportSpeedHack(BaseModel):
    detectedDate: str = ""
    scene: str = ""


class ReqPacket_ReportModifiedHashCatalog(BaseModel):
    platform: str = ""
    hashvalue: str = ""


class ReqPacket_SaveMiniStoryWeek(BaseModel):
    weekId: int = 0


class ReqPacket_CompleteMinistory(BaseModel):
    storyId: str = ""


class ResPacket_GetMirrorDungeonSaveInfoAll(BaseModel):
    originSaveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()
    simulationsaveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ResPacket_GetMirrorDungeonSaveInfo(BaseModel):
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ReqPacket_EnterMirrorDungeonCommand(BaseModel):
    dungeonid: int = 0
    idx: int = 0
    isOrigin: int = 0


class ResPacket_EnterMirrorDungeonCommand(BaseModel):
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()
    recentCharacterList: List[MirrorDungeonGetCharacterInfoFormat] = []


class ReqPacket_ReEnterMirrorDungeonCommand(BaseModel):
    dungeonid: int = 0
    idx: int = 0
    isOrigin: int = 0


class ReqPacket_UpdateMirrorDungeonCommand(BaseModel):
    characterInfos: List[MirrorDungeonGetCharacterInfoFormat] = []
    formation: List[MirrorDungeonFormationFormat] = []
    isOrigin: int = 0


class ResPacket_UpdateMirrorDungeonCommand(BaseModel):
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ReqPacket_SelectFormationAndCreateThemePoolMirrorDungeonCommand(BaseModel):
    characterInfos: List[MirrorDungeonGetCharacterInfoFormat] = []
    formation: List[MirrorDungeonFormationFormat] = []
    isOrigin: int = 0


class ResPacket_SelectFormationAndCreateThemePoolMirrorDungeonCommand(BaseModel):
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ResPacket_RecreateThemeFloorPoolMirrorDungeonCommand(BaseModel):
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ReqPacket_SelectThemeFloorMirrorDungeonCommand(BaseModel):
    selectedThemeFoorId: int = 0


class ResPacket_SelectThemeFloorMirrorDungeonCommand(BaseModel):
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ResPacket_ExitMirrorDungeonCommand(BaseModel):
    isEndDungeon: int = 0
    isclear: int = 0
    statistics: List[DungeonStatisticsDataFormat] = []


class ReqPacket_AcquireMirrorDungeonLastReward(BaseModel):
    useEnkephalinModule: int = 0
    usehardbonus: int = 0
    useweeklybonus: int = 0
    isOrigin: int = 0


class ResPacket_AcquireMirrorDungeonLastReward(BaseModel):
    rewardList: List[Element] = []
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()
    acquiredChip: MirrorDungeonAcquiredChipFormat = MirrorDungeonAcquiredChipFormat()
    history: MirrorDungeonHistoryFormat = MirrorDungeonHistoryFormat()
    startBuffInfo: MirrorDungeonStartBuffInfoFormat = MirrorDungeonStartBuffInfoFormat()


class ReqPacket_EnterMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    abnormalityids: List[int] = []
    participatedPIds: List[int] = []
    isOrigin: int = 0


class ResPacket_EnterMirrorDungeonMapNodeCommand(BaseModel):
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    passingNodeIds: List[int] = []
    currentNode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    shopInfo: UserMirrorDungeonShopDataFormat = ()
    egogifts: List[DungeonMapEgoGiftFormat] = []
    prevdul: List[MirrorDungeonPrevUnitInfoFormat] = []
    preves: List[int] = []


class ReqPacket_UpdateMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []
    isOrigin: int = 0


class ResPacket_UpdateMirrorDungeonMapNodeCommand(BaseModel):
    prevChoiceEvent: List[DungeonChoiceEventSaveDataFormat] = []
    currentEgoGifts: List[DungeonMapEgoGiftFormat] = []
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_EnterMirrordungeonMapNodeBattleAfterChoice(BaseModel):
    participatedPids: List[int] = []
    abnormalityids: List[int] = []
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    isOrigin: int = 0


class ResPacket_EnterMirrordungeonMapNodeBattleAfterChoice(BaseModel):
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_ExitMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    dungeonunitlist: List[MirrorDungeonSaveUnitInfoFormat] = []
    noderesult: int = 0
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    isupdatedEgoSkillStock: int = 0
    egoSkillStockList: List[DungeonEgoSkillStockFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []
    statistics: List[DungeonStatisticsDataFormat] = []
    usedDanteAbilityCount: int = 0
    battleStatus: int = 0
    isOrigin: int = 0


class ResPacket_ExitMirrorDungeonMapNodeCommand(BaseModel):
    currentInfo: MirrorDungeonCurrentInfoFormat = MirrorDungeonCurrentInfoFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_UpdateMirrorDungeonUnits(BaseModel):
    dungeonunitlist: List[MirrorDungeonSaveUnitInfoFormat] = []
    isOrigin: int = 0


class ReqPacket_MirrorDungeonCommon(BaseModel):
    isOrigin: int = 0


class ResPacket_ExitMirrorDungeonMapNodeByForcely(BaseModel):
    currentInfo: MirrorDungeonCurrentInfoFormat = MirrorDungeonCurrentInfoFormat()


class ReqPacket_AcquireRewardEgoGiftsMirrorDungeonCommand(BaseModel):
    selectIndexList: List[int] = []
    isOrigin: int = 0


class ResPacket_AcquireRewardEgoGiftsMirrorDungeonCommand(BaseModel):
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    saveinfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ReqPacket_AcquireRewardEgoGiftsWithEnemyBufMirrorDungeonCommand(BaseModel):
    selectIndexList: List[int] = []
    isOrigin: int = 0


class ResPacket_AcquireRewardEgoGiftsWithEnemyBufMirrorDungeonCommand(BaseModel):
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    levelAdders: List[int] = []
    saveinfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ResPacket_RejectRewardEgoGiftsMirrorDungeonCommand(BaseModel):
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    saveinfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ResPacket_RejectRewardEgoGiftWithEnemyBufsMirrorDungeonCommand(BaseModel):
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    levelAdders: List[int] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    saveinfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ReqPacket_AcquireCharacterEventDataMirrorDungeonCommand(BaseModel):
    acquirePersonalities: List[MirrorDungeonGetCharacterInfoFormat] = []
    isOrigin: int = 0


class ResPacket_AcquireCharacterEventDataMirrorDungeonCommand(BaseModel):
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []


class ReqPacket_PersonalityLevelUpEventMirrorDungeonCommand(BaseModel):
    levelUpPersonalityFormat: RandomDungeonLevelUpPersonalityInfoFormat = (
        RandomDungeonLevelUpPersonalityInfoFormat()
    )
    isOrigin: int = 0


class ResPacket_PersonalityLevelUpEventMirrorDungeonCommand(BaseModel):
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []


class ReqPacket_AcquireMirrorDungeonBattleRewardCommand(BaseModel):
    selectIndexList: List[int] = []
    isOrigin: int = 0


class ResPacket_AcquireMirrorDungeonBattleRewardCommand(BaseModel):
    saveinfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()


class ResPacket_GetMirrorDungeonEgoGiftRecordCommand(BaseModel):
    acquiredegogifts: List[int] = []


class ReqPacket_UnLockMirrorDungeonEgoGiftCommand(BaseModel):
    egogiftIds: List[int] = []


class ReqPacket_SendMirrorDungeonLogErrorCommand(BaseModel):
    type: int = Field(default=0, alias="type_")


class ReqPacket_PurchaseHealMirrorDungeon(BaseModel):
    idx: int = 0
    pid: int = 0


class ResPacket_PurchaseHealMirrorDungeon(BaseModel):
    cost: int = 0
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()


class ReqPacket_PurchaseFormationMirrorDungeon(BaseModel):
    formation: List[MirrorDungeonFormationFormat] = []


class ResPacket_PurchaseFormationMirrorDungeon(BaseModel):
    cost: int = 0
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    prevUnitInfo: MirrorDungeonPrevUnitInfoFormat = MirrorDungeonPrevUnitInfoFormat()


class ReqPacket_PurchaseUpgradePersonalityMirrorDungeon(BaseModel):
    idx: int = 0


class ResPacket_PurchaseUpgradePersonalityMirrorDungeon(BaseModel):
    cost: int = 0
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()


class ReqPacket_PurchaseEgoGiftMirrorDungeon(BaseModel):
    idx: int = 0


class ResPacket_PurchaseEgoGiftMirrorDungeon(BaseModel):
    cost: int = 0
    egogifts: List[DungeonMapEgoGiftFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_SellEgoGift(BaseModel):
    id: int = 0


class ResPacket_SellEgoGift(BaseModel):
    cost: int = 0
    egogifts: List[DungeonMapEgoGiftFormat] = []


class ReqPacket_RefreshShopEgoGiftsMirrorDungeonCommand(BaseModel):
    isPaidWithChip: bool = False
    keyword: str = ""
    isOrigin: int = 0


class ResPacket_RefreshShopEgoGiftsMirrorDungeonCommand(BaseModel):
    cost: int = 0
    consumedChipIn: int = 0
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()


class ReqPacket_GetStartBuffFInfoMirrorDungeon(BaseModel):
    dungeonid: int = 0


class ResPacket_GetStartBuffFInfoMirrorDungeon(BaseModel):
    startBuffInfo: MirrorDungeonStartBuffInfoFormat = MirrorDungeonStartBuffInfoFormat()


class ReqPacket_PurchaseStartBuffMirrorDungeon(BaseModel):
    dungeonid: int = 0
    buffids: List[int] = []


class ResPacket_PurchaseStartBuffMirrorDungeon(BaseModel):
    startBuffInfo: MirrorDungeonStartBuffInfoFormat = MirrorDungeonStartBuffInfoFormat()


class ReqPacket_EnableSpecialStartBuffMirrorDungeon(BaseModel):
    dungeonid: int = 0
    buffids: List[int] = []


class ResPacket_EnableSpecialStartBuffMirrorDungeon(BaseModel):
    startBuffInfo: MirrorDungeonStartBuffInfoFormat = MirrorDungeonStartBuffInfoFormat()


class ReqPacket_DisableStartBuffMirrorDungeon(BaseModel):
    dungeonid: int = 0
    buffids: List[int] = []


class ResPacket_DisableStartBuffMirrorDungeon(BaseModel):
    startBuffInfo: MirrorDungeonStartBuffInfoFormat = MirrorDungeonStartBuffInfoFormat()


class ReqPacket_RemoveMirrorDungeonEgoGift(BaseModel):
    egogiftId: int = 0


class ResPacket_RemoveMirrorDungeonEgoGift(BaseModel):
    egs: List[DungeonMapEgoGiftFormat] = []


class ResPacket_MirrorDungeonGiveUpSelectingEgoGift(BaseModel):
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []


class ReqPacket_GetMirrorDungeonPreset(BaseModel):
    dungeonid: int = 0
    idx: int = 0


class ResPacket_GetMirrorDungeonPreset(BaseModel):
    recentCharacterList: List[MirrorDungeonFormationFormat] = []


class ReqPacket_GetMirrorDungeonRewardChip(BaseModel):
    pass


class ResPacket_GetMirrorDungeonRewardChip(BaseModel):
    acquiredChip: MirrorDungeonAcquiredChipFormat = MirrorDungeonAcquiredChipFormat()
    rewardList: List[MirrorDungeonAcquiredRewardFormat] = []


class ReqPacket_SelectMirrorDungeonRandomPickFormation(BaseModel):
    dungeonid: int = 0
    idx: int = 0


class ResPacket_SelectMirrorDungeonRandomPickFormation(BaseModel):
    formation: List[MirrorDungeonFormationFormat] = []


class ReqPacket_AcquireStartEgoGiftsMirrorDungeonCommand(BaseModel):
    selectedSetId: int = 0
    selectedEgoGiftIds: List[int] = []
    isOrigin: int = 0


class ResPacket_AcquireStartEgoGiftsMirrorDungeonCommand(BaseModel):
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    startEgoGiftPoolSets: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    startEgoGiftCreatedCount: int = 0


class ReqPacket_RefreshStartEgoGiftsMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0


class ResPacket_RefreshStartEgoGiftsMirrorDungeonCommand(BaseModel):
    startEgoGiftPoolSets: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    startEgoGiftCreatedCount: int = 0


class ReqPacket_UpgradeEgoGiftMirrorDungeonCommand(BaseModel):
    egoGiftId: int = 0
    isOrigin: int = 0


class ResPacket_UpgradeEgoGiftMirrorDungeonCommand(BaseModel):
    cost: int = 0
    egoGift: DungeonMapEgoGiftFormat = DungeonMapEgoGiftFormat()
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_CombineEgoGiftMirrorDungeonCommand(BaseModel):
    materialEgoGiftIds: List[int] = []
    keyword: str = ""
    isOrigin: int = 0


class ResPacket_CombineEgoGiftMirrorDungeonCommand(BaseModel):
    resultEgoGift: DungeonMapEgoGiftFormat = DungeonMapEgoGiftFormat()
    isSuccess: bool = False
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []


class ResPacket_PreviewMirrorDungeonExitReward(BaseModel):
    acquiredChip: MirrorDungeonAcquiredChipFormat = MirrorDungeonAcquiredChipFormat()
    rewardList: List[MirrorDungeonExitRewardFormat] = []


class ReqPacket_AcquireMirrorDungeonExitReward(BaseModel):
    useEnkephalinModule: bool = False
    chanceConsumption: int = 0


class ResPacket_AcquireMirrorDungeonExitReward(BaseModel):
    rewardList: List[Element] = []
    saveInfo: MirrorDungeonSaveInfoFormat = MirrorDungeonSaveInfoFormat()
    acquiredChip: MirrorDungeonAcquiredChipFormat = MirrorDungeonAcquiredChipFormat()
    history: MirrorDungeonHistoryFormat = MirrorDungeonHistoryFormat()
    startBuffInfo: MirrorDungeonStartBuffInfoFormat = MirrorDungeonStartBuffInfoFormat()


class ReqPacket_AcquireMissionRewardsCommand(BaseModel):
    missionIds: List[int] = []


class ResPacket_AcquireMissionRewardsCommand(BaseModel):
    acquiredElements: List[Element] = []


class ReqPacket_ReportError(BaseModel):
    errorCode: str = ""
    url: str = ""
    requestJson: str = ""
    message: str = ""


class ReqPacket_GetTermsOfUseStateAll(BaseModel):
    uid: int = 0


class ResPacket_GetTermsOfUseStateAll(BaseModel):
    termsOfUseStateList: List[TermsOfUseState] = []


class ReqPacket_UpdateTermsOfUseState(BaseModel):
    uid: int = 0
    termsVersion: int = 0
    state: int = 0


class ResPacket_GetTheaterInfo(BaseModel):
    theaterInfo: UserTheaterInfoFormat = UserTheaterInfoFormat()


class ReqPacket_CompleteTheaterStory(BaseModel):
    storyId: str = ""


class ResPacket_CompleteTheaterStory(BaseModel):
    isRewarded: bool = False
    acquiredElements: List[Element] = []
    theaterInfo: UserTheaterInfoFormat = UserTheaterInfoFormat()


class ReqPacket_UpdateFormationCommand(BaseModel):
    formation: FormationFormat = FormationFormat()


class ResPacket_GetUserBanners(BaseModel):
    banners: List[UserBannerDataFormat] = []


class ResPacket_GetFriendsData(BaseModel):
    friendprofileList: List[UserPublicProfileFormat] = []
    sendprofileList: List[UserPublicProfileFormat] = []
    receiveprofileList: List[UserPublicProfileFormat] = []


class ReqPacket_FindFriend(BaseModel):
    publicUID: str = ""


class ResPacket_FindFriend(BaseModel):
    success: bool = False
    friendprofile: UserPublicProfileFormat = UserPublicProfileFormat()


class ResPacket_GetRecommendFriends(BaseModel):
    recomendedFriends: List[UserPublicProfileFormat] = []


class ReqPacket_SendFriendRequest(BaseModel):
    receiverPublicUID: str = ""


class ResPacket_SendFriendRequest(BaseModel):
    success: int = 0
    receiverprofile: UserPublicProfileFormat = UserPublicProfileFormat()


class ReqPacket_AcceptReceivedFriendRequest(BaseModel):
    senderPublicUID: str = ""


class ResPacket_AcceptReceivedFriendRequest(BaseModel):
    success: int = 0


class ReqPacket_RejectReceivedFriendRequest(BaseModel):
    senderPublicUID: str = ""


class ReqPacket_CancelSentFriendRequest(BaseModel):
    receivedPublicUID: str = ""


class ReqPacket_DeleteFriend(BaseModel):
    deletedPublicUID: str = ""


class ReqPacket_GetFriendSupportPersonalities(BaseModel):
    publicUID: str = ""


class ResPacket_GetFriendSupportPersonalities(BaseModel):
    supportpersonalities: List[SupportPersonalitySlotFormat] = []


class ReqPacket_GetFriendSupportPersonalitiesByCharacterId(BaseModel):
    characterid: int = 0


class ResPacket_GetFriendSupportPersonalitiesByCharacterId(BaseModel):
    supportpersonalities: List[SupportPersonalityFormat] = []


class ReqPacket_UpdateUserProfile(BaseModel):
    illustId: int = 0
    illustGacksungLevel: int = 0
    sentenceId: int = 0
    wordId: int = 0
    banners: List[UserPublicBannerFormat] = []
    supportPersonalities: List[SupportPersonalitySlotFormat] = []


class ResPacket_GetProfileTicketDecoDatas(BaseModel):
    leftBorders: List[UserProfileBorderFormat] = []
    rightBorders: List[UserProfileBorderFormat] = []
    egoBackgrounds: List[UserProfileEgobackgroundFormat] = []


class ReqPacket_UpdateProfileTicketDeco(BaseModel):
    leftBorderId: int = 0
    rightBorderId: int = 0
    egoBackgroundId: int = 0


class ResPacket_UpdateProfileTicketDeco(BaseModel):
    leftBorderId: int = 0
    rightBorderId: int = 0
    egoBackgroundId: int = 0


class ReqPacket_PlayVendingMachine(BaseModel):
    vendingMachineId: int = 0
    targetType: str = ""
    targetId: int = 0
    coupons: List[int] = []
    isPaidByLunacy: bool = False


class ResPacket_PlayVendingMachine(BaseModel):
    itemConsumptions: List[ItemFormat] = []


class ReqPacket_ExchangeTwine(BaseModel):
    paidPieces: List[ItemFormat] = []


class ReqPacket_AcquireEgoGiftEventStoryMirrorDungeonCommand(BaseModel):
    selectIndexList: List[int] = []


class ResPacket_AcquireEgoGiftEventStoryMirrorDungeonCommand(BaseModel):
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []


class ReqPacket_AcquireCharacterEventDataStoryMirrorDungeonCommand(BaseModel):
    acquirePersonalities: List[StoryMirrorDungeonGetCharacterInfoFormat] = []


class ResPacket_AcquireCharacterEventDataStoryMirrorDungeonCommand(BaseModel):
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []


class ReqPacket_PersonalityLevelUpEventStoryMirrorDungeonCommand(BaseModel):
    levelUpPersonalityFormat: StoryMirrorDungeonLevelUpPersonalityInfoFormat = (
        StoryMirrorDungeonLevelUpPersonalityInfoFormat()
    )


class ResPacket_PersonalityLevelUpEventStoryMirrorDungeonCommand(BaseModel):
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []


class ReqPacket_EnterStoryMirrorDungeonCommand(BaseModel):
    dungeonid: int = 0
    idx: int = 0


class ResPacket_EnterStoryMirrorDungeonCommand(BaseModel):
    saveInfo: StoryMirrorDungeonSaveInfoFormat = StoryMirrorDungeonSaveInfoFormat()


class ReqPacket_ReEnterStoryMirrorDungeonCommand(BaseModel):
    dungeonid: int = 0


class ReqPacket_UpdateStoryMirrorDungeonCommand(BaseModel):
    formation: List[MirrorDungeonFormationFormat] = []


class ResPacket_UpdateStoryMirrorDungeonCommand(BaseModel):
    saveInfo: StoryMirrorDungeonSaveInfoFormat = StoryMirrorDungeonSaveInfoFormat()


class ResPacket_ExitStoryMirrorDungeonCommand(BaseModel):
    saveInfo: StoryMirrorDungeonSaveInfoFormat = StoryMirrorDungeonSaveInfoFormat()
    isclear: int = 0
    statistics: List[DungeonStatisticsDataFormat] = []
    cleartype: int = 0
    adduserexp: int = 0
    personalityinfos: List[StagePersonalityInfoFormat] = []
    normalrewards: List[Element] = []
    exrewards: List[Element] = []
    firstrewarditem: List[Element] = []
    expticket: List[Element] = []
    givebackstaminabyDefeat: Element = Element()


class ReqPacket_EnterStoryMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    abnormalityids: List[int] = []
    participatedPIds: List[int] = []


class ResPacket_EnterStoryMirrorDungeonMapNodeCommand(BaseModel):
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    passingNodeIds: List[int] = []
    currentNode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    egogifts: List[DungeonMapEgoGiftFormat] = []
    prevdul: List[MirrorDungeonPrevUnitInfoFormat] = []
    preves: List[int] = []


class ReqPacket_UpdateStoryMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []


class ResPacket_UpdateStoryMirrorDungeonMapNodeCommand(BaseModel):
    prevChoiceEvent: List[DungeonChoiceEventSaveDataFormat] = []
    currentEgoGifts: List[DungeonMapEgoGiftFormat] = []
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_EnterStoryMirrorDungeonMapNodeBattleAfterChoiceCommand(BaseModel):
    participatedPids: List[int] = []
    abnormalityids: List[int] = []
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ResPacket_EnterStoryMirrorDungeonMapNodeBattleAfterChoiceCommand(BaseModel):
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_ExitStoryMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    dungeonunitlist: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    noderesult: int = 0
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    isupdatedEgoSkillStock: int = 0
    egoSkillStockList: List[DungeonEgoSkillStockFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []
    statistics: List[DungeonStatisticsDataFormat] = []
    usedDanteAbilityCount: int = 0


class ResPacket_ExitStoryMirrorDungeonMapNodeCommand(BaseModel):
    currentInfo: StoryMirrorDungeonCurrentInfoFormat = (
        StoryMirrorDungeonCurrentInfoFormat()
    )
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ResPacket_NULL(BaseModel):
    pass


class ReqPacket_UpdateStoryMirrorDungeonUnitsCommand(BaseModel):
    dungeonunitlist: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_AcquireRewardEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    selectIndexList: List[int] = []


class ResPacket_AcquireRewardEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_NULL(BaseModel):
    pass


class ResPacket_RejectRewardEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    remainRewardEvent: List[RandomDungeonEncounterRewardEventInfoFormat] = []


class ReqPacket_PurchaseHealStoryMirrorDungeonCommand(BaseModel):
    idx: int = 0
    pid: int = 0


class ResPacket_PurchaseHealStoryMirrorDungeonCommand(BaseModel):
    cost: int = 0
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()


class ReqPacket_PurchaseFormationStoryMirrorDungeonCommand(BaseModel):
    formation: List[MirrorDungeonFormationFormat] = []


class ResPacket_PurchaseFormationStoryMirrorDungeonCommand(BaseModel):
    cost: int = 0
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    prevUnitInfo: MirrorDungeonPrevUnitInfoFormat = MirrorDungeonPrevUnitInfoFormat()


class ReqPacket_PurchaseUpgradePersonalityStoryMirrorDungeonCommand(BaseModel):
    idx: int = 0


class ResPacket_PurchaseUpgradePersonalityStoryMirrorDungeonCommand(BaseModel):
    cost: int = 0
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()


class ReqPacket_PurchaseEgoGiftStoryMirrorDungeonCommand(BaseModel):
    idx: int = 0


class ResPacket_PurchaseEgoGiftStoryMirrorDungeonCommand(BaseModel):
    cost: int = 0
    egogifts: List[DungeonMapEgoGiftFormat] = []
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_SellEgoGiftStoryMirrorDungeonCommand(BaseModel):
    id: int = 0


class ResPacket_SellEgoGiftStoryMirrorDungeonCommand(BaseModel):
    cost: int = 0
    egogifts: List[DungeonMapEgoGiftFormat] = []


class ReqPacket_AcquireStartEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    selectedSetId: int = 0
    selectedEgoGiftIds: List[int] = []


class ResPacket_AcquireStartEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    startEgoGiftPoolSets: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    startEgoGiftCreatedCount: int = 0


class ReqPacket_UpgradeEgoGiftStoryMirrorDungeonCommand(BaseModel):
    egoGiftId: int = 0


class ResPacket_UpgradeEgoGiftStoryMirrorDungeonCommand(BaseModel):
    cost: int = 0
    egoGift: DungeonMapEgoGiftFormat = DungeonMapEgoGiftFormat()
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_CombineEgoGiftStoryMirrorDungeonCommand(BaseModel):
    materialEgoGiftIds: List[int] = []
    keyword: str = ""


class ResPacket_CombineEgoGiftStoryMirrorDungeonCommand(BaseModel):
    resultEgoGift: DungeonMapEgoGiftFormat = DungeonMapEgoGiftFormat()
    isSuccess: bool = False
    egoGifts: List[DungeonMapEgoGiftFormat] = []
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqPacket_RefreshStartEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    pass


class ResPacket_RefreshStartEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    startEgoGiftPoolSets: List[MirrorDungeonEgoGiftPoolSetFormat] = []
    startEgoGiftCreatedCount: int = 0


class ReqPacket_RefreshShopEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    keyword: str = ""


class ResPacket_RefreshShopEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    cost: int = 0
    shopInfo: UserMirrorDungeonShopDataFormat = UserMirrorDungeonShopDataFormat()


class ReqPacket_RemoveStoryMirrorDungeonEgoGift(BaseModel):
    egogiftId: int = 0


class ResPacket_RemoveStoryMirrorDungeonEgoGift(BaseModel):
    egs: List[DungeonMapEgoGiftFormat] = []


class ReqPacket_EnterRailwayDungeon(BaseModel):
    dungeonId: int = 0
    personalities: List[RailwayUnitInfoFormat] = []


class ResPacket_EnterRailwayDungeon(BaseModel):
    saveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    startNodeData: RailwayNodeDataFormat = RailwayNodeDataFormat()


class ReqPacket_EnterRailwayDungeonMapNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    abnormalityids: List[int] = []
    participatedPIds: List[int] = []
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ResPacket_EnterRailwayDungeonMapNodeCommand(BaseModel):
    nodeid: int = 0
    deletedNodeIds: List[int] = []
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    prevStatusData: List[RailwayUnitStatusFormat] = []
    prevEgoStockData: List[RailwayEGOStockFormat] = []
    prevEnemyData: SaveDataForRailwayDungeon = SaveDataForRailwayDungeon()
    prevClearNodeId: int = 0
    currentNodeId: int = 0


class ReqPacket_GetRailwayDungeonNodeAndLogAllCommand(BaseModel):
    dungeonId: int = 0


class ResPacket_GetRailwayDungeonNodeAndLogAllCommand(BaseModel):
    nodeDatas: List[RailwayNodeDataFormat] = []
    logDatas: List[RailwayLogDataFormat] = []


class ReqPacket_ExitRailwayDungeonMapNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    unitStatusList: List[RailwayUnitStatusFormat] = []
    egoSkillStockList: List[RailwayEGOStockFormat] = []
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    statistics: List[RailwayStatisticsDataFormat] = []
    usedDanteAbilityCount: int = 0
    clearTurn: int = 0
    iswin: bool = False
    enemy: SaveDataForRailwayDungeon = SaveDataForRailwayDungeon()


class ResPacket_ExitRailwayDungeonMapNodeCommand(BaseModel):
    saveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    nodeData: RailwayNodeDataFormat = RailwayNodeDataFormat()
    updateNodeDatas: List[RailwayNodeDataFormat] = []


class ReqPacket_ExitRailwayDungeonRestNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    personalities: List[RailwayUnitInfoFormat] = []


class ResPacket_ExitRailwayDungeonRestNodeCommand(BaseModel):
    saveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    deletedNodeIds: List[int] = []
    nodeData: RailwayNodeDataFormat = RailwayNodeDataFormat()


class ReqPacket_ExitRailwayDungeonCommand(BaseModel):
    dungeonId: int = 0
    isClear: bool = False


class ResPacket_ExitRailwayDungeonCommand(BaseModel):
    isclear: bool = False
    saveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    currentLog: RailwayLogDataFormat = RailwayLogDataFormat()
    rewards: List[Element] = []


class ReqPacket_GiveUpRailwayDungeonNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ResPacket_GiveUpRailwayDungeonNodeCommand(BaseModel):
    saveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    nodeData: RailwayNodeDataFormat = RailwayNodeDataFormat()


class ReqPacket_GiveUpRailwayDungeonNodeInBattle(BaseModel):
    dungeonid: int = 0
    nodeid: int = 0
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ResPacket_GiveUpRailwayDungeonNodeInBattle(BaseModel):
    nodeData: RailwayNodeDataFormat = RailwayNodeDataFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqPacket_SelectRailwayDungeonBuffCommand(BaseModel):
    dungeonId: int = 0
    selectedBuffs: List[RailwayBuffSetRequestFormat] = []


class ResPacket_SelectRailwayDungeonBuffCommand(BaseModel):
    saveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    nodeData: RailwayNodeDataFormat = RailwayNodeDataFormat()


class ReqPacket_AcquireRailwayDungeonReward(BaseModel):
    dungeonId: int = 0


class ResPacket_AcquireRailwayDungeonReward(BaseModel):
    saveInfo: RailwayDungeonSaveInfoFormat = RailwayDungeonSaveInfoFormat()
    rewardList: List[Element] = []

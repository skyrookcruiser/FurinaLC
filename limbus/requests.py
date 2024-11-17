from pydantic import BaseModel
from typing import List, Generic, TypeVar, Optional
from limbus.formats import *

A = TypeVar("A")


class Cs(BaseModel, Generic[A]):
    userAuth: ServerUserAuth = ServerUserAuth()
    parameters: Optional[A] = None


class ReqNull(BaseModel):
    pass


class ReqAcquireHellsChickenReward(BaseModel):
    rewardId: int = 0


class ReqChangeCurrentAnnouncer(BaseModel):
    announcerIds: List[int] = []


class ReqAcquireAttendanceReward(BaseModel):
    partid: int = 0
    id: int = 0


class ReqBattleLog(BaseModel):
    type: str = ""
    uuid: str = ""
    platform: int = 0
    log: bytes = bytes()


class ReqBattlePassMissionReward(BaseModel):
    missionType: int = 0
    missionid: int = 0


class ReqBattlePassReward(BaseModel):
    level: int = 0


class ReqPurchaseBattlePassLevel(BaseModel):
    level: int = 0


class ReqUseCoupon(BaseModel):
    code: str = ""


class ReqEnterExpDungeon(BaseModel):
    dungeonid: int = 0


class ReqExitExpDungeon(BaseModel):
    formationId: int = 0
    isWin: int = 0
    supportCharacterId: int = 0
    supportParticipate: bool = False
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    usedDanteAbilityCount: int = 0


class ReqSkipExpDungeon(BaseModel):
    dungeonid: int = 0


class ReqEnterThreadDungeon(BaseModel):
    dungeonid: int = 0
    level: int = 0
    abnormalityids: List[int] = []


class ReqExitThreadDungeon(BaseModel):
    isWin: int = 0
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    usedDanteAbilityCount: int = 0


class ReqSkipThreadDungeon(BaseModel):
    dungeonid: int = 0
    dungeonlevel: int = 0


class ReqAcquireDailyLoginReward(BaseModel):
    weekid: int = 0
    id: int = 0


class ReqGetStageProgressRateRewardCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    rewardType: int = 0


class ReqEnterStageBattleCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0
    abnormalityids: List[int] = []


class ReqExitStageBattleCommand(BaseModel):
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


class ReqGetDungeonSaveInfoAll(BaseModel):
    railwayDungeonId: int = 0


class ReqEnterStoryDungeon(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0
    personalities: List[StoryDungeonSaveUnitInfoFormat] = []


class ReqReEnterStoryDungeonCommand(BaseModel):
    stageid: int = 0


class ReqExitStoryDungeonCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0


class ReqEnterStoryDungeonMapNodeCommand(BaseModel):
    floornumber: int = 0
    sectornumber: int = 0
    nodeid: int = 0
    abnormalityids: List[int] = []
    participatedPIds: List[int] = []


class ReqUpdateStoryDungeonMapNodeCommand(BaseModel):
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    dungeonUnitList: List[StoryDungeonSaveUnitInfoFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []


class ReqEnterStoryDungeonMapNodeBattleAfterChoice(BaseModel):
    dungeonUnitList: List[StoryDungeonSaveUnitInfoFormat] = []
    participatedPids: List[int] = []
    abnormalityids: List[int] = []


class ReqExitStoryDungeonMapNodeCommand(BaseModel):
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


class ReqUpdateStoryDungeonUnits(BaseModel):
    dungeonunitlist: List[StoryDungeonSaveUnitInfoFormat] = []


class ReqExitStoryCommand(BaseModel):
    mainchapterid: int = 0
    subchapterid: int = 0
    nodeid: int = 0
    stageid: int = 0


class ReqGetAbnormalityLogData(BaseModel):
    abnormalityIds: List[int] = []


class ReqUpdateAbnormalityLogData(BaseModel):
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqGetStoryDungeonNodeRecord(BaseModel):
    dungeonid: int = 0


class ReqClaimEventRewardCommand(BaseModel):
    eventId: int = 0
    eventRewardId: int = 0
    count: int = 0


class ReqClaimEventReward_ALLCommand(BaseModel):
    eventId: int = 0
    count: int = 0


class ReqPlayGacha(BaseModel):
    gachaId: int = 0
    paymentId: int = 0


class ReqUseGachaPityPoint(BaseModel):
    gachaId: int = 0
    targetIdx: int = 0


class ReqPurchase(BaseModel):
    productId: str = ""
    receipt: str = ""
    platform: int = 0


class ReqInitPurchase(BaseModel):
    productId: str = ""


class ReqInitPurchaseAsSteam(BaseModel):
    productId: str = ""
    steamId: str = ""
    language: str = ""
    productDesc: str = ""


class ReqFinalizePurchaseAsSteam(BaseModel):
    orderId: str = ""


class ReqGetSteamWalletCurrency(BaseModel):
    steamId: str = ""


class ReqPurchaseIngameProduct(BaseModel):
    igProductId: int = 0


class ReqUseItem(BaseModel):
    itemId: int = 0
    usage: int = 0
    targetIdx: int = 0
    target: Element = Element()


class ReqPurchaseEnkephalinModule(BaseModel):
    num: int = 0


class ReqPurchaseEnkephalin(BaseModel):
    num: int = 0


class ReqPersonalityGacksung(BaseModel):
    personalityId: int = 0


class ReqSetPersonalityGacksungIllust(BaseModel):
    personalityId: int = 0
    type: int = 0


class ReqEgoGacksung(BaseModel):
    egoId: int = 0


class ReqUsePersonalityExpItem(BaseModel):
    targetPersonalityId: int = 0
    items: List[ItemFormat] = []


class ReqUseEgoGacksungItem(BaseModel):
    targetEgoId: int = 0
    usingItem: ItemFormat = ItemFormat()


class ReqPersonalityGacksungWithItems(BaseModel):
    personalityId: int = 0
    usingPieces: List[ItemFormat] = []


class ReqEgoGacksungWithItems(BaseModel):
    egoId: int = 0
    usingPieces: List[ItemFormat] = []


# Parity


class ReqLoadUserDataAll(BaseModel):
    pass


class ReqLobbyCgCommand(BaseModel):
    lobbyCg: LobbyCgFormat = LobbyCgFormat()


class ReqSignInAsGuest(BaseModel):
    guestId: int = 0
    authToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ReqSignInAsNewGuest(BaseModel):
    deviceModel: str = ""


class ReqSignInAsGoogle(BaseModel):
    googleToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ReqLinkWithGoogle(BaseModel):
    googleToken: str = ""
    version: str = ""


class ReqSignInAsApple(BaseModel):
    appleToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ReqLinkWithApple(BaseModel):
    appleToken: str = ""
    version: str = ""


class ReqSignInAsSteam(BaseModel):
    steamToken: str = ""
    version: str = ""
    deviceModel: str = ""


class ReqRefreshLinkAuth(BaseModel):
    details: str = ""


class ReqGetInfoOfLinkWith(BaseModel):
    targetPublicId: str = ""
    password: str = ""


class ReqLinkWithAnother(BaseModel):
    targetPublicId: str = ""
    password: str = ""
    mainIsTarget: bool = False


class ReqUnLinkWithAnother(BaseModel):
    accountInfo: AccountInfoFormat = AccountInfoFormat()
    isUnlinkGoogle: bool = False
    isUnlinkApple: bool = False
    isUnlinkSteam: bool = False
    accountType: str = ""


class ReqUnsealMails(BaseModel):
    mailIds: List[int] = []


class ReqReportSpeedHack(BaseModel):
    detectedDate: str = ""
    scene: str = ""


class ReqReportModifiedHashCatalog(BaseModel):
    platform: str = ""
    hashvalue: str = ""


class ReqSaveMiniStoryWeek(BaseModel):
    weekId: int = 0


class ReqCompleteMinistory(BaseModel):
    storyId: str = ""


class ReqMirrorDungeonCommon(BaseModel):
    isOrigin: int = 0


class ReqEnterMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    dungeonid: int = 0
    idx: int = 0


class ReqReEnterMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    dungeonid: int = 0
    idx: int = 0


class ReqUpdateMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    characterInfos: List[MirrorDungeonGetCharacterInfoFormat] = []
    formation: List[MirrorDungeonFormationFormat] = []


class ReqSelectFormationAndCreateThemePoolMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    characterInfos: List[MirrorDungeonGetCharacterInfoFormat] = []
    formation: List[MirrorDungeonFormationFormat] = []


class ReqSelectThemeFloorMirrorDungeonCommand(BaseModel):
    selectedThemeFloorId: int = 0


class ReqAcquireMirrorDungeonLastReward(BaseModel):
    isOrigin: int = 0
    useEnkephalinModule: int = 0
    useHardBonus: int = 0
    useWeeklyBonus: int = 0


class ReqEnterMirrorDungeonMapNodeCommand(BaseModel):
    isOrigin: int = 0
    currentNode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    abnormalityIds: List[int] = []
    participatedPIds: List[int] = []


class ReqUpdateMirrorDungeonMapNodeCommand(BaseModel):
    isOrigin: int = 0
    currentNode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []


class ReqEnterMirrorDungeonMapNodeBattleAfterChoice(BaseModel):
    isOrigin: int = 0
    participatedPids: List[int] = []
    abnormalityIds: List[int] = []
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []


class ReqExitMirrorDungeonMapNodeCommand(BaseModel):
    isOrigin: int = 0
    currentNode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []
    nodeResult: int = 0
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    isUpdatedEgoSkillStock: int = 0
    egoSkillStockList: List[DungeonEgoSkillStockFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []
    statistics: List[DungeonStatisticsDataFormat] = []
    usedDanteAbilityCount: int = 0
    battleStatus: int = 0


class ReqUpdateMirrorDungeonUnits(BaseModel):
    isOrigin: int = 0
    dungeonUnitList: List[MirrorDungeonSaveUnitInfoFormat] = []


class ReqAcquireRewardEgoGiftsMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    selectIndexList: List[int] = []


class ReqAcquireRewardEgoGiftsWithEnemyBufMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    selectIndexList: List[int] = []


class ReqAcquireCharacterEventDataMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    acquirePersonalities: List[MirrorDungeonGetCharacterInfoFormat] = []


class ReqPersonalityLevelUpEventMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    levelUpPersonalityFormat: RandomDungeonLevelUpPersonalityInfoFormat = (
        RandomDungeonLevelUpPersonalityInfoFormat()
    )


class ReqAcquireMirrorDungeonBattleRewardCommand(BaseModel):
    isOrigin: int = 0
    selectIndexList: List[int] = []


class ReqUnLockMirrorDungeonEgoGiftCommand(BaseModel):
    egoGiftIds: List[int] = []


class ReqSendMirrorDungeonLogErrorCommand(BaseModel):
    type: int = 0


class ReqSendMirrorDungeonIndex(BaseModel):
    index: int = 0


class ReqSendMirrorDungeonId(BaseModel):
    id: int = 0


class ReqPurchaseHealMirrorDungeon(BaseModel):
    idx: int = 0
    pid: int = 0


class ReqPurchaseFormationMirrorDungeon(BaseModel):
    formation: List[MirrorDungeonFormationFormat] = []


class ReqPurchaseUpgradePersonalityMirrorDungeon(BaseModel):
    idx: int = 0


class ReqPurchaseEgoGiftMirrorDungeon(BaseModel):
    idx: int = 0


class ReqSellEgoGift(BaseModel):
    id: int = 0


class ReqRefreshShopEgoGiftsMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    isPaidWithChip: bool = False
    keyword: str = ""


class ReqGetStartBuffFInfoMirrorDungeon(BaseModel):
    dungeonid: int = 0


class ReqPurchaseStartBuffMirrorDungeon(BaseModel):
    dungeonid: int = 0
    buffids: List[int] = []


class ReqEnableSpecialStartBuffMirrorDungeon(BaseModel):
    dungeonid: int = 0
    buffids: List[int] = []


class ReqDisableStartBuffMirrorDungeon(BaseModel):
    dungeonid: int = 0
    buffids: List[int] = []


class ReqRemoveMirrorDungeonEgoGift(BaseModel):
    egogiftId: int = 0


class ReqGetMirrorDungeonPreset(BaseModel):
    dungeonid: int = 0
    idx: int = 0


# Parity


class ReqGetMirrorDungeonRewardChip(BaseModel):
    pass


class ReqSelectMirrorDungeonRandomPickFormation(BaseModel):
    dungeonid: int = 0
    idx: int = 0


class ReqAcquireStartEgoGiftsMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    selectedSetId: int = 0
    selectedEgoGiftIds: List[int] = []


class ReqRefreshStartEgoGiftsMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0


class ReqUpgradeEgoGiftMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    egoGiftId: int = 0


class ReqCombineEgoGiftMirrorDungeonCommand(BaseModel):
    isOrigin: int = 0
    materialEgoGiftIds: List[int] = []
    keyword: str = ""


class ReqAcquireMirrorDungeonExitReward(BaseModel):
    useEnkephalinModule: bool = False
    chanceConsumption: int = 0


class ReqAcquireMissionRewardsCommand(BaseModel):
    missionIds: List[int] = []


class ReqReportError(BaseModel):
    errorCode: str = ""
    url: str = ""
    requestJson: str = ""
    message: str = ""


class ReqGetTermsOfUseStateAll(BaseModel):
    uid: int = 0


class ReqUpdateTermsOfUseState(BaseModel):
    uid: int = 0
    termsVersion: int = 0
    state: int = 0


class ReqCompleteTheaterStory(BaseModel):
    storyId: str = ""


class ReqUpdateFormationCommand(BaseModel):
    formation: FormationFormat = FormationFormat()


class ReqFindFriend(BaseModel):
    publicUID: str = ""


class ReqSendFriendRequest(BaseModel):
    receiverPublicUID: str = ""


class ReqAcceptReceivedFriendRequest(BaseModel):
    senderPublicUID: str = ""


class ReqRejectReceivedFriendRequest(BaseModel):
    senderPublicUID: str = ""


class ReqCancelSentFriendRequest(BaseModel):
    receivedPublicUID: str = ""


class ReqDeleteFriend(BaseModel):
    deletedPublicUID: str = ""


class ReqGetFriendSupportPersonalities(BaseModel):
    publicUID: str = ""


class ReqGetFriendSupportPersonalitiesByCharacterId(BaseModel):
    characterid: int = 0


class ReqUpdateUserProfile(BaseModel):
    illustId: int = 0
    illustGacksungLevel: int = 0
    sentenceId: int = 0
    wordId: int = 0
    banners: List[UserPublicBannerFormat] = []
    supportPersonalities: List[SupportPersonalitySlotFormat] = []


class ReqUpdateProfileTicketDeco(BaseModel):
    leftBorderId: int = 0
    rightBorderId: int = 0
    egoBackgroundId: int = 0


class ReqPlayVendingMachine(BaseModel):
    vendingMachineId: int = 0
    targetType: str = ""
    targetId: int = 0
    coupons: List[int] = []
    isPaidByLunacy: bool = False


class ReqExchangeTwine(BaseModel):
    paidPieces: List[ItemFormat] = []


# Parity


class ReqStoryMirrorDungeonCommon(BaseModel):
    pass


class ReqAcquireEgoGiftEventStoryMirrorDungeonCommand(BaseModel):
    selectIndexList: List[int] = []


class ReqAcquireCharacterEventDataStoryMirrorDungeonCommand(BaseModel):
    acquirePersonalities: List[StoryMirrorDungeonGetCharacterInfoFormat] = []


class ReqPersonalityLevelUpEventStoryMirrorDungeonCommand(BaseModel):
    levelUpPersonalityFormat: StoryMirrorDungeonLevelUpPersonalityInfoFormat = (
        StoryMirrorDungeonLevelUpPersonalityInfoFormat()
    )


class ReqEnterStoryMirrorDungeonCommand(BaseModel):
    dungeonid: int = 0
    idx: int = 0


class ReqReEnterStoryMirrorDungeonCommand(BaseModel):
    dungeonid: int = 0


class ReqUpdateStoryMirrorDungeonCommand(BaseModel):
    formation: List[MirrorDungeonFormationFormat] = []


class ReqEnterStoryMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    abnormalityids: List[int] = []
    participatedPIds: List[int] = []


class ReqUpdateStoryMirrorDungeonMapNodeCommand(BaseModel):
    currentnode: DungeonMapNodeFormat = DungeonMapNodeFormat()
    choiceEventData: DungeonChoiceEventSaveDataFormat = (
        DungeonChoiceEventSaveDataFormat()
    )
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []
    updatedEgoGifts: List[DungeonMapEgoGiftFormat] = []


class ReqEnterStoryMirrorDungeonMapNodeBattleAfterChoiceCommand(BaseModel):
    participatedPids: List[int] = []
    abnormalityids: List[int] = []
    dungeonUnitList: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqExitStoryMirrorDungeonMapNodeCommand(BaseModel):
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


class ReqUpdateStoryMirrorDungeonUnitsCommand(BaseModel):
    dungeonunitlist: List[StoryMirrorDungeonSaveUnitInfoFormat] = []


class ReqAcquireRewardEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    selectIndexList: List[int] = []


class ReqPurchaseHealStoryMirrorDungeonCommand(BaseModel):
    idx: int = 0
    pid: int = 0


class ReqPurchaseFormationStoryMirrorDungeonCommand(BaseModel):
    formation: List[MirrorDungeonFormationFormat] = []


class ReqPurchaseUpgradePersonalityStoryMirrorDungeonCommand(BaseModel):
    idx: int = 0


class ReqPurchaseEgoGiftStoryMirrorDungeonCommand(BaseModel):
    idx: int = 0


class ReqSellEgoGiftStoryMirrorDungeonCommand(BaseModel):
    id: int = 0


class ReqAcquireStartEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    selectedSetId: int = 0
    selectedEgoGiftIds: List[int] = []


class ReqUpgradeEgoGiftStoryMirrorDungeonCommand(BaseModel):
    egoGiftId: int = 0


class ReqCombineEgoGiftStoryMirrorDungeonCommand(BaseModel):
    materialEgoGiftIds: List[int] = []
    keyword: str = ""


# Parity


class ReqRefreshStartEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    pass


class ReqRefreshShopEgoGiftsStoryMirrorDungeonCommand(BaseModel):
    keyword: str = ""


class ReqRemoveStoryMirrorDungeonEgoGift(BaseModel):
    egogiftId: int = 0


class ReqEnterRailwayDungeon(BaseModel):
    dungeonId: int = 0
    personalities: List[RailwayUnitInfoFormat] = []


class ReqEnterRailwayDungeonMapNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    abnormalityids: List[int] = []
    participatedPIds: List[int] = []
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqGetRailwayDungeonNodeAndLogAllCommand(BaseModel):
    dungeonId: int = 0


class ReqExitRailwayDungeonMapNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    unitStatusList: List[RailwayUnitStatusFormat] = []
    egoSkillStockList: List[RailwayEGOStockFormat] = []
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []
    statistics: List[RailwayStatisticsDataFormat] = []
    usedDanteAbilityCount: int = 0
    usedDanteAbilityId: int = 0
    clearTurn: int = 0
    iswin: bool = False
    enemy: SaveDataForRailwayDungeon = SaveDataForRailwayDungeon()


class ReqExitRailwayDungeonRestNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    personalities: List[RailwayUnitInfoFormat] = []


class ReqExitRailwayDungeonCommand(BaseModel):
    dungeonId: int = 0
    isClear: bool = False


class ReqGiveUpRailwayDungeonNodeCommand(BaseModel):
    dungeonId: int = 0
    nodeid: int = 0
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqGiveUpRailwayDungeonNodeInBattle(BaseModel):
    dungeonid: int = 0
    nodeid: int = 0
    battlePassParameters: BattlePassParameterFormat = BattlePassParameterFormat()
    abnormalityLogs: List[AbnormalityUnlockInformationFormat] = []


class ReqSelectRailwayDungeonBuffCommand(BaseModel):
    dungeonId: int = 0
    selectedBuffs: List[RailwayBuffSetRequestFormat] = []


class ReqAcquireRailwayDungeonReward(BaseModel):
    dungeonId: int = 0

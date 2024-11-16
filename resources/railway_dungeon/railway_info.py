from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from limbus.formats import MembershipFormat

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/railway-dungeon"


class BannerReward(BaseModel):
    type: str
    id: int
    num: int


class RailwayBannerRewardCondition(BaseModel):
    type: str
    count: int


class RailwayBannerReward(BaseModel):
    clearTurn: Optional[int] = None
    requiredConditions: List[RailwayBannerRewardCondition]
    endDate: Optional[str] = None
    reward: BannerReward
    localizeId: str


class RailwayNodeCollectionForLog(BaseModel):
    collectionId: int
    nodeIds: List[int]
    formationTargetNode: int


class RailwayOpenChapter(BaseModel):
    mainChapterId: int
    subChapterId: int
    nodeId: int
    unlockCode: int


class ExtraRewardCondition(BaseModel):
    type: str
    count: int


class ExtraRewardConfigUI(BaseModel):
    showStationNumber: Optional[int] = None
    isSpecialReward: Optional[bool] = None
    descLocalizeId: Optional[str] = None
    isHideAtNode: Optional[bool] = None


class ExtraReward(BaseModel):
    id: int
    requiredConditions: List[ExtraRewardCondition]
    rewards: List[BannerReward]
    uiConfig: Optional[ExtraRewardConfigUI] = None


class RelatedNode(BaseModel):
    spriteId: Optional[str] = None
    name: Optional[str] = None


class SectorNode(BaseModel):
    nodeId: int
    stageId: Optional[int] = None
    spriteId: Optional[str] = None
    nextNodes: List[int] = None
    clearRequiredNodesForEnter: List[int] = None
    UI_nextMoveTargetId: Optional[int] = None
    nodeType: Optional[str] = None
    nodeUIText: Optional[str] = None
    isBossNode: Optional[bool] = None
    relatedNodes: Optional[List[RelatedNode]] = None


class RailwayInfo(BaseModel):
    id: int
    requiredModule: int
    openChapterData: RailwayOpenChapter
    challengeType: str
    isSaveBattleState: bool
    isLoadSinFromSave: bool
    isNotAbleToAddSlot: bool
    isGiveUpNodeWhenAllDead: bool
    hasRestHeal: bool
    restHPHealRate: int
    restMPHeal: int
    isResetMPAtRestNode: bool
    isResetAfterLose: bool
    disableDanteAbilityIds: List[int]
    nodeIdCollection_ForLog: List[RailwayNodeCollectionForLog]
    startDate: str
    startDateForUI: str
    endDate: str
    endDateForUI: Optional[str] = None
    bannerRewards: List[RailwayBannerReward]
    extraRewards: Optional[List[ExtraReward]] = None
    sector: Optional[List[SectorNode]] = None


class RailwayInfoList(BaseModel):
    list: List[RailwayInfo]


def fetch_railway_info_list(
    railway_id: Optional[str] = None,
    season_part: Optional[str] = None,
    directory: str = FOLDER,
) -> Optional[RailwayInfoList]:
    folder_path = Path(directory)

    for file_path in folder_path.glob("**/*.json"):
        if railway_id and railway_id not in str(file_path):
            continue
        if season_part and season_part not in str(file_path):
            continue

        try:
            return RailwayInfoList.parse_file(file_path)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return None

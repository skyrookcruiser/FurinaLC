import re
from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from limbus.formats import BattlePassFormat, BattlePassMissionState, MISSION_STATE

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/battlepass"
SEASON = 5


class PassUiConfigData(BaseModel):
    bannerId: str
    newSubchapterId: Optional[int] = None


class PassPriceData(BaseModel):
    requiredItemId: int
    requiredItemNum: int
    requiredChanceId: int


class PassRewardInfoRewardData(BaseModel):
    type: str
    id: int
    num: int


class SpecialPassData(BaseModel):
    isIncludeLimbusPass: bool
    requiredChanceForLimbusPass: Optional[int] = None
    requiredChanceId: int
    requiredItemId: int
    requiredItemNum: int
    acquirements: List[PassRewardInfoRewardData]


class PassMissionData(BaseModel):
    missionType: str
    missionId: int
    missionCode: str
    countMax: int
    exp: int


class PassMissionsInfoData(BaseModel):
    missionList: List[PassMissionData]


class PassRewardsInfoRewardInfo(BaseModel):
    level: int
    defaultRewardList: List[PassRewardInfoRewardData]
    limbusRewardList: List[PassRewardInfoRewardData]


class PassRewardsInfoParitionsData(BaseModel):
    index: int
    partialStartDate: str
    partialMaxLevel: int


class PassRewardsInfoLevelPurchasePaymentData(BaseModel):
    requiredItemId: int
    requiredNum: int


class PassRewardsInfoData(BaseModel):
    maxLevel: int
    requiredExp: int
    levelPurchasePayment: PassRewardsInfoLevelPurchasePaymentData
    partitions: List[PassRewardsInfoParitionsData]
    rewardInfoList: List[PassRewardsInfoRewardInfo]
    exDefaultRewardList: List[PassRewardInfoRewardData]
    exLimbusRewardList: List[PassRewardInfoRewardData]


class PassSeasonInfoData(BaseModel):
    startDate: str
    startDateForUI: Optional[str] = None
    endDate: str
    banner: str
    acquireableEgoIds: Optional[List[int]] = None
    acquireableAnnouncerIds: Optional[List[int]] = None


class BattlepassData(BaseModel):
    id: int
    isCurrentForUI: bool
    currentPartitionForUI: Optional[int] = None
    isExRewardAcquireable: Optional[bool] = None
    limbusExRewardAcquireType: str
    exRewardStartDate: str
    passSeasonInfo: PassSeasonInfoData
    passRewardsInfo: PassRewardsInfoData
    passMissionsInfo: PassMissionsInfoData
    specialPassProduct_IncludeLimbusPass: Optional[SpecialPassData] = None
    specialPassProduct_NotIncludeLimbusPass: Optional[SpecialPassData] = None
    uiConfigs: Optional[PassUiConfigData] = None
    limbusPassPriceInfo: Optional[PassPriceData] = None


class BattlepassDataList(BaseModel):
    list: List[BattlepassData]


def create_battlepass_format(directory: str = FOLDER) -> BattlePassFormat:
    folder_path = Path(directory)
    try:
        for file_path in folder_path.glob("**/*.json"):
            season = file_path.stem.split("-")
            current_season = int(season[1])

            if current_season is not SEASON:
                continue

            battlepass_data_list = BattlepassDataList.parse_file(file_path)
            battlepass_data = battlepass_data_list.list[0]
            max_level = battlepass_data.passRewardsInfo.maxLevel
            # TODO: use intenum for rewardstate
            rewards_state = [2] * max_level

            missions_state = [
                BattlePassMissionState(
                    id=mission.missionId,
                    count=mission.countMax,
                    state=MISSION_STATE.OPENED,
                )
                for mission in battlepass_data.passMissionsInfo.missionList
            ]

            return BattlePassFormat(
                current_pass_id=current_season,
                is_limbus=True,
                level=5000,
                exp=0,
                today_rand_value=12,
                ex_reward_level=max_level,
                limbus_apply_level=5000,
                rewards_state=rewards_state,
                missions_state=missions_state,
                special_product_state=max_level + 1,
                ex_reward_limbus_level=max_level,
            )
    except Exception as e:
        print(f"Error creating BattlePassFormat: {e}")

        return None

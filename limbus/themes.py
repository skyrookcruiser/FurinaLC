from pydantic import BaseModel
from typing import List
from limbus.formats import *


class MirrorDungeonThemeFloorStaticDataList(BaseModel):
    list: List[MirrorDungeonThemeFloorStaticData] = []


class MirrorDungeonThemeFloorStaticData(BaseModel):
    id: int = 0
    unlockCondition: UnlockCondition = UnlockCondition()
    uiConfigs: MirrorDungeonThemeFloorUIConfigsStaticData = (
        MirrorDungeonThemeFloorUIConfigsStaticData()
    )
    exceptionConditions: List[MirrorDungeonThemeExceptionCondition] = []
    egoGiftPool: List[int] = []
    specificEgoGiftPool: List[int] = []
    mapGenSequence: List[MirrorDungeonMapGenSequenceOption] = []
    battlevictorycostvaluList: List[MirrorDungeonOriginBattleVictoryCostValue] = []


class UnlockCondition(BaseModel):
    mainChapterId: int = 0
    subChapterId: int = 0
    nodeId: int = 0
    unlockCode: int = 0
    possession: Element = Element()


class MirrorDungeonThemeExceptionCondition(BaseModel):
    dungeonIdx: int = 0
    selectableFloors: List[int] = []


class MirrorDungeonMapGenSequenceOption(BaseModel):
    type: str = ""
    numberList: List[int] = []


class StringKey_StringValue(BaseModel):
    key: str = ""
    value: str = ""


class MirrorDungeonThemeFloorUIConfigsStaticData(BaseModel):
    packSpriteId: str = ""
    bossSpriteId: str = ""
    showBossIds: List[int] = []
    attributeType: str = ""
    textColor: str = ""
    isHideLogo: bool = False
    isShowWarning: bool = False
    mapOptions: List[StringKey_StringValue] = []
    attributeTypeArrowCount: int = 0
    attackType: str = ""
    attackTypeArrowCount: int = 0


class MirrorDungeonOriginBattleVictoryCostValue(BaseModel):
    encounterType: STR_ENCOUNTER = STR_ENCOUNTER.HARD_BATTLE
    cost: int = 0

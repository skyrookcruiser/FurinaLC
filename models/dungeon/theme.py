from pydantic import BaseModel, Field
from typing import List, Optional, Any


class UnlockCondition(BaseModel):
    unlockCode: int = 0


class ExceptionCondition(BaseModel):
    dungeonIdx: int = 0
    selectableFloors: List[int] = []


class MapGenOption(BaseModel):
    bossPool: List[int] = []
    battlePool: List[int] = []
    abBattlePool: List[int] = []
    hardBattlePool: List[int] = []
    eventPool: List[int] = []


class NodeList(BaseModel):
    sector: int = 0
    idx: int = 0
    encounterType: int = 0
    encounterId: int = 0
    connectedNextNodeIdxList: List[int] = []


class MapGenSequence(BaseModel):
    type: str = Field(default="", alias="type_")
    numberList: List[int] = []
    nodeList: List[NodeList] = []
    numberValue: Optional[int] = None


class MapOption(BaseModel):
    key: str = ""
    value: Optional[str] = None


class UiConfigs(BaseModel):
    showBossIds: List[int] = []
    packSpriteId: str = ""
    mapOptions: List[MapOption] = []


class MirrorDungeonTheme(BaseModel):
    id: int = 0
    unlockCondition: UnlockCondition = UnlockCondition()
    desc: str = ""
    exceptionConditions: List[ExceptionCondition] = []
    mapGenOption: MapGenOption = MapGenOption()
    egoGiftPool: List[int] = []
    specificEgoGiftPool: List[Any] = []
    mapGenSequence: List[MapGenSequence] = []
    uiConfigs: UiConfigs = UiConfigs()


class MirrorDungeonThemeList(BaseModel):
    list: List[MirrorDungeonTheme] = []

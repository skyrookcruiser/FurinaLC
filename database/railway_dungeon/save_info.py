from pydantic import BaseModel
from database.client import db
from resources.railway_dungeon.railway_info import fetch_railway_info_list
from limbus.formats import (
    RailwayUnitInfoFormat,
    RailwayExtraRewardStateFormat,
    RailwayBuffSetFormat,
    SaveDataForRailwayDungeon,
)


class RailwayDungeonSaveInfoFormatWithUID(BaseModel):
    uid: int
    id: int
    prevclearnode: int
    currentnode: int
    lastclearnode: int
    personalities: List[RailwayUnitInfoFormat]
    payreward: int
    rewardstate: int
    extrarewardstate: List[RailwayExtraRewardStateFormat]
    firstcleardate: str = ""
    currentclearrotation: int
    lastenternodeid: int
    lastclearrotation: int
    buffsets: List[RailwayBuffSetFormat]
    initseed: int
    currentseed: int
    enemySaveData: SaveDataForRailwayDungeon

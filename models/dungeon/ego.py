from pydantic import BaseModel
from typing import List, Optional


class UpgradeData(BaseModel):
    upgradeLevel: int = 0
    localizeID: int = 0
    abilityIDList: List[int] = []


class Ego(BaseModel):
    id: int = 0
    attributeType: str = 0
    subEgoGiftAbilityIDList: List[int] = []
    tag: List[str] = []
    keyword: str = ""
    lockType: bool = False
    price: int = 0
    upgradeDataList: Optional[List[UpgradeData]] = None


class EgoList(BaseModel):
    list: List[Ego] = []

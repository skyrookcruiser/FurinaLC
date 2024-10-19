from pydantic import BaseModel, Field
from typing import List, Optional
from models.types import *


class ItemReward(BaseModel):
    type: str = Field(default="", alias="type_")
    rewardId: Optional[int] = None
    num: int = 0
    prob: float = 0.0


class ResultForm(BaseModel):
    resultEffectTarget: Optional[str] = None
    resultEffectTarget: str = ""
    nextBattleID: Optional[int] = 0
    itemReward: Optional[ItemReward] = None


class EventResultData(BaseModel):
    resultForm: ResultForm = ResultForm()


class Result(BaseModel):
    resultIndex: int = 0
    resultCondition: str = ""
    nextEventID: Optional[int] = 0
    eventResultDataList: Optional[
        List[EventResultData]
    ] = None


class EachOption(BaseModel):
    index: int = 0
    cantSelectInThisCase: str = ""
    resultList: List[Result] = []


class ActionEvent(BaseModel):
    eachOptionList: List[EachOption] = []

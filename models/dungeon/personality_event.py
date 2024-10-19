from pydantic import BaseModel, Field
from typing import List, Optional


class ParticipantInfo(BaseModel):
    min: int = 0
    max: int = 0


class AdderInfo(BaseModel):
    pass


class JudgementData(BaseModel):
    attributeType: str = ""


class Judgement(BaseModel):
    upDownType: int = 0
    inclusiveValue: int = 0
    exclusiveValue: int = 0
    judgementDataList: List[JudgementData] = []


class ItemReward(BaseModel):
    type: str = Field(default="", alias="type_")
    rewardId: Optional[int] = 0
    num: int = 0
    prob: float = 0.0


class ResultForm(BaseModel):
    resultEffect: str = ""
    itemReward: Optional[ItemReward] = None


class ResultFormWrapper(BaseModel):
    resultForm: ResultForm = ResultForm()


class EventResultData(BaseModel):
    resultIndex: int = 0
    resultCondition: str = ""
    nextEventID: int = 0
    eventResultDataList: Optional[
        List[ResultFormWrapper]
    ] = None


class EventResult(BaseModel):
    eventResult: str = ""
    eventResultDataList: List[EventResultData] = []


class PersonalityEvent(BaseModel):
    participantInfo: ParticipantInfo = ParticipantInfo()
    silenceCharacterUniqueIdList: List[int] = []
    adderInfo: List[AdderInfo] = []
    judgement: Judgement = Judgement()
    eventResults: List[EventResult] = []

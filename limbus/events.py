from enum import IntEnum
from pydantic import BaseModel
from typing import List
from limbus.formats import *


class CHOICE_EVENT_TYPE(IntEnum):
    NONE = 0
    EVENT = 1
    COIN_EVENT = 2
    UNRECOGNIZED = -1


class JudgementType(IntEnum):
    AND = 0
    OR = 1
    UNRECOGNIZED = -1


class CHOICE_EVENT_RESULT(IntEnum):
    SUCCESS = 0
    FAILURE = 1
    NONE = 2
    UNRECOGNIZED = -1


class STR_CHOICE_EVENT_TYPE(StrEnum):
    NONE = "NONE"
    EVENT = "EVENT"
    COIN_EVENT = "COIN_EVENT"
    UNRECOGNIZED = "UNRECOGNIZED"


class STR_JudgementType(StrEnum):
    AND = "AND"
    OR = "OR"
    UNRECOGNIZED = "UNRECOGNIZED"


class STR_CHOICE_EVENT_RESULT(StrEnum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    NONE = "NONE"
    UNRECOGNIZED = "UNRECOGNIZED"


class ChoiceEventStaticDataList(BaseModel):
    list: List[ChoiceEventStaticData] = []


class ChoiceEventStaticData(BaseModel):
    id: int = 0
    canSkip: bool = False
    personalityEvent: PersonalityChoiceEventData = PersonalityChoiceEventData()
    actionEvent: ActionChoiceEventData = ActionChoiceEventData()
    eventType: STR_CHOICE_EVENT_TYPE = STR_CHOICE_EVENT_TYPE.NONE
    _type: CHOICE_EVENT_TYPE = CHOICE_EVENT_TYPE.NONE


class PersonalityChoiceEventData(BaseModel):
    canDuplicateChoose: bool = False
    participantInfo: ParticipantsInfo = ParticipantsInfo()
    adderInfo: List[PersonalityEventAdder] = []
    judgement: PersonalityChoiceEventJudgementData = (
        PersonalityChoiceEventJudgementData()
    )
    eventResults: List[PersonalityEventResult] = []
    silenceCharacterUniqueIdList: List[int] = []
    notAllowedCharacterList: List[int] = []


class ParticipantsInfo(BaseModel):
    min: int = 0
    max: int = 0
    mustIncludeIdList: List[int] = []


class PersonalityEventAdder(BaseModel):
    correctionCase: str = ""
    adder: int = 0


class PersonalityChoiceEventJudgementData(BaseModel):
    inclusiveValue: int = 0
    exclusiveValue: int = 0
    upDownType: int = 0
    judgementType: STR_JudgementType = STR_JudgementType.AND
    _type: JudgementType = JudgementType.AND
    judgementDataList: List[OnePersonalityChoiceEventJudgementData] = []


class OnePersonalityChoiceEventJudgementData(BaseModel):
    attributeType: STR_ATTRIBUTE_TYPE = STR_ATTRIBUTE_TYPE.NONE
    _attribute_type: ATTRIBUTE_TYPE = ATTRIBUTE_TYPE.NONE
    minProb: int = 0


class PersonalityEventResult(BaseModel):
    eventResult: STR_CHOICE_EVENT_RESULT = STR_CHOICE_EVENT_RESULT.NONE
    _eventResult: CHOICE_EVENT_RESULT = CHOICE_EVENT_RESULT.NONE
    eventResultDataList: List[CommonChoiceEventResult] = []


class CommonChoiceEventResult(BaseModel):
    resultIndex: int = 0
    resultCondition: str = ""
    nextEventID: int = 0
    eventResultDataList: List[EventResultStaticData] = []


class EventResultStaticData(BaseModel):
    resultForm: EventResultForm = EventResultForm()


class EventResultForm(BaseModel):
    resultEffectCondition1: str = ""
    resultEffectCondition2: str = ""
    resultEffectTarget: str = ""
    resultEffect: str = ""
    resultDescId: str = ""
    itemReward: Reward = Reward()
    nextBattleID: int = 0


class Reward(BaseModel):
    type: STR_ELEMENT_TYPE = ELEMENT_TYPE.NONE
    _rewardType: ELEMENT_TYPE = ELEMENT_TYPE.NONE
    rewardId: int = 0
    num: int = 0
    prob: int = 0


class ActionChoiceEventData(BaseModel):
    eachOptionList: List[EachActionChoiceEventData] = []


class EachActionChoiceEventData(BaseModel):
    index: int = 0
    cantSelectInThisCase: str = ""
    resultList: List[CommonChoiceEventResult] = []


class EGOGiftStaticDataList(BaseModel):
    list: List[EGOGiftStaticData] = []


class EGOGiftStaticData(BaseModel):
    id: int = 0
    iconId: int = 0
    egoGrade: int = 0
    useLimit: int = 0
    destroyConditionEventID: List[int] = []
    subEgoGiftAbilityIDList: List[int] = []
    attributeType: STR_ATTRIBUTE_TYPE = STR_ATTRIBUTE_TYPE.NONE
    _attributeType: ATTRIBUTE_TYPE = ATTRIBUTE_TYPE.NONE
    type: str = ""
    upgradeDataList: List[EGOGiftUpgradeStaticData] = []
    tag: List[STR_MIRRORDUNGEON_EGOGIFT_TAG] = []
    _tag: List[MIRRORDUNGEON_EGOGIFT_TAG] = []
    price: int = 0
    lockType: bool = False
    isShowAtStart: bool = False
    keyword: STR_MIRRORDUNGEON_EGOGIFT_KEYWORD = STR_MIRRORDUNGEON_EGOGIFT_KEYWORD.NONE
    _keyword: MIRRORDUNGEON_EGOGIFT_KEYWORD = MIRRORDUNGEON_EGOGIFT_KEYWORD.NONE


class EGOGiftUpgradeStaticData(BaseModel):
    upgradeLevel: int = 0
    localizeID: int = 0
    abilityIDList: List[int] = []

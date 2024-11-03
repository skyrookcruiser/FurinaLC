from pydantic import BaseModel
from typing import List, Optional
import os

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/personality"


class AttributeData(BaseModel):
    skillId: int
    number: int


class AtkResistData(BaseModel):
    # SLASH, PENETRATE, HIT
    type: str
    value: float


class PersonalityResistInfoData(BaseModel):
    atkResistList: List[AtkResistData]


class PersonalityBreakSectionData(BaseModel):
    sectionList: List[int]


class PersonalityMentalConditionID(BaseModel):
    conditionID: str


class PersonalityMentalConditionData(BaseModel):
    level: int
    conditionIDList: List[PersonalityMentalConditionID]


class PersonalityMentalConditionInfoData(BaseModel):
    add: List[PersonalityMentalConditionData]
    min: List[PersonalityMentalConditionData]


class PersonalityHpData(BaseModel):
    defaultStat: int
    incrementByLevel: float


class PersonalityData(BaseModel):
    id: int
    appearance: str
    # check UNIT_KEYWORD in limbus.formats
    unitKeywordList: List[str]
    associationList: List[str]
    characterId: int
    panicType: int
    season: Optional[int] = None
    defenseSkillIDList: List[int]
    panicSkillOnErosion: int
    slotWeightConditionList: List[str]
    rank: int
    hp: PersonalityHpData
    defCorrection: int
    minSpeedList: List[int]
    maxSpeedList: List[int]
    # check ATTRIBUTE_TYPE in limbus.formats
    uniqueAttribute: str
    mentalConditionInfo: PersonalityMentalConditionInfoData
    breakSection: PersonalityBreakSectionData
    resistInfo: PersonalityResistInfoData
    attributeList: List[AttributeData]


class PersonalityDataList(BaseModel):
    list: List[PersonalityData]


def fetch_personality_ids(directory: str = FOLDER) -> List[int]:
    ids = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                try:
                    personality_data_list = PersonalityDataList.parse_file(file_path)
                    ids.extend(
                        personality.id for personality in personality_data_list.list
                    )
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
    return ids

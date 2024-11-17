from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from utils import get_date_time
from limbus.formats import PersonalityFormat

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
    folder_path = Path(directory)
    for file_path in folder_path.glob("**/*.json"):
        try:
            personality_data_list = PersonalityDataList.parse_file(file_path)
            ids.extend(personality.id for personality in personality_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return ids


def get_order_id(personality_id: int) -> int:
    match str(personality_id)[:3]:
        case "101":
            return 1
        case "102":
            return 2
        case "103":
            return 3
        case "104":
            return 4
        case "105":
            return 5
        case "106":
            return 6
        case "107":
            return 7
        case "108":
            return 8
        case "109":
            return 9
        case "110":
            return 10
        case "111":
            return 11
        case "112":
            return 12
        case _:
            return 0


def create_personality_format_list(directory: str = FOLDER) -> List[PersonalityFormat]:
    personality_ids = fetch_personality_ids(directory)
    personality_format_list = [
        PersonalityFormat(
            personality_id=personality_id,
            level=50,
            exp=0,
            gacksung=4,
            order_id=get_order_id(personality_id),
            gacksung_illust_type=1,
            acquire_time=get_date_time(),
        )
        for personality_id in personality_ids
    ]

    return personality_format_list

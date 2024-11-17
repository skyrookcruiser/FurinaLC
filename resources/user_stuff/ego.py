from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from utils import get_date_time
from limbus.formats import EgoFormat

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/ego"


class EgoCorrosionChanceData(BaseModel):
    section: float
    probability: float


class EgoRequirementData(BaseModel):
    # check ATTRIBUTE_TYPE in limbus.formats
    attributeType: str
    num: int


class EgoAttributeResistData(BaseModel):
    # check ATTRIBUTE_TYPE in limbus.formats
    type: str
    value: float


class EgoData(BaseModel):
    id: int
    characterId: int
    # check EGO_TYPE in limbus.formats
    egoType: str
    egoClass: Optional[int] = None
    season: int
    skillTier: Optional[int] = None
    attributeResistList: List[EgoAttributeResistData]
    requirementList: List[EgoRequirementData]
    corrosionSectionList: List[EgoCorrosionChanceData]
    passiveList: Optional[List[None]] = None
    awakeningSkillId: int
    corrosionSkillId: Optional[int] = None


class EgoDataList(BaseModel):
    list: List[EgoData]


def fetch_ego_ids(directory: str = FOLDER) -> List[int]:
    ids = []
    folder_path = Path(directory)
    for file_path in folder_path.glob("**/*.json"):
        try:
            ego_data_list = EgoDataList.parse_file(file_path)
            ids.extend(ego.id for ego in ego_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return ids


def create_ego_format_list(directory: str = FOLDER) -> List[EgoFormat]:
    ego_ids = fetch_ego_ids(directory)
    ego_format_list = [
        EgoFormat(ego_id=ego_id, gacksung=4, acquire_time=get_date_time())
        for ego_id in ego_ids
    ]

    return ego_format_list

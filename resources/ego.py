from pydantic import BaseModel
from typing import List, Optional
import os

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
    # passiveList: Optional[List[]]
    awakeningSkillId: int
    corrosionSkillId: Optional[int] = None


class EgoDataList(BaseModel):
    list: List[EgoData]


def fetch_ego_ids(directory: str = FOLDER) -> List[int]:
    ids = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                try:
                    ego_data_list = EgoDataList.parse_file(file_path)
                    ids.extend(ego.id for ego in ego_data_list.list)
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
    return ids

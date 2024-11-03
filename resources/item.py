from pydantic import BaseModel
from typing import List, Optional
import os

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/item"


class ItemFunctionData(BaseModel):
    # check ITEM_USE_FUNC_TYPE in limbus.formats
    itemUseFuncType: str
    itemUseFuncValue: Optional[int] = None
    # ALEPH, etc.
    itemUseFuncString: Optional[str] = None


class ItemUiConfigData(BaseModel):
    # Season1_BattlePass, etc.
    tags: List[str]


class ItemContentData(BaseModel):
    # check ELEMENT_TYPE in limbus.formats
    type: str
    id: int
    num: Optional[int] = None
    minNum: Optional[int] = None
    maxNum: Optional[int] = None


class ItemSeasonTargetElementData(BaseModel):
    # check ELEMENT_TYPE in limbus.formats
    type: str
    id: int


class ItemData(BaseModel):
    id: int
    ignoreExcess: Optional[bool] = None
    # check ITEM_CONTENTS_OPEN_TYPE in limbus.formats
    season: Optional[int] = None
    seasonalTargetElement: Optional[ItemSeasonTargetElementData] = None
    contentsOpenType: Optional[str] = None
    contents: Optional[List[ItemContentData]] = None
    category: Optional[str] = None
    # check ITEM_USE_TYPE in limbus.formats
    itemUseType: Optional[str] = None
    spriteStr: Optional[str] = None
    optionalSample: Optional[ItemContentData] = None
    itemUseFuncs: Optional[List[ItemFunctionData]] = None
    uiConfig: Optional[ItemUiConfigData] = None


class ItemDataList(BaseModel):
    list: List[ItemData]


def fetch_item_ids(directory: str = FOLDER) -> List[int]:
    ids = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                try:
                    item_data_list = ItemDataList.parse_file(file_path)
                    ids.extend(item.id for item in item_data_list.list)
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
    return ids

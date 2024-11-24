from pydantic import BaseModel
from typing import List, Optional
from limbus.formats import Element
from pathlib import Path

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/gacha"


class GachaElement(BaseModel):
    type: str
    id: int
    num: int


class GachaPityCatalog(BaseModel):
    element: GachaElement
    requiredPityPoint: int


class GachaPitySystem(BaseModel):
    endDate: Optional[str] = None
    catalog: Optional[List[GachaPityCatalog]] = None


class GachaOccupancyCase(BaseModel):
    occupancyCase: str
    occupancy: int


class GachaContent(BaseModel):
    groupType: str
    occupancyCaseList: List[GachaOccupancyCase]
    elementType: str
    elementIdList: List[int]


class GachaPayment(BaseModel):
    paymentId: int
    gachaUIState: str
    requiredItemId: int
    requiredNum: int
    requiredChanceId: Optional[int] = None
    count: int


class GachaBannerInfo(BaseModel):
    endDate: Optional[str] = None
    bannerType: str
    priority: int
    pickupIdList: List[int]
    illustList: List[str]
    videoList: List[int]


class GachaData(BaseModel):
    id: int
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    bannerInfo: GachaBannerInfo
    payments: List[GachaPayment]
    contents: List[GachaContent]
    pitySystem: Optional[GachaPitySystem] = None


class GachaDataList(BaseModel):
    list: List[GachaData]


def fetch_gacha_data_list(folder: str = FOLDER) -> GachaDataList:
    folder_path = Path(folder)
    combined_gacha_data = GachaDataList(list=[])

    for file_path in folder_path.glob("**/*.json"):
        try:
            gacha_data_list = GachaDataList.parse_file(file_path)
            combined_gacha_data.list.extend(gacha_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

            return combined_gacha_data

    return combined_gacha_data

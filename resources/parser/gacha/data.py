from pydantic import BaseModel
from typing import List, Optional
from limbus.formats import Element
from pathlib import Path
from enum import StrEnum
import random

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


def fetch_gacha_data_list_by_id(id: int, folder: str = FOLDER) -> GachaDataList:
    folder_path = Path(folder)
    for file_path in folder_path.glob("**/*.json"):
        try:
            file_name = file_path.stem
            path_parts = file_name.split("-")

            if len(path_parts) < 2:
                continue
            if id == int(path_parts[1]):
                gacha_data_list = GachaDataList.parse_file(file_path)

                return gacha_data_list

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return GachaDataList(list=[])


class GACHA_GROUPS(StrEnum):
    BASE_FEATURED = "1_pickup"
    BASE_IDS = "1"
    TWO_STAR = "2"
    THREE_STAR = "3"
    THREE_STAR_FEATURED = "3_pickup"
    TWO_STAR_FEATURED = "2_pickup"
    EGO = "EGO"
    EGO_FEATURED = "EGO_pickup"
    ANNOUNCER = "ANNOUNCER"
    ANNOUNCER_FEATURED = "ANNOUNCER_pickup"


# I'm not gonna lie, I kinda forgot we have announcers
# I'm not gonna bother implementing this properly
# I have never done any gacha on official server at all
# I am fr eyeballing the rng system
def fetch_random_gacha_element_ids(
    id: int,
    payment_id: int,
    element_type: str = "PERSONALITY",
    folder: str = FOLDER,
) -> List[int]:
    gacha_data_list = fetch_gacha_data_list_by_id(id)

    if not gacha_data_list.list:
        print(f"WARN:     No gacha data found for ID {id}.")
        return []

    # Default chance distribution for each group
    chance_distribution = {
        GACHA_GROUPS.BASE_FEATURED: 0.1,  # 10% chance
        GACHA_GROUPS.BASE_IDS: 0.8,  # 80% chance
        GACHA_GROUPS.TWO_STAR: 0.075,  # 7.5% chance
        GACHA_GROUPS.THREE_STAR: 0.025,  # 2.5% chance
        GACHA_GROUPS.THREE_STAR_FEATURED: 0.0,  # 0% chance initially
        GACHA_GROUPS.TWO_STAR_FEATURED: 0.0,  # 0% chance initially
        GACHA_GROUPS.EGO: 0,  # 0% chance
        GACHA_GROUPS.EGO_FEATURED: 0,  # 0% chance
        GACHA_GROUPS.ANNOUNCER: 0,  # 0% chance
        GACHA_GROUPS.ANNOUNCER_FEATURED: 0,  # 0% chance
    }

    # Check groups in the gacha data to adjust chances
    featured_group_adjusted = False
    for gacha_data in gacha_data_list.list:
        group_types = [
            content.groupType
            for content in gacha_data.contents
            if content.elementType == element_type
        ]

        if (
            GACHA_GROUPS.THREE_STAR_FEATURED in group_types
            and not featured_group_adjusted
        ):
            chance_distribution[GACHA_GROUPS.THREE_STAR_FEATURED] = 0.05
            chance_distribution[GACHA_GROUPS.BASE_IDS] -= 0.05
            featured_group_adjusted = True
        elif (
            GACHA_GROUPS.TWO_STAR_FEATURED in group_types
            and not featured_group_adjusted
        ):
            chance_distribution[GACHA_GROUPS.TWO_STAR_FEATURED] = 0.15
            chance_distribution[GACHA_GROUPS.BASE_IDS] -= 0.15
            featured_group_adjusted = True

    # Find the count of items to pull
    num_items_to_pull = 0
    for gacha_data in gacha_data_list.list:
        gacha_payment = next(
            (
                payment
                for payment in gacha_data.payments
                if payment.paymentId == payment_id
            ),
            None,
        )
        if gacha_payment:
            num_items_to_pull = gacha_payment.count
            break

    if num_items_to_pull == 0:
        print(f"WARN:     Payment ID {payment_id} not found in the Gacha data.")
        return []

    # Aggregate available IDs by group
    available_ids_by_group = {group: [] for group in chance_distribution.keys()}
    for gacha_data in gacha_data_list.list:
        for content in gacha_data.contents:
            if content.elementType == element_type:
                group = GACHA_GROUPS(content.groupType)
                if group in available_ids_by_group:
                    available_ids_by_group[group].extend(content.elementIdList)

    # Distribute pulls based on the chance distribution
    pulled_ids = []
    remaining_pulls = num_items_to_pull

    for group, chance in chance_distribution.items():
        if chance > 0 and available_ids_by_group[group]:
            group_pull_count = round(num_items_to_pull * chance)
            group_pull_count = min(group_pull_count, len(available_ids_by_group[group]))
            group_pulls = random.sample(available_ids_by_group[group], group_pull_count)
            pulled_ids.extend(group_pulls)
            remaining_pulls -= len(group_pulls)

    # Handle leftover pulls (if rounding caused some discrepancy)
    if remaining_pulls > 0:
        leftover_ids = [
            id
            for group_ids in available_ids_by_group.values()
            for id in group_ids
            if id not in pulled_ids
        ]
        if leftover_ids:
            pulled_ids.extend(
                random.sample(leftover_ids, min(remaining_pulls, len(leftover_ids)))
            )

    # Ensure we don't exceed the number of pulls
    pulled_ids = random.sample(pulled_ids, min(num_items_to_pull, len(pulled_ids)))

    return pulled_ids

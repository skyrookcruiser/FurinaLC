from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from limbus.formats import UserProfileBorderFormat, UserProfileEgobackgroundFormat
from utils import get_date_time

FOLDER_R = "./resources/LimbusStaticData/StaticData/static-data/userticket-r"
FOLDER_L = "./resources/LimbusStaticData/StaticData/static-data/userticket-l"
FOLDER_EGO = "./resources/LimbusStaticData/StaticData/static-data/userticket-egobg"


class UserTicketData(BaseModel):
    id: int
    useEffect: Optional[bool] = None
    color: Optional[str] = None


class UserTicketDataList(BaseModel):
    list: List[UserTicketData]


def fetch_unique_ids_from_directory(directory: str) -> List[int]:
    ids = set()
    folder_path = Path(directory)

    for file_path in folder_path.glob("**/*.json"):
        try:
            data_list = UserTicketDataList.parse_file(file_path)
            ids.update(ticket.id for ticket in data_list.list if ticket.id > 7)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return list(ids)


def create_border_right_format_list(
    directory: str = FOLDER_R,
) -> List[UserProfileBorderFormat]:
    border_ids = fetch_unique_ids_from_directory(directory)

    return [
        UserProfileBorderFormat(
            id=border_id,
            date=get_date_time(),
        )
        for border_id in border_ids
    ]


def create_border_left_format_list(
    directory: str = FOLDER_L,
) -> List[UserProfileBorderFormat]:
    border_ids = fetch_unique_ids_from_directory(directory)

    return [
        UserProfileBorderFormat(
            id=border_id,
            date=get_date_time(),
        )
        for border_id in border_ids
    ]


def create_egobg_format_list(
    directory: str = FOLDER_EGO,
) -> List[UserProfileEgobackgroundFormat]:
    egobg_ids = fetch_unique_ids_from_directory(directory)

    return [
        UserProfileEgobackgroundFormat(
            id=egobg_id,
            date=get_date_time(),
        )
        for egobg_id in egobg_ids
    ]

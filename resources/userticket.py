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


def fetch_user_ticket_r_ids(directory: str = FOLDER_R) -> List[int]:
    ids = []
    folder_path = Path(directory)
    for file_path in folder_path.glob("**/*.json"):
        try:
            ticket_r_data_list = UserTicketDataList.parse_file(file_path)
            ids.extend(ticket.id for ticket in ticket_r_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    return ids


def create_border_right_format_list(
    directory: str = FOLDER_R,
) -> List[UserProfileBorderFormat]:
    border_ids = fetch_user_ticket_r_ids()

    return [
        UserProfileBorderFormat(
            id=border_id,
            date=get_date_time(),
        )
        for border_id in border_ids
    ]


def fetch_user_ticket_l_ids(directory: str = FOLDER_L) -> List[int]:
    ids = []
    folder_path = Path(directory)
    for file_path in folder_path.glob("**/*.json"):
        try:
            ticket_r_data_list = UserTicketDataList.parse_file(file_path)
            ids.extend(ticket.id for ticket in ticket_r_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    return ids


def create_border_left_format_list(
    directory: str = FOLDER_L,
) -> List[UserProfileBorderFormat]:
    border_ids = fetch_user_ticket_l_ids(directory)

    return [
        UserProfileBorderFormat(
            id=border_id,
            date=get_date_time(),
        )
        for border_id in border_ids
    ]


def fetch_user_ticket_egobgs_ids(directory: str = FOLDER_EGO) -> List[int]:
    ids = []
    folder_path = Path(directory)
    for file_path in folder_path.glob("**/*.json"):
        try:
            ticket_r_data_list = UserTicketDataList.parse_file(file_path)
            ids.extend(ticket.id for ticket in ticket_r_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    return ids


def create_egobg_format_list(
    directory: str = FOLDER_EGO,
) -> List[UserProfileEgobackgroundFormat]:
    egobg_ids = fetch_user_ticket_egobgs_ids(directory)

    return [
        UserProfileEgobackgroundFormat(
            id=egobg_id,
            date=get_date_time(),
        )
        for egobg_id in egobg_ids
    ]

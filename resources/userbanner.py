from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from limbus.formats import UserBannerDataFormat
from utils import get_date_time

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/userbanner"


class ValueText(BaseModel):
    prefix: str


class StaticUserBannerData(BaseModel):
    id: int
    value1Text: Optional[ValueText] = None
    value2Text: Optional[ValueText] = None
    value1Max: Optional[int] = None
    value2Max: Optional[int] = None
    effectId: Optional[int] = None


class StaticUserBannerDataList(BaseModel):
    list: List[StaticUserBannerData]


def fetch_user_banner_ids(directory: str = FOLDER) -> List[int]:
    ids = set()
    folder_path = Path(directory)

    for file_path in folder_path.glob("**/*.json"):
        try:
            user_banner_data_list = StaticUserBannerDataList.parse_file(file_path)
            ids.update(banner.id for banner in user_banner_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return list(ids)


def create_user_banner_data_format_list(
    directory: str = FOLDER,
) -> List[UserBannerDataFormat]:
    banner_ids = fetch_user_banner_ids(directory)
    banner_data_format_list = []

    for banner_id in banner_ids:
        # hardcoding this because
        # im not gonna bother checking
        # localize resource and
        # get the highest tier lol
        match banner_id:
            # railway 1
            case 5 | 6 | 7:
                banner_data_format_list.append(
                    UserBannerDataFormat(
                        id=banner_id,
                        acquiretime=get_date_time(),
                        value=52,
                        value2=-1,
                    )
                )
            # railway 2
            case 13 | 14 | 15 | 16 | 17 | 18 | 19:
                banner_data_format_list.append(
                    UserBannerDataFormat(
                        id=banner_id,
                        acquiretime=get_date_time(),
                        value=70,
                        value2=5,
                    )
                )
            # railway 3
            case 26 | 27:
                banner_data_format_list.append(
                    UserBannerDataFormat(
                        id=banner_id,
                        acquiretime=get_date_time(),
                        value=31,
                        value2=-1,
                    )
                )
            # railway 4
            case 39 | 40:
                banner_data_format_list.append(
                    UserBannerDataFormat(
                        id=banner_id,
                        acquiretime=get_date_time(),
                        value=29,
                        value2=-1,
                    )
                )
            # everything else
            case _:
                banner_data_format_list.append(
                    UserBannerDataFormat(
                        id=banner_id,
                        acquiretime=get_date_time(),
                        value=-1,
                        value2=-1,
                    )
                )

    return banner_data_format_list

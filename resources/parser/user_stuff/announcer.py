from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from limbus.formats import AnnouncerFormat

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/announcer"


class AnnouncerKeyword(BaseModel):
    voicetype: str
    path: str
    priority: int
    index: int


class AnnouncerData(BaseModel):
    id: int
    imgStr: str
    walpurgisType: Optional[str] = None
    announcerKeywords: List[AnnouncerKeyword]


class AnnouncerDataList(BaseModel):
    list: List[AnnouncerData]


def create_announcer_format(directory: str = FOLDER) -> AnnouncerFormat:
    folder_path = Path(directory)
    announcer_ids = []

    for file_path in folder_path.glob("**/*.json"):
        try:
            announcer_data_list = AnnouncerDataList.parse_file(file_path)
            announcer_ids.extend(announcer.id for announcer in announcer_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    cur_announcer_ids = announcer_ids[:10]

    return AnnouncerFormat(
        announcer_ids=announcer_ids, cur_announcer_ids=cur_announcer_ids
    )

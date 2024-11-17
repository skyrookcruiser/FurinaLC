from pydantic import BaseModel
from typing import List
from limbus.formats import UnlockCodeFormat
from pathlib import Path

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/unlockcode/"


class UnlockCodeSubChapterData(BaseModel):
    id: int
    unlockcodeType: str
    desc: str


class UnlockCodeSubChapterDataList(BaseModel):
    list: List[UnlockCodeSubChapterData]


def fetch_unlockcode_ids(directory: str = FOLDER) -> List[int]:
    ids = set()
    folder_path = Path(directory)

    for file_path in folder_path.glob("**/*.json"):
        try:
            if "event" in str(file_path):
                continue
            unlock_code_data_list = UnlockCodeSubChapterDataList.parse_file(file_path)
            ids.update(code.id for code in unlock_code_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return list(ids)


def create_unlock_code_format_list(directory: str = FOLDER) -> List[UnlockCodeFormat]:
    unlockcode_ids = fetch_unlockcode_ids(directory)

    return [
        UnlockCodeFormat(unlockcode=unlockcode_id)
        for unlockcode_id in unlockcode_ids
        if unlockcode_id != 107
    ]

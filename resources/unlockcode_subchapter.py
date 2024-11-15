from pydantic import BaseModel
from typing import List
from limbus.formats import UnlockCodeFormat

FILE = "./resources/LimbusStaticData/StaticData/static-data/unlockcode/unlockcode-subchapter/unlockcode-subchapter.json"


class UnlockCodeSubChapterData(BaseModel):
    id: int
    unlockcodeType: str
    desc: str


class UnlockCodeSubChapterDataList(BaseModel):
    list: List[UnlockCodeSubChapterData]


def fetch_unlockcode_ids(directory: str = FILE) -> List[int]:
    data = UnlockCodeSubChapterDataList.parse_file(FILE)

    return [code.id for code in data.list]


def create_unlock_code_format_list(directory: str = FILE) -> List[UnlockCodeFormat]:
    unlockcode_ids = fetch_unlockcode_ids(directory)

    return [
        UnlockCodeFormat(unlockcode=unlockcode_id) for unlockcode_id in unlockcode_ids
    ]

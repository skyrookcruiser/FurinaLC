from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from limbus.formats import ChanceFormat

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/chance"


class ChanceData(BaseModel):
    id: int
    max: int
    resetTimeType: str


class ChanceDataList(BaseModel):
    list: List[ChanceData]


def create_chance_format_list(directory: str = FOLDER) -> List[ChanceFormat]:
    chance_formats = []
    folder_path = Path(directory)

    for file_path in folder_path.glob("**/*.json"):
        try:
            chance_data_list = ChanceDataList.parse_file(file_path)
            for chance in chance_data_list.list:
                chance_format = ChanceFormat(id=chance.id, value=chance.max)
                chance_formats.append(chance_format)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return chance_formats

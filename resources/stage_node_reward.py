from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from resources.unlockcode_subchapter import fetch_unlockcode_ids
from limbus.formats import (
    MainChapterStateFormat,
    SubChapterStateFormat,
    NodeStateFormat,
)

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/stagenodereward"


class StageNodeClearRewardData(BaseModel):
    # Check ELEMENT_TYPE in limbus.formats
    type: str
    id: int
    num: Optional[int] = None


class StageNodeRewardData(BaseModel):
    nodeid: int
    acquireExp: int
    acquireTotalExpForPersonality: int
    normalClearRewards: Optional[List[StageNodeClearRewardData]] = None
    exClearRewards: List[StageNodeClearRewardData]
    exclearConditionTurnCount: Optional[int] = None


class StageNodeRewardList(BaseModel):
    list: List[StageNodeRewardData]


def fetch_node_ids(directory: str = FOLDER) -> List[int]:
    ids = []
    folder_path = Path(directory)
    for file_path in folder_path.glob("**/*.json"):
        try:
            stage_node_data_list = StageNodeRewardList.parse_file(file_path)
            ids.extend(stage_node.nodeid for stage_node in stage_node_data_list.list)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    return ids


def create_main_chapter_state_list() -> List[MainChapterStateFormat]:
    main_chapter_state_ids = [1, 91]

    main_chapter_states = []
    for id in main_chapter_state_ids:
        sub_chapters = []

        for code in fetch_unlockcode_ids():
            if code // 100 == id:
                node_states = [
                    NodeStateFormat(
                        id=code * 100 + sub_id,
                        ct=2,
                        cn=1,
                        dn=0,
                    )
                    for sub_id in range(1, 100)
                ]
                sub_chapter = SubChapterStateFormat(
                    id=code,
                    nss=node_states,
                    rss=[1, 2, 3, 10],
                )
                sub_chapters.append(sub_chapter)

        main_chapter_state = MainChapterStateFormat(id=id, subcss=sub_chapters)
        main_chapter_states.append(main_chapter_state)

    return main_chapter_states

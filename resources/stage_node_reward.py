from pydantic import BaseModel
from typing import List, Optional
from limbus.formats import (
    MainChapterStateFormat,
    SubChapterStateFormat,
    NodeStateFormat,
)
import os

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/stagenodereward"


class StageNodeClearRewardData(BaseModel):
    # check ELEMENT_TYPE in limbus.formats
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
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root, file_name)
                try:
                    stage_node_data_list = StageNodeRewardList.parse_file(file_path)
                    ids.extend(
                        stage_node.nodeid for stage_node in stage_node_data_list.list
                    )
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
    return ids


def chunk_by(vec: List[int], chunk_size: int) -> List[List[int]]:
    return [vec[i : i + chunk_size] for i in range(0, len(vec), chunk_size)]


def load_main_chapter_state(directory: str = FOLDER) -> List[MainChapterStateFormat]:
    node_ids = fetch_node_ids(directory)
    chunked_ids = chunk_by(node_ids, 100)
    main_chapter_states = []
    for chunk in chunked_ids:
        main_chapter_state = MainChapterStateFormat(id=chunk[0] // 100, subcss=[])

        for node_id in chunk:
            sub_css = SubChapterStateFormat(
                id=node_id,
                rss=[1, 2, 3, 10],
                nss=[NodeStateFormat(id=node_id, ct=2, cn=1, dn=0)],
            )
            main_chapter_state.subcss.append(sub_css)
        main_chapter_states.append(main_chapter_state)

    return main_chapter_states

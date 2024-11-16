from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from itertools import groupby
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
    node_ids = fetch_node_ids()

    grouped_by_main = {
        key: list(group)
        for key, group in groupby(sorted(node_ids), key=lambda x: x // 100)
    }

    main_chapter_states = []
    for main_chapter_state_id, sub_node_ids in grouped_by_main.items():
        grouped_by_sub = {
            key: list(group)
            for key, group in groupby(sorted(sub_node_ids), key=lambda x: x // 100)
        }

        sub_chapters = [
            SubChapterStateFormat(
                id=sub_chapter_id,
                rss=[1, 2, 3, 10],
                nss=[
                    NodeStateFormat(
                        id=node_id,
                        ct=2,
                        cn=1,
                        dn=0,
                    )
                    for node_id in nodes
                ],
            )
            for sub_chapter_id, nodes in grouped_by_sub.items()
        ]

        main_chapter_states.append(
            MainChapterStateFormat(
                id=main_chapter_state_id,
                subcss=sub_chapters,
            )
        )

    return main_chapter_states

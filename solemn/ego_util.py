from solemn.database import ego_collection
from models.types import EgoFormat
from typing import List, Optional


def get_ego() -> List[EgoFormat]:
    ego_find = ego_collection.find()

    return [
        EgoFormat(
            acquire_time=doc.get("acquire_time"),
            gacksung=doc.get("gacksung"),
            ego_id=doc.get("ego_id"),
        )
        for doc in ego_find
    ]


def get_ego_by_id(ego_id: int) -> Optional[EgoFormat]:
    ego_doc = ego_collection.find_one({"ego_id": ego_id})

    if ego_doc:
        return EgoFormat(
            acquire_time=ego_doc.get("acquire_time"),
            gacksung=ego_doc.get("gacksung"),
            ego_id=ego_doc.get("ego_id"),
        )

    return None

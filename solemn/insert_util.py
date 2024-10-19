from typing import List
from solemn.database import (
    ego_collection,
    personality_collection,
    item_collection,
)
from models.types import (
    PersonalityFormat,
    EgoFormat,
    ItemFormat,
)


def insert_ego(data: EgoFormat) -> bool:
    ego_collection.insert_one(data.dict())

    return True


def insert_ego_many(data_list: List[EgoFormat]) -> bool:
    ego_docs = [data.dict() for data in data_list]
    ego_collection.insert_many(ego_docs)

    return True


def insert_personality(data: PersonalityFormat) -> bool:
    personality_collection.insert_one(data.dict())

    return True


def insert_personality_many(
    data_list: List[PersonalityFormat],
) -> bool:
    personality_docs = [
        data.dict() for data in data_list
    ]
    personality_collection.insert_many(personality_docs)

    return True


def insert_item(data: ItemFormat) -> bool:
    item_collection.insert_one(data.dict())

    return True


def insert_item_many(
    data_list: List[ItemFormat],
) -> bool:
    item_docs = [data.dict() for data in data_list]
    item_collection.insert_many(item_docs)

    return True

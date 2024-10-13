from solemn.database import item_collection
from models.types import ItemFormat
from typing import List, Optional


def get_item() -> List[ItemFormat]:
    item_find = item_collection.find()

    return [
        ItemFormat(
            item_id=doc.get("item_id"),
            num=doc.get("num"),
        )
        for doc in item_find
    ]


def get_item_by_id(item_id: int) -> Optional[ItemFormat]:
    item_doc = item_collection.find_one({"item_id": item_id})

    if item_doc:
        return ItemFormat(
            item_id=doc.get("item_id"),
            num=doc.get("num"),
        )

    return None

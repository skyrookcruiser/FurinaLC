from solemn.database import personality_collection
from models.types import PersonalityFormat
from typing import List, Optional


def get_personality() -> List[PersonalityFormat]:
    personality_find = personality_collection.find()

    return [
        PersonalityFormat(
            order_id=doc.get("order_id"),
            personality_id=doc.get("personality_id"),
            gacksung_illust_type=doc.get("gacksung_illust_type"),
            gacksung=doc.get("gacksung"),
            acquire_time=doc.get("acquire_time"),
            level=doc.get("level"),
            exp=doc.get("exp"),
        )
        for doc in personality_find
    ]


def get_personality_by_id(personality_id: int) -> Optional[PersonalityFormat]:
    personality_doc = personality_collection.find_one(
        {"personality_id": personality_id}
    )

    if personality_doc:
        return PersonalityFormat(
            order_id=personality_doc.get("order_id"),
            personality_id=personality_doc.get("personality_id"),
            gacksung_illust_type=personality_doc.get("gacksung_illust_type"),
            gacksung=personality_doc.get("gacksung"),
            acquire_time=personality_doc.get("acquire_time"),
            level=personality_doc.get("level"),
            exp=personality_doc.get("exp"),
        )

    return None

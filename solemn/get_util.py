from solemn.database import (
    formation_collection,
    ego_collection,
    personality_collection,
    item_collection,
)
from models.types import (
    FormationFormat,
    FormationDetailFormat,
    EgoFormat,
    PersonalityFormat,
    ItemFormat,
)
from typing import List, Optional


def get_formation() -> List[FormationFormat]:
    formation_find = formation_collection.find()

    return [
        FormationFormat(
            id=doc["id"],
            formationDetails=[
                FormationDetailFormat(
                    personalityId=detail[
                        "personalityId"
                    ],
                    egos=detail["egos"],
                    isParticipated=detail.get(
                        "isParticipated", False
                    ),
                    participationOrder=detail.get(
                        "participationOrder", 0
                    ),
                )
                for detail in doc["formationDetails"]
            ],
        )
        for doc in formation_find
    ]


def get_formation_by_id(
    formation_id: int,
) -> Optional[FormationFormat]:
    formation_doc = formation_collection.find_one(
        {"id": formation_id}
    )

    if formation_doc:
        return FormationFormat(
            id=formation_doc["id"],
            formationDetails=[
                FormationDetailFormat(
                    personalityId=detail[
                        "personalityId"
                    ],
                    egos=detail["egos"],
                    isParticipated=detail.get(
                        "isParticipated", False
                    ),
                    participationOrder=detail.get(
                        "participationOrder", 0
                    ),
                )
                for detail in formation_doc[
                    "formationDetails"
                ]
            ],
        )

    return None


def get_item() -> List[ItemFormat]:
    item_find = item_collection.find()

    return [
        ItemFormat(
            item_id=doc.get("item_id"),
            num=doc.get("num"),
        )
        for doc in item_find
    ]


def get_item_by_id(
    item_id: int,
) -> Optional[ItemFormat]:
    item_doc = item_collection.find_one(
        {"item_id": item_id}
    )

    if item_doc:
        return ItemFormat(
            item_id=item_doc.get("item_id"),
            num=item_doc.get("num"),
        )

    return None


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
    ego_doc = ego_collection.find_one(
        {"ego_id": ego_id}
    )

    if ego_doc:
        return EgoFormat(
            acquire_time=ego_doc.get("acquire_time"),
            gacksung=ego_doc.get("gacksung"),
            ego_id=ego_doc.get("ego_id"),
        )

    return None


def get_personality() -> List[PersonalityFormat]:
    personality_find = personality_collection.find()

    return [
        PersonalityFormat(
            order_id=doc.get("order_id"),
            personality_id=doc.get("personality_id"),
            gacksung_illust_type=doc.get(
                "gacksung_illust_type"
            ),
            gacksung=doc.get("gacksung"),
            acquire_time=doc.get("acquire_time"),
            level=doc.get("level"),
            exp=doc.get("exp"),
        )
        for doc in personality_find
    ]


def get_personality_by_id(
    personality_id: int,
) -> Optional[PersonalityFormat]:
    personality_doc = personality_collection.find_one(
        {"personality_id": personality_id}
    )

    if personality_doc:
        return PersonalityFormat(
            order_id=personality_doc.get("order_id"),
            personality_id=personality_doc.get(
                "personality_id"
            ),
            gacksung_illust_type=personality_doc.get(
                "gacksung_illust_type"
            ),
            gacksung=personality_doc.get("gacksung"),
            acquire_time=personality_doc.get(
                "acquire_time"
            ),
            level=personality_doc.get("level"),
            exp=personality_doc.get("exp"),
        )

    return None

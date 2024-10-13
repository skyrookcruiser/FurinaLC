from solemn.database import formation_collection
from models.types import FormationFormat, FormationDetailFormat
from typing import List, Optional


def get_formation() -> List[FormationFormat]:
    formation_find = formation_collection.find()

    return [
        FormationFormat(
            id=doc["id"],
            formationDetails=[
                FormationDetailFormat(
                    personalityId=detail["personalityId"],
                    egos=detail["egos"],
                    isParticipated=detail.get("isParticipated", False),
                    participationOrder=detail.get("participationOrder", 0),
                )
                for detail in doc["formationDetails"]
            ],
        )
        for doc in formation_find
    ]


def get_formation_by_id(formation_id: int) -> Optional[FormationFormat]:
    formation_doc = formation_collection.find_one({"id": formation_id})

    if formation_doc:
        return FormationFormat(
            id=formation_doc["id"],
            formationDetails=[
                FormationDetailFormat(
                    personalityId=detail["personalityId"],
                    egos=detail["egos"],
                    isParticipated=detail.get("isParticipated", False),
                    participationOrder=detail.get("participationOrder", 0),
                )
                for detail in formation_doc["formationDetails"]
            ],
        )

    return None


def modify_formation_by_id(
    formation_id: int,
    personality_id: Optional[int] = None,
    egos: Optional[List[int]] = None,
    is_participated: Optional[bool] = None,
    participation_order: Optional[int] = None,
) -> bool:
    formation_doc = formation_collection.find_one({"id": formation_id})

    if not formation_doc:
        print(f"Formation with id {formation_id} not found.")
        return False

    for detail in formation_doc["formationDetails"]:
        if str(detail["personalityId"])[:3] == str(personality_id)[:3]:
            if personality_id is not None:
                detail["personalityId"] = personality_id
            if egos is not None:
                detail["egos"] = egos
            if is_participated is not None:
                detail["isParticipated"] = is_participated
            if participation_order is not None:
                detail["participationOrder"] = participation_order
            break
    else:
        print(f"Personality ID {personality_id} not found in formation {formation_id}.")
        return False

    result = formation_collection.update_one(
        {"id": formation_id},
        {"$set": {"formationDetails": formation_doc["formationDetails"]}},
    )

    if result.modified_count == 0:
        print(f"No documents were modified for formation ID {formation_id}.")
        return True

    return True

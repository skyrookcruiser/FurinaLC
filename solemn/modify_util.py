from solemn.database import formation_collection
from typing import List, Optional


def modify_formation_by_id(
    formation_id: int,
    personality_id: Optional[int] = None,
    egos: Optional[List[int]] = None,
    is_participated: Optional[bool] = None,
    participation_order: Optional[int] = None,
) -> bool:
    formation_doc = formation_collection.find_one(
        {"id": formation_id}
    )

    if not formation_doc:
        print(
            f"Formation with id {formation_id} not found."
        )
        return False

    for detail in formation_doc["formationDetails"]:
        if (
            str(detail["personalityId"])[:3]
            == str(personality_id)[:3]
        ):
            if personality_id is not None:
                detail["personalityId"] = personality_id
            if egos is not None:
                detail["egos"] = egos
            if is_participated is not None:
                detail["isParticipated"] = (
                    is_participated
                )
            if participation_order is not None:
                detail["participationOrder"] = (
                    participation_order
                )
            break
    else:
        print(
            f"Personality ID {personality_id} not found in formation {formation_id}."
        )
        return False

    result = formation_collection.update_one(
        {"id": formation_id},
        {
            "$set": {
                "formationDetails": formation_doc[
                    "formationDetails"
                ]
            }
        },
    )

    if result.modified_count == 0:
        print(
            f"No documents were modified for formation ID {formation_id}."
        )
        return True

    return True

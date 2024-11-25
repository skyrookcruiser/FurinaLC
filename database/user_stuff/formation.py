from pydantic import BaseModel
from database.client import db
from resources.parser.user_stuff.formation import create_formation_format_list
from limbus.formats import FormationFormat, FormationDetailFormat, FormationNameElement
from typing import List, Optional

formation_collection = db["formations"]


class FormationFormatWithUID(BaseModel):
    uid: int
    id: int
    formationDetails: List[FormationDetailFormat]
    formationNameFormat: List[FormationNameElement]


def insert_formation_formats(uid: int) -> None:
    try:
        formation_format_list = create_formation_format_list()
        formation_format_with_uid_list = [
            FormationFormatWithUID(
                uid=uid,
                id=formation_format.id,
                formationDetails=formation_format.formationDetails,
                formationNameFormat=formation_format.formationNameFormat,
            )
            for formation_format in formation_format_list
        ]

        if formation_format_with_uid_list:
            formation_collection.insert_many(
                [formation.dict() for formation in formation_format_with_uid_list]
            )
    except Exception as e:
        print("WARN:     " + str(e))


def get_formation_formats_by_uid(uid: int) -> List[FormationFormat]:
    try:
        formation_docs = formation_collection.find({"uid": uid})

        return [
            FormationFormat(
                id=doc["id"],
                formationDetails=doc["formationDetails"],
                formationNameFormat=doc["formationNameFormat"],
            )
            for doc in formation_docs
        ]

    except Exception as e:
        print("WARN:     " + str(e))

        return []


def get_one_formation_format(uid: int, formation_id: int) -> Optional[FormationFormat]:
    try:
        formation_doc = formation_collection.find_one({"uid": uid, "id": formation_id})

        if formation_doc:
            return FormationFormat(
                id=formation_doc["id"],
                formationDetails=formation_doc["formationDetails"],
                formationNameFormat=formation_doc["formationNameFormat"],
            )

        return None

    except Exception as e:
        print("WARN:     " + str(e))

        return None


def update_formation_format(
    uid: int,
    formation_id: int,
    formationDetails: Optional[List[FormationDetailFormat]] = None,
    formationNameFormat: Optional[List[FormationNameElement]] = None,
) -> bool:
    try:
        update_fields = {}
        if formationDetails is not None:
            update_fields["formationDetails"] = [
                detail.dict() for detail in formationDetails
            ]
        if formationNameFormat is not None:
            update_fields["formationNameFormat"] = [
                name_element.dict() for name_element in formationNameFormat
            ]

        if update_fields:
            formation_collection.update_one(
                {"uid": uid, "id": formation_id}, {"$set": update_fields}
            )

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False

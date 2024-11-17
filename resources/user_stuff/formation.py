from typing import List
from limbus.formats import FormationFormat, FormationDetailFormat, FormationNameElement


def create_formation_format_list() -> List[FormationFormat]:
    return [
        FormationFormat(
            id=i,
            formationDetails=[
                FormationDetailFormat(
                    personalityId=10101 + j * 100,
                    egos=[20101 + j * 100],
                    isParticipated=False,
                    participationOrder=j + 1,
                )
                for j in range(12)
            ],
            formationNameFormat=[
                FormationNameElement(
                    k=-1,
                    v=-1,
                )
            ],
        )
        for i in range(20)
    ]

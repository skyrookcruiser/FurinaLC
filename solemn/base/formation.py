from models.types import FormationFormat, FormationDetailFormat

formation_list = [
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
    )
    for i in range(19)
]

formation_dicts = [
    {
        "id": formation.id,
        "formationDetails": [
            {
                "personalityId": detail.personalityId,
                "egos": detail.egos,
                "isParticipated": detail.isParticipated,
                "participationOrder": detail.participationOrder,
            }
            for detail in formation.formationDetails
        ],
    }
    for formation in formation_list
]

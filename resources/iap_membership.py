from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
from limbus.formats import MembershipFormat

FOLDER = "./resources/LimbusStaticData/StaticData/static-data/iap-product"


class IapElement(BaseModel):
    type: str
    id: int
    num: int


class IapMembershipData(BaseModel):
    id: int
    category: str
    returnpolicytype: Optional[str] = None
    productId: str
    priceTier: int
    chanceId: Optional[int] = None
    nextIdAfterChance: Optional[int] = None
    membershipDailyChanceId: Optional[int] = None
    defaultElements: Optional[List[IapElement]] = None
    membershipDailyElements: Optional[List[IapElement]] = None


class IapMembershipDataList(BaseModel):
    list: List[IapMembershipData]


def create_membership_formats(directory: str = FOLDER) -> List[MembershipFormat]:
    membership_formats = []
    folder_path = Path(directory)

    for file_path in folder_path.glob("**/*.json"):
        try:
            if "a1" in file_path.stem:
                continue
            iap_membership_data_list = IapMembershipDataList.parse_file(file_path)

            for membership_data in iap_membership_data_list.list:
                if (
                    membership_data.productId
                    and any(
                        keyword in membership_data.productId.lower()
                        for keyword in ["monthly", "pass"]
                    )
                    and "fixed" not in membership_data.productId.lower()
                ):
                    membership_format = MembershipFormat(
                        iap_id=membership_data.id,
                        expiry_date="2098-11-09T22:10:00.864Z",
                    )
                    membership_formats.append(membership_format)

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return membership_formats

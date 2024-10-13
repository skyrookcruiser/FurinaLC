from models.types import UserInfo
from util.time import get_curr_time


def get_user() -> UserInfo:
    return UserInfo(
        uid=404, level=404, stamina=404, last_stamina_recover="2024-06-24T20:00:00.000Z"
    )

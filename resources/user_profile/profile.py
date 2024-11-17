from limbus.formats import UserPublicProfileWithSupportersFormat
from utils import get_date_time
import random
import string


def random_letter():
    return random.choice(string.ascii_uppercase)


def create_user_public_profile_with_supporters_format(
    uid: int,
) -> UserPublicProfileWithSupportersFormat:
    letter = random_letter()
    formatted_uid = f"{uid:09d}"
    profile_uid = f"{letter}{formatted_uid}"

    return UserPublicProfileWithSupportersFormat(
        # Don't know why the public uid doesnt work.
        public_uid=profile_uid,
        illust_id=10101,
        illust_gacksung_level=1,
        leftborder_id=-1,
        rightborder_id=-1,
        egobackground_id=-1,
        sentence_id=1,
        word_id=1,
        banners=[],
        level=302,
        date=get_date_time(),
        support_personalities=[],
    )

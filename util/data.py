from typing import List
from models.types import (
    UnlockCodeFormat,
    MainChapterStateFormat,
    NodeStateFormat,
    SubChapterStateFormat,
    UserInfo,
)
from util.time import get_curr_time

UNLOCK_CODES = [
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    9103,
    9104,
    9105,
    9106,
    9107,
    9108,
    9109,
    9110,
    9111,
    10644,
]

LOCKED_CODES = [107]


def get_user() -> UserInfo:
    return UserInfo(
        uid=404,
        level=404,
        stamina=404,
        last_stamina_recover=get_curr_time(),
    )


def get_chapter_codes() -> List[int]:
    codes = UNLOCK_CODES.copy()
    codes.extend(LOCKED_CODES)
    return codes


def get_formatted_user_codes() -> (
    List[UnlockCodeFormat]
):
    return [
        UnlockCodeFormat(unlockcode=code)
        for code in UNLOCK_CODES
    ]


def load_main_chapter_state() -> (
    List[MainChapterStateFormat]
):
    main_chapter_state_ids = [1, 91]

    main_chapter_states = []
    for id in main_chapter_state_ids:
        sub_chapters = []

        for code in get_chapter_codes():
            if code // 100 == id:
                node_states = [
                    NodeStateFormat(
                        id=code * 100 + sub_id,
                        ct=2,
                        cn=1,
                        dn=0,
                    )
                    for sub_id in range(1, 100)
                ]
                sub_chapter = SubChapterStateFormat(
                    id=code,
                    nss=node_states,
                    rss=[1, 2, 3, 10],
                )
                sub_chapters.append(sub_chapter)

        main_chapter_state = MainChapterStateFormat(
            id=id, subcss=sub_chapters
        )
        main_chapter_states.append(main_chapter_state)

    return main_chapter_states

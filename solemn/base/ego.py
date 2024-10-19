from models.types import EgoFormat
from util.time import get_curr_time

ego_list = [
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20101,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20201,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20301,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20401,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20501,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20601,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20701,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20801,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=20901,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=21001,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=21101,
    ),
    EgoFormat(
        acquire_time=get_curr_time(),
        gacksung=4,
        ego_id=21201,
    ),
]

ego_dicts = [
    {
        "acquire_time": e.acquire_time,
        "gacksung": e.gacksung,
        "ego_id": e.ego_id,
    }
    for e in ego_list
]

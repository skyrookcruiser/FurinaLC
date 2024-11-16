from limbus.requests import Cs, ReqGetDungeonSaveInfoAll
from limbus.responses import Sc, RspGetDungeonSaveInfoAll
from limbus.formats import (
    StoryDungeonSaveInfoFormat,
    MirrorDungeonSaveInfoFormat,
    RailwayDungeonSaveInfoFormat,
    StoryMirrorDungeonSaveInfoFormat,
    # StoryDungeonCurrentInfoFormat,
    # DungeonMapNodeFormat,
    MirrorDungeonCurrentInfoFormat,
    StoryMirrorDungeonCurrentInfoFormat,
    MirrorDungeonClearInfoFormat,
    MirrorDungeonHistoryFormat,
)


async def handle(req: Cs[ReqGetDungeonSaveInfoAll]):
    railway_id = req.parameters.railwayDungeonId

    story_safe_info = StoryDungeonSaveInfoFormat()

    mirror_origin_save_info = MirrorDungeonSaveInfoFormat(
        dungeonId=-1,
        idx=-1,
        currentInfo=MirrorDungeonCurrentInfoFormat(
            eid=-1,
        ),
    )

    railway_save_info = RailwayDungeonSaveInfoFormat(
        id=railway_id,
        prevclearnode=-1,
        lastenternodeid=1,
    )

    story_mirror_save_info = StoryMirrorDungeonSaveInfoFormat(
        dungeonid=-1,
        currentinfo=StoryMirrorDungeonCurrentInfoFormat(
            eid=-1,
        ),
    )

    mirror_dungeon_clear_infos = [
        MirrorDungeonClearInfoFormat(
            dungeonid=railway_id,
            idx=0,
            clearnumber=1,
            defeatnumber=1,
        )
    ]

    mirror_dungeon_histories = [
        MirrorDungeonHistoryFormat(
            dungeonid=railway_id,
        )
    ]

    return Sc[RspGetDungeonSaveInfoAll](
        result=RspGetDungeonSaveInfoAll(
            storySaveInfo=story_safe_info,
            mirrorOriginSaveInfo=mirror_origin_save_info,
            railwaySaveInfo=railway_save_info,
            storyMirrorSaveInfo=story_mirror_save_info,
            mirrorDungeonClearInfos=mirror_dungeon_clear_infos,
            mirrorDungeonHistories=mirror_dungeon_histories,
        )
    )

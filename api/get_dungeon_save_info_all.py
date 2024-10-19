from fastapi import Request
from models.packets import (
    ResPacket_GetDungeonSaveInfoAll,
)
from models.server import ResponsePacket
from models.types import (
    StoryDungeonSaveInfoFormat,
    MirrorDungeonSaveInfoFormat,
    RailwayDungeonSaveInfoFormat,
    StoryMirrorDungeonSaveInfoFormat,
    MirrorDungeonClearInfoFormat,
    MirrorDungeonHistoryFormat,
    MirrorDungeonCurrentInfoFormat,
    StoryMirrorDungeonCurrentInfoFormat,
)


async def handle(request: Request):
    res_packet = ResPacket_GetDungeonSaveInfoAll(
        storySaveInfo=StoryDungeonSaveInfoFormat(),
        mirrorOriginSaveInfo=MirrorDungeonSaveInfoFormat(
            dungeonId=-1,
            idx=-1,
            currentInfo=MirrorDungeonCurrentInfoFormat(
                eid=-1,
            ),
        ),
        railwaySaveInfo=RailwayDungeonSaveInfoFormat(
            id=3, prevclearnode=-1, lastenternodeid=-1
        ),
        storyMirrorSaveInfo=StoryMirrorDungeonSaveInfoFormat(
            dungeonid=-1,
            currentinfo=StoryMirrorDungeonCurrentInfoFormat(
                eid=-1,
            ),
        ),
        mirrorDungeonClearInfos=[
            MirrorDungeonClearInfoFormat(
                dungeonid=4,
                idx=0,
                clearnumber=404,
                defeatnumber=404,
            ),
        ],
        mirrorDungeonHistories=[
            MirrorDungeonHistoryFormat(
                dungeonid=4,
            ),
        ],
    )

    response = ResponsePacket[
        ResPacket_GetDungeonSaveInfoAll
    ](result=res_packet)

    return response.dict()

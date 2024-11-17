from fastapi import FastAPI
from . import (
    CheckSeasonLog,
    FetchLatestSynchronousData,
    LoadUserDataAll,
    UpdateFormation,
    ChangeCurrentAnnouncer,
    SetPersonalityGacksungIllust,
    GetUserCouponState,
    UseCoupon,
    GetUserBanners,
    GetProfileTicketDecoDatas,
    UpdateUserProfile,
    UpdateProfileTicketDeco,
    UpdateLobbyCg,
    GetFriendsData,
    GetDungeonSaveInfoAll,
    GetRailwayDungeonNodeAndLogAll,
    EnterRailwayDungeon,
    ClaimClosedGachaRewards,
    EnterStageBattle,
    ExitStageBattle,
)


def add_api_handler(app: FastAPI):
    app.post("/api/FetchLatestSynchronousData")(FetchLatestSynchronousData.handle)
    app.post("/api/LoadUserDataAll")(LoadUserDataAll.handle)
    app.post("/api/CheckSeasonLog")(CheckSeasonLog.handle)
    app.post("/api/UpdateFormation")(UpdateFormation.handle)
    app.post("/api/ChangeCurrentAnnouncer")(ChangeCurrentAnnouncer.handle)
    app.post("/api/SetPersonalityGacksungIllust")(SetPersonalityGacksungIllust.handle)
    app.post("/api/GetUserCouponState")(GetUserCouponState.handle)
    app.post("/api/UseCoupon")(UseCoupon.handle)
    app.post("/api/GetUserBanners")(GetUserBanners.handle)
    app.post("/api/GetProfileTicketDecoDatas")(GetProfileTicketDecoDatas.handle)
    app.post("/api/UpdateUserProfile")(UpdateUserProfile.handle)
    app.post("/api/UpdateProfileTicketDeco")(UpdateProfileTicketDeco.handle)
    app.post("/api/UpdateLobbyCg")(UpdateLobbyCg.handle)
    app.post("/api/GetFriendsData")(GetFriendsData.handle)
    app.post("/api/GetDungeonSaveInfoAll")(GetDungeonSaveInfoAll.handle)
    app.post("/api/GetRailwayDungeonNodeAndLogAll")(
        GetRailwayDungeonNodeAndLogAll.handle
    )
    app.post("/api/EnterRailwayDungeon")(EnterRailwayDungeon.handle)
    app.post("/api/ClaimClosedGachaRewards")(ClaimClosedGachaRewards.handle)
    app.post("/api/EnterStageBattle")(EnterStageBattle.handle)
    app.post("/api/ExitStageBattle")(ExitStageBattle.handle)

from fastapi import FastAPI
from middleware import schnajang
from login import (
    check_client_version,
    sign_in_as_steam,
    get_terms_of_use_state_all,
)
from iap import update_steam_pending_purchase
from api import (
    fetch_latest_synchronous_data,
    load_user_data_all,
    check_season_log,
    refresh_mailbox,
    update_formation,
    get_dungeon_save_info_all,
    exit_stage_battle,
    get_user_coupon_state,
    use_coupon,
    claim_closed_gacha_rewards,
    play_gacha,
    enter_stage_battle,
)


def add_middleware(app: FastAPI):
    app.middleware("http")(schnajang.handle)


def add_iap_routes(app: FastAPI):
    app.post("/iap/UpdateSteamPendingPurchase")(
        update_steam_pending_purchase.handle
    )


def add_login_routes(app: FastAPI):
    app.post("/login/CheckClientVersion")(
        check_client_version.handle
    )
    app.post("/login/SignInAsSteam")(
        sign_in_as_steam.handle
    )
    app.post("/login/GetTermsOfUseStateAll")(
        get_terms_of_use_state_all.handle
    )


def add_api_routes(app: FastAPI):
    app.post("/api/FetchLatestSynchronousData")(
        fetch_latest_synchronous_data.handle
    )
    app.post("/api/LoadUserDataAll")(
        load_user_data_all.handle
    )
    app.post("/api/CheckSeasonLog")(
        check_season_log.handle
    )
    app.post("/api/RefreshMailbox")(
        refresh_mailbox.handle
    )
    app.post("/api/UpdateFormation")(
        update_formation.handle
    )
    app.post("/api/GetDungeonSaveInfoAll")(
        get_dungeon_save_info_all.handle
    )
    app.post("/api/ExitStageBattle")(
        exit_stage_battle.handle
    )
    app.post("/api/GetUserCouponState")(
        get_user_coupon_state.handle
    )
    app.post("/api/UseCoupon")(use_coupon.handle)
    app.post("/api/ClaimClosedGachaRewards")(
        claim_closed_gacha_rewards.handle
    )
    app.post("/api/PlayGacha")(play_gacha.handle)
    app.post("api/EnterStageBattle")(
        enter_stage_battle.handle
    )

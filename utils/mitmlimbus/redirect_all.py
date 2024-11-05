from mitmproxy import http
from update import load_limbus_update, get_limbus_update

HOST = "127.0.0.1"
PRIVATE_SERVER_PORT = 21000
MINI_DOWNLOAD_SERVER_PORT = 2070
get_update = []

# mitmproxy -s redirect_all.py
# redirects:
#   game api (handled by whatever gameserver there is at port 21000),
#   update data (for offline play, handled by miniserver),
#   battlelog (handled by miniserver)


def check_and_update_args():
    catalog_arg = None
    serverinfo_arg = None
    sound_arg = None

    for item in get_update:
        if "catalog" in item:
            catalog_arg = item
        elif "serverinfo" in item:
            serverinfo_arg = item
        elif "Sound" in item:
            sound_arg = item

    if catalog_arg is not None and serverinfo_arg is not None and sound_arg is not None:
        return catalog_arg, serverinfo_arg, sound_arg

    return None, None, None


def has_catalog_hash(name):
    updates = load_limbus_update().dict().get("update", [])
    return any(update["hash"] in name for update in updates)


def has_server_info_json(name):
    updates = load_limbus_update().dict().get("update", [])
    return any(update["server_info"] in name for update in updates)


def has_sound_patch_json(name):
    updates = load_limbus_update().dict().get("update", [])
    return any(update["sound_patch"] in name for update in updates)


def handle_download_request(flow, uri):
    if "catalog" in uri:
        catalog_hash = uri.replace("/catalog", "_catalog")
        if has_catalog_hash(catalog_hash):
            flow.request.scheme = "http"
            flow.request.host = HOST
            flow.request.port = MINI_DOWNLOAD_SERVER_PORT
            flow.request.path = f"/hash{catalog_hash}"
        else:
            get_update.append("https://download.limbuscompany.site" + uri)

    elif "serverinfo" in uri:
        if has_server_info_json(uri):
            flow.request.scheme = "http"
            flow.request.host = HOST
            flow.request.port = MINI_DOWNLOAD_SERVER_PORT
            flow.request.path = f"/server_info{uri}"
        else:
            get_update.append("https://download.limbuscompany.site" + uri)

    elif "Sound" in uri:
        sound_patch_name = uri.replace("/Assets/Sound/", "_Sound")
        if has_sound_patch_json(sound_patch_name):
            flow.request.scheme = "http"
            flow.request.host = HOST
            flow.request.port = MINI_DOWNLOAD_SERVER_PORT
            flow.request.path = f"/sound_patch{sound_patch_name}"
        else:
            sound_patch_name = uri.replace("/Assets/Sound/", "_Sound")
            get_update.append("https://download.limbuscompany.site" + uri)

    if len(get_update) >= 3:
        catalog_arg, serverinfo_arg, sound_arg = check_and_update_args()
        if catalog_arg and serverinfo_arg and sound_arg:
            get_limbus_update(catalog_arg, serverinfo_arg, sound_arg)
            get_update.clear()


def request(flow: http.HTTPFlow) -> None:
    uri = flow.request.path
    host = flow.request.pretty_host

    if "download" in host and "limbus" in host:
        handle_download_request(flow, uri)

    elif host == "battlelog.limbuscompanyapi.com":
        flow.request.scheme = "http"
        flow.request.host = HOST
        flow.request.port = MINI_DOWNLOAD_SERVER_PORT
        flow.request.path = "/log"

    elif host.endswith(".limbuscompanyapi.com") or host.endswith(
        ".limbuscompanyapi-2.com"
    ):
        flow.request.scheme = "http"
        flow.request.host = HOST
        flow.request.port = PRIVATE_SERVER_PORT

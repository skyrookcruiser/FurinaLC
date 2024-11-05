from mitmproxy import http


# mitmproxy -s redirect.py
# doesn't redirect download.limbuscompany.site
def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host.endswith(
        ".limbuscompanyapi.com"
    ) or flow.request.pretty_host.endswith(".limbuscompanyapi-2.com"):
        flow.request.scheme = "http"
        flow.request.host = "127.0.0.1"
        flow.request.port = 21000

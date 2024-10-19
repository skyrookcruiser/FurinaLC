from mitmproxy import http
from server.config import C


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host.endswith(
        ".limbuscompanyapi.com"
    ) or flow.request.pretty_host.endswith(
        ".limbuscompanyapi-2.com"
    ):
        flow.request.scheme = "http"
        flow.request.host = C[0]
        flow.request.port = C[1]

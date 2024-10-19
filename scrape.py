from mitmproxy import contentviews, flow, http
from middleware.encryption import decrypt
import json

domain = "www.limbuscompanyapi.com"


def parse_encrypted(data):
    if data.startswith(b'"'):
        return json.loads(data)
    else:
        return data.decode()
    return None


class LimbusDeobfCase(contentviews.View):
    name = "limbus_deobf"

    def __call__(
        self,
        data: bytes,
        *,
        content_type: str | None = None,
        flow: flow.Flow | None = None,
        http_message: http.Message | None = None,
        **unknown_metadata,
    ) -> contentviews.TViewResult:
        encrypted_timestamp = http_message.headers.get(
            "Content-Encrypted"
        )
        if not encrypted_timestamp:
            return
        try:
            encrypted_timestamp = int(
                encrypted_timestamp
            )
        except Exception:
            raise print("{e}")

        hexdump = parse_encrypted(data)
        if not hexdump:
            return

        encrypted = bytes.fromhex(hexdump)
        decrypted = decrypt(
            encrypted, encrypted_timestamp
        ).decode()

        try:
            decrypted_json = json.loads(decrypted)
            decrypted = json.dumps(
                decrypted_json, indent=2
            )
        except Exception:
            raise print("{e}")

        return (
            "limbus deobfuscate",
            contentviews.format_text(decrypted),
        )

    def render_priority(
        self,
        data: bytes,
        *,
        content_type: str | None = None,
        flow: flow.Flow | None = None,
        http_message: http.Message | None = None,
        **unknown_metadata,
    ) -> float:
        if http_message.headers.get(
            "Content-Encrypted"
        ):
            return 1
        else:
            return 0


view = LimbusDeobfCase()


def load(l):
    contentviews.add(view)


def done():
    contentviews.remove(view)

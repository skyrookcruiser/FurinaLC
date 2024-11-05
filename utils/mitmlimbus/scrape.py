import os
import json
import logging
from mitmproxy import contentviews, flow, http

# mitmweb -s scrape.py
# Open the flow -> request/response
# Otherwise, won't output json files in scrapes

key = bytes.fromhex(
    "20826c5b34e60ea154a26f3880622e8bdc7a4cd3f008bcfd8b71cdcd3c86cb9984b20664e3c8841e62787f8e0536d44249d7cffdca232ecaa4f2616e64504d37"
)
domain = "www.limbuscompanyapi.com"
output_directory = "./scrapes/"

os.makedirs(output_directory, exist_ok=True)


def decrypt(ciphertext, timestamp):
    plaintext = bytearray(len(ciphertext))
    time_mod_max_length = timestamp % len(key)

    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[i] ^ key[time_mod_max_length]
        time_mod_max_length = (time_mod_max_length + 1) % len(key)

    return plaintext


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
        encrypted_timestamp = http_message.headers.get("Content-Encrypted")
        if not encrypted_timestamp:
            return
        try:
            encrypted_timestamp = int(encrypted_timestamp)
        except ValueError:
            return

        hexdump = parse_encrypted(data)
        if not hexdump:
            return

        encrypted = bytes.fromhex(hexdump)
        decrypted = decrypt(encrypted, encrypted_timestamp).decode()

        try:
            decrypted_json = json.loads(decrypted)
            decrypted = json.dumps(decrypted_json, indent=2)
        except json.JSONDecodeError:
            pass

        uri_path = (
            flow.request.path.replace("/", "_") if flow and flow.request else "unknown"
        )
        message_type = "request" if http_message == flow.request else "response"
        filename = (
            f"{output_directory}{uri_path}_{message_type}_{encrypted_timestamp}.json"
        )
        with open(filename, "w") as f:
            f.write(decrypted)

        logging.info(f"Decrypted data saved to {filename}")

        return "limbus deobfuscate", contentviews.format_text(decrypted)

    def render_priority(
        self,
        data: bytes,
        *,
        content_type: str | None = None,
        flow: flow.Flow | None = None,
        http_message: http.Message | None = None,
        **unknown_metadata,
    ) -> float:
        return 1 if http_message.headers.get("Content-Encrypted") else 0


view = LimbusDeobfCase()


def load(l):
    contentviews.add(view)


def done():
    contentviews.remove(view)

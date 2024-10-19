key_parts = [
    "20826c5b34e60ea154a26f3880622e8bdc7a4cd3f00",
    "8bcfd8b71cdcd3c86cb9984b20664e3c8841e62787f",
    "8e0536d44249d7cffdca232ecaa4f2616e64504d37",
]

combined_key = (
    key_parts[0] + key_parts[1] + key_parts[2]
)

key = bytes.fromhex(combined_key)

import time

SECRET_KEY = bytes.fromhex("THOSE WHO KNOW:")


def generate_seed() -> int:
    """Get the current time for offset seed."""
    return int(time.time())


def decode_bytes(byte_data: bytes) -> str:
    """Convert bytes to a UTF-8 string."""
    return byte_data.decode("utf-8")


def xor_layer(data: bytes, seed: int) -> bytes:
    """Apply XOR using the SECRET_KEY and a seed value for offset."""
    return bytes(
        byte ^ SECRET_KEY[(i + seed) % len(SECRET_KEY)] for i, byte in enumerate(data)
    )


def deobfuscate(hex_encoded: bytes, seed: int) -> bytes:
    """Convert a hex-encoded byte string back to original bytes using XOR decryption."""
    hex_str = decode_bytes(hex_encoded)
    if hex_str[0] == '"':
        hex_str = hex_str[1:-1]

    byte_data = bytes.fromhex(hex_str)

    return xor_layer(byte_data, seed)


def obfuscate(data: bytes, seed: int) -> str:
    """Convert data to a hex-encoded string after XOR encryption."""
    encrypted_bytes = xor_layer(data, seed)

    return f'"{encrypted_bytes.hex()}"'

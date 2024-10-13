import logging
from typing import Optional

key = bytes.fromhex(
    "20826c5b34e60ea154a26f3880622e8bdc7a4cd3f008bcfd8b71cdcd3c86cb9984b20664e3c8841e62787f8e0536d44249d7cffdca232ecaa4f2616e64504d37"
)


def decrypt(ciphertext, timestamp):
    plaintext = bytearray(len(ciphertext))
    time_mod_max_length = timestamp % len(key)

    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[i] ^ key[time_mod_max_length]
        time_mod_max_length = (time_mod_max_length + 1) % len(key)

    return plaintext


def encrypt(plaintext, timestamp):
    ciphertext = bytearray(len(plaintext))
    time_mod_max_length = timestamp % len(key)

    for i in range(len(plaintext)):
        ciphertext[i] = plaintext[i] ^ key[time_mod_max_length]
        time_mod_max_length = (time_mod_max_length + 1) % len(key)

    return ciphertext


def deobfuscate(encrypted_data: bytes, encrypted_timestamp: int) -> Optional[str]:
    try:
        encrypted = bytes.fromhex(encrypted_data.decode())
        decrypted = decrypt(encrypted, encrypted_timestamp).decode()
        return decrypted
    except Exception as e:
        logging.error(f"Decryption failed: {e}")
        return None


def obfuscate(plaintext_data: bytes, encrypted_timestamp: int) -> Optional[str]:
    try:
        encrypted = encrypt(plaintext_data, encrypted_timestamp).hex()
        return f'"{encrypted}"'  # client wants u to have quote marks, bffr
    except Exception as e:
        logging.error(f"Encryption failed: {e}")
        return None

import json
import httpx
from pathlib import Path
from typing import Tuple, List, Optional
from pydantic import BaseModel


class UpdateData(BaseModel):
    hash: Optional[str] = None
    server_info: Optional[str] = None
    sound_patch: Optional[str] = None


class LimbusUpdate(BaseModel):
    update: List[UpdateData] = []


def load_limbus_update(
    filepath: Path = Path("./version.json"),
) -> LimbusUpdate:
    if filepath.exists():
        return LimbusUpdate.parse_file(filepath)
    return LimbusUpdate()


def insert_limbus_update_data(
    hash: str,
    server_info: str,
    sound_patch: str,
    filepath: Path = Path("./version.json"),
) -> None:
    limbus_update = load_limbus_update(filepath)

    new_data = UpdateData(hash=hash, server_info=server_info, sound_patch=sound_patch)

    limbus_update.update.append(new_data)

    with open(filepath, "w") as file:
        json.dump(limbus_update.dict(), file, indent=4)


def fetch_limbus_update_data(
    hash: str, filepath: Path = Path("./version.json")
) -> Tuple[str, str, str]:
    limbus_update = load_limbus_update(filepath)

    for update_data in limbus_update.update:
        if update_data.hash == hash:
            return update_data.hash, update_data.server_info, update_data.sound_patch

    return None


def get_limbus_update(
    uri_hash: str, uri_server_info: str, uri_sound_patch: str
) -> None:
    try:
        with httpx.Client() as client:
            hash_response = client.get(uri_hash)
            hash_response.raise_for_status()
            hash_parts = uri_hash.split("/")[-2:]
            hash_file_name = f"{hash_parts[0]}_{hash_parts[1]}"
            hash_file_path = Path(f"./hashes/{hash_file_name}")
            with open(hash_file_path, "wb") as hash_file:
                hash_file.write(hash_response.content)
            print(f"Saved hash data to {hash_file_path}")

            server_info_response = client.get(uri_server_info)
            server_info_response.raise_for_status()
            server_info_file_name = uri_server_info.replace(
                "https://download.limbuscompany.site/", ""
            )
            server_info_file_path = Path(f"./server_infos/{server_info_file_name}")
            with open(server_info_file_path, "wb") as server_info_file:
                server_info_file.write(server_info_response.content)
            print(f"Saved server_info data to {server_info_file_path}")

            sound_patch_response = client.get(uri_sound_patch)
            sound_patch_response.raise_for_status()
            sound_patch_file_name = uri_sound_patch.replace(
                "https://download.limbuscompany.site/", ""
            ).replace("/Assets/Sound/", "_Sound")
            sound_patch_file_path = Path(f"./sound_patches/{sound_patch_file_name}")
            with open(sound_patch_file_path, "wb") as sound_patch_file:
                sound_patch_file.write(sound_patch_response.content)
            print(f"Saved sound_patch data to {sound_patch_file_path}")

            insert_limbus_update_data(
                hash=hash_file_name,
                server_info=server_info_file_name,
                sound_patch=sound_patch_file_name,
            )

    except httpx.RequestError as e:
        print(f"An error occurred while requesting: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")

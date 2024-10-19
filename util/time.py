from datetime import datetime, timezone


def get_curr_time() -> str:
    current_time = datetime.now(timezone.utc)
    formatted_time = current_time.isoformat(
        timespec="milliseconds"
    ).replace("+00:00", "Z")

    return formatted_time

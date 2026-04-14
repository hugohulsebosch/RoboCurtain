import json
from pathlib import Path
from datetime import datetime
from logger import get_logger


ALARM_FILE = Path.home() / \
    "Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Alarm/data/alarm.json"


log = get_logger(__name__)


def get_wake_up_time() -> datetime | None:
    """
    Reads the alarm.json written by the iPhone Shortcut from iCloud Drive.
    Returns the alarm time as a timezone-aware datetime, or None if the
    alarm is disabled or the file is missing.
    """
    if not ALARM_FILE.exists():
        log.error(f"Alarm file not found at {ALARM_FILE}")
        return None

    with ALARM_FILE.open() as f:
        data = json.load(f)

    if not data.get("alarm_enabled"):
        log.info("Alarm is disabled, skipping curtain schedule.")
        return None

    alarm_time = datetime.fromisoformat(data["alarm_time"])
    log.info(
        f"Wake-up time read from {data['device']}: {alarm_time.strftime('%H:%M %Z')}")
    return alarm_time


if __name__ == "__main__":
    print("This will be the RoboCurtain functionality.")
    wake_up = get_wake_up_time()
    if wake_up:
        print(f"Parsed datetime: {wake_up}")

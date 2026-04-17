import subprocess
from pathlib import Path
from datetime import datetime
from logger import get_logger

log = get_logger(__name__)

LAUNCH_AGENTS = Path.home() / "Library/LaunchAgents"
VENV_PYTHON = "/Users/hugohulsebosch/Documents/Code/RoboCurtain/.venv/bin/python"
SRC = "/Users/hugohulsebosch/Documents/Code/RoboCurtain/src"


def _write_plist(label: str, action: str, run_at: datetime) -> Path:
    plist_path = LAUNCH_AGENTS / f"{label}.plist"
    plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{label}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{VENV_PYTHON}</string>
        <string>{SRC}/curtain_job.py</string>
        <string>{action}</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>{run_at.hour}</integer>
        <key>Minute</key>
        <integer>{run_at.minute}</integer>
    </dict>
</dict>
</plist>"""
    plist_path.write_text(plist)
    return plist_path


def _load_plist(plist_path: Path) -> None:
    # Unload first in case it's already registered from yesterday
    subprocess.run(["launchctl", "unload", str(plist_path)],
                   capture_output=True)
    subprocess.run(["launchctl", "load", str(plist_path)], check=True)
    log.info(f"Loaded launchd job: {plist_path.name}")


def schedule_open(run_at: datetime) -> None:
    plist_path = _write_plist(
        "com.hugohulsebosch.robocurtain.open", "open", run_at)
    _load_plist(plist_path)
    log.info(f"Curtain open scheduled at {run_at.strftime('%H:%M')}")


def schedule_close(run_at: datetime) -> None:
    plist_path = _write_plist(
        "com.hugohulsebosch.robocurtain.close", "close", run_at)
    _load_plist(plist_path)
    log.info(f"Curtain close scheduled at {run_at.strftime('%H:%M')}")


if __name__ == "__main__":
    from datetime import timedelta

    schedule_close(datetime.now() + timedelta(minutes=1))
    schedule_open(datetime.now() + timedelta(minutes=3))

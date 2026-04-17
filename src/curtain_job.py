import asyncio
import subprocess
import sys
from pathlib import Path
from curtain import open_curtain, close_curtain
from logger import get_logger

log = get_logger(__name__)

PLIST_DIR = Path.home() / "Library/LaunchAgents"


async def main(action: str) -> None:
    match action:
        case "open":
            await open_curtain()
        case "close":
            await close_curtain()
        case _:
            log.error(f"Unknown action '{action}'. Use 'open' or 'close'.")
            sys.exit(1)

    label = f"com.hugohulsebosch.robocurtain.{action}"
    plist_path = PLIST_DIR / f"{label}.plist"
    subprocess.run(["launchctl", "unload", str(plist_path)],
                   capture_output=True)
    plist_path.unlink(missing_ok=True)
    log.info(f"Job '{label}' unloaded and removed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: curtain_job.py <open|close>")
        sys.exit(1)

    asyncio.run(main(sys.argv[1]))

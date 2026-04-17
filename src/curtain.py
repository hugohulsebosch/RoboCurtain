import asyncio
import switchbot
from logger import get_logger

log = get_logger(__name__)

CURTAIN_ADDRESS = "DE241397-2B26-E443-19DB-B02615793D16"


async def get_device() -> switchbot.SwitchbotCurtain:
    scanner = switchbot.GetSwitchbotDevices()
    curtains = await scanner.get_curtains()
    advertisement = curtains.get(CURTAIN_ADDRESS)
    if not advertisement:
        raise RuntimeError(f"Curtain {CURTAIN_ADDRESS} not found during scan.")
    return switchbot.SwitchbotCurtain(device=advertisement.device)


async def open_curtain() -> None:
    device = await get_device()
    if await device.open():
        log.info("Curtain opened successfully.")
    else:
        log.error("Failed to open curtain.")


async def close_curtain() -> None:
    device = await get_device()
    if await device.close():
        log.info("Curtain closed successfully.")
    else:
        log.error("Failed to close curtain.")

if __name__ == "__main__":
    asyncio.run(open_curtain())

import asyncio
import switchbot


async def main():
    scanner = switchbot.GetSwitchbotDevices()
    curtains = await scanner.get_curtains()
    for address, advertisement in curtains.items():
        print(f"Address       : {address}")
        print(f"Advertisement : {advertisement}")
        print(f"Attributes    : {vars(advertisement)}")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from tg_updater import tg_update, client

async def main():
    await asyncio.gather(tg_update())

if __name__ == "__main__":
    asyncio.run(main())
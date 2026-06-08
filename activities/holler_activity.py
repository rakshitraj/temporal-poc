import asyncio

from temporalio import activity

@activity.defn
async def holler(name:str) -> str:
    activity.logger.info(f"Hollering {name}!")
    print("Hollering...")

    await asyncio.sleep(5)

    return f"HOLLER {name.capitalize()}!!"
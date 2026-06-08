import asyncio

from temporalio import activity

@activity.defn
async def say_hello(name:str) -> str:
    activity.logger.info(f"Saying hello to {name}!")

    await asyncio.sleep(15)

    return f"Hello {name}!"
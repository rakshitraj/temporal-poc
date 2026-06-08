import asyncio

from temporalio import activity

@activity.defn
async def say_hello(name:str) -> str:
    activity.logger.info(f"Saying hello to {name}!")
    print("Saying hello...")

    await asyncio.sleep(5)

    return f"Hello {name}!"
import asyncio
from temporalio import activity

@activity.defn
async def say_goodbye(name:str) -> str:
    activity.logger.info(f"Saying goodbye to {name}!")

    # await asyncio.sleep(10)

    return f"Goodbye {name}!"


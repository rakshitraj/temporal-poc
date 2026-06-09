import random

from temporalio import activity


@activity.defn
async def flaky_task(name: str) -> str:
    activity.logger.info(f"Running flaky task for {name}, attempt #{activity.info().attempt}")

    num = random.random()
    print(f"flaky num {num}")

    if num < 0.8:
        if num < 0.6: 
            raise Exception(f"Flaky task failed randomly on attempt #{activity.info().attempt}")
        else:
            raise ValueError
    
    return f"Flaky task succeeded for {name} on attempt #{activity.info().attempt}"

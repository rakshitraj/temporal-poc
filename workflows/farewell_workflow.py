import asyncio
from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities.hello_activity import say_hello
    from activities.goodbye_activity import say_goodbye
    from activities.holler_activity import holler

@workflow.defn
class FarewellWorkflow:

    @workflow.run
    async def run(self, name:str):

        greet, farewell = await asyncio.gather(
            workflow.execute_activity(
                say_hello,
                name,
                start_to_close_timeout=timedelta(seconds=10)
            ),
            workflow.execute_activity(
                say_goodbye,
                name,
                start_to_close_timeout=timedelta(seconds=10)
            )
        )

        holler_result = await workflow.execute_activity(
            holler,
            name,
            start_to_close_timeout=timedelta(seconds=10)
        )

        return f"{greet} | {farewell} | {holler_result}"
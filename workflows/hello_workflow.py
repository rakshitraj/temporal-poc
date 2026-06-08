from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities.hello_activity import say_hello

@workflow.defn
class HelloWorkflow:

    @workflow.run
    async def run(self, name:str):
        
        result = await workflow.execute_activity(
            say_hello,
            name,
            start_to_close_timeout=timedelta(seconds=10)
        )

        return result
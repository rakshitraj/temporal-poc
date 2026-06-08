import asyncio

from temporalio.client import Client
from temporalio.common import WorkflowIDReusePolicy

from workflows.hello_workflow import HelloWorkflow
from workflows.farewell_workflow import FarewellWorkflow

async def main():

    client = await Client.connect("localhost:7233")

    hello_result, farewell_result = await asyncio.gather(
        client.execute_workflow(
            HelloWorkflow.run,
            "Rakshit",
            id="hello-workflow",
            task_queue="default-task-queue",
            id_reuse_policy=WorkflowIDReusePolicy.TERMINATE_IF_RUNNING
        ),
        client.execute_workflow(
            FarewellWorkflow.run,
            "Rakshit",
            id="farewell-workflow",
            task_queue="default-task-queue",
            id_reuse_policy=WorkflowIDReusePolicy.TERMINATE_IF_RUNNING
        )
    )

    print(hello_result)
    print(farewell_result)

if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from temporalio.client import Client

from workflows.hello_workflow import HelloWorkflow

async def main():

    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        HelloWorkflow.run,
        "Rakshit",
        id="hello-workflow",
        task_queue="default-task-queue"
    )

    print(result)

if __name__ == "__main__":
    asyncio.run(main())

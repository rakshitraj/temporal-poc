import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from workflows.hello_workflow import HelloWorkflow
from activities.hello_activity import say_hello


async def main() -> None:

    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="default-task-queue",
        workflows=[HelloWorkflow],
        activities=[say_hello]
    )

    print("Worker started")

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
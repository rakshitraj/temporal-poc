import asyncio
import logging

from temporalio.client import Client
from temporalio.worker import Worker

from workflows.hello_workflow import HelloWorkflow
from workflows.farewell_workflow import FarewellWorkflow
from workflows.flaky_workflow import FlakyWorkflow

from activities.hello_activity import say_hello
from activities.goodbye_activity import say_goodbye
from activities.holler_activity import holler
from activities.flaky_activity import flaky_task


logging.basicConfig(level=logging.INFO)


async def main() -> None:

    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="default-task-queue",
        workflows=[
            HelloWorkflow, 
            FarewellWorkflow,
            FlakyWorkflow
        ],
        activities=[
            say_hello, 
            say_goodbye, 
            holler,
            flaky_task
        ]
    )

    print("Worker started")

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
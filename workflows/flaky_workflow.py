from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from activities.flaky_activity import flaky_task


@workflow.defn
class FlakyWorkflow:

    @workflow.run
    async def run(self, name: str) -> str:

        retry_policy = RetryPolicy(
            # Stop after this many total attempts (1 = no retries)
            maximum_attempts=30,

            # Wait 1s before the first retry
            initial_interval=timedelta(seconds=1),

            # Each retry waits longer: 1s → 2s → 4s → 8s …
            backoff_coefficient=1.0,

            # Cap the wait so it never exceeds this, no matter the coefficient
            maximum_interval=timedelta(seconds=5),

            # These error types are NOT retried — fail immediately
            # Matches the ValueError raised in flaky_activity.py
            non_retryable_error_types=["ValueError"],
        )

        result = await workflow.execute_activity(
            flaky_task,
            name,
            start_to_close_timeout=timedelta(seconds=30),
            retry_policy=retry_policy,
        )

        return result

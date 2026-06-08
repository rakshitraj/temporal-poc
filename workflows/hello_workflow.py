from temporalio import workflow

@workflow.defn
class HelloWorkflow:

    @workflow.run
    async def run(self, name:str):
        
        return f"Hello {name}!"


# WebhookPayloadWorkflowRunExecution


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Workflow run (execution) id. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | running on workflow.run.started; completed or exited (ended on purpose before the last node, e.g. a handoff) on workflow.run.completed; failed on workflow.run.failed. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| WAITING | &quot;waiting&quot; |
| COMPLETED | &quot;completed&quot; |
| EXITED | &quot;exited&quot; |
| FAILED | &quot;failed&quot; |




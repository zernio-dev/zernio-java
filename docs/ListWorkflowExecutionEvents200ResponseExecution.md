

# ListWorkflowExecutionEvents200ResponseExecution


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**startedAt** | **OffsetDateTime** |  |  [optional] |
|**completedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| WAITING | &quot;waiting&quot; |
| COMPLETED | &quot;completed&quot; |
| EXITED | &quot;exited&quot; |
| FAILED | &quot;failed&quot; |



